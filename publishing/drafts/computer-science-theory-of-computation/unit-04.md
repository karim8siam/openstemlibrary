# Unit 4: Computability

*Editorial draft; not approved for live publication.*

## Turing Machines
**Turing Machines: conceptual explanation**

### Turing-machine configurations and transitions
A Turing machine has a finite set of control states, a tape alphabet containing a blank symbol, a transition function, a head position, and an initial tape encoding. A deterministic single-tape machine's configuration specifies its current control state, full nonblank tape contents together with the finite region relevant to the head, and the head position. A step writes a tape symbol, moves the head left or right (or stays when allowed by the convention), and changes state. Acceptance and rejection are distinguished halting outcomes. A machine may also run forever without reaching either outcome.

For a concrete unary incrementer, input 111 represents three. Scan right over every 1 until encountering blank, write one additional 1, and halt with 1111. A trace includes state, head index, tape slice and rule applied at each step. Head direction must be consistent; treating the origin as fixed across an expanding left tape requires care. A machine that accepts a word need not preserve that word as output, so keep the notions of recognizer and transducer separate.

Termination of a bounded test is easy to observe; termination of an arbitrary Turing-machine program is not a general decidable property. Use a per-example step budget in the simulator to prevent locking the interface. Report `limit reached` rather than incorrectly classifying the machine as rejecting when it has not halted. A correctness proof for a deliberately simple machine can use an invariant of the scan: every symbol to the left of the head has already been verified as a 1.

### Encode a unary machine without ambiguity
A unary incrementer can be written with transition table `scan,1 -> scan,1,R` and `scan,blank -> halt,1,S` under a convention permitting a stay move S. The tape initially contains 1^n starting at the head. Inductively, after k scan transitions with 0≤k≤n, the head is at position k, the first n tape cells still contain 1, and no new symbol has yet been written. At k=n the head sees blank, so the next transition writes one additional 1 and halts. This proves the output is 1^(n+1) for every n, assuming blank cells extend to the right.

The number of transitions is n+1 with that counting convention. But input length zero is a real edge case: the head begins at blank, writes 1 and halts after one transition. If unary zero is represented by ε, incrementing zero gives unary one; if zero is represented differently, the machine specification must be revised. A teaching tool should show the head moving while preserving an explicit indexing origin, because merely printing a trimmed tape string can make leftward motion ambiguous.

A Turing machine can rewrite or erase cells, move left past the initial written region if the tape convention permits it, and change control state. A finite trace viewer using a JavaScript array must synthesize blank cells when the head moves beyond stored positions; otherwise it silently imposes a fixed-space bound. A bounded viewer may still be useful if it reports the configured window and stops with an appropriate resource outcome.

A general Turing-machine simulator is an interpreter for finite transition tables, not a halting oracle. Adding a loop-detection heuristic for repeated finite snapshots can detect some loops, but it cannot solve the full halting problem when unbounded tape growth or complex behavior is possible.

## Equivalent Models
**Equivalent Models: conceptual explanation**

### Equivalence of computational models
Multi-tape Turing machines, standard single-tape Turing machines, register machines with suitable instruction sets, and common idealized programming languages recognize the same class of Turing-recognizable languages. Simulation of one model by another is the basis for this equivalence. A single-tape machine can encode multiple simulated tapes using delimiters and tracks, scanning the representation to update virtual head locations. The simulation may incur overhead but does not require a new kind of mathematical decision procedure.

The Church–Turing thesis concerns effectively computable functions and the reach of these formal models. It is a thesis connecting an informal notion to a mathematical notion, not a theorem proved from the definition of all imaginable physical computers. Complexity-sensitive versions require their own assumptions: a polynomial-time simulation result does not follow merely from computability equivalence. Nondeterministic machines can be simulated by systematic exploration of branching computation histories for recognizability, but the runtime can expand dramatically.

When proving equivalence, describe an encoding and both directions of simulation. For example, a two-tape machine can be represented on one tape by separate marked tracks indicating each simulated head position. Each simulated step searches the representation for both head markers, reads their associated symbols, then updates them. Address tape expansion and delimiters rather than saying only that one machine is 'universal.' A simulator that stores the entire work tape in a programming-language array still assumes unbounded memory in the mathematical model; finite physical hardware implements only a bounded approximation.

### Simulate two tapes on one tape
Suppose the abstract machine has two tapes, each with its own head. Use one physical tape to store two encoded tracks separated by delimiters, with special symbols marking simulated head positions. To simulate one logical transition, the physical head scans the encoded tracks to find each marked symbol and records the two scanned symbols in finite control. It then scans again to rewrite the symbols and move or create head markers, expanding the representation if needed. The result can emulate any step of the two-tape machine using finitely many physical steps.

The slowdown is relevant for complexity but not for computability. The representation length grows with the simulated work space; scanning it per logical step introduces overhead, often described by a polynomial bound for standard variants. It is misleading to say that the machines perform exactly the same number of operations. Equivalence of computable functions means eventual outputs agree for all inputs where the function is defined, not that hardware characteristics, constant factors or space locality are identical.

An analogous simulation translates a finite-register abstract machine into a Turing-machine encoding. Registers need not be bounded if they can hold arbitrary natural numbers in the ideal model, but the values must be encoded using finite strings on each finite computation prefix. Conversely, a sufficiently expressive register-machine program can maintain a data structure encoding tape cells and a head index. The existence of such translations supports the computational equivalence claim.

For a classroom proof, formalize the encoding function E(C) from logical multi-tape configurations C to physical single-tape configurations. Show that for every permitted logical step C→C', the simulator starting at E(C) eventually reaches E(C'). Add a base case for the initial configuration. That simulation invariant proves correctness over any finite run.

## Decidability
**Decidability: conceptual explanation**

### Deciders and recognizers
A decider halts on every input and correctly accepts or rejects membership in its language. A recognizer accepts members after finitely many steps but may loop forever on nonmembers. Every decidable language is recognizable. There are recognizable languages that are not decidable, including the language of encoded machine-input pairs whose simulated computation eventually accepts under a suitable universal encoding.

A language is decidable exactly when it and its complement are both Turing-recognizable. In the nontrivial direction, suppose recognizers R and S accept L and its complement respectively. On input w, dovetail the two simulations: execute one step of R, one step of S, then repeat. Because w belongs to exactly one of the two languages, one recognizer must eventually accept; halt and return the appropriate answer. Running R to completion before starting S would be invalid, because the first recognizer might never terminate. This dovetailing proof is an instructive example of a construction that converts partial evidence into a total decision procedure.

Decidability claims require precise input encoding and problem definition. Regular-language membership is decidable by simulating a DFA across the finite input. DFA language equivalence is decidable by product-state reachability. Whether an arbitrary program halts on an arbitrary input is not decidable. A finite test budget or a large precomputed table does not decide the unbounded version. Write the quantifiers first: the algorithm must succeed for every valid encoded input, not merely for inputs encountered during a benchmark.

### Totality through parallel semidecision
Why does recognizing both L and its complement imply deciding L? Because there is no third truth value: a particular input belongs to one of the two sets. Let A recognize L and B recognize its complement. Build D that advances both machines in rounds. On each round, inspect whether either has accepted; if A accepts, return yes, and if B accepts, return no. Exactly one of these events must happen eventually because the relevant recognizer is guaranteed to accept its members.

Be careful about implementations that allocate a fixed timeout to both recognizers. If a recognizer takes more than the chosen timeout, the combined system returns unknown, which is a useful engineering result but not a total decider in the mathematical sense. The theoretical dovetailing machine has an unbounded number of rounds and, for every fixed input, halts after finitely many rounds whose count may not have a computable uniform bound known in advance.

The theorem also suggests how to reason about proof systems. A recognizable language has enumerable positive witnesses in the broad sense that acceptance is observable after finite time. If both positive and negative memberships have recognizable evidence, one can search for both kinds of evidence in parallel until one appears. The subtlety is that a failed search is not itself a witness; only an eventual positive acceptance terminates the algorithm.

Try a concrete pair of recognizers: one accepts binary strings containing `00`; the other accepts strings that do not contain `00`. Because these particular languages are regular, both procedures can halt immediately. The dovetailing construction is unnecessarily expensive but still correct. Its value is logical: the same structure works even when the original recognizers need not halt on nonmembers.

## Recognizable Languages
**Recognizable Languages: conceptual explanation**

### Enumerators and semidecision procedures
A language is Turing-recognizable if there is a machine that eventually lists all its members, possibly with repetition and no guarantee of when a particular member appears. To derive an enumerator from a recognizer, enumerate all possible strings, then dovetail recognizer executions for increasingly many steps. After stage t, run the first t candidate strings for at most t steps each; output any candidates that have accepted and have not already been reported, if deduplication is desired. This schedule ensures every member is eventually discovered even when earlier nonmembers run forever.

Conversely, given an enumerator for L, a recognizer for candidate w runs the enumerator and accepts if w appears. If w is not in L, the recognizer may run forever. The word 'eventually' has no finite bound independent of w. An enumerator can emit a large early prefix and then pause for an enormous period without violating the definition. This model is useful when thinking about theorem search: proof-checkable theorems can be systematically enumerated from finite proof strings, assuming an effectively checkable proof system, while not all semantic validity questions become decidable.

Be careful with a common false conclusion: from 'we have not seen w in the enumeration yet' it does not follow that w is outside L. Negative evidence needs either a finite search bound proved sufficient or an independent recognizer for the complement. In programming practice, distinguish a timeout, an explicit rejection, and a runtime error. They are three different observations about the procedure, not three logical membership values.

### Enumerating words and machines fairly
To enumerate all finite binary strings, start with ε, then 0 and 1, then 00,01,10,11, then the eight length-three words, and continue by length. Every finite word appears after finitely many previous words. To enumerate accepted words of a recognizable language, however, running the recognizer on ε to completion before moving to 0 may block forever. Fair dovetailing is necessary: at stage t allocate one additional simulated step to each of the first t words, preserving their computational histories.

If a machine accepts input w after k simulated steps and w occurs among the first i enumerated strings, then by stage t≥max(i,k) the dovetailing process will have advanced the corresponding simulation far enough to discover acceptance. This is the constructive proof that every recognized member will eventually be output. The enumerator may print a word more than once; if uniqueness is required, maintain a growing set of emitted words, which is finite at each stage but unbounded overall in the ideal model.

For a teaching implementation, cap the number of candidates and simulated steps, and label the output as a bounded prefix of an ideal enumeration. Use reproducible small recognizers whose membership is independently known; verify that every accepted candidate within the stated bounds eventually appears. Include a recognizer that loops on some nonmember to demonstrate why sequential enumeration fails.

This method is related to fair scheduling in concurrency: tasks that cannot be predicted to terminate must be interleaved if progress of other tasks matters. But the analogy has a limit—actual operating systems use finite time slices and resource budgets, whereas the theorem assumes ideal unbounded time and storage.

## Integrated Case Study and Model Limitations
**Unit synthesis: Computability.** The following case study integrates formal definitions, correctness reasoning, limitations and realistic testing.

### Build a bounded tape-machine laboratory
Implement a tiny deterministic machine that scans unary input until blank, appends 1 and halts. Represent the transition rules in a table keyed by `(state,read-symbol)`; reject duplicate keys because the simulator promises determinism. Record every trace row as step number, state before, scanned symbol, action, and resulting tape. A test with input 111 should produce 1111; empty unary input may produce one symbol, depending on whether empty input represents zero. State that representation explicitly.

Inject a deliberate infinite loop: a state reading blank moves right and stays in the same state forever. The simulator must stop after the user-selected budget, report incomplete observation, and never label the input rejected. Also include a rejecting machine that halts, so learners see the difference between rejection and nontermination. Test left-tape expansion, blank writes, and malformed rules. For simple machines write loop invariants that prove behavior for arbitrary unary input size rather than relying on finitely many traces.

The lab's larger lesson is the separation of specification, implementation, and theorem. A simulator with a step limit is an excellent teaching tool, but its output depends on hardware and the selected budget. The equivalence of machine models and the existence of undecidable problems are mathematical conclusions not established by animation. When documenting the model, tell readers which mathematical operations it approximates and which unbounded claims it cannot demonstrate.

### Fair recognition under unbounded search
The difference between recognizing and deciding a language appears clearly in theorem enumeration. Suppose formal proofs are finite strings and a proof checker can decide whether a string is a valid proof of formula φ. To recognize theoremhood of φ, enumerate candidate proof strings in increasing length and run the checker. If φ has a proof, one finite string eventually appears and the recognizer accepts. If φ has no proof, the enumeration continues indefinitely without accepting, assuming the candidate space has no proven finite completeness bound. This is recognition, not decision.

A similar construction recognizes instances where some finite witness can be checked mechanically. But complexity claims need more than the existence of a finite witness; polynomial size and polynomial verification are required for NP. In general computability, a witness may be enormous and there may be no computable upper bound on when a successful witness will be found.

Dovetailing is necessary if some candidate checks themselves do not terminate. Rather than finish the first attempt before starting the second, allocate progressively more steps to each candidate in a fair schedule. If one candidate would accept in k steps, then after sufficiently many stages it receives those k steps and acceptance is discovered. A finite simulator must report that enumeration is still pending when its budget expires.

To verify the concept, implement two toy recognizers: one accepts binary words containing 101, and another accepts binary words where the number of 1 symbols is even. These are actually decidable regular languages, so the pedagogic recognizers can halt immediately. Then deliberately replace one nonmember branch by an infinite loop; the fair combined enumerator should still make progress on other candidates. The distinction between an ideal proof and a bounded browser animation should remain visible.

### Machine-model notebook
Represent a Turing-machine step as a transformation of a full configuration: control state, tape contents and head position. In a small interpreter, maintain default blank symbols for unallocated tape positions, rather than assuming tape index zero is a hard boundary. Trace unary increment for inputs ε,1,11,111; assert output lengths of one, two, three and four respectively. Induct over the number of input ones to justify all lengths. Explicitly record whether the halting transition counts as one step.

Then insert a nonhalting rule whose state and head both move indefinitely over blanks. After any finite budget, display 'not halted within budget', not 'reject'. Add a separate rejecting halt rule so learners can compare three outcomes: accepting halt, rejecting halt and incomplete bounded observation. Explain how fair dovetailing allows an enumeration of recognized words to progress even when some candidate simulations do not terminate. The same conceptual distinction underlies trustworthy theorem search and program analysis.

### Independent self-check: partial evidence
For each result of a bounded Turing-machine simulator, choose one of accepting halt, rejecting halt, or limit reached. Invent a terminating computation longer than the configured limit and explain why it receives the third outcome even though its mathematical final status is known to you. Design a test that verifies the simulator records configurations in chronological order and never invents a halting transition. Then explain why even a perfectly tested bounded simulator cannot certify nontermination for arbitrary programs. The missing ingredient is not stronger hardware but a decision procedure ruled out by the halting theorem.

### Worked question: Unary-machine trace
A single-tape deterministic machine scans right across all 1 symbols, writes one 1 at the first blank, and halts. What output does input 111 produce?

**State the formal contract**
At the start, the head is on the first 1. The transition for reading 1 preserves it and moves right, so after three scan steps the head reaches the first blank.

**Derive the result**
The blank transition writes 1 and enters a halting state. The nonblank tape portion changes from 111 to 1111, representing unary four when the input represented unary three.

**Check the scope and a counterexample**
A trace tool must specify whether it counts the final write-halt transition as one additional step. Head-movement and off-by-one assumptions can otherwise make two correct explanations appear inconsistent.

**Answer:** The output tape contains 1111.

### Worked question: Dovetailing recognizers
Suppose R recognizes L and S recognizes its complement. Construct a decider for L without allowing R to run forever before S starts.

**State the formal contract**
On input w initialize saved configurations of R(w) and S(w). At stage t execute one transition of R then one transition of S, preserving their states between stages.

**Derive the result**
If R accepts, answer yes; if S accepts, answer no. Because w lies in exactly one of L and its complement, at least one relevant recognizer eventually accepts, so the combined machine halts.

**Check the scope and a counterexample**
An implementation that completes R before starting S may never reach the complement recognizer. The interleaving is the key termination argument. Neither recognizer needs to halt on inputs it does not accept.

**Answer:** Alternating the recognizers produces a total decider for L.

### Worked question: Timeout is not rejection
A general Turing-machine simulator runs M(w) for at most 1000 steps and does not observe a halt. What may it conclude?

**State the formal contract**
It has observed a finite prefix of the computation, namely that no halting transition occurred within the chosen budget. That is a correct bounded observation.

**Derive the result**
It cannot infer that M(w) never halts: construct a machine that counts through 1001 transitions and halts on the next transition. The bounded observation is identical until the cutoff.

**Check the scope and a counterexample**
A good result type reports inconclusive or budget-exceeded. A real halting state that explicitly rejects is a different semantic event and can be reported as rejection immediately.

**Answer:** Only that the machine has not halted within the first 1000 steps.
