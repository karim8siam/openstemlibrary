# Algorithms — Unit 3: Divide and conquer


## Decomposition

**Core model — Decomposition**

Divide-and-conquer algorithms must define the subproblem, disjoint or overlapping responsibilities, and a recombination rule. A recursion only saves work when its subproblem structure reduces the original difficulty.

**Original worked illustration**

A mergesort call on eight entries creates two groups of four, then four groups of two, and finally eight singletons; the merge phase restores the ordering using linear work at each level.

**Boundary conditions and checks**

Recursive decomposition is not automatically efficient: recomputing the same overlapping Fibonacci subproblems yields exponential work without memoization.

**Connections in this unit**

The adjacent subjects are Merge Strategies, Geometric Algorithms, Matrix Algorithms. They are studied alongside Decomposition because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Divide and conquer partitions a problem into smaller subproblems, solves them and combines their answers. The decomposition must make subproblems genuinely smaller and preserve enough information for the combination step to reconstruct a correct global result. Independent subproblems may run in parallel; overlapping subproblems suggest memoization instead. A balanced split is a performance objective, not a guarantee automatically implied by recursion. The combine cost can dominate if a routine copies large intermediate arrays at each level or repeatedly concatenates immutable strings.

### Derivation and worked trace

Consider computing the maximum in an array of 16 numbers. Split into two blocks of eight, compute each block's maximum recursively, and compare the two winners. The recurrence is C(n)=2C(n/2)+1 for power-of-two n, C(1)=0, giving exactly n-1 comparisons. A linear left-to-right scan also needs n-1 comparisons; recursion has not improved the total comparison count. It has, however, exposed parallel subproblems, yielding a logarithmic comparison depth on suitable parallel hardware. This contrast demonstrates why work and span should be reported separately when evaluating parallel algorithms.

### Counterexample and failure diagnosis

A broken divide-and-conquer design may compute a correct answer at every leaf but combine them incorrectly. If a subproblem returns an index relative to its own slice, the parent must translate the right-slice index to a global offset. Failure to do so yields plausible indices only for the left half. Likewise maximum-subarray solutions need enough boundary information to consider segments crossing the split; taking the maximum of the left-only and right-only optimum is insufficient. Define the recursive return contract before writing code.

### Applications, engineering constraints and validation

In practical systems recursion also consumes call-stack space. A depth of Theta(log n) is usually manageable, but unbalanced recursion can reach Theta(n) and overflow a stack for sufficiently large input. Iterative implementations or explicit stacks can offer more predictable resource use. Before claiming parallel speedup, measure task creation, allocation, synchronization and cache traffic. For small partitions a sequential base case commonly outperforms creating new tasks, even when unlimited parallelism would be mathematically available.

## Merge Strategies

**Core model — Merge Strategies**

The merge phase should preserve a semantic invariant, such as sorted prefixes, cross-boundary validity, or an aggregate statistic. Its complexity can dominate otherwise efficient recursive calls.

**Original worked illustration**

Counting inversions in [3,1,2] splits [3] and [1,2]. When 3 is greater than the right head 1, it contributes one inversion; comparing 3 against 2 contributes another, for total two.

**Boundary conditions and checks**

Counting only inversions inside child arrays misses cross-boundary pairs, so the merge logic must explicitly include them.

**Connections in this unit**

The adjacent subjects are Decomposition, Geometric Algorithms, Matrix Algorithms. They are studied alongside Merge Strategies because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Merging combines two already sorted sequences into one sorted sequence. It is not enough to know that each input is sorted; the algorithm must preserve elements, advance at least one pointer after each comparison, and copy any unconsumed suffix. Two monotone input cursors supply a direct invariant: everything already emitted is sorted and no larger than any item not yet emitted. A stable merge chooses from the left input on equality so that equal-key records preserve their relative ordering from the original concatenation.

### Derivation and worked trace

Merge [1,4,7,10] with [2,4,8,11]. Compare 1 and 2, output 1. Compare 4 and 2, output 2. Compare 4 and 4, choose the left 4 for stability. Then choose the right 4, followed by 7 and 8, then 10 and 11. The final merged sequence is [1,2,4,4,7,8,10,11]. A naïve equality branch that advances both cursors after emitting one value would lose an item. The critical test therefore checks multiplicities, not just nondecreasing order. An implementation must also avoid reading from an exhausted run.

### Counterexample and failure diagnosis

The worst-case key-comparison count for two nonempty runs of lengths a and b is a+b-1. Once one run empties, no further comparisons are needed to copy the rest. This bound does not imply that every merge takes a+b-1 comparisons: if every key in the left run precedes every key in the right run, only a comparisons are required in a standard left-first merge. Input arrangement affects comparisons while the number of output writes remains a+b. Distinguish a temporary-buffer merge from an in-place merge; the latter often involves much more complicated movement and proofs.

### Applications, engineering constraints and validation

Merging appears in external sorting, distributed analytics and versioned search indexes. On disks and networks, sequential throughput matters more than isolated comparison counts. An LSM storage engine repeatedly merges ordered runs but also faces write amplification, duplicate-key resolution and tombstone semantics. A merge that is correct for simple integer arrays can be wrong for versioned key-value entries if it discards a newer deletion record. Specify item identity, ordering, tie policy and output semantics before reusing the routine.

## Geometric Algorithms

**Core model — Geometric Algorithms**

Geometric divide-and-conquer problems require correct boundary handling as well as asymptotic analysis. For closest-pair algorithms, presorting and a bounded-neighbor strip argument are central.

**Original worked illustration**

Given planar points (0,0), (2,1), (4,0), (2,2), the closest pair is (2,1) and (2,2), separated by distance 1. A vertical split may separate the closest pair, requiring a strip check.

**Boundary conditions and checks**

Naively comparing all points across the split can restore quadratic time; floating-point geometric predicates also require tolerance and degeneracy analysis.

**Connections in this unit**

The adjacent subjects are Decomposition, Merge Strategies, Matrix Algorithms. They are studied alongside Geometric Algorithms because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Geometric divide-and-conquer algorithms often exploit order in physical space to avoid examining every pair. The closest-pair problem is a central example. Split points by x-coordinate, solve each side and let delta be the smaller returned distance. Any cross-border pair beating delta must lie in a narrow vertical strip around the split. Sorting strip points by y-coordinate allows checking only a bounded number of subsequent candidates per point, yielding an O(n log n) algorithm with careful presorting. The correctness proof hinges on planar packing, not just on the idea that nearby x-coordinates imply nearby points.

### Derivation and worked trace

Take points (0,0), (2,2), (3,3), (8,1), (9,1). Their closest pair is (8,1) and (9,1), with Euclidean distance one. A naïve all-pairs calculation on five points examines ten distances. For larger n the number of unordered pairs is n(n-1)/2, quadratic. A geometric solver can use squared distances to avoid expensive square roots while comparing candidates, because square root is monotone on nonnegative inputs. However raw squared coordinate differences may overflow fixed-width integer types if coordinates are large. Choose an arithmetic representation that preserves comparisons.

### Counterexample and failure diagnosis

Common failures include sorting the strip repeatedly at each recursive level, which can unintentionally add an extra logarithmic factor, and ignoring points exactly on a split boundary. Duplicated coordinates create a true minimum distance of zero; a robust implementation should handle them without dividing by delta or assuming strict coordinate separation. Degenerate configurations such as collinear points need not invalidate the mathematical algorithm but can expose hidden implementation assumptions. Test symmetric point sets, identical points, thin strips and coordinates close to numeric limits.

### Applications, engineering constraints and validation

Geometric algorithms support collision checking, map features, image registration and scientific simulation. In high dimensions, spatial indexes often degrade because locality becomes less discriminating, and approximate nearest-neighbor methods may be preferable. This is not a failure of the two-dimensional packing proof; it is a change in the geometric setting. An engineering comparison should report dimension, coordinate precision, metric, update frequency and whether exactness is mandatory.

## Matrix Algorithms

**Core model — Matrix Algorithms**

Matrix algorithms expose a tradeoff between asymptotic arithmetic and implementation constants. Standard dense multiplication uses three nested indices and Theta(n cubed) multiply-add terms.

**Original worked illustration**

For two 2-by-2 matrices A=[[1,2],[3,4]] and B=[[5,6],[7,8]], entry (1,1) is 1*5+2*7=19. Computing the four entries uses eight scalar multiplications under the standard method.

**Boundary conditions and checks**

Asymptotically faster schemes can create numerical-stability and temporary-memory costs. Verify matrix dimensions before claiming a product exists.

**Connections in this unit**

The adjacent subjects are Decomposition, Merge Strategies, Geometric Algorithms. They are studied alongside Matrix Algorithms because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Divide-and-conquer matrix algorithms show that different algebraic factorizations can reduce arithmetic work. Ordinary n-by-n matrix multiplication computes n² outputs, each as a dot product with n multiplications and roughly n additions, giving cubic arithmetic cost. Strassen's method partitions matrices into quadrants and replaces eight half-size multiplications with seven using additional matrix additions and subtractions. The recurrence T(n)=7T(n/2)+O(n²) yields an exponent log2 7 of about 2.807, better than three in the abstract arithmetic model. This improvement is neither free nor universally faster for finite sizes.

### Derivation and worked trace

Multiply A=[[1,2],[3,4]] and B=[[5,6],[7,8]] by ordinary row-column products. The result is [[19,22],[43,50]], since the top-left entry is 1*5+2*7=19 and the bottom-right entry is 3*6+4*8=50. This tiny case is useful as an exact oracle for any recursive or accelerated implementation. Split-based algorithms should produce the same values under exact arithmetic. In floating point the order of additions matters, so the last few bits may differ, requiring a tolerance tied to input magnitude and expected numerical conditioning.

### Counterexample and failure diagnosis

Padding matrices to powers of two can add storage and operations; ignoring the padded dimensions when mapping the output back can create incorrect result shapes. Strassen's reduced multiplication count comes with extra additions, temporary arrays and stability concerns. A tuned library typically switches to a straightforward blocked kernel below a threshold. The switch point depends on hardware, element types and memory layout. The asymptotic exponent by itself is insufficient to predict whether a 100-by-100 multiplication benefits.

### Applications, engineering constraints and validation

Applications such as machine learning often prioritize fast dense linear algebra, but the fastest practical algorithm may rely on vectorized kernels, cache tiling and specialized hardware instructions rather than a theoretically lower multiplication exponent. For sparse matrices, the nonzero structure becomes central; dense complexities can be misleading. Validate against a simple trusted multiplication oracle on identity, zero, diagonal, rectangular and randomly generated small matrices, and report numeric error separately from performance.

## Unit 3 integrated computational laboratory

## Integrated laboratory: recursive work, parallel span, and geometric precision

A parallel algorithm should be evaluated through both total work and the longest dependency chain. For a balanced recursive maximum over sixteen values, the total number of comparisons is fifteen regardless of whether the comparisons run sequentially or in a tree. A serial scan performs those comparisons one after another; a binary reduction tree can complete them in four dependent rounds if each round's comparisons run in parallel. Four rounds do not mean four processor instructions or four milliseconds, because data transfer and scheduling overhead are omitted. Distinguish the theoretical span from actual wall-clock speedup on a finite machine.

Take values [4,1,8,2,9,3,5,7]. The first comparison round can produce winners [4,8,9,7] from adjacent pairs. The second yields [8,9], and the third yields [9]. The tree has seven comparisons and three rounds. A sequential scan still needs seven comparisons but has seven dependent accumulator updates. These two schemes compute the same maximum and expose different parallel structures. For an array with one item no comparison is required, a base case that must appear in both the recurrence and the code.

Now consider the closest-pair problem in two dimensions. The brute-force oracle enumerates pairs for a small point set, computes squared Euclidean distance and records the smallest value. If points are (0,0),(6,8),(1,1),(3,2), their squared distances include 2 between (0,0) and (1,1), 13 between (0,0) and (3,2), and 5 between (1,1) and (3,2). The minimum is therefore 2, corresponding to distance sqrt(2). A recursive spatial algorithm must return the same result. Its strip reasoning examines candidate cross-boundary pairs rather than pretending that the closest pair always lies entirely on one side of the divide. A critical invariant is that delta already bounds the closest distance found within the individual halves.

Presorting points by x and y can prevent repeated sorting inside recursive calls. But maintaining the two orderings requires careful partition bookkeeping when x coordinates tie. A code path that assigns all equal-x points to the same side can create seriously unbalanced recursion even though the conceptual split was by count. Tests should include many points on the same vertical line, repeated coordinates, and symmetric grids. If coordinates are huge signed integers, evaluating (x1-x2)^2 in a narrow integer type can overflow; testing only small coordinates conceals that risk.

The same discipline appears in recursive matrix multiplication. For A=[[2,1],[0,3]] and B=[[4,5],[6,7]], direct multiplication produces [[14,17],[18,21]]. Verify each output entry by dot product: top-left equals 2*4+1*6=14; top-right equals 2*5+1*7=17. An optimized block algorithm must match this oracle. A Strassen implementation that pads dimensions to a power of two must trim the result back to the actual shape, preserve matrix ordering and account for temporary storage. When multiplying floating-point matrices, compare against a numerically reliable reference with a justified error tolerance rather than demanding bitwise identity under reordered arithmetic.

A broader engineering question is where recursion should stop. The recurrence T(n)=2T(n/2)+an may predict O(n log n) total work, but a call that handles one or two elements may cost more in overhead than an iterative implementation. A hybrid algorithm chooses a fixed small threshold, solves below it directly and uses recursion above it. The asymptotic class can remain unchanged while real performance improves. This does not validate any universal threshold: measure the break-even point under realistic input types and hardware.

When parallelizing divide-and-conquer, control task proliferation. Creating two new tasks for every one-element subproblem can produce more scheduling work than useful arithmetic. A work-stealing runtime, chunked leaf processing or explicit task cutoff can reduce overhead. Also check whether two tasks write overlapping slices; disjoint recursion in an abstract array does not automatically establish absence of data races if the implementation shares scratch buffers. A correct parallel design pairs the mathematical subproblem decomposition with an ownership or synchronization policy.

The capstone assessment should have two independent parts: prove that the recursive combine rule yields the correct answer under the chosen invariant, and compare output against a small brute-force oracle. A failed test can indicate a coding bug, a mistaken base case, or an invalid model assumption. A passed test is evidence about the tested instances; the proof is what establishes the universal claim.

### Independent audit exercise: recursive interface contracts

Create a maximum-subarray function returning the largest sum of a nonempty contiguous subsequence. On input [4,-7,5,6,-2,3], the best segment [5,6,-2,3] sums to twelve. A recursive routine that compares only the best entirely-left and entirely-right segments may miss an optimum crossing its midpoint. To combine correctly it needs the maximum suffix sum of the left half and maximum prefix sum of the right half. The crossing candidate is their sum. Each subproblem can return four values: total sum, best prefix, best suffix and best subarray; two such summaries combine in constant time.

Suppose one summary has total A, best prefix P_A, best suffix S_A, best segment B_A, and the neighboring summary has corresponding B values. Their combined total is A+B. The best prefix is max(P_A, A+P_B); best suffix is max(S_B, B+S_A); and best subarray is max(B_A,B_B,S_A+P_B). These identities account for the three possible locations of an optimum: wholly left, wholly right or crossing the boundary. Inductively, if summaries are correct for the two halves, the formulas provide a correct summary for their concatenation.

Do not silently allow the empty subarray unless the specification permits it. On [-4,-2,-8], a nonempty maximum-subarray answer is -2, whereas an empty-allowed variant may return zero. This semantic difference changes base cases and tests. Recovering the actual start and end indices requires storing or reconstructing witness positions along with the values. Avoid stringifying a result as just the maximum number when users need the location of the segment.

The four-value summary also supports parallel reduction: independent array blocks can be summarized and combined in a tree. The associative combine operator yields the same overall summary regardless of parenthesization, though the tie-breaking policy for equally optimal segments must be consistent. A small quadratic-time oracle enumerating all contiguous intervals can verify both maximum value and witness indices on short arrays.

## Worked questions and solutions

### Question 1: Decomposition: worked application 1

Count inversions in [3,1,2] by merge reasoning.

1. **Set up the model and conditions:** The left singleton is [3]; the right [1,2] has zero internal inversions.

2. **Carry out the calculation or proof:** Merging counts 3>1 and 3>2 as two cross inversions.

3. **State the result and its scope:** The inversion count is 2.

**Answer:** The inversion count is 2.


### Question 2: Merge Strategies: worked application 2

Multiply A=[[1,2],[3,4]] by B=[[5,6],[7,8]] using standard multiplication.

1. **Set up the model and conditions:** Compute the first row: 1×5+2×7=19 and 1×6+2×8=22.

2. **Carry out the calculation or proof:** Compute the second row: 3×5+4×7=43 and 3×6+4×8=50.

3. **State the result and its scope:** AB=[[19,22],[43,50]].

**Answer:** AB=[[19,22],[43,50]].


### Question 3: Geometric Algorithms: worked application 3

For points (0,0),(2,1),(4,0),(2,2), compute the minimum pair distance.

1. **Set up the model and conditions:** List short candidate separations: between (2,1) and (2,2) distance is one.

2. **Carry out the calculation or proof:** Every pair involving (0,0) or (4,0) is at least sqrt(5), and between endpoints is four.

3. **State the result and its scope:** The closest pair is (2,1) and (2,2), distance 1.

**Answer:** The closest pair is (2,1) and (2,2), distance 1.

