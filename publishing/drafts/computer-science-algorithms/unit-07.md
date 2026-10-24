# Algorithms — Unit 7: Complexity and approximation


## Np-Completeness

**Core model — Np-Completeness**

NP-completeness combines membership in NP with NP-hardness under polynomial-time reductions. A yes-certificate can be checked efficiently even when no efficient method to find one is known.

**Original worked illustration**

For Hamiltonian cycle, a certificate is a vertex ordering. In polynomial time we verify each vertex occurs once and consecutive endpoints, including the final-to-first edge, exist.

**Boundary conditions and checks**

An NP-complete problem is not proved unsolvable in polynomial time; P versus NP remains open. Reduction direction must be from known-hard problem to target.

**Connections in this unit**

The adjacent subjects are Reductions, Approximation Ratios, Parameterized Ideas. They are studied alongside Np-Completeness because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Computational complexity studies resources required as a function of input representation size and distinguishes problems from particular programs. The class P contains decision problems solvable by deterministic polynomial-time algorithms in the standard model. NP contains decision problems whose yes-instances admit certificates verifiable in polynomial time, equivalently problems solvable by nondeterministic polynomial-time algorithms. The phrase NP means nondeterministic polynomial time, not not polynomial. NP-hardness and NP-completeness require reductions and careful direction of implication; neither is a synonym for practically impossible in every instance.

### Derivation and worked trace

For a Boolean formula such as (x OR y) AND (NOT x OR z), a certificate consists of truth values for x,y,z. An assignment x=false, y=true, z=false satisfies the first clause through y and the second through NOT x. Checking each literal and clause takes time proportional to formula length under a straightforward representation. This demonstrates efficient verification of a proposed answer; it does not by itself show how to find a satisfying assignment quickly. To establish NP-completeness of a new decision problem, one must show both membership in NP and hardness by reducing a known NP-complete problem to it.

### Counterexample and failure diagnosis

A frequent logical error is to treat exponential worst-case running time of one algorithm as a proof that the underlying problem has no polynomial algorithm. Another is to infer P≠NP from the failure of decades of search. That conjecture remains unresolved in standard complexity theory. Pseudopolynomial algorithms such as capacity-indexed knapsack DP run polynomially in the numeric capacity but can be exponential in the number of bits used to encode that capacity. Always name the encoding and count it when analyzing whether a bound is polynomial.

### Applications, engineering constraints and validation

Complexity classifications inform engineering decisions but do not choose implementations on their own. Small NP-hard instances may be solved optimally by branch-and-bound or modern integer programming; structured instances may have efficient specialized algorithms; large instances may require approximation or heuristics. A book should distinguish a theoretical worst-case lower bound from empirical performance on a particular workload. Report instance size, structural assumptions, allowed error and available compute budget rather than describing any NP-complete problem as unsolvable.

## Reductions

**Core model — Reductions**

A reduction maps one problem's instances to another in polynomial time and preserves yes/no answers. To show B is hard, map known-hard A into B, not the reverse.

**Original worked illustration**

An instance of Independent Set of size k in graph G corresponds to a vertex cover of size cardinality(V)-k in the same graph, since a set is independent exactly when its complement covers all edges.

**Boundary conditions and checks**

A mapping that only works in one direction of the equivalence is not a correctness-preserving reduction.

**Connections in this unit**

The adjacent subjects are Np-Completeness, Approximation Ratios, Parameterized Ideas. They are studied alongside Reductions because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

A polynomial-time many-one reduction transforms an instance of problem A into an instance of problem B so that the answer to A is yes exactly when the transformed answer to B is yes. To prove B is NP-hard, reduce a problem A already known to be NP-hard to B, written A≤p B. This direction matters: transforming B into A would show how an oracle for A could solve B, not necessarily that B is at least as hard as A. The construction must run in polynomial time and preserve both positive and negative instances.

### Derivation and worked trace

As a simple modeling illustration, map a graph G and desired integer k from the Independent Set decision problem to a Vertex Cover question on the same graph with budget |V|-k. A set S is independent exactly when its complement V\S covers every edge: if an edge had both endpoints in S, S would not be independent; conversely if an edge had no endpoint outside S, its endpoints would both lie in S. Therefore G has an independent set of size at least k if and only if it has a vertex cover of size at most |V|-k. The mapping copies the graph and modifies only the target size, so its running time is polynomial.

### Counterexample and failure diagnosis

Do not prove only that every yes-instance maps to yes; a valid equivalence also requires the reverse implication or explicit preservation of no-instances. Ensure a reduction handles degenerate cases such as empty graphs and budgets outside the legal range. The transformed instance's size must be polynomial in the original encoding length, not merely in a large numeric parameter represented with a few bits. A reduction that searches for the optimum as part of its construction is circular unless that search is already known to be efficient.

### Applications, engineering constraints and validation

Reductions can reveal useful algorithmic relationships beyond hardness. A matching problem can sometimes be modeled as max flow; a scheduling restriction might become shortest path in a DAG. Such reductions justify reusing tested algorithms with clear contracts. For hardness arguments, a source problem must have an established classification under compatible assumptions, and the target must use the exact decision variant being claimed. Convert small instances both ways and compare exhaustive answers as a sanity check before finalizing a proof.

## Approximation Ratios

**Core model — Approximation Ratios**

An approximation ratio compares an algorithm's objective with the optimum under a declared minimization or maximization convention. Feasibility remains mandatory before a ratio is meaningful.

**Original worked illustration**

For minimum vertex cover, repeatedly choosing both endpoints of an uncovered edge yields a cover of size at most twice optimum: chosen edges form a matching, and every cover needs at least one endpoint of each matched edge.

**Boundary conditions and checks**

A ratio derived for nonnegative objective values may not transfer unchanged when negative costs or infeasible solutions are permitted.

**Connections in this unit**

The adjacent subjects are Np-Completeness, Reductions, Parameterized Ideas. They are studied alongside Approximation Ratios because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

An approximation algorithm returns a feasible solution whose objective is provably near optimum on every legal instance of the specified problem. For a minimization problem, an alpha-approximation typically guarantees algorithm cost ≤ alpha times optimum for alpha≥1. For maximization, conventions differ, often guaranteeing algorithm value ≥ optimum/alpha. Feasibility and the direction of the inequality are indispensable. An empirical result that happened to be close to optimum on ten examples is not an approximation guarantee. When optimum is zero or negative, multiplicative ratios require special treatment or a different error measure.

### Derivation and worked trace

The classic 2-approximation for unweighted vertex cover starts with a maximal matching M and selects both endpoints of every edge in M. Its chosen vertices form a cover: if an uncovered edge remained with neither endpoint selected, that edge could be added to the matching, contradicting maximality. Any vertex cover must contain at least one endpoint of each edge in M, so OPT≥|M|. The algorithm selects exactly 2|M| vertices, hence solution size≤2OPT. On a star with at least one leaf the algorithm may select the center and one leaf, while the optimum chooses only the center; the factor two can be attained.

### Counterexample and failure diagnosis

Do not claim that this algorithm finds a minimum vertex cover or that every greedy vertex-cover heuristic has the same guarantee. The proof depends on using a matching and taking both endpoints of every matched edge. For weighted vertex cover, selecting both endpoints may violate a useful weighted ratio unless the algorithm and bound are adapted. A maximal matching is not necessarily a maximum matching; the approximation proof requires only maximality. Confusing those two words is a common but consequential error in teaching this example.

### Applications, engineering constraints and validation

Approximation methods are important when exact optimization is too expensive at scale, but user requirements may prefer predictable feasibility over a ratio. For routing or facility location, a solution may obey a strong global cost bound while violating an operational constraint if the implementation encoded feasibility incorrectly. Report both the mathematical approximation factor and the practical quality observed on representative data. For small graphs, exhaustively compute an optimum cover and verify that the implementation's ratio never exceeds two under the intended model.

## Parameterized Ideas

**Core model — Parameterized Ideas**

Parameterized algorithms separate a structural parameter k from the overall input size n. Fixed-parameter tractability means running time f(k)*n^c for constant c independent of k.

**Original worked illustration**

A branching vertex-cover solver chooses an uncovered edge (u,v), then recursively includes u or v in the cover, giving at most 2^k branches before polynomial overhead.

**Boundary conditions and checks**

An n^k algorithm is not FPT merely because it is polynomial for each fixed k: its exponent depends on k.

**Connections in this unit**

The adjacent subjects are Np-Completeness, Reductions, Approximation Ratios. They are studied alongside Parameterized Ideas because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Parameterized complexity asks whether an algorithm can isolate the main combinatorial difficulty in a selected parameter k, running in time f(k)·n^c for a constant c independent of k. Such algorithms are called fixed-parameter tractable with respect to k. This is different from merely having runtime n^k, whose exponent grows with the parameter. Selecting a meaningful parameter such as solution size, treewidth or number of violations can turn a generally hard problem into one that is tractable for small practical values. The algorithm is useful only when the parameter is genuinely small on expected instances.

### Derivation and worked trace

For Vertex Cover parameterized by desired cover size k, pick an uncovered edge (u,v). Any feasible cover must include u or v, so branch on including u or including v, then remove incident edges and decrement k. The search tree has branching factor two and depth at most k, yielding O(2^k·poly(n)) with suitable representation. If k=3, there are at most eight depth-three leaves, not n³ candidate subsets. This bound omits optimization details and polynomial work at each node, but it explains why small-k instances can be manageable even though general Vertex Cover is NP-complete.

### Counterexample and failure diagnosis

A crucial pruning rule says that if k becomes negative while uncovered edges remain, the branch fails. If no uncovered edge remains, a valid cover has been found. Testing the wrong base case can turn a sound branching idea into an incorrect algorithm. A kernelization preprocessing rule may reduce instance size while preserving yes/no equivalence. But arbitrarily deleting low-degree vertices is not necessarily safe; each reduction rule needs its own proof. Distinguish a parameterized algorithm from an approximate one, because the former may return exact yes/no answers.

### Applications, engineering constraints and validation

In scheduling, parameter k might count exceptional jobs rather than the total number of tasks. In computational biology, it might be the number of edits or mismatches tolerated. A report should specify which quantity is treated as the parameter and how it is measured. An algorithm with f(k)=2^(2^k) may be theoretically fixed-parameter tractable but useless even for moderately small k. Compare realistic constants, pruning, memory and observed parameter distributions before choosing it over a heuristic.

## Unit 7 integrated computational laboratory

## Integrated laboratory: complexity claims versus solvable instances

Hardness theory and exact algorithm engineering answer different questions. Complexity theory asks what resources are required across all input instances as size grows, while implementation practice often deals with a narrower distribution of instances and a strict operational budget. Consider a small festival planning system that selects event rooms subject to incompatible session pairs. If each conflict forbids two sessions from sharing a slot, a graph coloring model may be appropriate; if some sessions are optional and the objective is the smallest number of rooms, the exact decision and optimization problems must be separated. Calling a problem NP-hard does not exempt a developer from specifying feasible schedules or testing a solver's claimed optimum.

Take a graph with vertices A,B,C,D forming a path A-B-C-D. A minimum vertex cover has size two: for example {B,C} covers all three edges; {A,C} also covers all edges. No one-vertex cover exists because no single vertex touches both edge AB and edge CD. This optimum can be verified by enumerating the four singleton choices and then presenting the size-two witness. A matching with edges AB and CD has size two, so every vertex cover must have at least two vertices, giving a more elegant lower-bound certificate. The witness and lower bound agree, establishing optimality without enumerating all sixteen subsets.

Now apply the maximal-matching 2-approximation. Select a maximal matching, then include both endpoints of every selected matching edge. On the four-vertex path, selecting edges AB and CD returns all four vertices, twice the optimum. The approximation promise is satisfied, even though this particular answer is clearly wasteful. The algorithm's appeal is the universal factor-two guarantee and low computational cost, not the claim that every result is nearly optimal in an informal sense. Change the graph to a star; selecting a single edge returns two vertices while the optimum is the center, again reaching ratio two.

For exact solution with small parameter k, branch on one uncovered edge. Any cover of size at most k must include at least one endpoint, so explore those two choices. This produces an at-most 2^k branching tree times polynomial per-node work, assuming suitable pruning and update costs. For k=2, a depth-two tree has at most four leaves; this count is about branching decisions, not a guarantee of four total machine instructions. A practical solver should stop if no uncovered edges remain, reject when the remaining budget is negative, and prune using other sound lower bounds. Always test the branching solver against brute force for graphs with at most six vertices.

A reduction clarifies where hardness comes from. Independent Set asks for a set of pairwise nonadjacent vertices. The complement of a vertex cover is independent: if an edge connected two vertices outside the cover, that edge would have no endpoint covered. Thus a graph on n vertices has a vertex cover of size at most k exactly when it has an independent set of size at least n-k. This transformation is polynomial and preserves yes/no answers. Show both directions, because transforming yes-instances alone does not establish equivalence.

Knapsack illustrates a different subtlety. Dynamic programming over capacity W can use O(nW) time, which appears polynomial if W is treated as a number. But if W=2^m, its binary representation has only m+1 bits. O(nW) then becomes exponential in m. This distinction is why pseudopolynomial algorithms are not a proof that all standard NP-hard knapsack variants lie in P. A valid analysis must measure input encoding length rather than replacing it with an arbitrarily large numeric field.

Many applied instances have structure that generic worst-case families lack. A conflict graph might be a tree or have small treewidth; a budget might be tiny; an approximation factor might suffice for an online dashboard but not for an audit. A good design process identifies parameters from real use, measures their distribution, and compares exact, parameterized and approximation solvers on the same objectives and feasibility constraints. Reporting only the fastest runtime without solution quality would be a partial evaluation; reporting only a theoretically elegant guarantee without memory or scaling evidence would also be partial.

The final assessment must distinguish four categories of evidence. A reduction supports a theoretical hardness classification. An approximation proof supports a ratio under explicit assumptions. A parameterized branching argument supports an exact bound in k and n. A benchmark supports performance claims only for the tested implementation and workload. Students should be able to state the scope of each claim without confusing proof, experiment, conjecture and engineering estimate.

### Independent audit exercise: decision certificates and counterexamples

A SAT instance may be easy to verify once an assignment is supplied even when finding one is hard in the general case. Consider formula F=(a OR b) AND (NOT a OR c) AND (NOT b OR c). Assignment a=false, b=true, c=true satisfies every clause: the first through b, the second through NOT a or c, and the third through c. A verifier can scan the clauses, evaluate their literals and accept the certificate in time bounded by the formula representation length. A verifier that checks only two of three clauses is incorrect even if it accepts this particular satisfying assignment.

A certificate of infeasibility is different. Failure to find a satisfying assignment after trying ten random guesses does not prove no assignment exists. For three variables, exhaustive evaluation of all eight assignments can decide this one small instance. For general SAT, proving unsatisfiability can require more sophisticated methods, and the existence of short certificates for all no-instances is not established by the definition of NP. Teaching should not blur the distinction between a verified witness and an unsuccessful search.

For graph reductions, test a vertex-cover/independent-set pair. In the four-vertex path A-B-C-D, {B,C} is a vertex cover, and its complement {A,D} is an independent set. Each vertex-cover constraint corresponds to a prohibition against selecting both endpoints in the independent set. The transformation uses the same graph and target adjustment k ↦ |V|-k. Show why both logical directions hold. Reversing an implication or applying the target arithmetic incorrectly can invalidate a hardness proof even when all sample instances appear to agree.

Test approximate solutions through both witnesses and lower bounds. A matching of size m proves that any vertex cover uses at least m vertices because matched edges have disjoint endpoints. Selecting both endpoints of a maximal matching gives a cover of size 2m. Those two facts establish a factor-two upper bound without knowing the exact optimum. A report should explain that the matching need be maximal, not maximum, and that weighted vertex cover requires another argument.

## Worked questions and solutions

### Question 1: Np-Completeness: worked application 1

Explain why Hamiltonian cycle is in NP.

1. **Set up the model and conditions:** A candidate certificate lists vertices in cyclic order.

2. **Carry out the calculation or proof:** Check each vertex appears exactly once and each consecutive pair, including last to first, is an edge.

3. **State the result and its scope:** Verification is polynomial in graph size; this alone does not prove NP-hardness.

**Answer:** Verification is polynomial in graph size; this alone does not prove NP-hardness.


### Question 2: Reductions: worked application 2

For a graph with 8 vertices, convert an independent-set requirement of size at least 3 into a vertex-cover bound.

1. **Set up the model and conditions:** Take the complement of an independent set; every edge then has an endpoint outside it.

2. **Carry out the calculation or proof:** The complement has 8−3=5 vertices and covers every edge.

3. **State the result and its scope:** There is an independent set of size ≥3 iff a vertex cover of size ≤5 exists.

**Answer:** There is an independent set of size ≥3 iff a vertex cover of size ≤5 exists.


### Question 3: Approximation Ratios: worked application 3

For vertex cover on triangle edges AB, BC, AC, run the maximal-matching 2-approximation.

1. **Set up the model and conditions:** Select edge AB into the matching; it excludes BC and AC from the matching.

2. **Carry out the calculation or proof:** Return both matched endpoints A and B; this covers all triangle edges.

3. **State the result and its scope:** Cover size 2 equals optimum 2 in this instance and is within the proven factor 2.

**Answer:** Cover size 2 equals optimum 2 in this instance and is within the proven factor 2.

