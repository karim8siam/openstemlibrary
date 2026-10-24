# Unit 3: Counting


## Permutations

**Core model — Permutations**

A permutation is an ordered arrangement of distinct items. With n distinguishable items, there are n! full permutations and n!/(n-r)! length-r arrangements without replacement.

**Original worked illustration**

Three distinct books can be ordered in 3!=6 ways. Choosing and ordering two of them gives 3*2=6 arrangements.

**Boundary conditions and checks**

If objects are identical or repetition is allowed, the factorial formula must be modified rather than applied blindly.

### Permutations count order-sensitive arrangements
If n objects are distinct and exactly k positions are filled without replacement, there are n(n−1)...(n−k+1)=n!/(n−k)! arrangements. The first position has n choices, the second n−1, and so on. When every object is used, the count is n!. A sample with four distinct books A,B,C,D can be ordered on a shelf in 24 ways. If only two ordered award positions are assigned, there are 4×3=12 possibilities. For unordered two-person committees, the answer is six instead, because swapping the two selected people does not produce a different committee.

### Repeated elements and overcounting
For a multiset such as the letters of 'LEVEL', there are 5!/(2!2!)=30 distinct arrangements: two E letters and two L letters are indistinguishable. The denominator divides out permutations that leave the visible word unchanged. It is not appropriate to use the same formula when nominally equal items carry unique identifiers; two database records with the same displayed label can still be distinct objects. Counting requires a precise definition of when two outcomes are considered different.

### Derangements as a constraint problem
A derangement is a permutation with no item in its original position. For n distinct items, use inclusion–exclusion on events Ei that item i remains fixed: D(n)=n! Σ_{k=0}^n (−1)^k/k!. For n=3, the six permutations contain exactly two derangements. A direct enumeration lists 231 and 312 if the original order is 123. The formula connects permutations, constraints, and inclusion–exclusion; it also illustrates why multiplying independent-looking probabilities can fail, because individual fixed-point events under a permutation are not independent.

### Algorithm and verification
A basic recursive permutation generator swaps each available item into the current position and recurses on the remaining suffix. At recursion depth i, the prefix of length i is fixed and the suffix contains all unused items. The algorithm enumerates n! leaves and necessarily has factorial output size. If duplicates exist, either deduplicate the output or count multiplicities deliberately. Compare the number of generated unique strings for 'LEVEL' with the multiset formula as an independent check. Memory use can be limited to the recursion stack and one working array when permutations are emitted incrementally rather than all stored.



## Combinations

**Core model — Combinations**

A combination selects an unordered subset. The binomial coefficient C(n,k)=n!/[k!(n-k)!] counts the number of k-subsets of an n-set.

**Original worked illustration**

Choosing two people from a team of five yields C(5,2)=10. Ordering the selected pair would double this to 20.

**Boundary conditions and checks**

Never use a combination count to answer a question in which assigned roles make order relevant.

### Combinations remove ordering from selection
A k-element subset of an n-element labeled set can be ordered in k! ways. Since there are n!/(n−k)! ordered selections, the number of subsets is C(n,k)=n!/[k!(n−k)!]. The symmetry C(n,k)=C(n,n−k) follows by taking complements: selecting a committee of k members determines exactly which n−k are excluded. This argument is often simpler and safer than manipulating large factorials.

### Pascal's recurrence
Choose a distinguished element x from an n-element set. A k-subset either does not contain x, giving C(n−1,k) possibilities, or it contains x, leaving C(n−1,k−1) choices for the remaining members. Therefore C(n,k)=C(n−1,k)+C(n−1,k−1). The argument proves Pascal's rule by a disjoint classification and suggests a dynamic-programming algorithm. For n=6,k=2 it gives C(5,2)+C(5,1)=10+5=15.

### With replacement and other models
Selecting k items from n types with unlimited repetition and no order yields C(n+k−1,k) multisets. One way to prove this is the stars-and-bars encoding: arrange k identical stars and n−1 separators, with the number of stars between successive separators representing each type's multiplicity. This model differs from a committee of people, since selecting the same person twice is normally forbidden. Do not choose the formula from the words 'choose k from n' alone; ask whether order matters and whether repetition is allowed.

### Statistical and computational uses
The binomial coefficient counts the number of binary strings of length n with exactly k ones; it also appears as the coefficient of x^k in (1+x)^n. A binary vector can encode membership in a subset, creating a direct connection among set theory, bit operations and combinatorics. The sum over k of C(n,k) equals 2^n because every subset has a unique size. To compute C(100,50), multiplying 100! first can overflow fixed-width integers long before the result is reached. A multiplicative formula with exact integer reductions or Pascal dynamic programming is more robust. Correctness checks should include C(n,0)=1 and C(n,n)=1.



## Inclusion–Exclusion

**Core model — Inclusion–Exclusion**

Inclusion-exclusion corrects double-counting of overlapping sets. For two finite sets, size(A union B)=size(A)+size(B)-size(A intersection B).

**Original worked illustration**

Among 20 students, 12 study Python, 9 study R and 5 study both; 12+9-5=16 study at least one.

**Boundary conditions and checks**

The sign alternation for three or more sets requires adding back triple intersections after subtracting all pairwise intersections.

### Counting unions without counting an item twice
For finite sets A and B, the identity |A∪B|=|A|+|B|−|A∩B| subtracts the overlap that appeared in both counts. For three sets, add the three individual sizes, subtract the three pairwise intersections, and add the triple intersection. The alternating pattern is inclusion–exclusion; it counts each element exactly once according to how many sets contain it. An item lying in exactly r selected sets contributes Σ_{j=1}^r (−1)^{j+1}C(r,j)=1.

### A realistic query audit
Suppose a site survey reports 80 users who use Python, 65 who use R, and 30 who use both. The number using at least one tool is 80+65−30=115. Adding 80 and 65 without subtracting the intersection would overestimate reach. If the total sampled population is 150, then 35 use neither. The figures must refer to the same population and time window; combining a monthly Python count with a weekly R count is not a legitimate set calculation.

### General principle and complements
Let Ei be the event or subset satisfying condition i. To count elements satisfying none of m conditions in universe U, subtract the size of the union from |U|. This is the backbone of many derangement and occupancy formulas. For example, count integers from 1 to 60 divisible by 2 or 3: 30+20−10=40, since multiples of 6 lie in the overlap. Extending to divisibility by 2,3,5 requires terms for multiples of 6,10,15 and a final positive term for multiples of 30. Arithmetic details are easier to audit when each intersection is labeled before values are substituted.

### When inclusion–exclusion is not ideal computationally
With m sets, the full formula involves 2^m−1 nonempty intersections. For m=30 the symbolic enumeration can be impractical even when each individual membership test is easy. Bitsets may count a concrete finite union directly, and dynamic programming or generating functions can exploit structured constraints. Inclusion–exclusion remains a proof technique even when an optimized implementation computes the answer differently. When developing a solution, distinguish a mathematical identity (always true for finite sets) from a selected algorithm (whose cost depends on representation).



## Generating Functions

**Core model — Generating Functions**

Generating functions encode sequence coefficients in a formal power series; multiplication corresponds to convolution. Convergence is optional for formal identities.

**Original worked illustration**

For a_n=1 for n>=0, A(x)=1/(1-x). Squaring yields 1/(1-x)^2=sum_{n>=0}(n+1)x^n, encoding the number of ordered pairs of nonnegative integers summing to n.

**Boundary conditions and checks**

An algebraic manipulation of a formal series should not be mistaken for a numerical convergence claim at arbitrary x.

### Encoding combinatorial families with coefficients
A generating function packages an infinite sequence a0,a1,... as A(x)=Σ_{n≥0} an x^n. In ordinary generating functions, coefficients record counts at different sizes; the variable x is often formal, so numerical convergence is not required to justify coefficient identities. For one type of item available in any nonnegative quantity, the series is 1+x+x²+...=1/(1−x) as a formal power series. For an item available at most once, the factor is 1+x. Multiplying factors combines independent choices and adds their sizes.

### Convolution appears naturally
If A(x)=Σ an x^n and B(x)=Σ bn x^n, the coefficient of x^n in A(x)B(x) is Σ_{k=0}^n ak b_{n−k}. The sum counts all ways to split total size n into a contribution of size k from the first family and size n−k from the second. This is the Cauchy product, and it mirrors convolution in discrete signal processing. If two independent types of tickets can each be bought in any quantity, (1−x)^{-2} has coefficient n+1 at x^n: the solutions of a+b=n with a,b≥0 are (0,n),(1,n−1),...,(n,0).

### Restricted choices and a worked coefficient
Suppose three kinds of parts have costs 1,2,3 units, and we may use any number of each. The generating function is (1−x)^{-1}(1−x²)^{-1}(1−x³)^{-1}. To count assemblies of cost 5, solve a+2b+3c=5 for nonnegative integers. For c=0, b=0,1,2 gives three assemblies. For c=1, the remainder is 2, so b=0 or 1 gives two more. Total five. This is a coefficient calculation rather than a claim that products are physically interchangeable; if order of assembly matters, a different counting model is needed.

### Recurrences become algebra
For Fibonacci numbers F0=0, F1=1 and Fn=F_{n−1}+F_{n−2}, let F(x)=Σ_{n≥0} Fn x^n. Multiply the recurrence by x^n and sum over n≥2 to obtain F(x)−x=xF(x)+x²F(x), so F(x)=x/(1−x−x²). This one equation encodes all the recurrence values. The algebra requires tracking initial terms; simply writing F=xF+x²F would erase the source term and imply the incorrect zero solution. Generating functions can solve recurrence problems, but ordinary coefficient extraction still matters for obtaining numerical answers.

### Extended laboratory: counting test cases in a configuration system
A configurable learning application has three independent on/off features A, B, C and two user modes student/instructor. At first glance, there are 2³×2=16 configurations. This is a multiplication-principle calculation: choose one of eight Boolean feature assignments and independently choose one of two modes. The word independently here concerns combinatorial choices, not statistical independence. If the instructor-only feature C must be off for students, some of those sixteen syntactically possible configurations are invalid.

Count valid configurations with a case split. For instructor mode, all eight feature assignments are permitted. For student mode, C is fixed false while A and B are free, giving four. Thus there are twelve valid configurations. An independent check counts the forbidden ones: among the original sixteen, exactly four have student mode and C=true, so sixteen minus four equals twelve. The two methods agree. The agreement is a useful test, not the only proof; both calculations rely on exactly the same policy interpretation.

Now add a rule that A and B cannot both be enabled. In instructor mode, A and B have three allowed states (00,01,10), while C remains free, giving six configurations. In student mode, C is false and A,B have three possibilities, giving three. Total is nine. We can also use inclusion–exclusion: start with sixteen; remove four student/C violations and four A/B violations; add back the one configuration where both violations occur? Work through the overlap carefully: student and C=true fixes mode and C but permits any A,B, giving four. A=B=true fixes A and B but permits either mode and either C, giving four. Both conditions together fix mode=student, C=true, A=true, B=true, giving exactly one. Therefore 16−4−4+1=9.

This tiny audit shows why independence assumptions cannot replace logic. The two constraints overlap on one assignment, so subtracting their forbidden sets separately without adding the intersection back gives eight, an undercount. For larger systems a SAT solver may be more suitable than constructing every combination manually. Nevertheless, a small exhaustive oracle is valuable for validating a solver or configuration validator on reduced instances.

The system also needs test execution order. Suppose eight unique inputs must be executed in an ordered regression sequence; there are 8! possible orders. But if the intent is to choose three tests as an unordered smoke-test suite, the count is C(8,3)=56. If test order matters because one test mutates state, the combination formula does not capture all possible operational traces. Distinguish selection of test cases from ordering of executions, and always specify whether repetition is permitted.

Use generating functions for a different resource question. Three components consume one, two and three units of memory, respectively, and may be instantiated in arbitrary nonnegative quantities. The number of ways to consume exactly five units is the coefficient of x^5 in 1/[(1−x)(1−x²)(1−x³)]. Enumerate solutions a+2b+3c=5: with c=0, (a,b)=(5,0),(3,1),(1,2); with c=1, (a,b)=(2,0),(0,1). There are five. Here order of components within the deployment is ignored; if the orchestration order also matters, compositions or word-counting methods would be more appropriate.

For verification, implement a generator that enumerates all sixteen Boolean-mode inputs, records which pass each constraint, and asserts that nine survive the combined filter. Test the limiting cases separately: no constraints yields sixteen, both constraints enabled yields nine, and student-only restrictions yield twelve. Then compare the number of accepted test configurations against the logical specification. The aim is not to maximize test count but to ensure the combinatorial model accurately describes the feature policy and that no forbidden states can leak through the validator.

### Experiment card: binomial coefficients and inclusion–exclusion
The middle-binomial model computes C(n,floor(n/2)). Test n=1 where the result is one, n=4 where it is six, and n=6 where it is twenty. A separate dynamic-programming implementation can construct Pascal's triangle: set C(n,0)=C(n,n)=1 and fill interior cells with C(n−1,k−1)+C(n−1,k). Comparing this recurrence-based implementation with the multiplicative formula helps detect mistakes in both. The largest supported n is twelve, so exact integer arithmetic is straightforward.

The second model counts integers in 1 through 6n divisible by two or three. Count multiples of two as 3n, multiples of three as 2n, and multiples of both as n. Inclusion–exclusion therefore gives 4n. For n=1, the qualifying integers are 2,3,4,6 and the result is four. For n=3, the universe has eighteen elements and the qualifying count is twelve. An enumeration oracle can loop through the complete bounded universe and test whether i mod 2=0 or i mod 3=0.

The two models answer different questions. The binomial coefficient selects an unordered subset of a prescribed size. Inclusion–exclusion counts a union of overlapping conditions. Their connection is in systematic classification and in the avoidance of overcounting. A careful student should explain why binomial coefficients appear in a subset count and why an overlap term must be removed from a union count, rather than memorizing either formula without context.

For an extension exercise, ask what happens to the union count if the universe is 1 through 6n+1. The extra integer might or might not be divisible by two or three depending on n. Since 6n+1 leaves remainder one under division by six, it is divisible by neither two nor three, so the count remains 4n. This concrete edge case tests whether the model counts selected properties rather than blindly multiplying the size of the universe by two-thirds. Another extension is adding divisibility by five, which introduces additional intersections requiring the three-set formula.



## Fully worked questions

### Question 1: Permutations: worked application 1

How many ordered two-person assignments can be made from five distinct people?


**Set up the model and conditions:** There are five choices for the first role.


**Carry out the calculation or proof:** There are four remaining choices for the second role.


**State the result and its scope:** The number of assignments is 5×4=20.


**Independent reasoning check and edge conditions:** Order matters because the two assignments are distinct positions. First choose one of five people for position one; then one of the remaining four for position two. By the multiplication principle there are 5×4=20 outcomes. The same answer comes from the falling-factorial formula P(5,2)=5!/(5−2)!=20. We do not divide by two because switching the assignees produces a different result. If positions were identical, the model would change to unordered selection and would give ten pairs instead.


**Answer:** The number of assignments is 5×4=20.


### Question 2: Combinations: worked application 2

How many unordered pairs can be selected from five distinct people?


**Set up the model and conditions:** There are 5×4=20 ordered pairs.


**Carry out the calculation or proof:** Each unordered pair was counted twice, in both orders.


**State the result and its scope:** The number is 20/2=C(5,2)=10.


**Independent reasoning check and edge conditions:** Select any two different individuals without assigning an order. There are five choices for the first person and four for the second, giving twenty ordered pairs. Every unordered pair {a,b} appears exactly twice among those pairs, as (a,b) and (b,a). Therefore dividing by 2! gives ten distinct committees. The binomial formula C(5,2)=5!/(2!3!)=10 agrees. The key assumption is that the five people are distinct and that repeated selection of the same person is not allowed.


**Answer:** The number is 20/2=C(5,2)=10.


### Question 3: Inclusion–Exclusion: worked application 3

Given 12 Python learners, 9 R learners, 5 both, find how many study either.


**Set up the model and conditions:** Sum the individual group counts to obtain 21.


**Carry out the calculation or proof:** Subtract the five who were counted twice.


**State the result and its scope:** The union has 12+9−5=16 learners.


**Independent reasoning check and edge conditions:** Define P as the set of Python learners and R as the set of R learners in one common survey. The disjoint decomposition of the union consists of Python-only users, R-only users, and users of both tools. The intersection size five was counted in each of |P| and |R|, so subtract it once: 12+9−5=16. Independently, there are 7 Python-only, 4 R-only and 5 dual learners; 7+4+5=16. The result is a count of distinct learners, not of reported tool memberships, which would be twenty-one.


**Answer:** The union has 12+9−5=16 learners.

