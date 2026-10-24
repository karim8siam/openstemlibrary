# Unit 6: Complexity classes

*Editorial draft; not approved for live publication.*

## Time Bounds
**Time Bounds: conceptual explanation**

### Measuring time and input length
Time complexity counts computational steps as a function of input length under a specified machine model. For a bit string x, input length |x| is the number of encoded symbols, not its numerical value. For example, a positive integer N has binary encoding length roughly floor(log2 N)+1. An algorithm using O(N) iterations can therefore be exponential in the length of that binary input. Conversely, iterating once through n elements of an explicit list can be linear in the encoding length of the list. Failing to distinguish these models creates misleading polynomial-time claims.

Big-O states an asymptotic upper bound: f(n)=O(g(n)) if there exist constants C and n0 such that for n≥n0, f(n)≤Cg(n). Big-Theta gives matching upper and lower bounds, while big-Omega gives a lower bound. These notations abstract away constants, but constants and memory traffic matter to implementation decisions. A cubic algorithm may beat a linearithmic one on a tiny fixed input range. Complexity theory does not give a universal measured-runtime prediction for real systems.

Before analyzing an algorithm, fix its primitive operations, encoding, termination rule, and worst-case, average-case, or randomized quantity of interest. For a simple nested loop with n outer iterations and i inner iterations at outer index i, the operation count is 1+2+...+n=n(n+1)/2. Prove the expression algebraically; do not infer O(n^2) from the presence of two loop keywords alone, because their bounds and correlations can differ.

### Step-count proofs rather than loop-count guesses
Consider the code: for i from 1 to n, perform i constant-cost operations. The total is Σ_i i = n(n+1)/2. Using n≥1, this lies between n²/2 and n², up to lower-order terms, so runtime is Θ(n²) in the unit-cost model. If inner loop length were instead n/i and integer division were used, the total could resemble n·H_n=Θ(n log n), a substantially different result despite syntactically nested loops. Counting occurrences of 'for' in code is not an asymptotic analysis method.

Binary encoding can change a bound more dramatically. An algorithm that loops N times after reading an N-valued integer represented in binary uses time Θ(N) but its input length is Θ(log N), yielding exponential worst-case dependence on encoding length. A pseudo-polynomial dynamic-programming algorithm can perform very well when numerical magnitudes are moderate while lacking a polynomial bound in the bit-length of its largest numeric parameter. This is common in knapsack-style algorithms and should be explained without equating pseudo-polynomial with universally impractical.

Distinguish resource functions for different models: a randomized algorithm has a distribution over runtimes or answers; a nondeterministic machine's time measure follows its formal acceptance model; a parallel computation has work and span rather than one serial step count. Standard polynomial-time robustness relies on reasonable machine encodings, not on arbitrary operations such as factoring an enormous integer in one declared unit step.

When giving a Big-O answer, identify constants and the threshold n0. Saying T(n)=O(n²) means there exist constants such that T(n) is eventually bounded above by Cn². It does not imply T(n)≥cn² or that the function increases monotonically at every integer.

## Space Bounds
**Space Bounds: conceptual explanation**

### Space bounds and machine configurations
Space complexity measures how many work-tape cells or equivalent memory units a computation uses, usually excluding a read-only input tape in formal complexity classes. This convention is why logarithmic-space algorithms are meaningful even though their input is already n symbols long. A counter from 0 to n can be stored in O(log n) bits, whereas explicitly copying an n-bit input uses O(n) additional bits. Recursion depth can contribute to space usage even when each activation record is small.

For a deterministic machine with polynomially bounded work space s(n), there are only finitely many possible configurations on a fixed n-bit input: choices include control state, work-tape contents, and head positions. If a deterministic machine revisits the same complete configuration without having halted, it will repeat its future behavior forever. This configuration argument helps explain why space bounds can yield upper bounds on time for deciders with certain conventions. The number of configurations is exponential in s(n) up to machine-dependent factors.

Savitch's theorem states that nondeterministic space s(n) can be simulated deterministically within O(s(n)^2) space for sufficiently large s(n), such as s(n)≥log n. The theorem is not merely a claim that trying every path is efficient. It uses a recursive reachability idea in a configuration graph, trading potentially enormous time for controlled space. Distinguish a theoretical complexity upper bound from a practical algorithm one should run on large graphs.

### Graph reachability and log-space intuition
In a graph with n vertices, a vertex identifier needs O(log n) bits. A deterministic graph traversal using an explicit visited bitmap uses Ω(n) bits beyond the input in the straightforward representation. However, nondeterministic reachability can guess a path while maintaining only a current vertex and a step counter of O(log n) bits, with appropriate choices and a polynomial length bound. This helps motivate NL, the class of languages decidable by nondeterministic logarithmic-space machines.

The theorem NL=coNL is a nontrivial space-complexity result; it should not be justified by the false statement that a nondeterministic machine can simply reverse accept and reject states. On a nondeterministic machine, acceptance means at least one successful branch, so complementing branch labels does not produce universal rejection. The Immerman–Szelepcsényi theorem uses counting-style ideas to establish closure under complement for suitable nondeterministic space classes. This illustrates why decision-class relationships require proofs, not only visual Venn diagrams.

Savitch's theorem gives deterministic space O(s(n)²) for nondeterministic space s(n)≥log n. A recursive algorithm asks whether configuration y is reachable from x within at most 2^t steps and guesses an intermediate configuration at halfway depth. The recursion stores only a logarithmic number of configuration descriptions per depth, controlling space despite astronomical possible paths. The recurrence is expensive in time but demonstrates a surprising space upper bound.

For a simulator, show configuration counts for finite toy machines, but make clear that configuration-graph size depends exponentially on work space and on representation conventions. A small observed path length is not a general theorem about space complexity.

## P And Np
**P And Np: conceptual explanation**

### P, NP, witnesses and verification
P is the class of decision languages decidable by deterministic polynomial-time algorithms. NP is the class of decision languages whose yes-instances have polynomial-size certificates verifiable in deterministic polynomial time, equivalently recognizable by nondeterministic polynomial-time machines. NP does not stand for 'not polynomial.' Every P problem belongs to NP because a verifier can ignore a certificate and run the deterministic decider. Whether P=NP remains an open mathematical question; no finite set of solver benchmarks resolves it.

SAT asks whether a Boolean formula has an assignment making it true. An assignment to n variables can be represented using n bits, and a verifier evaluates the formula under that assignment in time polynomial in the formula encoding length. This establishes SAT∈NP. It does not show that finding a satisfying assignment is polynomial-time; brute-force search considers up to 2^n assignments. For a 3-CNF formula with clauses (x∨y∨z) and (¬x∨y∨¬z), test assignment x=1,y=0,z=1: the first clause is true, the second false, so the conjunction is unsatisfied. A verifier reports rejection of this certificate, not unsatisfiability of the entire formula.

When explaining search-versus-decision, distinguish finding one witness, checking a proposed witness, and deciding that no witness exists. Complementing a verifier's answer does not automatically provide an NP certificate for no-instances. That asymmetry motivates questions about NP, coNP, and proof systems.

### Certificates and quantifiers
A polynomial-time verifier V(x,c) establishes that a language L is in NP when x∈L if and only if there exists a certificate c of length at most polynomial in |x| for which V accepts, and V runs in polynomial time in the encoded input length. The existential quantifier is essential. For SAT a certificate is a truth assignment. An invalid assignment does not prove unsatisfiability, and a verifier's ability to reject particular certificates does not amount to a polynomial-time SAT solver.

For a graph with n vertices, a claimed Hamiltonian cycle can be encoded as an ordered list of n vertex identifiers. The verifier checks that each vertex appears exactly once and that every consecutive pair, including the last-to-first pair, is connected by an edge. These checks are polynomial in the explicit graph size. This proves the yes-witness condition, not that a cycle can be found efficiently. For a graph that lacks such a cycle, the verifier may reject exponentially many attempted sequences without having a succinct no-certificate from this construction.

Consider a common misunderstanding: NP problems are not all known to require exponential time. They are precisely those with polynomially verifiable yes-witnesses under the standard definition. Many NP languages are already in P. NP-complete languages are believed to be the hardest members of NP under polynomial reductions, but it remains unknown whether there is a deterministic polynomial-time solver for them.

The lab should compare a trusted certificate verifier against a brute-force solver on very small inputs. The two components answer different questions: the verifier checks a proposed witness, and the solver searches. Keep the APIs separate so the user cannot confuse 'this candidate failed' with 'no candidate exists'.

## Completeness
**Completeness: conceptual explanation**

### NP-completeness and reductions
A language B is NP-hard if every language in NP reduces to B by a polynomial-time many-one reduction. It is NP-complete if it is both NP-hard and a member of NP. To prove a fresh problem NP-complete, first establish polynomial verification; then select an already-known NP-complete source problem and build a correct polynomial-time transformation to the target. A proof must show yes-to-yes and no-to-no preservation, often by interpreting the target's feasible structures as source assignments.

As a concrete example, 3-SAT can be reduced to CLIQUE by creating one graph vertex for each literal occurrence in each clause. Connect vertices from different clauses when they are not contradictory. A clique with one vertex chosen from each of m clauses has size m exactly when a consistent selection of satisfying literals exists. The graph has polynomial size in the formula. Trace the reduction on a formula with two short clauses and identify precisely why opposite-literal vertices lack an edge. Reversing the implication or permitting two vertices from one clause breaks the proof.

NP-completeness is a worst-case asymptotic classification. It does not imply that every instance of a target problem is hard or that every exact algorithm is useless in practice. Solvers exploit structure, parameterization, constraints and heuristics. A claimed optimal solver must still report whether it guarantees correctness, bounds runtime, or only returns a plausible candidate. Such distinctions are part of making complexity theory relevant to software engineering.

### A reduction proof is a two-way semantic argument
For a 3-SAT instance with clauses C1,...,Cm, make a graph with one vertex per literal occurrence. Connect vertices that come from different clauses and do not contradict one another. If the Boolean formula is satisfiable, choose one true literal from each clause; no selected pair is complementary under that assignment, so the chosen vertices form a clique of size m. Conversely, if there is an m-clique, it contains at most one vertex from each clause because within-clause edges are absent. Thus it picks exactly one literal per clause, and mutual compatibility means the choices can be extended to a consistent satisfying assignment.

To test the reduction, build a formula with two clauses and inspect all cross-clause pairs. Remove an edge between x and ¬x. If a graph builder mistakenly connects contradictory literals, a clique may exist even when there is no consistent assignment. This is a correctness failure of the reduction implementation, not a refutation of NP-completeness. A proof must also show the graph is constructible in polynomial time: there are at most O(L) vertices and O(L²) candidate edges, where L is the total number of literal occurrences.

The reduction direction is from known-hard 3-SAT to CLIQUE, proving CLIQUE is NP-hard. Membership in NP is proved separately because a clique's vertices are a polynomial-length certificate whose pairwise edges can be checked in polynomial time. Only then is the term NP-complete justified.

A different transformation may prove a variant such as INDEPENDENT SET hard by taking graph complements with correct conventions. Avoid assuming that every graph optimization form is automatically equivalent to its decision version without explaining the threshold connection.

## Integrated Case Study and Model Limitations
**Unit synthesis: Complexity classes.** The following case study integrates formal definitions, correctness reasoning, limitations and realistic testing.

### Complexity triage for a scheduling problem
Consider a planning application that assigns n tasks to slots while respecting resource conflicts. Some restricted instances admit greedy or dynamic-programming solutions; a richer formulation may encode graph coloring or SAT. Before selecting an algorithm, identify the exact decision version: 'is there a feasible schedule using at most k slots?' A numerical optimization goal, 'minimize slots', must be related carefully to its threshold decision problem. Constraints such as task durations, precedence, and resource capacities change both modeling fidelity and complexity.

Write down the encoding size: if all pairwise conflict relationships are explicit, the input can contain O(n^2) bits; if constraints are generated by compact arithmetic descriptions, it may be much smaller. The same O(n^2) runtime can be nearly linear in a dense explicit encoding but much larger than the number of tasks. For yes-instances, a proposed slot assignment is an efficiently checkable witness: inspect all conflicts and slot bounds. This observation suggests membership in NP for the decision formulation, assuming numbers and constraints are polynomially representable.

Build a tiny reference implementation that enumerates every assignment for n≤8. Use it to test a heuristic on solvable and impossible cases, recording optimality gaps. For larger n, report heuristic results honestly without claiming an optimal answer unless a matching certificate or proven bound exists. Formal complexity does not remove the need for experimental design; it tells us which guarantees should be viewed skeptically.

### Fair benchmarking of exponential-time solvers
Suppose an exact SAT solver handles instances with thousands of variables in some practical workloads. This does not contradict worst-case NP-completeness: heuristics, clause structure and learned constraints can make typical instances tractable while adversarial instances remain hard. To evaluate a solver, record input encoding, clause-to-variable ratio, distribution of formulas, solver version, timeout, random seed and memory limit. Report median, tails and failure rates rather than only the fastest successful case.

Use small instances with at most twenty variables to cross-check an optimized solver against exhaustive enumeration. Every assignment is a finite witness candidate, so exhaustive search decides those instances given adequate resources. For larger instances, a solver can return SAT with an assignment that can be independently verified. UNSAT claims may be supported by proof logs in appropriate formats; without a certificate or trusted checker, the claim rests on implementation correctness.

Model instances can encode scheduling, verification or planning, but the quality of an encoding matters. A bug in a constraint translation might produce SAT for a formula that does not represent a valid schedule. Have a second program interpret found assignments back into domain objects and check every original constraint. This checks the translation boundary as well as the SAT core.

The broader practical lesson is to combine theorem-based limits with transparent engineering evidence. Worst-case complexity tells us which universal efficiency claims remain unproved; certificates and oracle tests tell us whether a particular solution is right; benchmarks describe only the measured workload.

### Complexity proof notebook
Choose a binary-encoded input integer N and compute its bit length for N=15,31,63. An algorithm that counts through N uses 15,31,63 steps while input lengths are four, five and six. The near doubling of work per added bit foreshadows exponential growth. Contrast with an algorithm that traverses an explicit list of N elements, where the input itself already contains N item encodings. Input-length conventions change the mathematical complexity question.

Verify a SAT assignment independently, then try a second assignment and show that rejection of one witness does not prove nonexistence. For an NP-hardness reduction, write a transformation from known-hard 3-SAT into CLIQUE, show polynomial output size, and prove both yes-to-yes and no-to-no behavior via consistent literal selection. Use a small brute-force solver to cross-check the reduction on instances with very few variables. All these exercises separate verification, search, transformation and proof, preventing the common mistake of calling a successful example a universal theorem.

### Independent self-check: complexity quantifiers
Write what a bound O(n²) says for all sufficiently large n, including constants, and then distinguish input bit length from an encoded numeric value. Demonstrate a certificate for a satisfiable Boolean formula and explicitly separate 'this assignment fails' from 'the formula is unsatisfiable.' Finally, check a reduction proof has both directions and polynomial transformation size. These habits prevent four common errors: guessing runtime from syntax, silently changing input encodings, confusing verification with existence, and using a reduction with the wrong direction.

### Worked question: Input encoding and pseudopolynomial time
An algorithm takes numerical integer N in binary and performs N loop iterations. Is the number of iterations polynomial in input length?

**State the formal contract**
For positive N, the input length n is approximately log2 N, since n=floor(log2 N)+1. Therefore an integer of n bits can be as large as 2^n−1.

**Derive the result**
The loop may execute Θ(2^n) iterations on n-bit inputs, exponential in n. A bound polynomial in numerical N alone is not automatically polynomial in the length of N’s encoding.

**Check the scope and a counterexample**
If the input were supplied in unary, its encoding would itself have length Θ(N), changing the classification. Complexity statements must say how integers are represented.

**Answer:** Not in general; the runtime can be exponential in binary input length.

### Worked question: SAT certificate verification
Formula F=(x∨y∨z)∧(¬x∨y∨¬z). Check the assignment x=true, y=false, z=true. Does a failed certificate prove unsatisfiability?

**State the formal contract**
The first clause is true because x and z are true. The second clause evaluates to false∨false∨false, hence false. The conjunction therefore evaluates to false.

**Derive the result**
The proposed assignment is not a satisfying witness. However, setting y=true satisfies both clauses, showing the formula is in fact satisfiable.

**Check the scope and a counterexample**
The verifier rejects an individual certificate; a rejection does not conclude that all 2^3 possible assignments fail. Distinguish verification from search or universal negative proof.

**Answer:** The given assignment fails, but F is satisfiable, for example with y=true.

### Worked question: Graph-based NP reduction invariant
In a reduction from 3-SAT with m clauses to CLIQUE, why must target clique size be m and why are within-clause edges omitted?

**State the formal contract**
The construction creates one vertex for each literal occurrence and edges between compatible literals from different clauses. A size-m clique should select a consistent literal from each of m clauses.

**Derive the result**
If vertices from the same clause were connected, a clique could waste multiple selections in one clause and fail to witness satisfaction of every clause. Forbidding those edges ensures each chosen clique vertex comes from a different clause.

**Check the scope and a counterexample**
The proof must check compatibility and both implication directions; the graph has polynomially many vertices and edges because it is built from the source formula’s literal occurrences.

**Answer:** Clique size m encodes one mutually compatible chosen literal per clause.
