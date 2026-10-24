# Unit 1: Logic and proof


## Propositions

**Core model — Propositions**

A proposition is a declarative sentence with a definite truth value in a specified interpretation. Connectives are defined by truth tables; implication P->Q is false only when P is true and Q is false.

**Original worked illustration**

For P=true and Q=false, P->Q is false while its contrapositive (not Q)->(not P) is also false. The converse Q->P, however, need not be equivalent.

**Boundary conditions and checks**

Natural-language 'or' is sometimes exclusive, but standard propositional disjunction is inclusive unless explicitly defined otherwise.

### Semantic interpretation and an executable truth-table audit
A syntax tree fixes the grouping of connectives before any truth values are assigned. Consider the expression (A or B) and (not C). The root node is conjunction, its left child is disjunction, and its right child is negation. A correct evaluator walks the tree bottom-up: first read the values of A, B, C; evaluate the disjunction; invert C; then conjoin the two results. This is different from interpreting A or (B and not C), which has a different root and can disagree. On A=true, B=false, C=true, the first expression is false but the second is true. Parentheses are not typographic decoration; they are part of the expression's semantics.

Material implication is an especially useful source of errors. A implies B denotes (not A) or B, so it does not express causation and does not assert that A ever happens. For a software contract, "if authentication succeeds, a session token is issued" places no condition on failed authentication. To specify that tokens are issued only following success, one needs the reverse implication as well. Together the two clauses form a biconditional. The distinction matters when formal tests uncover a token issued to an unauthenticated user: the original one-way claim may not be violated, even though the intended policy is.

Two formulas are equivalent when they yield equal results under *every* truth assignment, not merely in one example. To verify A implies B is equivalent to not B implies not A, enumerate the four rows (false,false), (false,true), (true,false), (true,true) in a fixed order. The implication columns are respectively true,true,false,true in both formulas. A truth-table check for n different Boolean variables has 2^n assignments; it is exhaustive for bounded n but grows exponentially. Symbolic equivalence transformations or SAT solvers are preferable for large specifications.

### Proof move: replacing implication without changing meaning
Take the compound condition (A implies B) and A. Substitute ((not A) or B) and A, distribute conjunction to obtain (A and not A) or (A and B), discard the contradictory term, and conclude A and B. Thus modus ponens can be justified as a valid inference rule. In a code review this is not permission to infer B from an observed B: that would be affirming the consequent. A service may issue a response for reasons unrelated to the branch represented by A.

Truth tables are also useful for checking whether a security policy is unsatisfiable. Let L mean "logged in" and D mean "data downloaded". Suppose requirements say L implies D, D implies L, and not (L and D). Setting both false satisfies all three, so the system has a possible state but never allows downloading. Adding a requirement that some user can download makes the combined constraints inconsistent. This illustrates why satisfiability and usefulness are separate questions: an internally consistent specification may still implement an unacceptable product.

### Practice and limitations
Write a four-row table for (A and B) implies A, and show why this formula is always true. Then compare A implies (B or C) with (A implies B) or (A implies C) by algebra, not by assertion. They are equivalent; distribute not A across the disjunction. As a counterexample to an unjustified inference, choose A=false and B=true, which makes A implies B true without making A true. When a Boolean formula describes a real system, also state how input propositions are measured. A perfectly evaluated predicate over unreliable sensor flags does not establish a reliable physical guarantee.



## Predicates

**Core model — Predicates**

Predicates turn assertions into truth-valued functions of variables. A quantifier binds a variable over a named domain; changing the quantifier order can change meaning.

**Original worked illustration**

Over integers, 'for all x there exists y with y>x' is true, while 'there exists y such that for all x, y>x' is false.

**Boundary conditions and checks**

Negating 'for all x P(x)' gives 'there exists x not P(x)' rather than 'for all x not P(x)'.

### Quantifiers as programs over explicit domains
A predicate P(x) is a rule producing true or false for values x from a declared domain. Binding x with universal quantification means checking that no counterexample exists; binding it existentially means showing at least one witness. Over a finite array of length m, these correspond to loops: "every item meets condition" starts with true and turns false when one item fails; "some item meets condition" starts with false and turns true when one item succeeds. On an empty array, the universal test is true and the existential test is false. These conventions follow the logical definitions and allow mathematical invariants to describe program behavior precisely.

Variable scope is important. In "for every request r there exists a server s able to handle r", the chosen server is allowed to depend on the request. The apparently similar "there exists a server s that can handle every request r" demands one universal server. Imagine servers S1 and S2, where S1 handles video but not audio, and S2 handles audio but not video. The first sentence is true while the second is false. A compiler specification or deployment policy that reverses quantifiers may impose a much stronger condition than intended.

### Negation by structural recursion
To negate for every x, P(x), search for an x where P(x) is false. To negate there exists x, P(x), assert that P(x) fails for every x. For nested quantifiers, move negation inward one binder at a time: the negation of "for every x exists y, R(x,y)" is "exists x for every y, not R(x,y)". This gives a concrete method for finding failing test cases. If a matching algorithm claims that every student can be assigned some available tutor, a counterexample consists of a particular student for whom no tutor is eligible. One should not claim failure merely because a chosen greedy assignment failed; perhaps another assignment exists.

For the integers Z, forall x exists y such that y>x is true: select y=x+1. Exchanging the quantifiers is false, since an alleged globally maximal integer M is defeated by x=M+1. This proof explicitly uses the unbounded integer domain. If the domain changes to {0,1,2,3}, the first statement becomes false because 3 has no greater element inside the domain; the second remains false. A domain change can alter the truth of the same printed formula.

### Queries, joins, and quantification
Existence conditions appear in database queries: a student is eligible if there exists a passed prerequisite record. Universal requirements are often implemented using the absence of a counterexample: a student has completed all required modules if there does not exist a required module for which there does not exist a completion record. This double-negation pattern is logically precise but must account for null or unknown database values; classical two-valued logic is not identical to SQL's three-valued interpretation. The empty-set boundary is also a product decision: formally a student has completed all requirements when the requirement set is empty, but the application may need a rule preventing empty curricula.

### Practical self-check
Translate the statement "every enrolled student has at least one verified email address" into quantifiers over Student and Email records. Then negate it and describe exactly what record would witness failure. When validating an automatic checker, test no students, one student without email, two students sharing an address, and one student with multiple verified addresses. Keep domain restrictions separate from the logical core. A checker that silently treats unverified addresses as verified implements a different predicate, even when its quantifier structure is correct.



## Induction

**Core model — Induction**

Mathematical induction uses a base case and a successor implication to establish a property over natural numbers. Strong induction allows the induction step to use all previous cases.

**Original worked illustration**

To prove 1+2+...+n=n(n+1)/2, verify n=1, then add n+1 to n(n+1)/2 and factor (n+1)(n+2)/2.

**Boundary conditions and checks**

The induction hypothesis is conditional, not a statement that may be assumed true without the base case and step.

### Invariant-based induction rather than pattern memorization
Induction proves a proposition P(n) for every natural number starting at a base index n0. The logical skeleton contains a verified base P(n0), a universally quantified implication P(k) implies P(k+1) for arbitrary k at least n0, and the conclusion that all subsequent cases hold. The crucial word is arbitrary: checking the step for k=1,2,3 is merely testing examples. The induction hypothesis may be used at k, but P(k+1) cannot be assumed while proving itself.

For the summation identity S(n)=n(n+1)/2, the base n=1 yields 1=1. Assuming S(k)=k(k+1)/2, append k+1 to the sum and factor: S(k+1)=k(k+1)/2+(k+1)=(k+1)(k+2)/2. Every algebraic step has a reason. The formula says nothing about the number of loop iterations in an arbitrary program unless that program's work really matches the sum. A triangular nested loop where the inner index ranges 1 through the outer index performs exactly S(n) body executions; if either loop has an early exit, the count may be smaller.

### Strong induction and recursive definitions
Strong induction assumes P(j) for all indices n0<=j<=k when proving P(k+1). This form matches recurrence relations whose new value depends on more than one predecessor. For example, a positive integer can be expressed as a sum of powers of two. Base n=1 is 2^0. For n>1, choose the largest power 2^m no greater than n. If n=2^m the proof ends. Otherwise the remainder r=n-2^m satisfies 1<=r<n and strong induction represents r as powers of two; adding 2^m represents n. The construction suggests a greedy decomposition, though uniqueness requires an additional argument about binary place values.

To prove termination of a recursive function, use induction on a well-founded measure. If an algorithm repeatedly removes the last element from a finite list, the measure is list length, a nonnegative integer decreasing by one at every recursive call. A recursively defined operation that sometimes leaves the measure unchanged has not yet been shown to terminate. The measure may need to be a pair of nonnegative integers ordered lexicographically; complexity of the state alone is not a proof.

### Loop invariants as inductive claims
Consider an iterative algorithm computing factorial: initialize product=1 and i=1; while i<=n, multiply product by i and increment i. At loop entry, the invariant is product=(i-1)!. It holds initially since 0!=1. If it holds at the beginning of an iteration, the multiplication changes product to i!, and incrementing i restores the invariant in the form (new i-1)!. On exit i=n+1, so product=n!. State the precondition n>=0 and the assumption of exact integer arithmetic; fixed-width integer overflow invalidates the numerical conclusion in typical programming languages.

### Common induction traps
A famous invalid proof claims that all horses have the same color. It considers an n+1 group, applies the hypothesis to its first n and last n horses, and concludes all match because the groups overlap. The overlap is empty when n=1, so the step from one to two is invalid. The example teaches the importance of checking boundary values for each claimed transformation. Another trap is proving a recurrence for n>=2 while forgetting to check two base cases. The number of base cases should cover every branch of the recurrence, not follow a remembered template.



## Contradiction

**Core model — Contradiction**

Proof by contradiction assumes the negation of the target and derives an impossibility. It is logically valid in classical logic but may obscure the constructive witness.

**Original worked illustration**

Assuming sqrt(2)=a/b in lowest terms forces a and b both even after squaring and considering parity, contradicting lowest terms.

**Boundary conditions and checks**

A derivation of an unrelated false statement from an unsupported extra premise is not a proof of the original theorem.

### Finding the right negation for a contradiction proof
A proof by contradiction assumes the negation of the desired statement and obtains a logical impossibility. The impossibility may be a direct formula X and not X, a violation of an established bound, or conflict with an already proved theorem. The method does not allow inserting a disputed assumption as if it were known. Before starting, write the exact logical negation; for existential claims, this often changes an existence quantifier to a universal one, and for statements with multiple clauses De Morgan's laws must be applied carefully.

To show that sqrt(2) is irrational, assume sqrt(2)=a/b for integers a,b with b nonzero and the fraction reduced to lowest terms. Squaring yields a^2=2b^2, making a^2 even and therefore a even. Write a=2c; substitution yields 4c^2=2b^2, hence b^2=2c^2 and b even. But then a and b share a factor 2, contradicting lowest terms. The proof uses the fact that an odd square is odd. It does not prove that every nonperfect-square root is irrational without further argument.

### Contrapositive proofs are often more constructive
To prove "if n^2 is even, then n is even", instead show "if n is odd, n^2 is odd". Writing n=2k+1 gives n^2=4k^2+4k+1=2(2k^2+2k)+1. This direct algebra is simpler than assuming n^2 even and n odd and announcing a contradiction without showing the intermediate calculation. Contraposition and contradiction are related but should not be confused with the converse; the proof of P implies Q does not establish Q implies P.

There is a computational analogue: an assertion "no input reaches an unsafe state" can be refuted by one concrete input and its execution trace. However, failure to find such a trace is not a proof of safety if the explored inputs cover only a finite subset of possibilities. Formal verification uses inductive invariants, symbolic state exploration, or theorem proving to turn test evidence into broader conclusions under explicit assumptions.

### Infinite sets and diagonalization
Suppose there were a complete list of infinite binary sequences s1,s2,s3,... . Construct a new sequence t where its nth bit differs from the nth bit of sn. Then t differs from every listed sequence in at least one position, so the list is not complete. This diagonal argument demonstrates that the set of infinite binary sequences is not countable. Its force comes from the construction relative to an arbitrary proposed enumeration, not from a large numerical estimate of how many sequences exist. For finite-length bitstrings, a complete enumeration is possible because there are exactly 2^n strings of length n.

### Decision-making checklist
Before trusting a contradiction proof, confirm that the initial negation is correct, each implication follows from declared assumptions, and the derived contradiction cannot be resolved by a hidden case. In impossibility results about algorithms, distinguish computationally impossible, mathematically impossible, and impossible within a restricted model. A result that no comparison-based algorithm can sort n arbitrary distinct keys with fewer than a constant multiple of n log n comparisons is not a claim about radix sorting under bounded-key assumptions. The model is part of the theorem.

### Extended laboratory: verifying a login-and-download policy
Consider an educational platform with three Boolean state flags: L means the user has authenticated, R means the user's role permits the requested resource, and D means the platform actually allowed a download. The intended safety rule is D implies (L and R). This rule does not require that all authenticated authorized users download; it says that a download must never happen without both prerequisites. A different progress rule might say (L and R and Q) implies eventually D, where Q represents an actual download request. The first rule is a propositional invariant on a state; the second introduces temporal behavior and cannot be established from a simple eight-row truth table.

Construct all eight assignments of L,R,D. A violation of the safety rule occurs precisely when D=true and either L=false or R=false. There are three invalid assignments: (L,R) equal (false,false), (false,true), or (true,false) with D=true. There are five satisfying assignments. The count is a useful check: four states have D=false and automatically satisfy implication; exactly one state with D=true satisfies its consequent. Observe how an overly permissive test might count any downloaded resource as success and miss every unsafe assignment.

Build the Boolean condition V=D and ((not L) or (not R)). By De Morgan's law this is the same as D and not(L and R). If V is true, the safety rule is violated. An implementation can compute V directly from recorded events, but it needs reliable mappings from real-world authentication and authorization to the flags. A stale token, a race between permission revocation and file delivery, or a database failure can make the flags inconsistent with the actual conditions. The propositional result establishes what the program should reject, not that the deployment already rejects it.

Suppose the business requirement adds "every approved download request eventually receives a response." Translate it as: for each request x, if Approved(x) then eventually Responded(x). A trace that ends after approval without a response is not automatically proof of a liveness violation; it may be a finite prefix of a longer execution. An infinite execution that postpones the request forever is a genuine counterexample when the system's fairness conditions require processing. This is why model checking must distinguish finite safety witnesses from infinite liveness counterexamples.

For a finite validation dataset, write a checker that scans each event and records the first event with D and not(L and R). Its worst-case work is linear in the number of events. The loop invariant is that all inspected earlier events satisfy the safety condition. At the end, absence of a violation proves the rule only for the scanned dataset. If some downloads were not logged, the conclusion does not cover them. A negative finding is evidence about observability and coverage, not a mathematical theorem about unseen production behavior.

Now design negative tests. When L=false, R=false, D=true, the policy must reject; when L=true, R=false, D=true it must reject; when L=false, R=true, D=true it must reject; and when L=true, R=true, D=true it may allow. With D=false, all four combinations satisfy the implication, although the user experience may have separate availability requirements. For the software, make the expected result explicit before running the test. A checker that marks all D=false cases as system success could hide a broken product that never serves any request.

Finally separate evidence into three layers. The truth-table enumeration demonstrates the Boolean claim for all mathematical assignments. Executing the validator for all eight inputs demonstrates its bounded implementation behavior. Integration tests with real sessions and storage permissions demonstrate that actual services set L, R and D as expected for representative cases. These layers reinforce one another but cannot be substituted for one another. The most instructive question is not simply whether a formula is true, but which precise claim the formula supports and what additional real-world assumptions would be necessary to trust it.

### Experiment card: from formula to reproducible Boolean test
Use the primary model in this unit to choose a number n of Boolean variables. The model reports 2^n assignments. To check the count independently, write a binary counter that iterates integer masks from zero through 2^n−1 inclusive. For each integer mask, examine its n least significant bits as a truth assignment. Exactly two choices exist for each bit, yielding the predicted product. With n=1 the enumerator should output two states; with n=3 it should output eight; at the permitted maximum n=12 it should output 4096. Report the exact number, rather than converting it to an estimate by repeated rounding.

Run the separate De Morgan model, which enumerates the same assignment domain to compare not(A1 and ... and An) with (not A1) or ... or (not An). The predicted mismatch count is zero for every n in the supported range. A mismatch would indicate an implementation error or a misinterpretation of Boolean values; a zero mismatch at n≤12 is exhaustive *for that finite size*, not a stand-alone proof for arbitrary n. The general proof follows from the binary De Morgan identity applied repeatedly, or by an inductive argument over the number of variables. The simulation makes it easier to spot an incorrect implementation of logical OR as exclusive OR.

Keep the distinction between the assignments being enumerated and the truth of the target identity. The number 4096 measures possible inputs at n=12. Zero is the number of counterexamples discovered to the stated identity in those inputs. The values answer different questions and should not be presented on the same axis without labels. In a web reader, a slider change should update both the displayed n and the computed result, while Reset should restore the documented initial value. Invalid noninteger or out-of-range input must be rejected by the model even if an HTML range slider ordinarily prevents it.

Challenge the model's teaching limit: truth-table enumeration is exponential in n, so an interactive browser should cap input size to avoid a frozen page. For a formula involving more variables, a SAT solver or symbolic manipulation engine may avoid enumerating all rows. That optimization changes the reasoning technique, not the truth of the underlying identity. A successful classroom model reports the supported domain and does not imply that an exhaustive enumeration scales to unrestricted software verification.



## Fully worked questions

### Question 1: Propositions: worked application 1

Evaluate P→Q and its contrapositive for P=true and Q=false.


**Set up the model and conditions:** P→Q is false precisely when the antecedent is true and consequent false.


**Carry out the calculation or proof:** The contrapositive ¬Q→¬P is true→false, also false.


**State the result and its scope:** The implication and contrapositive agree, as required.


**Independent reasoning check and edge conditions:** The truth assignment matters. For P=true and Q=false, implication P→Q fails because it promises Q whenever P occurs, and this is the unique failing combination. In the contrapositive, the antecedent ¬Q is true and the consequent ¬P is false, so it fails for exactly the same assignment. This is a local calculation consistent with the general equivalence theorem. The converse Q→P is true on these values, however, because its antecedent Q is false. That explicit comparison shows why replacing a statement by its converse would be an invalid reasoning step.


**Answer:** The implication and contrapositive agree, as required.


### Question 2: Predicates: worked application 2

Negate the assertion ∀x∈Z ∃y∈Z such that y>x.


**Set up the model and conditions:** Push negation through the outer universal: ∃x∈Z ¬(∃y∈Z:y>x).


**Carry out the calculation or proof:** Push negation through the existential and the comparison.


**State the result and its scope:** The negation is ∃x∈Z ∀y∈Z such that y≤x.


**Independent reasoning check and edge conditions:** First identify the scope of every binder: the original statement selects an arbitrary integer x, then permits y to depend on x. Negating the universal binder produces an existential witness x. Negating the remaining existential binder produces a universal claim about y. Finally negate y>x to obtain y≤x. The resulting formula asserts that some integer is at least as large as every integer. It is false for Z because choosing y=x+1 defeats any proposed x. The negation itself is still logically correct, regardless of whether it is true in the selected domain.


**Answer:** The negation is ∃x∈Z ∀y∈Z such that y≤x.


### Question 3: Induction: worked application 3

Prove 1+...+n=n(n+1)/2 by induction.


**Set up the model and conditions:** At n=1 both sides equal one.


**Carry out the calculation or proof:** Assume the result for n and add n+1: n(n+1)/2+(n+1)=(n+1)(n+2)/2.


**State the result and its scope:** The formula holds for all positive integers.


**Independent reasoning check and edge conditions:** An inductive proof needs an arbitrary k, not merely the numerical examples n=2 and n=3. The induction hypothesis asserts that the sum of the first k integers equals k(k+1)/2. Appending the one new term k+1 yields (k(k+1)+2(k+1))/2. Factoring the numerator produces (k+1)(k+2)/2, which is exactly the target formula with n replaced by k+1. The base case n=1 supplies the start. Together these premises establish the identity for every positive integer. The same sum also counts the operations in a triangular nested loop.


**Answer:** The formula holds for all positive integers.

