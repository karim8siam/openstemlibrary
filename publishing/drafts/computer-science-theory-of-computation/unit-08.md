# Unit 8: Formal applications

*Editorial draft; not approved for live publication.*

## Verification Limits
**Verification Limits: conceptual explanation**

### Model checking and bounded state spaces
Model checking takes a formal transition system and a property, then algorithmically determines whether the system satisfies that property under the chosen semantics. For a finite-state model, reachability properties can be checked by graph search. If S is the state set and E the transition relation, breadth-first search from initial state s0 identifies all states reachable along zero or more transitions. A safety property states that some bad condition never occurs on reachable states; its violation is witnessed by a concrete path to a bad state. A liveness property concerns eventual progress and may require examining cycles and fairness assumptions.

In temporal logic, CTL's EF p means there exists a path on which p holds eventually. For a finite graph, EF p can be checked backward by starting with p-states and repeatedly adding predecessors. In contrast, AG p asserts p on every reachable state along all paths and can be refuted with one reachable not-p state. Don't treat EF and AF as interchangeable: existence of one successful path is weaker than eventual success on every path. For models with deadlocks, the handling of infinite paths and totalized transitions must be specified.

State explosion occurs when composing components. If component A has m states and B has n states, a straightforward product has at most mn states before reachability pruning. Three independent Boolean flags alone admit eight combinations. Symmetry reduction, abstraction and compositional reasoning reduce practical workloads but require soundness arguments about which properties they preserve.

### Prove reachability properties on an explicit graph
Let a transition system consist of finite state set S, initial state s0, relation E and atomic propositions labeling states. For safety claim AG ¬bad, perform graph reachability from s0 and check every discovered state. If a reachable state satisfies bad, reconstruct the predecessor pointers to produce a finite counterexample trace. If the reachable search exhausts all states without a bad state, the claim holds for the finite model, assuming the transition relation and labeling are correctly encoded.

For EF target, start backward from every state labeled target and repeatedly add predecessors until the set stops changing. The resulting least fixed point includes exactly the states from which some finite path eventually reaches target. To establish this, induct on the length of the shortest target-reaching path. The base includes target states themselves. Every predecessor of an already included state has a path one step longer. Conversely, every state added by the algorithm has such a witness path. This is more rigorous than saying the checker 'tries paths until it finds one'.

State the treatment of terminal states. Many temporal-logic definitions use infinite paths, so deadlocked states may be supplemented with self-loops or treated according to a documented alternative convention. That choice can affect liveness formulas. On a branching system, EF p and AF p differ because AF quantifies over all paths; one path forever avoiding p refutes AF even when another reaches p quickly.

Testing should cover a graph with no target, a target at the initial state, cycles, disconnected components, and terminal nodes. Use an independent BFS reference for reachability; for temporal properties requiring fairness or cycles, implement the appropriate fixed-point or strongly connected component algorithm rather than approximating it with a fixed step count.

## Specification Languages
**Specification Languages: conceptual explanation**

### Specifications as mathematical interfaces
A specification language defines legal behaviors independently of one implementation. Finite-state protocols can be described by automata or temporal formulas, while preconditions and postconditions express input-output obligations. Hoare triples {P} C {Q} mean that if program C terminates from a state satisfying P, the final state satisfies Q in the standard partial-correctness reading. Total correctness adds termination. Confusing the two produces invalid safety guarantees for loops that never end.

Consider a bounded counter increment command with precondition 0≤x<MAX. A postcondition x'=x+1 ensures the resulting counter remains within its range if arithmetic is mathematical and the precondition excludes overflow. If x=MAX and the implementation uses fixed-width modular arithmetic, the postcondition may be false or require a different interpretation. This small example shows why proof obligations must reference the actual machine semantics and input representation.

Specifications can be inconsistent, overly weak or unrealistically strong. If the precondition is false, a partial-correctness Hoare triple is vacuously satisfied. If the postcondition is true, almost any terminating program satisfies it. Neither tells users much. Test whether intended valid inputs satisfy preconditions and whether the postcondition distinguishes correct from plausible incorrect implementations. Traceability should connect each informal requirement to a formal clause and a concrete falsification test.

### Refinement from informal requirements to formulas
An informal requirement such as 'every authenticated user eventually gets a response' has several interpretations. Does 'eventually' allow arbitrary delay? Does it assume the network continues to deliver packets? Does it apply when a user disconnects? A temporal formula may express a request-response liveness property, but its meaning depends on the transition system, path quantification and fairness assumptions. Formalization makes hidden policy choices explicit.

A safety requirement such as 'only administrators can change roles' can be stated as an invariant over every reachable transition that changes a role. If a role-change transition can occur while the actor is not an administrator, the checker produces a violating path. A bounded integration test may sample a few roles but miss a transition reachable only after an unusual sequence of state changes. Formal verification searches all paths in the model within its state space, yet can still miss an actual implementation flaw if the model omits an API endpoint or environmental event.

Hoare-style reasoning can help with individual actions. A precondition states that the actor is authenticated and authorized; the command mutates the role database; the postcondition constrains the new role state. Partial correctness alone does not guarantee that the command terminates or commits its transaction. For a distributed service, atomicity, failure recovery and concurrent interleavings must be modeled separately.

The lab should include a traceability matrix: source requirement, exact formal clause, model state variables, transitions that can affect it, and counterexample test. When a requirement changes, the matrix shows which formulas and tests must be updated.

## Computable Functions
**Computable Functions: conceptual explanation**

### Computable functions and safe partial results
A total computable function returns an output for every input in its domain, while a partial computable function may fail to halt on some inputs. Turing machines naturally describe both. When designing an API, a result type with `success`, `rejection`, and `unknown/timeout` captures more reality than forcing every non-success into the same Boolean. A theorem prover may find a proof of a statement after an unknown amount of search but cannot, in general, guarantee to prove or refute every statement in a sufficiently expressive setting under the relevant assumptions.

Function composition preserves computability when the component functions are appropriately effective; partiality introduces domain conditions. If f(x) is undefined, evaluating g(f(x)) need not produce a result even if g is total on all valid numerical arguments. This is not identical to an exception caught by a runtime handler: partial computability is a mathematical relation between inputs and halting outputs, while language-level exceptions may themselves terminate normally through a documented catch construct.

For a bounded semantic analyzer, report the exact search horizon or abstraction. If no counterexample was found within k loop iterations, the supported conclusion is 'no counterexample found within bound k,' unless a completeness bound has been proved. Never upgrade a bounded observation into global verification without a theorem linking the two.

### Reasoning about partial functions and timeouts
Consider a program `searchProof(x)` that enumerates candidate formal proofs and returns the first valid proof of x. If x is provable in the selected complete-enough formal deductive system, the search may eventually return. If x is not provable, the search may never terminate. As a partial computable function, its domain is the set of inputs on which it halts with a proof. Returning a timeout after a fixed budget changes the API into a total bounded procedure with an additional outcome, not into a full decider of provability.

This distinction is practical in theorem provers and analysis services. Represent results as `proved`, `counterexample`, or `unknown` when those categories make sense under the chosen logic. Unknown may indicate timeout, memory exhaustion, an abstraction too coarse to conclude, or unsupported language features; preserving the reason is better than one generic failure. A proof-producing success can be checked by an independent small kernel, which reduces trust placed in a large heuristic search engine.

Suppose a checker explores all states up to depth d. It can establish that there is no counterexample of length ≤d. To conclude there is no counterexample of any length, it needs a completeness argument, such as a finite state graph whose diameter is at most d, or a separately proved inductive invariant. Merely increasing d does not make the unbounded claim logically valid.

For a worked example, use a finite-state counter with values 0 through 5 and transitions incrementing up to 5. If all states are reachable and the search has exhausted the graph, no deeper new states exist; the finite closure can establish the invariant. Contrast it with a counter of unbounded natural-number range, where observing depth 100 says nothing about arbitrary later values.

## Complexity-Based Design
**Complexity-Based Design: conceptual explanation**

### Complexity-aware verification architecture
A practical verification service has a frontend that parses a specification, a model constructor, an exploration engine, a property evaluator, and a result reporter. Every boundary has a correctness obligation. Parser acceptance does not prove the model accurately captures a deployed system. A model checker may prove the model safe while omitting a real-world input, thread scheduler, or failure event. Conformance tests and abstraction arguments are needed to transfer conclusions back to implementation behavior.

When searching a graph, use a visited set keyed by canonical state representation. Without it, cycles can create an infinite exploration even for a finite model. If each state has bounded outgoing degree and the state count is finite, reachability can be computed in time O(|S|+|E|) using adjacency lists, excluding model-generation costs. For symbolic representations, the number of encoded states may be enormous even if a compact BDD or SAT-based method works well on structured instances. Worst-case complexity remains relevant when planning resource budgets.

A model checker should produce a reproducible counterexample path when a safety claim fails. Include the initial state, transition labels, violated predicate and configuration version. For a passing model, preserve the precise property and modeling assumptions, not merely a green status indicator. Changes to the transition relation or fairness interpretation invalidate parts of the previous result.

### Performance and correctness in model checking
Explicit BFS has time O(|S|+|E|) when the graph is materialized as adjacency lists and each state/edge is processed a constant number of times. Yet a program with thirty independent Boolean state flags has up to 2^30 possible valuations before accounting for control locations, far beyond a tiny teaching example. Symbolic model checking represents sets of states compactly using structures such as binary decision diagrams or SAT/SMT constraints, but compactness depends strongly on the structure of the transition relation and variable ordering. A good small demonstration must not be advertised as a general performance benchmark.

Partial-order reduction exploits independence between concurrent actions. If actions A and B commute and have no relevant interference, exploring both interleavings may be unnecessary for some properties. But incorrect independence assumptions can remove a real counterexample. Abstraction works similarly: map many concrete states to an abstract state, then prove a relation that preserves the property being checked. A coarse abstraction can yield false alarms; counterexample-guided refinement increases precision where needed.

Testing the checker should include a second, simple implementation of finite reachability and deliberately mutated graphs. Insert an unauthorized transition and require a counterexample path; remove it and verify the graph is exhaustively explored. Change the property, not only the graph, to ensure the evaluator does not use cached stale labels. Track number of visited states, edges, explored depth and termination reason.

The output's strongest claim is always limited by the model. A real distributed system has process crashes, delays and environmental assumptions that might not be represented. Proof reports should show the exact model version and scope next to the result.

## Integrated Case Study and Model Limitations
**Unit synthesis: Formal applications.** The following case study integrates formal definitions, correctness reasoning, limitations and realistic testing.

### Verify a small authorization workflow
Build a three-role authorization state machine with states logged-out, user, administrator, plus an account-lock flag. Transitions include log in, log out, elevate with authorization, and failed login. Specify the safety requirement: no unauthenticated transition may reach administrator state. Draw the finite transition graph and use BFS to search for a reachable violation. Inject a faulty elevate edge from logged-out directly to administrator; the model checker should return that shortest counterexample. Then remove the faulty edge and verify the property again.

Introduce the liveness claim that every legitimate user request eventually receives a response. A model in which the scheduler may ignore a request forever violates this claim even if every authorization rule is safe. Explain whether the model assumes weak fairness, retry delivery, and a bound on network failure. A formal checker will evaluate the stated model, not add missing fairness assumptions. If the model has only finitely many states, reachability and many temporal properties are decidable; this does not contradict undecidability for arbitrary programs with unbounded computation.

Compare the checker with an implementation-level integration test that exercises API calls. The test can reveal modeling errors and encoding mismatches but covers only selected traces. Formal verification covers all traces within its model but relies on model fidelity. A trustworthy final report describes both kinds of evidence, their limitations, and any state-space abstractions.

### Compose security and liveness obligations
Take a toy approval workflow with states guest, employee, admin, plus pending approvals. Guests may request access; employees may submit approvals; admins may grant roles after appropriate authentication. A safety specification forbids any path where a guest grants an admin role. A liveness specification might require that every valid pending approval is eventually resolved. The safety check can pass even when a pending request loops forever without resolution, showing that safety and liveness are distinct concerns.

Build a product model including authentication state and request state. Count theoretical combinations before reachability pruning, and document invariants that rule out impossible combinations. Add a faulty edge that permits a guest to elevate directly to admin and show the shortest error trace. Then add a scheduler that can ignore pending approvals indefinitely. An existential reachability query may still find a successful resolution, while a universal eventuality query exposes the starvation path. State fairness assumptions if the real workflow promises eventual scheduling.

For integration tests, execute a sample of the approved and forbidden API traces against a development service. Compare observed behavior with the formal model. Disagreement may mean an implementation bug, a wrong model, or an environmental effect missing from the model. The correct response is to investigate and revise evidence, not to declare the theorem disproved because a program behaved unexpectedly.

This case study unifies automata and computation limits: finite-state model checking can exhaustively verify a bounded workflow, while unrestricted program properties remain undecidable. The difference follows from the actual state model, not from how polished the simulation looks.

### Formal-methods notebook
Model a tiny authorization service as a graph. Mark states by whether the actor is authenticated and whether administrator privileges have been granted. Assert the safety property that no reachable state combines unauthenticated status with unauthorized administrator privilege. Reachability search should return a predecessor trace if it discovers a violation. Inject an edge that grants privilege without authentication to test the checker; then remove it and compare visited states. A green result means the finite model satisfies the specified invariant, not that every deployed endpoint is correctly represented.

Now write a liveness requirement: every pending request eventually receives a response. Create a cycle that keeps a request pending forever. The safety invariant may remain true while liveness fails. Distinguish the CTL statements EF responded and AF responded; one successful path suffices for the former but not the latter. Describe the treatment of deadlock states and fairness so path quantifiers have a stable meaning. Finish by mapping model transitions to real API operations and identifying omitted external events that would limit the proof's application.

### Independent self-check: scope of a verification certificate
Document a transition system, an initial state, a proposition labeling, and the temporal formula being checked. If the result is PASS, record how exhaustive search or a sound abstraction establishes the claim. If FAIL, save the shortest available counterexample path and identify the first violated transition. If UNKNOWN, preserve the timeout or abstraction limit. Then list implementation behaviors that the model omits, including network failures or race conditions. This report lets another researcher evaluate the actual evidence without relying on a reassuring colored status badge.

### Worked question: Evaluate CTL path quantifiers
A transition graph starts at s and branches to good and bad terminal states. Proposition p is true only in good. Are EF p and AF p both true at s?

**State the formal contract**
EF p asks for some path from s eventually reaching a p-state. The branch reaching good witnesses this existential eventuality.

**Derive the result**
AF p asks that every path from s eventually reaches p. The branch leading to bad and remaining there forever refutes this universal eventuality when terminals are totalized with self-loops.

**Check the scope and a counterexample**
A finite model checker must make terminal-state handling explicit. The difference is about quantification over paths, not whether the good state is reachable in a simple BFS.

**Answer:** EF p is true, while AF p is false.

### Worked question: Partial versus total correctness
A loop C never terminates when started in a state satisfying P. Is Hoare triple {P} C {Q} necessarily false?

**State the formal contract**
Under partial correctness, the triple promises that whenever execution terminates from a P-state, the resulting state satisfies Q. Here no such terminating execution exists.

**Derive the result**
The condition can be vacuously satisfied even though the loop is useless. Total correctness adds the requirement of termination from P-states and therefore would fail in this example.

**Check the scope and a counterexample**
Do not mark a process safe solely because no bad final state appears in a test trace; nontermination may be a separate liveness failure.

**Answer:** It can be true under partial correctness; total correctness fails.

### Worked question: Product-state explosion
Three independent components have respectively 3, 4, and 5 states. What is the maximum Cartesian-product state count, and does this equal the number of reachable states?

**State the formal contract**
A global state chooses one local state for each component, so the full Cartesian product contains 3×4×5=60 possible tuples.

**Derive the result**
Reachability may be a strict subset because transition rules or invariants forbid some combinations. Run BFS from the designated initial tuple to determine the actually reachable subset.

**Check the scope and a counterexample**
Changing a component’s state count can change the product dramatically, but the raw product is an upper bound, not an estimate of model-checking runtime for symbolic representations.

**Answer:** There are at most 60 product states; reachability must be checked separately.
