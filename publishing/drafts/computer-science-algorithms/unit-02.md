# Algorithms — Unit 2: Searching and sorting


## Comparison Sorting

**Core model — Comparison Sorting**

Stable comparison sorting preserves the original order of equal keys; its running time is analyzed in comparisons and moves, which are different resources. The choice among mergesort, heapsort and quicksort depends on memory and adversarial guarantees.

**Original worked illustration**

Merge two sorted lists [1,4,7] and [2,4,9]. Comparing heads successively emits [1,2,4,4,7,9]; choosing the left entry on equality preserves stability across the two runs.

**Boundary conditions and checks**

A linear-time counting sort depends on a bounded integer key range, and therefore does not contradict the comparison-sort lower bound.

**Connections in this unit**

The adjacent subjects are Selection, Binary Search, Lower Bounds. They are studied alongside Comparison Sorting because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Comparison sorting works by obtaining information about an unknown permutation through pairwise comparisons. Merge sort, heapsort and typical quicksort implementations differ in space requirements, stability, branch behavior and worst-case guarantees. Merge sort recursively sorts halves and combines them with a linear merge; heap sort maintains a partially ordered binary-heap invariant; quicksort partitions around a pivot and then recursively sorts the sides. The phrase faster sort is incomplete without an input distribution, a memory constraint, a comparator cost and a stability requirement. Distinct object identities matter when two records have the same sorting key.

### Derivation and worked trace

Sort records [(B,2),(A,1),(C,2),(D,1)] by the numeric component and preserve the original order of equal keys. A stable result places A before D among the ones and B before C among the twos. The sorted array is [(A,1),(D,1),(B,2),(C,2)]. Merge sort is stable only if ties are resolved in favor of the left run; a merge that chooses from the right on equal keys may violate stability even though output keys are nondecreasing. Insertion sort can likewise be stable when it moves only elements strictly greater than the inserted key. Stability becomes functionally important in multi-stage sorting pipelines.

### Counterexample and failure diagnosis

A naïve claim that quicksort is always Theta(n log n) ignores pivot degeneration. With the first element as pivot and already sorted unique input, partitions can be sizes zero and n-1. The comparison count then obeys C(n)=C(n-1)+(n-1), yielding n(n-1)/2 under a simple partition convention. Random pivot selection reduces the expected number of comparisons, but does not eliminate all possible bad random outcomes. A deterministic worst-case protection such as introsort can switch to heapsort when partition depth becomes excessive. Choose the guarantee your application needs and name the pivot rule used.

### Applications, engineering constraints and validation

For sorting millions of fixed-width integers, radix techniques may outperform comparison sorting when the key range and memory model are favorable. That does not refute the comparison lower bound because a radix pass extracts more information than a single pairwise comparison. An external-memory sort considers sequential disk reads and writes instead of merely CPU comparisons. Benchmark two variants on duplicated keys, sorted keys, reverse order, random keys and records with expensive comparators; count comparisons and temporary bytes separately from elapsed time.

## Selection

**Core model — Selection**

Selection asks for the kth order statistic rather than a total ordering. Partition-based selection can discard a side after comparing against a pivot; randomized pivoting gives expected linear performance with worst-case quadratic behavior.

**Original worked illustration**

For [9,1,6,3,8], the third-smallest value is 6. A pivot of 6 partitions values into [1,3], [6], [9,8], and the rank is determined without sorting the two outer groups.

**Boundary conditions and checks**

An implementation must account for duplicate pivots and avoid an empty-progress partition, otherwise it may loop indefinitely or mishandle ranks.

**Connections in this unit**

The adjacent subjects are Comparison Sorting, Binary Search, Lower Bounds. They are studied alongside Selection because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Selection finds a rank statistic such as the kth smallest item without necessarily sorting all items. Quickselect partitions around a pivot and keeps only the side containing the desired rank; expected linear running time follows under a suitable random pivot model. In contrast, a deterministic worst-case linear selection algorithm uses carefully organized pivots and has a larger constant factor. The algorithm's correctness relies on partition guarantees: all elements on one side are no greater than the pivot and those on the other are no smaller, with equality handled consistently. A rank is an index in a multiset ordering, not necessarily a distinct numerical value.

### Derivation and worked trace

For [7,2,9,4,2,8,1], the sorted order is [1,2,2,4,7,8,9]. The fourth order statistic under one-based ranking is four. If a partition pivots on four, the three elements smaller than four are 1,2,2; the pivot therefore occupies the fourth position in a fully three-way partition, and no recursive search is required. With repeated pivots, a two-way partition can process long ranges of equal values unnecessarily. A three-way partition counts items less than, equal to, and greater than the pivot and can terminate immediately when the requested rank falls in the equality block.

### Counterexample and failure diagnosis

Median of medians gives a worst-case linear bound through a structural guarantee about how many elements a good pivot discards, but the analysis requires group-size and recurrence reasoning. It is invalid to claim that every median-based pivot splits the array exactly in half. Another subtlety concerns numerical selection APIs: zero-based index k and one-based rank k refer to different positions. Make the convention explicit in the signature, handle empty input, and decide how NaN or partially ordered objects should behave. A comparator that is not transitive can invalidate partition proofs.

### Applications, engineering constraints and validation

Practical applications include percentile estimation, top-k dashboards, robust median filters and quantile partitions. If repeated percentiles are required from a static dataset, a complete sort may be better than rerunning selection many times. For streamed data that cannot fit in memory, approximate quantile sketches trade error guarantees against storage and merge costs. Test selection on all-equal arrays, duplicates, reverse order, strictly increasing values, and values with negative signs; use sorting as an independent small-input oracle.

## Binary Search

**Core model — Binary Search**

Binary search operates on a monotone predicate or sorted sequence and maintains an interval containing any candidate answer. Half-open intervals [lo,hi) help avoid special cases and support an empty interval.

**Original worked illustration**

In [2,5,8,11,14,17,20], locating 14 compares against 11, then 17, then 14. After three comparisons, a matching index is established.

**Boundary conditions and checks**

For integers, compute the midpoint as lo + floor((hi-lo)/2) when overflow is possible; an unsorted array invalidates the comparison-based pruning.

**Connections in this unit**

The adjacent subjects are Comparison Sorting, Selection, Lower Bounds. They are studied alongside Binary Search because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Binary search is a strategy for maintaining a shrinking set of possible answers under a monotone predicate. Searching a sorted array is one application; finding the earliest feasible resource limit or maximum allowable parameter is another. Two popular interval conventions are [lo,hi] inclusive and [lo,hi) with the right endpoint excluded. Both are correct when updates maintain their stated invariants. The integer midpoint should avoid avoidable overflow in fixed-width languages, for example lo + floor((hi-lo)/2) when subtraction itself is safe. A search loop must make progress even when only one or two candidates remain.

### Derivation and worked trace

Consider the sorted sequence [2,4,4,4,9,12,15]. To find the first occurrence of four, keep the invariant that any earlier candidate must be in [lo,hi). Start lo=0, hi=7. The midpoint three has value four, so set hi=3 rather than returning immediately. Midpoint one also has four, so set hi=1. Midpoint zero has two, so set lo=1. Now lo equals hi, producing index one. Returning from the first equality test would instead produce index three, which is a correct membership answer but not the correct lower-bound position.

### Counterexample and failure diagnosis

The prerequisite for ordinary array binary search is sortedness under the same comparator, not merely that the data looks mostly ordered. A rotated sorted array or data sorted on a different field does not satisfy the usual monotone predicate. Floating-point binary search adds termination considerations because there may be no representable midpoint strictly between adjacent machine values. State an error tolerance or a maximum iteration count and distinguish an approximate root from an exact discrete index. Never convert an unchecked negative search result into an unsigned array index.

### Applications, engineering constraints and validation

Binary search on the answer can solve problems whose objective is not presented as a search. If a predicate feasible(x) becomes true for all x above a threshold, search for the minimum true x. The substantive work is proving monotonicity; without it, halving can permanently discard the correct answer. A good lab plots the predicate over a small finite domain, implements brute-force enumeration as an oracle, and checks binary search against it. This directly tests both the algorithm and the modeling assumption.

## Lower Bounds

**Core model — Lower Bounds**

In a decision-tree model, a comparison has at most three outcomes, but for distinct keys a binary comparison suffices to establish an Omega(n log n) lower bound for sorting. The n! permutations need distinct decision leaves.

**Original worked illustration**

A binary tree with height h has at most 2^h leaves, so h must be at least log2(n!). Stirling's approximation shows log2(n!) grows proportionally to n log2 n.

**Boundary conditions and checks**

The result concerns algorithms that learn ordering only by pairwise comparisons, not counting sort on bounded integer keys or special distributions.

**Connections in this unit**

The adjacent subjects are Comparison Sorting, Selection, Binary Search. They are studied alongside Lower Bounds because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

The comparison-sorting lower bound arises from a decision-tree argument. With n distinct keys, there are n! possible input orders, and a deterministic algorithm based solely on binary comparisons must distinguish all of them to return a correct permutation. A binary decision tree of height h has at most 2^h leaves, so 2^h >= n! and therefore h >= ceil(log2(n!)). Using an asymptotic estimate for the factorial yields Omega(n log n) worst-case comparisons. The lower bound is not a statement about writes, CPU cycles or sorting over a restricted input domain.

### Derivation and worked trace

For four distinct keys, there are 4!=24 possible orders, so a pure binary-comparison algorithm requires at least ceil(log2 24)=5 comparisons in its worst path. This does not say that five comparisons are sufficient for every sorting implementation, nor that every input requires five. Some algorithms use more because they have additional structural constraints. For two keys there are only two orders and one comparison suffices. These small cases are valuable tests of the decision-tree idea because the leaves and branching limits can be enumerated exactly.

### Counterexample and failure diagnosis

The bound assumes comparison questions have at most two outcomes. A three-way comparator can report less, equal and greater, though equality cannot arise for distinct keys; information-theoretic accounting must match the allowed outcomes. Counting sort escapes this lower bound by using an explicit bounded integer range and indexing into buckets. But if the key range is enormous relative to n, the memory cost can make counting sort unattractive. Calling a linear-time integer sort universally superior confuses the abstract computational model with a constrained application.

### Applications, engineering constraints and validation

Information lower bounds are powerful for identifying impossible ambitions. If a feature must produce a complete order of arbitrary records while accessing keys only through comparisons, repeated independent sorting cannot guarantee sub-n-log-n worst-case comparison work. However if data arrives nearly ordered or the system maintains a balanced index incrementally, the cost of an individual update can be logarithmic rather than rebuilding the entire order. The workload and permitted retained state determine which lower bound is applicable.

## Unit 2 integrated computational laboratory

## Integrated laboratory: sorting, searching, and order statistics

A catalog service must support ordering books by publication year, searching by accession number and finding the median checkout count. These are three different computational tasks. Sorting gives an ordered enumeration, exact lookup determines whether a specific identifier is present, and selection identifies one ranked value. A decision about data layout should consider how often each operation runs and whether updates occur between queries. A sorted array can support binary search by year only if its comparator orders by year; it cannot automatically support efficient binary search by an unrelated accession number. Maintaining several indexes can make both queries fast at the cost of additional storage and update coordination.

Work through a fully specified dataset: accession IDs [K7,K2,K5,K1,K9,K3,K8], with checkout counts [10,3,10,7,1,3,12]. Sorting by count ascending with accession ID as the secondary order yields entries with counts 1,3,3,7,10,10,12. The median count is seven, the fourth value under one-based rank. A three-way quickselect partition on pivot seven can separate the three smaller values, one equal value, and three larger values. It then knows the fourth value is the pivot without sorting either side internally. Returning the accession ID associated with the median count requires a tie policy if several books share that count; the numeric median alone is insufficient to select a unique record under all datasets.

Suppose a second service sorts by count descending but searches the array for a particular accession ID with binary search. It may appear to work by accident on one sample. Yet the order is not monotone under the ID comparator, so the reasoning behind binary search is invalid. The fix is to search linearly, maintain a secondary hash index keyed by accession number, or rebuild a correctly ordered index. Do not try to solve a failed precondition by merely adding more test cases. A program that breaks the theorem's assumptions needs a different algorithm or representation.

Stability becomes important when users first sort by title and then by year. If the second sort is stable, records with equal years retain title order, producing a year-primary, title-secondary ordering. An unstable algorithm may reorder equal-year titles unpredictably. This behavior can be checked using records carrying both an ordering key and a unique identity. The test asserts the relative positions of equal-key records, not just that the years are nondecreasing. A sorter that loses a duplicate item can pass a naive sortedness test; a multiset equality check catches the missing data.

There is a fundamental limit on unrestricted sorting by comparisons. For n=5 there are 120 permutations of five distinct values, requiring a binary decision tree of height at least ceil(log2 120)=7. For n=8 there are 40,320 permutations and the lower bound becomes ceil(log2 40320)=16 comparisons. These small numerical bounds are illustrations of the general inequality 2^h≥n!, not exact minimum counts for a particular named sorter. Comparison-based sorting cannot guarantee one comparison per arbitrary element for growing n, but counting and radix methods can exploit a constrained key domain and pay different costs.

Build tests around the contract: empty arrays, singleton arrays, all equal keys, alternating high and low keys, reverse order, multiple distinct records with identical primary keys, and values near the integer representation limit. For binary search, test lower bound, upper bound, missing values between present keys and a missing key at each end. Instrument comparison counts separately from moves or swaps; a stable merge sort often copies arrays, and those writes matter for memory performance. Report whether external allocations are included.

A controlled scaling study compares array sizes 64,128,256,512 and 1,024, counting comparisons and checking them against a theoretical growth envelope. Do not assert that an n log n implementation must exactly double its comparison count when n doubles: the logarithmic factor changes, input patterns influence branches, and implementation overhead matters. Instead test that the measured counts remain within a conservative provable worst-case upper bound for the algorithm actually used. For quicksort, deliberately use sorted inputs and a first-pivot implementation to expose its quadratic degeneration. Then randomize pivots with recorded seeds and compare the distribution across trials.

Finish by comparing full sorting and selection. A single median query over a large array may favor expected-linear quickselect, but repeated quantile queries on a static array may justify sorting once and then answering each query by indexing. If users need stable sorted output rather than just the median, selection alone does not meet the functional requirement. Performance optimization starts with delivering the correct object, not merely a smaller asymptotic expression.

### Independent audit exercise: sortedness as a proof obligation

A package-distribution system stores shipment records ordered by a numeric tracking sequence. A binary-search method returns the first record whose sequence is at least a requested threshold. If its precondition is the ascending ordering invariant, inserting a record into the middle without preserving that ordering invalidates every subsequent binary-search correctness proof. The search routine has not become mathematically wrong; it is being called on an illegal state. Define the array's representation invariant and enforce it through the update API.

Compare two alternatives. Maintain a sorted array and use binary search to find an insertion point, then shift following records; lookup costs logarithmic comparisons but insertion may move linearly many records. Maintain an ordinary unsorted array and append in amortized constant time, then search linearly; writing is fast but repeated queries can be expensive. A balanced tree offers logarithmic worst-case ordered queries and updates under its balancing guarantees, though it uses node metadata and generally worse cache locality. An application with millions of reads and rare updates may favor the sorted array; a stream with continuous ordered updates may favor the tree.

Construct a cross-check using records of sequences [3,3,5,8,8,11]. Lower_bound(8) should yield zero-based index three. Upper_bound(8) should yield index five. The interval [3,5) therefore contains both records with key eight. For missing threshold seven, both bounds produce index three. For threshold twelve, lower bound returns the length six, which is a valid insertion position rather than a valid element index. A caller that immediately dereferences position six is faulty even though the search result is correct.

In a full program, compare every returned boundary against a small linear scan oracle. Use a total comparator, test ties, preserve record multiplicity and record whether the array is allowed to mutate. Avoid the common shortcut of saying that binary search locates duplicates: a generic membership search identifies some occurrence, while equal-range APIs must specifically implement lower and upper boundary semantics.

## Worked questions and solutions

### Question 1: Comparison Sorting: worked application 1

Merge the sorted records [(2,A),(4,B)] and [(2,C),(3,D)], maintaining stable order.

1. **Set up the model and conditions:** Compare the two leading keys 2 and 2; emit the left record (2,A).

2. **Carry out the calculation or proof:** Then emit (2,C), (3,D) and (4,B) as remaining heads permit.

3. **State the result and its scope:** The stable merged sequence is (2,A),(2,C),(3,D),(4,B).

**Answer:** The stable merged sequence is (2,A),(2,C),(3,D),(4,B).


### Question 2: Selection: worked application 2

Find the third-smallest element of [9,1,6,3,8] without sorting the entire sequence.

1. **Set up the model and conditions:** Partition around pivot 6: smaller values are 1 and 3, pivot is 6, greater values 8 and 9.

2. **Carry out the calculation or proof:** Exactly two elements are smaller than 6.

3. **State the result and its scope:** The requested third order statistic is 6.

**Answer:** The requested third order statistic is 6.


### Question 3: Binary Search: worked application 3

Trace binary search for 14 in [2,5,8,11,14,17,20] using inclusive bounds 0..6.

1. **Set up the model and conditions:** At mid 3 the value 11 is too small, so search indices 4..6.

2. **Carry out the calculation or proof:** At mid 5 the value 17 is too large, so search index 4.

3. **State the result and its scope:** At mid 4 the value is 14; search succeeds in three comparisons.

**Answer:** At mid 4 the value is 14; search succeeds in three comparisons.

