# Unit 6: Recurrences


## Recursive Definitions

**Core model — Recursive Definitions**

Recursive definitions express an object using earlier or smaller objects, with base cases preventing infinite regress.

**Original worked illustration**

The Fibonacci numbers F0=0, F1=1, Fn=F(n-1)+F(n-2) produce 0,1,1,2,3,5,8,... .

**Boundary conditions and checks**

A recursive specification without a well-founded decrease may fail to define a computable termination procedure.

### Recursive definitions have two obligations
A recursive definition gives base objects and rules for constructing larger objects from previously defined ones. For example, define a list by either the empty list or an element followed by a list. A recursively defined function must supply values for base cases and ensure recursive calls move toward those cases. A syntactically recursive program is not necessarily terminating. The call f(n)=f(n)+1 is a recursive equation, but it does not determine finite values or offer progress toward a base.

### Factorial as an exact reference
The factorial function is given by 0!=1 and n!=n(n−1)! for n≥1. A direct recursive implementation that returns 1 at n=0 and otherwise returns n times factorial(n−1) terminates for nonnegative integer input. Its maximum recursion depth is n+1. The mathematical result may be extremely large: 21! exceeds the maximum value of a signed 64-bit integer, so a 64-bit implementation can overflow even though the recurrence is correct. Mathematical specification and machine representation require separate validation.

### Structural recursion over trees
For a binary tree, define size(empty)=0 and size(node(left,right))=1+size(left)+size(right). Termination follows because both children are strictly smaller subtrees. Correctness can be proved by structural induction: assume size returns the correct node count for each child, then the root contributes one additional node. The same pattern defines height(empty)=0 and height(node)=1+max(height(left),height(right)). In an unbalanced chain of n nodes, recursion uses O(n) stack depth; an explicit stack or iterative traversal may be more robust.

### Mutual recursion
Mutually recursive definitions call one another. One example defines even(n) in terms of odd(n−1) and odd(n) in terms of even(n−1), with even(0)=true and odd(0)=false. The common measure n decreases in both kinds of calls. When debugging a mutual recursion cycle, verifying termination of each function in isolation is not enough if calls can bounce between functions without decreasing a shared measure. Mutual recursion also occurs in grammar parsers where expression and term parsing functions invoke one another across different grammatical constructs.

### Refactoring to iteration
Tail-recursive functions may sometimes be transformed into loops with accumulators. A factorial accumulator implementation maintains the invariant acc×n! equal to the desired original factorial while reducing n each iteration. A non-tail-recursive Fibonacci implementation with two repeated recursive calls grows exponentially because it recomputes overlapping subproblems; a loop maintaining consecutive Fibonacci values uses O(n) time and O(1) extra state. Recursion is a definition technique, not an automatic statement of efficiency.



## Recurrence Solving

**Core model — Recurrence Solving**

A linear homogeneous recurrence with constant coefficients can be solved by testing powers r^n and analyzing characteristic roots.

**Original worked illustration**

For a_n=3a_(n-1) with a_0=2, induction gives a_n=2*3^n. The characteristic root r=3 matches this growth.

**Boundary conditions and checks**

Repeated roots require polynomial factors in the general solution, so copying a distinct-root formula can be incorrect.

### From a recurrence to a closed expression
A recurrence defines sequence values in terms of earlier values, together with enough initial conditions to determine a unique sequence. Consider T(n)=T(n−1)+3 for n≥1 and T(0)=2. Repeated substitution gives T(n)=2+3n. To check the formula, verify the base T(0)=2 and substitution 2+3(n−1)+3=2+3n. A claimed solution without checking initial conditions may solve the difference equation but not the intended sequence.

### Linear homogeneous recurrences
For Fibonacci's recurrence Fn=Fn−1+Fn−2, try a solution of the form r^n. The characteristic equation is r²=r+1 with roots (1±sqrt(5))/2. The general solution combines powers of the roots, and the initial values F0=0, F1=1 determine the coefficients. The expression is exact over real arithmetic, but calculating large Fibonacci numbers using floating-point root powers can lose integer precision. An integer recurrence or fast-doubling method is preferable for exact computation.

### A first-order runtime recurrence
Suppose a loop processes the current array element and recursively handles n−1 remaining elements with constant cost c, giving T(n)=T(n−1)+c and T(0)=d. Expansion produces d+cn, which is Θ(n). The constant c is an abstract bound on unit work; actual CPU running time can include caches, memory allocation, and language overhead. Asymptotic notation distinguishes growth rates, not precise benchmark values. To establish Θ(n), provide both O(n) and Ω(n) bounds under stated operation-cost assumptions.

### Summation recurrences and nested loops
For T(n)=T(n−1)+n with T(0)=0, unfolding gives Σ_{i=1}^n i=n(n+1)/2 and therefore Θ(n²). A triangular loop is an implementation analog. If the incremental work is log n rather than n, summing log i over i from 1 to n gives Θ(n log n); this can be bounded above by n log n and below by (n/2) log(n/2) for n≥2. Showing both bounds avoids unjustified jumps from a summation to an asymptotic class.

### Nonhomogeneous and boundary-aware solving
For T(n)=2T(n−1)+1 with T(0)=0, repeated expansion yields 2^n−1. Check n=0,1,2: 0,1,3. This growth can arise from a recursively doubling workload; it should not be confused with the linear-cost version T(n)=T(n−1)+2. When a recurrence is defined only for powers of two, a solution for arbitrary n needs a rounding or extension convention. Replacing n/2 with floor(n/2) can alter exact constants while preserving the asymptotic class under suitable regularity.



## Divide-And-Conquer Relations

**Core model — Divide-And-Conquer Relations**

Divide-and-conquer recurrences combine costs of subproblems and a merge term. Boundary conditions establish exact formulas while asymptotics describe growth.

**Original worked illustration**

For n=2^k and T(n)=2T(n/2)+n, with T(1)=1, k recursion levels each contribute n operations; total T(n)=n(k+1).

**Boundary conditions and checks**

An uneven recurrence or nonuniform split cannot automatically be simplified with a Master theorem case that assumes balanced partitions.

### Splitting problems creates recurrence trees
Divide-and-conquer algorithms partition an input into smaller subproblems, solve them, and combine their answers. The cost recurrence describes both branching and merging. For balanced mergesort on n=2^k inputs, T(n)=2T(n/2)+cn for some linear merging cost c. At each level of recursion the total combine work is cn because the sizes of that level's subproblems add to n. There are log2 n non-leaf levels, so total work is Θ(n log n). Counting recursion levels and per-level work is more explanatory than merely quoting a theorem.

### Contrast: binary search
Binary search discards half of a sorted search interval after one comparison with its midpoint. Its recurrence is T(n)=T(ceil(n/2))+c with T(1)=d. There is only one recursive subproblem at each level, not two. The depth is Θ(log n) because repeated halving reaches size one after logarithmically many steps. This analysis depends on constant-time indexing into an array and a monotonic ordering. Running binary search on an unsorted array or a linked list without efficient random access changes the correctness or cost story.

### A recurrence with a dominant combining cost
If T(n)=2T(n/2)+n², the work at the root is n², at the next level it is 2(n/2)²=n²/2, then n²/4, and so on. The geometric sum is bounded by 2n², so T(n)=Θ(n²) for suitable base cost. Compare that with mergesort, where every level contributes equal work. The recurrence tree makes the different growth rates visible.

### Conditions of the Master Theorem
The familiar Master Theorem concerns recurrences of the form T(n)=aT(n/b)+f(n) under constraints such as a≥1 and b>1. It compares f(n) with n^{log_b a}; its cases have technical requirements, especially at regularity boundaries. A recurrence like T(n)=T(n−1)+n is outside that standard form and should be handled by summation. Recurrences with uneven splits may need alternative methods such as substitution, recursion trees, or Akra–Bazzi-style analysis. The theorem is a tool chosen after inspecting the recurrence, not a universal replacement for reasoning.

### Independent numerical checking
For powers of two up to 1024, compute recurrence values in a small dynamic-programming table and compare T(n)/(n log2 n) to a bounded range. Such numerical behavior is a useful sanity check but cannot prove an asymptotic theorem on an infinite domain. A derivation should still state the base case, rounding convention, and cost model. Separating the numerical experiment from the proof helps students use simulation constructively.



## Discrete Growth

**Core model — Discrete Growth**

Discrete growth compares polynomial, exponential and factorial rates. Logarithms change multiplicative growth into addition but do not preserve every ordering for small n.

**Original worked illustration**

The inequality n^3<2^n eventually holds: at n=10, 1000<1024. Exponential eventually beats any fixed-degree polynomial.

**Boundary conditions and checks**

One observed crossover does not constitute a general proof; formal asymptotic statements require a bound for all sufficiently large n.

### Discrete growth rates and why scales matter
Growth comparisons often focus on polynomial, logarithmic, and exponential functions. For n≥2, log2 n grows far more slowly than n, and n^k grows more slowly than c^n for any fixed positive k and c>1 as n tends to infinity. These are asymptotic comparisons; for small n, constants and lower-order terms can reverse which program is faster. An O(n log n) implementation with expensive memory allocation can be slower than a simple O(n²) algorithm on small fixed inputs.

### Exact arithmetic versus floating-point evidence
Consider an algorithm counting binary strings of length n, which needs 2^n as an exact integer. JavaScript's standard Number type represents integers exactly only up to 2^53−1. After that, treating outputs as exact counts can silently produce rounding. Arbitrary-precision integers or symbolic expressions preserve correctness for large n. The issue is not that the mathematical expression grows too quickly to define; the issue is the finite representational capacity of a chosen machine type.

### Distinguishing average, worst and amortized growth
A dynamic array may occasionally resize and copy all n elements in an expensive operation, yet have O(1) amortized append cost under geometric capacity growth. If capacity doubles, the total number of old elements copied across expansions up to n appends is less than 1+2+4+...<2n, so the total append-plus-copy work is O(n). This is neither a worst-case O(1) guarantee for each individual append nor an average over random inputs; amortized analysis aggregates costs across a sequence.

### Resource growth beyond running time
Memory complexity, bandwidth, energy, and communication can dominate computational feasibility. A truth-table generator with n variables has 2^n rows; even if each row were computed extremely quickly, materializing the complete table would require exponential output space. A streaming generator may use only O(n) working memory while still taking time proportional to the output. State whether reported memory complexity includes the input, output buffer, recursion stack and data structures used for caching.

### Modeling a real threshold
If algorithm A requires 5n² elementary steps while B requires 200n log2 n, solve approximately for a crossover rather than saying B is universally faster. At n=16, A costs 1280 while B costs 12800, so A wins under the toy cost model. At n=1024, A costs about 5.24 million while B costs 2.048 million, so B wins. Actual time depends on the validity of the step-cost constants, but the exercise illustrates why asymptotic superiority is a large-input statement and should not conceal practical parameter ranges.

### Extended laboratory: reasoning about a divide-and-conquer service
A service merges two sorted lists into one sorted list. Let n be the combined list length. The merge operation compares the first unconsumed elements, appends the smaller one, and advances exactly one pointer. When one list is exhausted, the remainder of the other list is appended without further key comparisons. For nonempty lists of combined length n, there are at most n−1 key comparisons, because every comparison consumes one element and the last remaining element needs no comparison. In a best case, one short list may be exhausted after fewer comparisons.

If mergesort always divides n items into two nearly equal groups, its runtime satisfies T(n)=T(floor(n/2))+T(ceil(n/2))+M(n) with M(n)=O(n). For n a power of two and linear merge cost cn, this reduces to 2T(n/2)+cn. Draw a recursion tree for n=8: the root has one size-eight merge, its children have two size-four merges, then four size-two merges. With cost proportional to the total number of elements merged, each non-leaf level does eight units of proportional work. There are three levels, giving work proportional to 8×3, plus leaf costs.

Now contrast a recursive Fibonacci implementation. Fib(n) naively calls Fib(n−1) and Fib(n−2), creating a branching call tree that recomputes Fib(n−2) and smaller values through multiple paths. A memoized version stores results by n, making only n+1 distinct subproblem values for a query up to n. A bottom-up loop can avoid recursion stack space altogether. The lesson is not simply that recursion is slow: recursion with memoization, structural decomposition and suitable subproblem sharing can be efficient.

Consider the recurrence T(n)=3T(n/2)+n for n=2^k. At each level i, there are 3^i subproblems of size n/2^i, so that level contributes n(3/2)^i work. The sum is dominated by its deepest levels and grows as Θ(n^{log2 3}). This differs from mergesort's Θ(n log n). A common mistake is to see linear merging cost and conclude n log n regardless of branching factor. The size and number of recursive calls both affect the result.

A loop invariant demonstrates that the merge subroutine itself is correct: before each iteration, the output contains exactly the smallest consumed items from both inputs in sorted order, and the unconsumed suffixes remain sorted. Choosing the smaller next head preserves the invariant. When one suffix empties, appending the other preserves sortedness. Correctness of mergesort follows by structural induction: each recursive call returns a sorted subarray, and the merge combines two sorted subarrays correctly. Proving time cost and proving output correctness are separate tasks.

For a numerical simulation, calculate T(1)=1 and T(n)=2T(n/2)+n at n=2,4,8,16. The exact sequence is 1,4,12,32,80 when counting the toy cost this way. Check these results using a dynamic program and an independent recursion tree. Do not label these values actual milliseconds or CPU cycles, since they are abstract operation counts. Boundary tests should include n=1, where no split occurs, and odd input sizes, where floor and ceiling branches differ.

For a production implementation, include additional considerations: merge sort is stable only when ties are resolved consistently, often by choosing from the left first; array-based mergesort usually needs auxiliary storage, while linked-list variants have different tradeoffs. Extremely deep recursion can overflow stack memory. A trusted textbook distinguishes these implementation constraints from the clean mathematical recurrence, so that the abstract analysis informs but does not pretend to replace engineering measurements.

### Experiment card: two counting recurrences
The primary recurrence model reports Fibonacci Fn under F0=0 and F1=1. Its small outputs are F1=1, F2=1, F3=2, F4=3, F5=5 and F6=8. Derive these values by a loop with state (a,b), initially (0,1), replacing it by (b,a+b) at each step. The invariant is that after i updates, (a,b)=(Fi,F_{i+1}). This statement proves the loop calculates the intended recurrence, not merely a sequence resembling it for several samples.

The independent model counts binary strings of length n with no two adjacent ones. Let an denote that count. When a valid string ends in zero, its first n−1 positions form any valid shorter string. When it ends in one, its predecessor must be zero, so the first n−2 positions form any valid shorter string. Consequently an=a_{n−1}+a_{n−2}, with a0=1 for the empty string and a1=2 for 0 and 1. Thus a2=3, a3=5, a4=8. The values are Fibonacci-related but shifted: an=F_{n+2}.

For n=3, enumerate all eight possible bitstrings and reject 011,110,111 because they contain the substring 11. The five remaining strings are 000,001,010,100,101. This explicit check should agree with a3=5. For n=1, both one-symbol strings are valid. For n=12, a dynamic program avoids enumerating every string and provides a precise reference value that can be compared with the model's result.

These recurrences illustrate two different interpretations of a similar algebraic rule. Fibonacci's definition describes its own numerical sequence. The no-adjacent-ones recurrence counts combinatorial objects, and its base cases shift the index. A simulator that displays only the sequence value without a named meaning risks encouraging students to identify unrelated objects as the same problem. A good reader shows both the recurrence and the counted object, and lets learners reconstruct the recurrence from a last-symbol case split.



## Fully worked questions

### Question 1: Recursive Definitions: worked application 1

Compute Fibonacci F6 using F0=0,F1=1.


**Set up the model and conditions:** Apply F_n=F_{n−1}+F_{n−2} successively.


**Carry out the calculation or proof:** The sequence through n=6 is 0,1,1,2,3,5,8.


**State the result and its scope:** Therefore the sixth Fibonacci number is F6=8.


**Independent reasoning check and edge conditions:** Starting from F0=0 and F1=1, apply the recurrence Fn=Fn−1+Fn−2 successively: F2=1, F3=2, F4=3, F5=5 and F6=8. It is important to count the index: F6 is the term at index six under a zero-based convention, not necessarily what every writer calls the sixth listed term. A computational reference can keep two previous values and update them iteratively, avoiding the repeated work of a naive recursive function. The initial conditions and indexing convention are essential to the numerical result.


**Answer:** Therefore the sixth Fibonacci number is F6=8.


### Question 2: Recurrence Solving: worked application 2

Solve a_n=3a_(n−1), a0=2.


**Set up the model and conditions:** Repeated substitution yields a_n=3^n a0.


**Carry out the calculation or proof:** Insert a0=2 and verify substitution 2·3^n=3(2·3^(n−1)).


**State the result and its scope:** The solution is a_n=2·3^n.


**Independent reasoning check and edge conditions:** Repeated substitution gives a1=3a0=6, a2=3a1=18 and a3=54, suggesting an=2×3^n. Prove this form by induction. At n=0, 2×3^0=2 matches the initial condition. Assuming ak=2×3^k, the recurrence yields a_{k+1}=3ak=2×3^{k+1}. Thus the expression satisfies every recurrence step and the base condition. The sequence grows geometrically for n≥0; the proof does not depend on observing just the first few values.


**Answer:** The solution is a_n=2·3^n.


### Question 3: Divide-And-Conquer Relations: worked application 3

Compute T(8) for T(n)=2T(n/2)+n with T(1)=1.


**Set up the model and conditions:** T(2)=2(1)+2=4.


**Carry out the calculation or proof:** T(4)=2(4)+4=12 and T(8)=2(12)+8=32.


**State the result and its scope:** The exact result is T(8)=32.


**Independent reasoning check and edge conditions:** Calculate bottom-up using the given powers of two. T(1)=1. Then T(2)=2×1+2=4, T(4)=2×4+4=12 and T(8)=2×12+8=32. Each equation uses the immediately smaller defined subproblem. A recursion-tree check agrees: there are eight leaves each costing one, and each of three merge levels contributes eight more units, totaling 8+8+8+8=32. This is an abstract cost recurrence, not a measurement of seconds on a computer.


**Answer:** The exact result is T(8)=32.

