# Unit 2: Sets and functions


## Relations

**Core model — Relations**

A relation on A is a subset of A times A. Reflexivity, symmetry, antisymmetry and transitivity are distinct properties and should be checked independently.

**Original worked illustration**

On {1,2,3}, the relation a divides b is reflexive, antisymmetric and transitive, but not symmetric because 1 divides 2 and 2 does not divide 1.

**Boundary conditions and checks**

Antisymmetric does not mean 'never symmetric': equality is both symmetric and antisymmetric.

### A relation is a set of ordered pairs
For sets A and B, a relation from A to B is any subset of A×B. Writing R(x,y) means the ordered pair (x,y) belongs to that subset. The word ordered matters: (2,5) and (5,2) are different pairs unless the coordinates happen to be equal. A relation on A permits questions about reflexivity, symmetry, antisymmetry and transitivity. These are independent properties. Reflexivity demands (x,x) for every x in A. Symmetry demands that (x,y) implies (y,x). Antisymmetry demands that having both directions forces x=y; it does not mean that no two different elements can be related.

For divisibility on positive integers, xRy when x divides y. Every positive integer divides itself, so the relation is reflexive. Divisibility is transitive because x|y and y|z imply z=yk=x(jk) for integers j,k. It is antisymmetric on positive integers because if x|y and y|x, both positive, then their ratio is a positive integer and its inverse is also a positive integer; both must be one. It is not symmetric: 2 divides 6 but 6 does not divide 2. Changing the domain to all integers destroys antisymmetry in the usual sense because 2|-2 and -2|2 while 2≠-2.

### Representations and computational cost
A finite relation can be represented as a Boolean adjacency matrix M with M[i,j]=1 when (ai,aj) belongs to R. Reflexivity corresponds to ones on the diagonal; symmetry means M equals its transpose. For transitivity, any pair of edges i→j and j→k requires i→k. A direct checker can examine all triples in O(n^3) time, while specialized closure algorithms exploit Boolean matrix operations. Sparse relations are often better stored as adjacency lists, especially when the domain is large but each item has few related neighbors.

A useful operation is composition: if R relates users to groups and S relates groups to permissions, then S∘R relates a user to each permission reachable through one membership and one group-permission edge. This is exactly the mathematical shape of a database join. Composition is associative but need not commute. A permission system that accidentally reverses the order of composition may grant nonsense results or nothing at all.

### Worked mini-audit
Let A={a,b,c} and R={(a,a),(b,b),(c,c),(a,b),(b,c),(a,c)}. The relation is reflexive and transitive. It is not symmetric, because (a,b) exists but (b,a) does not. It is antisymmetric, because no distinct pair occurs in both directions. If (a,c) is removed, transitivity fails: (a,b) and (b,c) are present but (a,c) is absent. This removal is an explicit counterexample, stronger than saying the property feels absent. The matrix method reaches the same result from the missing entry in row a, column c.



## Mappings

**Core model — Mappings**

A function assigns exactly one output to each input in its domain. Injectivity prevents collisions; surjectivity covers every output of the codomain; bijections have inverses.

**Original worked illustration**

f:Z->Z defined by f(n)=n+1 is a bijection with inverse f^-1(m)=m-1. The function n->n squared fails injectivity on Z.

**Boundary conditions and checks**

Codomain and image differ; a function can fail surjectivity solely because the stated codomain is larger than its actual image.

### Functions as constrained relations
A function f:A→B assigns exactly one element of B to each element of A. It may assign the same output to different inputs; uniqueness applies to the output for a given input, not to inputs sharing an output. The domain A, codomain B, and mapping rule are all part of its definition. A rule such as f(x)=x^2 has different injectivity properties over integers, nonnegative integers, and real numbers even though the printed expression is unchanged.

Injectivity means distinct inputs always have distinct outputs; surjectivity means every codomain element is produced by at least one input. A bijection has both properties and therefore an inverse function B→A. A merely injective function has a left inverse on its image, but a full inverse on the declared codomain requires the appropriate conditions. For finite sets, the pigeonhole principle makes these properties especially transparent: a map from a larger finite domain to a smaller codomain cannot be injective.

### Mapping tables and inverse construction
Consider f:{0,1,2}→{a,b,c} with f(0)=b, f(1)=c, f(2)=a. All three outputs appear once, so f is bijective. Its inverse satisfies f⁻¹(a)=2, f⁻¹(b)=0 and f⁻¹(c)=1. If the last mapping changes to f(2)=b, then a is unused and b is hit twice, so neither injectivity nor surjectivity holds. An implementation can check injectivity by recording whether an output has already been assigned; it can check surjectivity by testing whether every codomain element has a preimage.

Function composition respects type constraints. Given f:A→B and g:B→C, the composite g∘f:A→C is defined by g(f(x)). In general f∘g is not defined because g's outputs lie in C, not necessarily A. A web application's authentication pipeline can be modeled similarly: a parser converts raw bytes to a request object, a validator produces a verified request, and an authorization function maps that object to a permitted action. Treating output types as domain and codomain constraints can prevent entire classes of accidental composition.

### Cardinality calculations
If |A|=m and |B|=n, then there are n^m functions A→B: each of m domain elements independently chooses one of n outputs. If m≤n, the number of injections is n(n−1)...(n−m+1), because outputs may not be reused. For m=n, this equals n!, the number of permutations. The count of onto functions is more subtle: by inclusion–exclusion it equals Σ from j=0 to n of (−1)^j C(n,j)(n−j)^m. These formulas presume labeled finite sets and distinguish mappings that differ on any domain element.



## Equivalence Classes

**Core model — Equivalence Classes**

An equivalence relation is reflexive, symmetric and transitive, partitioning a set into disjoint equivalence classes. Conversely every partition defines an equivalence relation.

**Original worked illustration**

Congruence modulo 3 on integers groups values into classes [0], [1], [2]. In the class [1] lie ..., -2, 1, 4, 7, ... .

**Boundary conditions and checks**

Do not confuse classes with single representatives; different representatives can describe the same class.

### Partitioning is the central equivalence-relation idea
An equivalence relation is reflexive, symmetric, and transitive. For each x in a set A, its equivalence class [x] consists of all y related to x. Equivalence classes are either identical or disjoint; together they partition A. To prove the claim, take any overlap element z in [x]∩[y]. Symmetry and transitivity show xRy, and then any object related to x is also related to y. This structural result explains why grouping records into classes is mathematically sound only when the underlying matching rule actually satisfies all three axioms.

Congruence modulo 5 is a concrete example on the integers. Write x~y if 5 divides x−y. The classes are the five residue sets labeled 0,1,2,3,4. For instance, −1 and 9 both represent residue 4. Their labels are canonical representatives, not the only members. Transitivity holds because if 5 divides x−y and y−z, it divides their sum x−z. Computation can map an integer to a remainder in {0,...,4}; programming languages differ in their treatment of negative remainders, so a normalization step such as ((x % 5)+5)%5 may be necessary.

### When clustering is not equivalence
Suppose a system regards two names as equivalent if their edit distance is at most one. Name 'cat' is close to 'bat' and 'bat' is close to 'bet', but 'cat' is not close to 'bet' under the same threshold. The relation is not transitive, so it does not induce legitimate disjoint equivalence classes. A clustering algorithm can still group these strings, but the result depends on the chosen clustering rule, not on the theorem for equivalence relations. Similar problems appear in approximate deduplication of scientific author names and in identity resolution.

### Quotient sets and useful abstractions
The quotient A/~ is the set of equivalence classes, not an ordinary subset of A. It represents many concrete objects by one abstract object. In modular arithmetic, Z/5Z supports addition and multiplication by class: [a]+[b]=[a+b] and [a][b]=[ab]. To make these operations meaningful, one must check they are well-defined: replacing a or b by equivalent representatives cannot change the resulting class. The divisibility definition supplies this guarantee. Quotient structures appear in compiler normalization, graph connected components, and many algebraic constructions where irrelevant distinctions are intentionally discarded.



## Partial Orders

**Core model — Partial Orders**

A partial order is reflexive, antisymmetric and transitive. Elements may be incomparable. Hasse diagrams show cover relations while suppressing reflexive and transitively implied edges.

**Original worked illustration**

Under subset inclusion on {a,b}, {a} and {b} are incomparable, both above the empty set and below {a,b}.

**Boundary conditions and checks**

A maximal element need not be a greatest element; every finite nonempty poset has at least one maximal element, not necessarily a greatest one.

### Partial orders, Hasse diagrams, and topological sorting
A partial order is reflexive, antisymmetric and transitive. It need not compare every pair. The subset relation on sets is a partial order: {a} and {b} are incomparable, while both are subsets of {a,b}. This is why a dependency graph can define a sensible ordering without dictating one total list of tasks. A total order has the additional property that for any two elements x,y, either x≤y or y≤x.

A Hasse diagram draws only the covering relations of a finite partial order. For the divisor order on {1,2,3,6}, draw upward links 1→2, 1→3, 2→6, 3→6. Do not add 1→6 as a covering link; it follows by transitivity through either middle element. The diagram is neither a physical network topology nor a weighted graph. It is a compact picture of the order relation, where the meaning of upward is prescribed by the chosen order.

### Minimal, maximal, least, and greatest are different
A minimal element has no strictly smaller distinct element. A least element is smaller than or equal to *every* element, so if it exists it is unique. A poset may have several minimal elements but no least element. For the set {{a},{b},{a,b}} ordered by inclusion, {a} and {b} are both minimal, and neither is a least element because the two are incomparable. The set {a,b} is greatest. Confusing these terms leads to invalid claims about optimization: a locally irreducible state may not be globally optimal.

### Scheduling as a partial-order application
Let tasks compile, test, package, and deploy have dependencies compile≺test, compile≺package, test≺deploy, package≺deploy. The ordering leaves test and package incomparable, so either may run before the other after compilation. Topological sorting produces one permitted linear order; it does not prove that this order minimizes total elapsed time when tasks have different durations and shared resources. A directed cycle such as deploy≺compile would invalidate the assumption that the dependency relation is a strict partial order, and topological sorting would detect this failure.

A topological sorter based on indegrees repeatedly removes a node with zero incoming edges. Every edge points from an earlier item to a later item in the output. If nodes remain but none has zero indegree, the remaining graph contains a directed cycle. The invariant is that all removed nodes had their incoming dependencies satisfied. This gives a practical proof of correctness under the acyclic-input assumption.

### Extended laboratory: permissions as relations and equivalence classes
An online university has students S={Ada,Ben,Cora,Din}, courses C={Logic,Algorithms,Data}, and groups G={Year1,Year2}. Define the enrollment relation E⊆S×C by pairs (Ada,Logic),(Ada,Algorithms),(Ben,Logic),(Cora,Data),(Din,Algorithms). Define a group membership relation M⊆S×G where Ada and Ben belong to Year1, and Cora and Din belong to Year2. A course membership query and a group membership query are two distinct relations even when the same student identifiers appear in both.

To answer "which students take at least one course?" project the first coordinate of E. The result has four students, not five, because Ada appears twice but belongs to the set only once. To answer "which students share a course with Ada?", join E to itself on course and filter one side to Ada. Ben shares Logic with Ada. Din shares Algorithms with Ada. Cora shares none. If the query allows a student to share a course with themselves, Ada also appears; a user-facing recommendation may explicitly exclude self-pairs. The mathematics does not choose that policy automatically.

Now define a relation P on students by P(x,y) if x and y are in the same academic year. Because every student has exactly one year in this example, P is an equivalence relation. It is reflexive, symmetric and transitive, and its classes are {Ada,Ben} and {Cora,Din}. Suppose instead that students may join several interest groups and P(x,y) means they share at least one group. A member of both groups can bridge two people who do not share any group with each other. Transitivity then fails; the groups are overlapping sets rather than equivalence classes. A system must not silently apply partition assumptions to overlapping membership.

Define course prerequisites as a strict partial order on course achievements. For instance, Logic must precede Algorithms, but Data is independent of both. A feasible study schedule could place Logic and Data together and Algorithms afterward. Turning every course into one total order would reject valid parallel schedules. If an administrator accidentally adds Algorithms as a prerequisite of Logic, the cycle prevents any standard topological progression. A topological-sort check can detect that structural fault before students encounter an impossible enrollment plan.

Consider a mapping advisor:S→G that assigns each student to exactly one year group. It is a function by construction. It is not injective, since Ada and Ben map to Year1, and cannot be injective because four students map to only two group labels. It is surjective if at least one student occupies each year. If the institution later creates a Year3 group with no students, the same mapping becomes nonsurjective to the expanded codomain even though no student assignment has changed. This illustrates why codomain declarations matter for a function's properties.

A precise implementation would keep enrollment, year membership and prerequisite edges as separate tables or graph structures with foreign-key or referential checks. To determine whether every student has a course, quantify over S and check that there exists a course c such that (s,c)∈E. To determine whether a specific course has no students, negate existence of a corresponding pair. Reversing these quantifiers produces a completely different data query. Include students with zero enrollments in test fixtures; inner joins alone often drop those records and create the illusion that the universal claim is satisfied.

The audit should report its assumptions. Unique identifiers are stable, duplicate enrollment pairs do not change set membership, every year assignment is known, and prerequisite edges mean actual completion requirements rather than loose recommendations. If any assumption fails, the resulting mathematical classification may not match the operational policy. The exercise turns abstract set and relation definitions into a way to design safer database queries and curriculum checks.

### Experiment card: quotient classes and mapping counts
Start with the residue-class model of integers 0 through n−1 modulo three. The number of elements in each class is determined by distributing the n integers across residues 0,1,2. With n=7, the classes are {0,3,6}, {1,4} and {2,5}; the sizes are 3,2,2. The largest class has size three. By the pigeonhole principle, the largest class must contain at least ceil(n/3) elements, and this construction attains that lower bound. This is a direct application of quotient partitions, not a probabilistic assertion about random placement.

The separate surjection experiment maps a domain of n distinguishable points into exactly two distinguishable labels. Every point has two independent label choices, so there are 2^n functions. To hit both labels, exclude the all-first-label function and the all-second-label function. The remaining count is 2^n−2 for n≥1. When n=1 the result is zero: one input cannot cover two distinct outputs. At n=2 the result is two, corresponding to the two possible bijections. These boundary cases are valuable when auditing code using exponential expressions.

Both experiments illuminate how the chosen domain determines the answer, but they are not the same counting problem. The residue partition groups an existing set according to a fixed equivalence relation. The surjection count enumerates all functions satisfying a property. Do not confuse the number of equivalence classes with the number of valid functions. A common coding error is to identify a residue by a potentially negative language-specific remainder without normalization. Another is to treat output labels as interchangeable and divide by two, which would solve a different unlabeled-target problem.

An independent cross-check for small n can enumerate every bitstring of length n, interpret zero and one as the two labels, and retain strings that contain both symbols. Compare that count to 2^n−2. For n=12, exhaustive enumeration inspects only 4096 assignments, which is manageable; for much larger n, calculate the formula using arbitrary-precision integers. The exercise demonstrates a proof-derived oracle, a finite exhaustive test, and an implementation boundary in one reproducible workflow.



## Fully worked questions

### Question 1: Relations: worked application 1

Check whether divisibility is a partial order on {1,2,3}.


**Set up the model and conditions:** Every integer divides itself; divisibility is reflexive.


**Carry out the calculation or proof:** If a divides b and b divides a for positive integers, a=b; transitivity follows from multiplication of divisors.


**State the result and its scope:** It is a partial order but not a total order: 2 and 3 are incomparable.


**Independent reasoning check and edge conditions:** Reflexivity: 1|1, 2|2 and 3|3. Antisymmetry: if positive integers a and b each divide the other, then a=b. Transitivity: if a|b and b|c, write b=ak and c=bj to obtain c=a(kj), hence a|c. These checks establish a partial order on the stated set. It is not a total order because neither 2 divides 3 nor 3 divides 2. Using all integers instead of the specified positive finite domain would require extra care: a and −a divide each other but need not be equal.


**Answer:** It is a partial order but not a total order: 2 and 3 are incomparable.


### Question 2: Mappings: worked application 2

For f:Z→Z defined by f(n)=n+1, find its inverse and prove bijection.


**Set up the model and conditions:** If f(a)=f(b), a+1=b+1 implies a=b, so f is injective.


**Carry out the calculation or proof:** Given target m, choose n=m−1, and f(n)=m, so f is surjective.


**State the result and its scope:** Its inverse is f⁻¹(m)=m−1.


**Independent reasoning check and edge conditions:** Injectivity follows by taking two integers a,b with f(a)=f(b). The equality a+1=b+1 implies a=b. Surjectivity follows because for every integer target m, choosing input n=m−1 gives f(n)=m. Thus the inverse exists on all Z and is g(m)=m−1. Check both compositions: g(f(n))=(n+1)−1=n and f(g(m))=(m−1)+1=m. This verifies the left and right inverse identities, not merely one sample calculation. If the codomain were restricted to nonnegative integers while the domain remained Z, the mapping would not have the same declared type.


**Answer:** Its inverse is f⁻¹(m)=m−1.


### Question 3: Equivalence Classes: worked application 3

Partition {0,1,2,3,4,5} into congruence classes modulo 3.


**Set up the model and conditions:** Two numbers are equivalent iff their difference is divisible by three.


**Carry out the calculation or proof:** Collect residues: {0,3}, {1,4}, {2,5}.


**State the result and its scope:** These three disjoint classes cover the whole set.


**Independent reasoning check and edge conditions:** Congruence modulo three means that two numbers differ by a multiple of three. Starting with 0 through 5, sort each by its remainder: 0 and 3 have remainder zero, 1 and 4 remainder one, 2 and 5 remainder two. Hence the classes are {0,3}, {1,4}, and {2,5}. Each element occurs in exactly one class, and the union of classes is the entire six-element set. This is a partition because congruence is reflexive, symmetric and transitive. Counting yields three classes of size two, confirming all six original elements are represented.


**Answer:** These three disjoint classes cover the whole set.

