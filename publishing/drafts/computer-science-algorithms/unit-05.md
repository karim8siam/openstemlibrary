# Algorithms — Unit 5: Dynamic programming


## State Design

**Core model — State Design**

Dynamic programming starts with a state whose inputs completely determine the remaining decision problem. Each transition must decrease some well-founded order or depend on already computed states.

**Original worked illustration**

For coin values 1,3,4, define dp[x]=1+min(dp[x-1],dp[x-3],dp[x-4]) across usable coins, with dp[0]=0. Then dp[6]=2 from 3+3.

**Boundary conditions and checks**

A state that omits remaining capacity, time or an essential constraint can merge different future possibilities and produce incorrect answers.

**Connections in this unit**

The adjacent subjects are Optimal Substructure, Sequence Problems, Resource Allocation. They are studied alongside State Design because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Dynamic programming begins by defining a state that retains exactly the information necessary to choose subsequent actions. The recurrence must be sound: its candidate transitions must cover every feasible optimum and exclude infeasible solutions. Memoization evaluates reachable states on demand, while tabulation places states in an order respecting dependencies. The number of states multiplied by transitions per state gives a useful time bound, but memory and reconstruction cost also matter. A state that omits relevant history can merge situations with different possible futures, producing a beautifully implemented but incorrect recurrence.

### Derivation and worked trace

For minimum coins with denominations 1,3,4 and target six, define D(x) as the minimum number of coins summing to x. Let D(0)=0 and D(x)=1+min(D(x-c)) over denominations c<=x. Values are D(1)=1, D(2)=2, D(3)=1, D(4)=1, D(5)=2, D(6)=2. The optimal answer is two coins of three. The greedy rule that takes four and then two ones uses three coins, proving the advantage of exploring alternative first choices in this coin system. The recurrence works because once the first coin is fixed, the remaining suffix is another instance of the same problem.

### Counterexample and failure diagnosis

Not every optimization has a small DP state space. Encoding all previously visited vertices can require an exponential subset state, as in the Held–Karp traveling-salesperson dynamic program. It remains valid but not generally polynomial in the number of cities. A common implementation bug is overwriting a one-dimensional table in the wrong order: for 0/1 knapsack, processing capacities upward can allow the same item to be taken repeatedly. Descending capacity preserves one-use semantics. For unbounded knapsack, upward updates are appropriate because repetitions are permitted. Update direction is part of the model.

### Applications, engineering constraints and validation

State design also determines how to reconstruct an actual solution rather than just its score. Record the predecessor choice or compare state values during backtracking. If ties exist, specify whether any optimum is acceptable or a deterministic tie-breaker is required. An app that reports a maximum value without the selected items may not meet the user's need. Validate with brute force on small instances, especially capacity zero, all items too heavy, duplicate items and cases where a locally high value-to-weight ratio is misleading.

## Optimal Substructure

**Core model — Optimal Substructure**

Optimal substructure asserts that an optimal solution contains optimal solutions to appropriate subproblems. Overlapping subproblems explain why memoization saves time, but optimal substructure alone is not enough.

**Original worked illustration**

For shortest paths with nonnegative weights, every subpath of a shortest path is shortest between its endpoints. Replacing a nonoptimal subpath would improve the whole route, contradicting optimality.

**Boundary conditions and checks**

Negative cycles can make the notion of a finite shortest path ill-posed. A recurrence should also specify tie-breaking if reconstruction matters.

**Connections in this unit**

The adjacent subjects are State Design, Sequence Problems, Resource Allocation. They are studied alongside Optimal Substructure because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Optimal substructure means that an optimal solution can be assembled from optimal solutions to well-defined subproblems after a suitable choice. It does not say that any local best move can be extended to a global optimum. Overlapping subproblems motivate caching, but are not logically required for optimal substructure. A proof usually fixes a particular feature of an optimal solution, assumes one chosen subpart were suboptimal, replaces it with a better subsolution and obtains a contradiction. The replacement must preserve compatibility with the remainder of the solution; otherwise the argument is invalid.

### Derivation and worked trace

For a shortest path from A to D passing through B, if the edge weights and path model permit subpath replacement, the A-to-B segment must itself be a shortest path between those vertices in a globally shortest route. Otherwise replacing it with a shorter A-to-B route would produce a shorter A-to-D walk. But the statement becomes more delicate when the path must be simple and negative cycles or globally constrained resources exist. A resource-constrained path cannot always be summarized only by the current vertex, because remaining fuel or budget affects the feasible continuation.

### Counterexample and failure diagnosis

For matrix-chain multiplication, the optimal placement of parentheses depends on the dimensions, not on the order of matrices themselves. Let matrices have dimensions A:10x100, B:100x5, C:5x50. Computing (AB)C costs 10*100*5+10*5*50=7,500 scalar multiplications. Computing A(BC) costs 100*5*50+10*100*50=75,000. Both are algebraically the same associative matrix product, yet the arithmetic work differs by a factor of ten. A DP over intervals considers each split point and caches the cheapest cost.

### Applications, engineering constraints and validation

Engineers should distinguish optimal substructure from greedy-choice property. A DP may examine all transitions at a state precisely because it cannot know which immediate choice is globally optimal. Caching a subproblem whose answer depends on an omitted constraint produces incorrect reuse. In a scheduling DP, the state might need the current time; in graph routing with limited fuel, it may need both vertex and remaining resource. A useful review exercise attempts to construct two different histories that reach the same proposed state but have different feasible futures; finding such a pair disproves state sufficiency.

## Sequence Problems

**Core model — Sequence Problems**

Many sequence problems use a two-dimensional state representing prefixes. For longest common subsequence, a mismatch branches by dropping one trailing symbol; a match extends both prefixes.

**Original worked illustration**

Let X=ABC and Y=AC. The LCS length is 2 (AC). At matching final C the recurrence adds one to LCS(AB,A), which has length one.

**Boundary conditions and checks**

A subsequence need not be contiguous; using a substring recurrence would solve a different problem and can badly underestimate the answer.

**Connections in this unit**

The adjacent subjects are State Design, Optimal Substructure, Resource Allocation. They are studied alongside Sequence Problems because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Sequence algorithms compare ordered collections while respecting relative positions. The longest common subsequence problem asks for an ordered sequence common to two strings, not necessarily contiguous. A substring is contiguous, so the two objectives have different recurrences and applications. For longest common subsequence, let L(i,j) be the answer length for prefixes of lengths i and j. Matching last symbols allow L(i,j)=1+L(i-1,j-1); otherwise take max(L(i-1,j),L(i,j-1)). The recurrence fills an (m+1) by (n+1) table in O(mn) time.

### Derivation and worked trace

For X=ABCBDAB and Y=BDCABA, one common subsequence is BCBA, of length four. The symbols need not occupy adjacent positions in either string. When reconstructing a subsequence from the DP table, multiple equal-score branches can lead to different valid answers. Returning one sequence of length four satisfies the optimum if the length table is correct. A common mistake is to use a greedy scan that matches the earliest possible occurrence in the second string and then assumes the result is longest; early choices can block better later combinations.

### Counterexample and failure diagnosis

Edit distance measures a different property. In Levenshtein distance with unit insertion, deletion and substitution cost, an optimal alignment may replace characters rather than only remove them. For example, converting cat to cut requires one substitution. The state recurrence examines three predecessor positions and their corresponding costs. Real biological sequence alignment often introduces affine gap penalties and scoring conventions, which change the state design. One cannot substitute an LCS recurrence and expect all alignment costs to be correct.

### Applications, engineering constraints and validation

Applications include document comparison, genome analysis and version-control systems. Memory can sometimes be reduced by storing only the previous DP row when only the optimum length is needed. Recovering an actual witness generally requires additional information or a divide-and-conquer reconstruction such as Hirschberg's method. Test empty strings, identical strings, repeated characters, ties, Unicode normalization and surrogate pairs. State whether a program works on bytes, code points or grapheme clusters; those units are not interchangeable.

## Resource Allocation

**Core model — Resource Allocation**

Resource-allocation DP tracks a budget alongside the set of processed items. In 0/1 knapsack, an item can be selected once; iterating capacities downward is essential for a one-row in-place implementation.

**Original worked illustration**

With capacity 5 and items (weight,value) (2,4), (3,5), (4,6), selecting the first two yields value 9 and weight 5, better than choosing the third alone.

**Boundary conditions and checks**

An upward capacity iteration with a one-dimensional DP can unintentionally allow unlimited copies of the same item; distinguish 0/1 from unbounded knapsack.

**Connections in this unit**

The adjacent subjects are State Design, Optimal Substructure, Sequence Problems. They are studied alongside Resource Allocation because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Resource-allocation dynamic programs encode a fixed capacity or budget alongside the choice history. In 0/1 knapsack, each item can be selected at most once, so a recurrence indexed by item count and remaining capacity distinguishes taken and not-taken branches. If weights and capacity are integers, the familiar table has O(nW) entries. This is pseudo-polynomial rather than polynomial in the binary-encoded input size because the bit length of W grows only logarithmically with its numeric value. Distinguishing those two size measurements is essential to complexity claims about knapsack.

### Derivation and worked trace

With capacity five and items (weight,value) equal to (2,3), (3,4), (4,5), (5,8), selecting the last item yields value eight. Selecting the first two produces value seven. Selecting the item of largest value-to-weight ratio happens to choose the final item in this instance, but ratio-greedy is not generally correct for 0/1 knapsack because items cannot be divided fractionally. The DP recurrence chooses the maximum of excluding item i and including it if capacity permits, thereby exploring the combinations systematically without enumerating every subset explicitly.

### Counterexample and failure diagnosis

A one-dimensional implementation iterating capacity forward after considering item (2,3) can reuse that same item twice, effectively solving an unbounded variant. Going backward protects the at-most-once condition. But backward iteration alone cannot repair an incorrect recurrence if the state is missing a second constrained resource. A project-planning variant with both money and personnel limits requires a state over two capacities or another optimization technique. State exactly which constraints the table enforces.

### Applications, engineering constraints and validation

Knapsack formulations are useful in packaging, procurement, memory placement and feature selection, but additional dependencies between items often break the simple recurrence. Two items may be mutually exclusive, one may require another, or value may depend on the combination. Benchmarks should measure how the dynamic program scales in both item count and capacity. For small n, compare every selected subset as an oracle, reconstruct the chosen items and verify both capacity and reported objective after backtracking.

## Unit 5 integrated computational laboratory

## Integrated laboratory: dynamic programming as a model of decisions

The first task in a dynamic-programming solution is not writing a table. It is deciding which aspects of the past can influence legal future actions. Suppose a charity has a budget of ten units and can fund each of four projects at most once. Their (cost,benefit) pairs are (6,9), (4,7), (5,8), (3,4). An item-by-item capacity table is sufficient if projects have independent benefits and no prerequisites. The state D(i,c) records the best benefit using only the first i projects with budget at most c. The recurrence compares excluding item i against including it when its cost fits. Using an at-most budget convention permits unused budget and makes D(i,c) nondecreasing in c for nonnegative benefits.

Compute the best selection under capacity ten. Choosing projects of costs six and four produces benefit 9+7=16. Choosing costs five and four produces benefit fifteen. Choosing costs six and three produces thirteen. Choosing costs four and five also uses nine, and adding cost three would exceed the ten-unit budget. Choosing five and three produces twelve. Single-project choices are at most nine. Therefore the optimum is sixteen, with the six- and four-unit projects selected. A brute-force oracle can enumerate the sixteen subsets of four projects and verify this result. That enumeration is too expensive for a large n, but it is ideal for small independent test cases.

If a programmer uses a one-dimensional DP and loops capacity upward, the six-unit project is safe from repeated reuse at capacity ten but the three-unit project might be counted multiple times across other capacities. Descending capacity iteration is the standard way to prevent accidental reuse for 0/1 knapsack. A proof of correctness proceeds by induction on the number of processed items. Each state either keeps a previously optimal subset that excludes the new item or adds the new item to an optimal subset of the prior items with reduced capacity. These cases partition all legal solutions, establishing completeness of the transition.

Now suppose project four can only be funded if project one is funded. The previous recurrence no longer represents the full feasibility condition, because the choice of project four depends on another chosen item. A pairwise bundling transformation may work for this particular dependency; more general prerequisites can require a different state or a constrained optimization model. The mistake would be to keep the same table and treat its numerically optimal answer as legally valid. A DP state is a compressed description of history only when it preserves all information relevant to future decisions.

A second capstone concerns matrix multiplication order. Multiply A of size 10x100, B of size 100x5, and C of size 5x50. The two possible binary parenthesizations have costs 7,500 and 75,000 scalar multiplications respectively. The order of matrices in the product cannot change, but the placement of parentheses may. The interval DP state M(i,j) records the minimum operations for matrices i through j and considers every possible final split k. The split at k combines an optimal left subchain and an optimal right subchain with one final matrix product whose dimensions are dictated by the boundary matrices. This recurrence is a direct example of optimal substructure: a nonoptimal subchain could be replaced without affecting dimensions and would improve the whole solution.

For text similarity, compare ABCBDAB against BDCABA and find a longest common subsequence. A valid length-four answer is BCBA. The correct DP uses two indices for the two prefixes; a single prefix-length index loses the relative position in the other string. Reconstruction follows the stored decisions backward through the table. An application may need an actual alignment, not just a number, so retaining reconstruction information can be more important than reducing memory to two rolling rows. Define whether Unicode input is compared as bytes, code points or grapheme clusters before interpreting results.

Performance claims for DP should count states and transitions, not simply say the algorithm is polynomial. The O(nW) 0/1 knapsack table depends on numeric capacity W and is pseudo-polynomial when W is binary encoded. A sequence DP of length m and n usually has O(mn) states, but a weighted edit-distance variant can have different transitions. Recursion with memoization avoids recomputation only if the cache key includes all relevant parameters; tabulation avoids recursion overhead only if a valid dependency order exists. Neither technique automatically remedies a logically incomplete state.

Finish the lab with three independent checks. First, use exhaustive subset enumeration or recursion on tiny instances as an oracle. Second, verify a witness: its total resource use does not exceed capacity, each item is used legally, and its reported value equals the sum of selected benefits. Third, perturb the input near boundaries: zero capacity, negative or zero benefit policies, repeated weights, empty item list and capacity smaller than every item. A DP that gives the correct objective on typical examples can still reconstruct an impossible selection if predecessor updates are wrong.

### Independent audit exercise: make a DP table independently checkable

Consider change-making with denominations 1,3,4 and exact target nine. The optimal result uses three coins of value three, but there is also an optimal three-coin combination 4+4+1. Construct the table D(0)=0, then for each positive total t compute one plus the smallest D(t-c) for legal coins c. A correctness argument should show that every nonempty optimal solution has a first coin and that removing it leaves an optimal solution for the remaining amount. If the remainder were not optimal, replacing it would reduce the original coin count, contradicting optimality.

Store predecessors to reconstruct actual coin choices. For target nine, a correct numerical answer D(9)=3 can still conceal broken predecessor links that return values summing to eight or ten. Validate the witness by checking its sum equals nine and its length equals D(9). When ties occur, any optimum is acceptable unless the interface specifies lexicographic or other deterministic tie-breaking. This separates optimal-value correctness from actual plan validity.

Changing coins to 2,4 removes the unit coin and makes odd targets impossible. A recurrence that initializes every D(t) to zero or assumes that every amount can be represented will return incorrect values. Use infinity as a sentinel for unreachable totals and guard against adding one to an infinite sentinel in a fixed-width language. For target seven the result should explicitly indicate infeasibility, not a large plausible-looking number. This one boundary change tests whether the implementation understands its mathematical model.

For 0/1 knapsack, also verify that descending-capacity updates prevent reuse of the same item. With one item weighing three and valued five, capacity six still permits value five, not ten. An unbounded-knapsack recurrence would allow two copies and correctly report ten under a different item-use contract. The same table array can implement either problem depending on loop direction. An informative textbook lab makes that semantic change visible instead of presenting a raw numerical output.

## Worked questions and solutions

### Question 1: State Design: worked application 1

For the coin system [1,3,4], compute the minimum number of coins for amount 6.

1. **Set up the model and conditions:** Initialize dp[0]=0; dp[x] is one plus the minimum usable predecessor.

2. **Carry out the calculation or proof:** For 6, choosing 3+3 uses two coins; choosing 4+1+1 needs three.

3. **State the result and its scope:** dp[6]=2; the greedy choice of 4 is not optimal.

**Answer:** dp[6]=2; the greedy choice of 4 is not optimal.


### Question 2: Optimal Substructure: worked application 2

Compute LCS length for X=ABC and Y=AC, and name one optimal subsequence.

1. **Set up the model and conditions:** A matches A and C matches C in their original order.

2. **Carry out the calculation or proof:** B appears only in X, so it cannot increase a common subsequence.

3. **State the result and its scope:** The LCS is AC with length 2.

**Answer:** The LCS is AC with length 2.


### Question 3: Sequence Problems: worked application 3

Solve the 0/1 knapsack with capacity 5 and items (2,4),(3,5),(4,6).

1. **Set up the model and conditions:** Feasible nonempty pairs: item 1 plus item 2 weighs 5 and gives value 9; other pairs exceed capacity.

2. **Carry out the calculation or proof:** Individual values are 4,5 and 6.

3. **State the result and its scope:** The maximum value is 9 using items 1 and 2.

**Answer:** The maximum value is 9 using items 1 and 2.

