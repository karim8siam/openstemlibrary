# Algorithms — Unit 1: Algorithm analysis


## Asymptotic Bounds

**Core model — Asymptotic Bounds**

A worst-case upper bound O(g(n)) means there are constants c and n0 for which T(n) is no larger than c*g(n) for every n at least n0. Omega reverses the inequality; Theta requires both. These statements are about functions as input grows, not seconds on a particular laptop.

**Original worked illustration**

If a loop performs 3n squared plus 5n plus 7 primitive operations, it belongs to Theta(n squared). For n at least 1 the expression is at most 15n squared, establishing an upper bound constructively.

**Boundary conditions and checks**

Never call a program O(1) simply because its test input is small; distinguish input length from numeric input value, and amortized from worst-case cost.

**Connections in this unit**

The adjacent subjects are Recurrences, Amortized Analysis, Correctness Proofs. They are studied alongside Asymptotic Bounds because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

An asymptotic bound is a statement about a family of running-cost functions, not a ranking of two finished programs. Let input size mean the number of stored keys, unless the representation has a different meaningful measure such as bit length. The cost model must say whether an operation means a comparison, pointer traversal, multiplication, allocation, or full machine instruction. A constant upper bound on one kind of primitive does not imply that all other primitives are bounded by the same constant. Proving a worst-case claim also differs from observing an average over a sample of random inputs. The mathematical quantifiers matter: an upper bound must hold eventually for every sufficiently large legal size and every input covered by the stated worst-case model.

### Derivation and worked trace

For T(n)=7n²+9n+12, the inequalities n<=n² and 1<=n² for n>=1 give T(n)<=28n². A lower bound follows from T(n)>=7n², so T is Theta(n²). Neither constant 28 nor threshold one is a claim about optimal engineering; they are witnesses satisfying the definition. Now compare A(n)=80n and B(n)=n². For n=5 the nominal counts are 400 and 25, while for n=100 they are 8000 and 10000. The asymptotically slower function may cost fewer operations at small sizes. This is why a benchmark should report both the size range and the observed crossover rather than claiming that big-O identifies the faster implementation at every scale.

### Counterexample and failure diagnosis

A particularly tempting mistake is to say that an algorithm with two nested loops necessarily takes quadratic time. The inner loop might be executed only once across all outer iterations, as in a two-pointer scan; the correct quantity is the sum of inner iterations over the complete run. Conversely, one visible loop might call a costly sorting routine inside its body. Analyze the operations actually performed and include work in called functions. If size is an integer encoded in binary, iterating from one through its numeric value can be exponential in the bit length. Distinguishing numeric value from encoding length is essential for claims about polynomial-time algorithms.

### Applications, engineering constraints and validation

For an inverted index lookup service, an O(log n) comparison tree and an O(1) expected hash lookup have distinct assumptions: the tree maintains total order, while the hash model assumes suitable distribution and collision control. A locality-sensitive implementation may win even with a worse asymptotic count because one contiguous scan has fewer cache misses than random pointer accesses. A responsible engineering report records the machine model, memory budget, input distribution, maximum permitted latency, and observed operational counts. Reproduce each candidate on adversarial patterns, not just conveniently shuffled arrays.

## Recurrences

**Core model — Recurrences**

A recurrence expresses a problem's cost in terms of smaller inputs, but the base case and rounding determine whether a derivation is valid. Substitution, recursion trees, and a properly applied Master theorem provide complementary methods.

**Original worked illustration**

For n a power of two, T(n)=2T(n/2)+n with T(1)=1 has solution T(n)=n(log2 n+1). At each of log2 n internal levels the combined nonrecursive work is n.

**Boundary conditions and checks**

Do not apply a balanced-divide Master theorem to T(n)=T(n-1)+n: its subproblem shrinks by subtraction, yielding Theta(n squared), not Theta(n log n).

**Connections in this unit**

The adjacent subjects are Asymptotic Bounds, Amortized Analysis, Correctness Proofs. They are studied alongside Recurrences because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

A recurrence is a specification of how a problem's cost decomposes. It becomes a proof only after the number of subproblems, their exact sizes, nonrecursive overhead, and base cases have been stated. An equation such as T(n)=2T(n/2)+n silently assumes clean division; for arbitrary positive integers an implementation usually uses floor and ceiling, which must be handled in a rigorous bound. A recursion tree measures work at each depth and counts the leaves, making it possible to explain a logarithmic recursion depth and linear per-level cost without relying on a memorized theorem name.

### Derivation and worked trace

Suppose mergesort splits sixteen keys into two equal halves. At the root there is work proportional to sixteen for merging; the next depth has two subproblems of eight and therefore again sixteen merged elements. The following depths have four runs of four, then eight runs of two. Each of the four internal levels touches sixteen elements, so the total merge-touch count is 64. A different cost convention counts key comparisons and can produce fewer than 64 comparisons; those are not contradictory because the primitive operations differ. For T(1)=1 and T(n)=2T(n/2)+n on powers of two, the leaf work adds n and therefore T(n)=n(log2 n+1).

### Counterexample and failure diagnosis

The Master theorem is inapplicable when the recurrence does not match its hypotheses. For T(n)=T(n-1)+n, repeatedly substitute to obtain n+(n-1)+...+2+T(1), hence a quadratic sum. For T(n)=T(n/2)+1, each level incurs constant work and there are logarithmically many levels. A divide-and-conquer routine whose pivot consistently creates subproblems of sizes zero and n-1 follows the first kind of recursion, even if its source code contains a function named partition. Always derive the size relationship from the algorithm and check whether the side work changes with the chosen pivot or split.

### Applications, engineering constraints and validation

Recurrences are also useful for parallel analysis. A binary recursive algorithm can have logarithmic critical-path depth while still performing linear or superlinear total work. A system with eight workers cannot divide a sequential dependency chain into eight independent tasks. Quantify work, span, communication and memory duplication separately. An optimized implementation might change the base case to insertion sort for tiny partitions; that changes constants and the recursion tree near its leaves, but need not change the overall asymptotic class.

## Amortized Analysis

**Core model — Amortized Analysis**

Amortized analysis bounds the total cost of a sequence, not the worst cost of any single operation. Aggregate analysis, banker credits and potential functions are equivalent accounting viewpoints when their invariants hold.

**Original worked illustration**

In a dynamic array starting with capacity one and doubling when full, insertion number nine may copy eight existing elements, but the copies over n appends sum to less than n for each level of capacity, so the total copying is below 2n.

**Boundary conditions and checks**

The potential must remain bounded below to imply a total-cost bound. Never confuse average over an assumed probability distribution with amortized cost over adversarial sequences.

**Connections in this unit**

The adjacent subjects are Asymptotic Bounds, Recurrences, Correctness Proofs. They are studied alongside Amortized Analysis because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Amortized analysis proves a bound on a sequence of updates even when individual updates may be costly. It needs no probabilistic distribution: an adversary may choose the input sequence, provided that the data structure satisfies the stated operational contract. In the aggregate method, sum the exact expensive events and divide by the number of operations. In the accounting method, charge certain cheap operations more than they cost and save credits to pay for future expensive ones. In the potential method, track a mathematical quantity of the current state so that actual cost plus potential change is inexpensive over the sequence. The three methods explain the same inequality from different perspectives.

### Derivation and worked trace

Imagine appending thirteen elements to an initially empty dynamic array of capacity one. Capacity changes occur when the second, third, fifth, and ninth elements arrive. Those four reallocation events copy one, two, four, and eight old elements, totaling fifteen copies across thirteen appends. A single ninth append costs at least eight copies plus one write, but the number of copied elements over many updates is geometric rather than quadratic. For n appends, the sum of copied capacities is smaller than twice the final occupied size under the usual doubling policy. The exact constant varies with the starting capacity and whether copies and writes share the same cost unit.

### Counterexample and failure diagnosis

A common false generalization is that all operations on a resizable array have amortized constant cost. Inserting at the beginning can shift the occupied prefix even when no reallocation occurs, and that is linear per operation. Another error is to infer expected cost from amortized cost: the latter bounds any permitted sequence, while the former depends on a probability model. When a potential function is allowed to become arbitrarily negative, its final value can invalidate a claimed total-cost bound. Explicitly establish that the potential is nonnegative or otherwise lower-bounded for all states reachable under the operation sequence.

### Applications, engineering constraints and validation

Operationally, amortization is attractive for applications that can tolerate occasional latency spikes, but not sufficient for strict real-time response limits. Compare a dynamic array that occasionally moves thousands of elements with a fixed-capacity ring buffer that rejects updates when full. The first may have superior space utilization but an unpredictable worst-case append; the second bounds each operation under a fixed capacity contract. Engineers sometimes reserve space in advance or grow incrementally to smooth latency. These are changes to the algorithmic guarantee, not exceptions to the mathematics.

## Correctness Proofs

**Core model — Correctness Proofs**

A correctness argument needs a precise precondition, postcondition, loop invariant and termination measure. Partial correctness says that if termination occurs, the result is valid; total correctness also establishes that execution ends.

**Original worked illustration**

For insertion sort, after iteration i the prefix of length i+1 is sorted and is a permutation of the original prefix. Initialization is immediate; inserting the next key preserves the invariant; the outer index eventually reaches n.

**Boundary conditions and checks**

Testing many inputs may expose errors but cannot prove a universal algorithmic claim; a missing termination argument invalidates a purported total-correctness proof.

**Connections in this unit**

The adjacent subjects are Asymptotic Bounds, Recurrences, Amortized Analysis. They are studied alongside Correctness Proofs because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Correctness requires a specification before a proof. A precondition describes legal inputs; a postcondition describes the observable result. A loop invariant must hold initially, remain true after one iteration whenever the loop continues, and imply the required postcondition when the loop ends. Termination needs a well-founded measure, often a nonnegative integer strictly decreasing or a bounded counter strictly increasing. Partial correctness without a termination argument establishes only that an output is valid if the procedure eventually returns. For sorting, correctness has two independent components: the final sequence is ordered, and it is a permutation of the input multiset.

### Derivation and worked trace

Take insertion sort on [5,1,4,2]. Before processing the key 1, the prefix [5] is ordered. Move 5 to the right and insert 1 to obtain [1,5,4,2]. Process key 4 to get [1,4,5,2]; then process key 2 to get [1,2,4,5]. At each stage, the processed prefix is sorted and contains exactly the elements originally observed in that prefix plus the key just inserted. The inner loop's index moves left until it reaches zero or finds a predecessor no larger than the key. That finite movement supplies a termination measure. A stable implementation uses a strict comparison when shifting equal keys so earlier equal items retain their relative order.

### Counterexample and failure diagnosis

Testing a million randomly generated arrays cannot establish a universal invariant, but it can detect a false one quickly. Consider a proposed binary-search implementation using while left<right yet claiming that the target always remains in the inclusive interval [left,right]. If the update drops mid without first checking the target at mid, the invariant fails. Write an explicit statement of the interval semantics: inclusive-inclusive, inclusive-exclusive, or some other convention. Then check each branch's new interval. Off-by-one bugs often come from mixing conventions rather than misunderstanding binary search at a conceptual level.

### Applications, engineering constraints and validation

Proof-driven development is useful in secure parsers, storage engines and distributed protocols. State which values may be null, whether integer arithmetic can overflow, whether duplicate keys exist and whether iteration can observe concurrent changes. A formal invariant can rule out classes of errors that a test suite might miss. Conversely a proof about ideal mathematical integers does not automatically establish correctness in a language using fixed-width arithmetic. Link the proof's assumptions to runtime assertions and test cases so an implementation review can decide whether the abstract model matches the real code.

## Unit 1 integrated computational laboratory

## Integrated laboratory: from requirements to asymptotic proof

A performance claim is not meaningful until the input size, the permitted operations, and the output contract have been specified. Consider an application that reports the five highest scores from an array of student examination records. One implementation sorts all n records and returns the final five; another maintains a bounded heap of the best five while scanning. If n is large and five remains fixed, these alternatives have markedly different work profiles. A comparison sort performs O(n log n) comparisons in general; a fixed-capacity heap of size five uses O(n log 5) work after constant-size initialization, which is linear in n. Yet the heap approach must decide whether equal scores are ordered by registration ID and whether students with missing scores are legal inputs. An underdefined API can be made faster and still be wrong.

Construct a precise contract: input consists of n non-null records, each holding an integer score and a unique identifier; order primarily by descending score and secondarily by ascending identifier; return min(5,n) records without changing the original array. Now the full-sort and bounded-heap implementations have the same observable target. For the heap, maintain the worst of the currently selected records at its root, using a comparator reflecting the reverse of the final preference. At each new record, decide whether it outranks that root; if so, replace the root and restore the heap property. The loop invariant says that after examining the first i records, the heap contains exactly the best min(5,i) records under the specified total ordering. Initialize it from no records; preserve it through each update; after n records the invariant gives the result. The selected records may need a final sort because heap order does not mean that a heap's array representation is sorted.

Analyze memory separately. A standard sort may use additional temporary memory depending on the implementation; the heap's auxiliary storage has size at most five, not counting the copied result. If an array of records is returned, that output memory is unavoidable. If n=0, an empty result is correct and both algorithms must avoid reading an absent first item. If n=3, all three legal records are returned in the specified order. If the input has six identical scores, the ID tie-breaker determines exactly which record is excluded. These cases test semantics that random distinct-score benchmarks might not exercise.

The word worst-case requires a particular input model. Heap comparisons are bounded as described even if scores are sorted or adversarial. A full comparison sort's worst-case bounds depend on whether it is mergesort, heapsort, introsort or a vulnerable first-pivot quicksort. The built-in sort of a language may change algorithms across versions, so a statement about it needs an implementation reference. Time in seconds is further affected by comparator cost, object layout and memory allocation. Counting key comparisons makes a cleaner algorithmic experiment than dividing one stopwatch reading by another.

A useful mathematical check selects n=100 and k=5. The comparison upper bound for a simple per-record heap update is proportional to n times the heap height, with height at most floor(log2 5)=2, plus construction and final ordering. This does not predict exactly two comparisons for every record, because some are rejected after a root comparison and because the heap repair may compare both children. Rather than inventing a precise count, instrument the implementation and publish the observed sequence. Compare the instrumented count against a proof-backed upper bound, not against a guessed equality.

In a second experiment, analyze a dynamic array that appends records before processing. Doubling capacity from one when full incurs copies at capacities 1,2,4,8,16 and so on. For the first 20 appends, the expansions at append indices 2,3,5,9,17 copy 1+2+4+8+16=31 old entries. The total is small compared with 20 times 20, but the seventeenth append alone copies 16 entries. The correct guarantee is amortized constant insertion, not constant worst-case insertion. Reserve space if the maximum is known and latency spikes are unacceptable.

Finally separate correctness evidence from performance evidence. A property test can compare the heap's output to the sorted oracle for hundreds of arrays, including duplicates and negative scores; it does not establish the asymptotic upper bound. A proof can establish the upper bound, but does not establish that the implementation uses the comparator correctly. The two forms of evidence strengthen one another. Document every assumption, including whether identifier comparison is constant time or proportional to string length. A reliable algorithm chapter teaches students to ask which part of the conclusion came from mathematics, which from tests, and which remains an empirical engineering hypothesis.

### Independent audit exercise: input representation and accounting

Analyze a duplicate-detection task under three representation choices. The input is a list of n strings, and the output is a Boolean indicating whether any two strings are exactly equal. A simple pairwise algorithm compares every unordered pair until it finds a duplicate. In the worst case there is no duplicate and it performs n(n-1)/2 string-equality tests. That count alone is not full running time: comparing two long strings may inspect many characters. If the strings each have length at most L, an elementary upper bound is O(n²L) character comparisons. Reporting O(n²) without the chosen primitive and its cost hides this distinction.

Sorting the strings and comparing neighbors creates a different route. A comparison sort uses O(n log n) string comparisons, and adjacent equal strings become neighbors in the sorted order; the input can be copied to avoid mutation. With costly lexicographic comparisons, an O(nL log n) upper bound is informative under a simplistic maximum-length model. Hashing offers expected fast lookup under an appropriate collision model, but calculating each string's hash visits its characters; expected O(nL) character work plus equality checks is a more useful approximation than declaring the entire problem O(n). Adversarial collisions can make worst-case guarantees weaker.

Test the same semantic contract with empty input, one string, two equal strings, strings differing only in capitalization, strings with visually identical but differently normalized Unicode, and a million repeated instances of one very short string. Define whether equality uses code units, normalized code points, or case-insensitive comparison before constructing the oracle. A reliable experimental report counts hash evaluations, equality calls and character inspections separately. The methods should agree on output when they use the same equality definition, despite their different performance models.

The analysis also illustrates space requirements. Pairwise comparison needs essentially constant auxiliary storage. A sort may allocate an array copy and temporary buffers. A hash table may retain each distinct key and buckets. The best algorithm under a memory limit can differ from the best under a throughput limit. A graded solution must connect the Big-O claim, the primitive operation model and the user's constraints instead of treating them as interchangeable.

## Worked questions and solutions

### Question 1: Asymptotic Bounds: worked application 1

For T(n)=3n²+5n+7, prove an O(n²) bound for integers n≥1.

1. **Set up the model and conditions:** For n≥1, use n≤n² and 1≤n² to bound lower-order terms.

2. **Carry out the calculation or proof:** Then 3n²+5n+7≤(3+5+7)n²=15n².

3. **State the result and its scope:** Choose c=15 and n0=1; the Big-O definition is satisfied.

**Answer:** Choose c=15 and n0=1; the Big-O definition is satisfied.


### Question 2: Recurrences: worked application 2

Solve T(n)=2T(n/2)+n when n is a power of two and T(1)=1.

1. **Set up the model and conditions:** At level j the 2^j subproblems each cost n/2^j, summing to n.

2. **Carry out the calculation or proof:** There are log2(n) non-leaf levels; n base leaves each cost one.

3. **State the result and its scope:** T(n)=n log2(n)+n.

**Answer:** T(n)=n log2(n)+n.


### Question 3: Amortized Analysis: worked application 3

An array doubles from capacity 1. Count element copies during the first 10 appends.

1. **Set up the model and conditions:** Capacities change at append numbers 2,3,5 and 9.

2. **Carry out the calculation or proof:** The reallocations copy 1,2,4 and 8 prior elements.

3. **State the result and its scope:** Total 15 copies, in addition to the ten writes of new elements.

**Answer:** Total 15 copies, in addition to the ten writes of new elements.

