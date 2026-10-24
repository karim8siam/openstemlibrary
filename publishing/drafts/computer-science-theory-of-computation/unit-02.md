# Unit 2: Finite automata

*Editorial draft; not approved for live publication.*

## Deterministic Machines
**Deterministic Machines: conceptual explanation**

### DFA definitions and traces
A deterministic finite automaton is a five-tuple (Q,Σ,δ,q0,F), where Q and Σ are finite, δ:Q×Σ→Q is a total transition function, q0∈Q, and F⊆Q. Its extended transition δ*(q,w) is defined recursively by δ*(q,ε)=q and δ*(q,wa)=δ(δ*(q,w),a). The membership decision is simply whether δ*(q0,w)∈F after the last symbol. The state is a summary of the already-read prefix. A DFA does not have an unbounded integer register merely because its states can be labeled by numbers.

Construct a DFA for binary strings interpreted as nonnegative integers divisible by three. Use remainder states 0,1,2, start in remainder 0, and transition on a bit b by r'=(2r+b) mod 3. Read 110 in that order: start 0; after 1 the remainder is 1; after 1 it is 0; after 0 it remains 0, so accept because binary 110 equals six. The leading-zero policy matters: any number of leading zeros leaves the remainder unchanged, while ε is accepted if zero is considered a valid empty encoding. If valid numerals must be nonempty, add an initial state so ε is rejected without changing residue arithmetic.

Verify determinism by ensuring exactly one successor for every (state,symbol) pair. Test transition coverage, unreachable states, and the full trace, not just the final answer. A transition table and a directed graph represent the same object; graph diagrams become misleading if edges or sink states are omitted. The model's correctness follows from induction on input length using the invariant that state r equals the numeric value of the processed prefix modulo three.

### Remainder machines and number encodings
The remainder-state DFA generalizes to divisibility by any fixed positive integer m. For base b digits, update r←(br+d) mod m, with states 0 through m−1. Prove the invariant by induction: if the prefix has numeric value V with remainder r, appending digit d produces new numeric value bV+d and remainder (br+d) mod m. This yields a uniform way to construct regular languages of base-b encodings divisible by m. It does not require the automaton to store the entire integer, only a fixed remainder.

But the representation contract matters. If the empty string is not considered a numeral, an extra start state can reject ε while ordinary leading-zero inputs still work. If negative numbers are allowed, the alphabet and sign-handling state must be extended. If the input may contain a digit outside 0 through b−1, the machine should transition to a rejecting sink. A transition graph missing such an edge is a partial automaton, not a complete DFA under the standard definition.

For a correctness experiment, enumerate all binary words of length up to ten, compute their values using a separate arithmetic routine, and compare DFA acceptance with divisibility. Include binary strings with leading zeros and record the accepted policy. Then prove the invariant symbol by symbol. Although finite enumeration can expose a faulty transition, the proof establishes correctness for every input length. For an optimization exercise, ask whether all m remainder states are distinguishable for the chosen language. Reachability and distinguishability require checking; an arbitrary fixed-state construction need not be minimal.

Also distinguish a DFA's transition cost from integer conversion cost. A DFA scans n digits in O(n) time with constant state for fixed m, whereas first converting an unbounded binary input to a machine integer may overflow. A direct modular scan avoids that representation problem.

## Nondeterministic Machines
**Nondeterministic Machines: conceptual explanation**

### NFA branching and subset construction
A nondeterministic finite automaton has a transition relation that may offer several next states, none, or ε-transitions. A word is accepted if at least one complete path ends in an accepting state. This is existential branching, not a probabilistic choice, and an NFA cannot become more powerful simply by guessing. During simulation, maintain a set of possible states. For ε-NFAs, first take the ε-closure, then take the transition of every state on the next symbol, and finally close under ε again.

Consider an NFA that recognizes strings containing substring 01. It can remain in a start-loop state while scanning arbitrary symbols, nondeterministically begin a match when it sees 0, then reach acceptance after a subsequent 1. The subset construction turns each reachable set of NFA states into one DFA state. If the NFA has n states, there are at most 2^n subsets, but often far fewer are reachable. The empty set can be a rejecting sink when no moves remain. For an accepting subset, it suffices that at least one member belongs to the NFA's final set.

A proof of equivalence uses an invariant: after reading any prefix, the DFA's subset exactly equals the states the NFA could occupy after that prefix, including ε moves. The proof proceeds by induction on the prefix length. A common error is treating the NFA's branching as if all branches must accept. Another is discarding a path because it becomes stuck, even though another path remains alive. Implement the subset construction with canonical set keys such as sorted state identifiers and compare languages by exhaustively enumerating short strings; the mathematical proof must still cover all strings.

### Subset construction as a reachable-state search
The theoretical upper bound of 2^n DFA subset states is not a prediction that all those states will appear. Start from the ε-closure of the NFA start state, then for every discovered subset S and alphabet symbol a calculate the ε-closure of all NFA successors on a. Insert a new subset in a work queue only if it has not been seen. This is BFS or DFS over reachable subsets, and it automatically omits the unreachable portion of the powerset. Use sorted tuples or bitset representations to ensure mathematically equal subsets receive identical keys.

When implementing this procedure, consider an NFA with three states, but only transitions that keep state q0 alive and occasionally activate q1. The subset {q2} might exist as a mathematical subset yet never be reached from the start. A DFA built only from reachable subsets can be dramatically smaller than the worst-case 2^n table. On the other hand, there are families of NFAs whose subset construction requires exponentially many reachable, pairwise distinguishable subsets, so the exponential bound is not merely a loose artifact.

The correctness proof tracks two simulations in lockstep. At initialization the DFA subset equals the NFA's ε-closure. Suppose equality holds after prefix w; for next input a, the subset transition computes exactly all NFA states reachable by one a-move and any ε-moves. Thus equality holds after wa. Acceptance is preserved because NFA acceptance means some possible current state is final. This proof also clarifies how to handle a dead subset: when the set becomes empty it stays empty on all later symbols.

A robust tool should show both the current subset and the chosen transition, rather than animating one arbitrary NFA path. Showing only one path misrepresents existential nondeterminism and can confuse learners when an input is accepted via an alternative branch.

## Regular Expressions
**Regular Expressions: conceptual explanation**

### Regular expressions and equivalence
Regular expressions denote sets of strings. The base expressions for ∅, ε and individual symbols generate the regular languages under union, concatenation and star. Syntax such as backreferences and lookaround in real regex libraries is not necessarily part of the formal regular-expression calculus; backreferences can change expressive power. Decide which definition is in use before applying automata theorems. For the regex (0|1)*01, the language consists of binary words ending in 01. The matched prefix can be empty, so the word 01 is accepted. The word 010 is not accepted even though it contains 01 as a substring.

Thompson's construction builds an ε-NFA from an expression in a compositional way. For concatenation, connect the accept state of the first fragment to the start of the second through ε. For alternation, create a new entry and exit joined to both fragments. For star, permit both zero repetitions and looping repetitions. The correctness argument mirrors the syntax-tree induction. It is better to implement construction from an AST than to manipulate raw textual regex characters because operator precedence and parentheses must be resolved first.

Regular expression equivalence is decidable by translating both to DFAs, taking their symmetric difference, and checking whether an accepting state is reachable. If no accepting product state is reachable, no string distinguishes the languages. If one is reachable, breadth-first search reconstructs a shortest counterexample. A test suite of twenty matching strings cannot establish equivalence, but a correctly implemented finite product-state reachability algorithm can. State blowups can make the procedure costly even though it terminates.

### Regular expressions are algebra, not just library syntax
To prove equivalence of two expressions R and S, translate them into finite automata and build a machine accepting the symmetric difference L(R)△L(S). This product state keeps a pair of DFA states (p,q), updates both on the same symbol, and accepts if exactly one component accepts. If an accepting product state is reachable, BFS reconstructs a distinguishing word; if none is reachable, the symmetric-difference language is empty and the two expressions are equivalent. Because the product graph is finite, emptiness is decidable.

Compare `(ab|a)b` and `a(bb|b)`. Distribution of concatenation over union shows both generate {abb,ab}; algebra gives equivalence immediately. Now compare `a(b|bb)*` and `(ab|abb)*`. The first requires one initial a followed by blocks of one or two b; the second may contain multiple a symbols, and also ε. Word ε is an immediate distinguishing witness. A few common positive examples might have concealed the difference, so counterexample search is more informative than only sampling valid strings.

Real-world regex engines have greedy matching, capture groups, anchors, and sometimes backreferences. Greediness is usually an operational rule for choosing among matches, not a change in the recognized language. Backreferences, however, can encode equality constraints not expressible by classical finite automata in the same way. Before invoking pumping or DFA equivalence theorems, identify which features the engine actually supports. Also discuss catastrophic backtracking: two regexes may recognize the same regular language but have drastically different behavior under a backtracking implementation. Recognition power and evaluation strategy must be analyzed separately.

The educational product should implement formal regex operators explicitly rather than embedding arbitrary user regex text into the browser's engine and pretending the results form a proof.

## Minimization
**Minimization: conceptual explanation**

### DFA minimization by distinguishing futures
Two DFA states are equivalent if every possible suffix leads both either to acceptance or to rejection. Begin partition refinement by separating final from nonfinal states. Repeatedly split a block when a symbol sends members into different existing blocks. Stop when the partition is stable. Each final block becomes one state of the minimized DFA; first remove unreachable states so they do not inflate the result. This algorithm implements the same future-distinguishability relation captured by the Myhill–Nerode theorem.

Take a DFA with states A,B,C,D, final states C and D, and suppose C and D have identical transitions to equivalence blocks while A and B differ on symbol 1. Finality initially places C and D together, but not A or B. A split of A and B is justified only by a concrete distinguishing suffix; if one transition reaches the accepting block and the other reaches a rejecting block, that symbol alone distinguishes them. If their immediate destinations appear equivalent, repeat refinement or search for a longer suffix.

The minimized automaton is unique up to renaming of states, for a fixed regular language and complete deterministic convention. This uniqueness does not mean all regular expressions have the same syntax or that an NFA minimizes by merging visually similar nodes. To verify a minimizer, compare original and reduced machines by product equivalence, and separately verify that every pair of distinct minimized states has a distinguishing suffix. Include test DFAs with unreachable states, missing transitions represented through an explicit sink, and no accepting states.

### Partition refinement and test witnesses
Begin DFA minimization with a partition of Q into accepting and rejecting states. For each partition block B and symbol a, split B according to the destination block of δ(q,a). Repeat until every block is stable under all input symbols. This stability condition means equivalent current states transition to equivalent next states. The quotient automaton then has one state per block, and its transition function is well-defined because members of a block agree on destination blocks.

Explain why two immediately matching transitions are not sufficient for equivalence unless their targets are already known equivalent. Equivalence is a greatest fixed-point condition over all future continuations. A partition refinement algorithm discovers it by repeatedly removing false candidate equivalences. In an implementation, record why a split occurred: symbol a and destination blocks that differ. Following those records backward can reconstruct a distinguishing suffix for students.

For testing, generate random total DFAs with a fixed small number of states and alphabet, minimize them, then compare accepted strings through a length bound. More strongly, build a product equivalence checker to verify exact equivalence of the two finite-state machines. To verify minimality, test pairwise distinguishability between every pair of reachable states in the quotient. An error that merges two distinguishable states might still pass a short bounded string suite; a product BFS should find the shortest missed witness.

State explosion affects the comparison algorithm too. The product graph has at most |Q_A||Q_B| states, but reachable pairs may be fewer. The verifier should report actual explored-state counts so learners see how a mathematical worst-case bound relates to one concrete machine.

## Integrated Case Study and Model Limitations
**Unit synthesis: Finite automata.** The following case study integrates formal definitions, correctness reasoning, limitations and realistic testing.

### Design and audit a lexical recognizer
Build a recognizer for identifiers over letters and digits where the first symbol must be a letter. A two-state partial DFA suffices for positive strings if an absent transition means rejection; a complete DFA adds a sink for a digit in the first position. Add a reserved-word policy: `while` is lexically an identifier-shaped string but may be classified as a keyword after scanning. That policy is not expressible by only the identifier DFA if the application uses a separate keyword table. Keep lexical recognition separate from downstream grammar membership.

Now include comments delimited by `/*` and `*/`. If comments cannot nest, a finite automaton can track whether the scanner is inside a comment and whether the most recent character is `*`. If comments can nest to unbounded depth, one finite-state scanner cannot remember depth; a counter or stack is needed. This provides a useful boundary between regular and nonregular parsing tasks. Real source languages may impose resource limits, but a resource-limited implementation is not proof that the intended unbounded language is regular.

Write a conformance matrix: valid identifiers, initial digits, empty strings, Unicode policy, delimiters, unterminated comments, and comments adjacent to operators. Derive expected acceptance by the language definition first, then run the machine. If two independently written recognizers disagree, minimize the counterexample and inspect which transition violates the specification. The finite-state argument permits complete equivalence checking of the recognizers even when random tests have stopped finding failures.

### Tokenizer audits and adversarial inputs
Implement the identifier and comment recognizer using a total transition table rather than a collection of ad hoc substring checks. In a maximal-munch scanner, the current best accepting position must be remembered: after consuming a prefix that could extend into a longer token, an eventual failure requires returning to the last accepted boundary. For instance, with operators `=`, `==`, and `===`, consuming the first `=` is valid but not necessarily final. The scanner must choose the longest operator that matches the declared policy.

Comments interact with strings. If the source includes `"/* not a comment */"`, an ordinary quoted-string state should keep the delimiters as string data; treating them as comment markers corrupts tokenization. Escape sequences complicate string termination: a quote preceded by a valid escape may not end the literal. This is still typically finite-state when escape rules are local and bounded, but it requires the correct states. Nested comments with arbitrary depth change the memory requirement.

Test cases should include end-of-input immediately after `/*`, multiple asterisks before the closing slash, a quote adjacent to a comment, and a Unicode character at a token boundary. Record whether token spans use byte offsets, code point indices, or UTF-16 code units. This affects editor diagnostics and can turn an apparently correct regex into a wrong source location. Formal models make such contracts explicit and reduce disagreement between tools.

A simple benchmark comparing regex scanning with table-driven scanning is not a correctness proof. First demonstrate language equivalence or a precise refinement relation; then measure throughput using representative inputs, cache effects, and long adversarial strings. Proper engineering uses theory to define behavior and measurements to compare implementations.

### State-machine proof notebook
Given a finite automaton, document start state, final states and a transition for every state-symbol pair. Trace an input by writing a sequence of pairs (position,state). A verifier can reconstruct the same trace by iteration and compare its final state with the acceptance predicate. To show that the machine recognizes binary numbers divisible by m, prove the modular invariant. To show it is minimal, a different argument is necessary: every pair of inequivalent residual future behaviors must be distinguished. These are two independent proof obligations, not one broad claim of correctness.

For an NFA, represent the current configuration as a set of states. Try input 001 with a language requiring the substring 01. One branch may abandon a tentative match on the second 0, while another begins a new tentative match; the set-based simulation preserves both. Convert to a reachable-subset DFA and verify exact equivalence by a product automaton. Report both reachable subset count and the theoretical 2^n upper bound. A small reachable count does not invalidate the exponential upper bound. These exercises demonstrate that proofs need invariants, while code needs independent boundary tests.

### Independent self-check: completeness of transition tables
Pick a machine with three states and a binary alphabet. List all six state-symbol pairs and verify that the declared DFA specifies one destination for each; absent entries either make the machine incomplete or imply a documented sink policy. Then verify a small NFA with multiple outgoing transitions and demonstrate why an acceptance trace requires only one successful path. Finally, construct a product of two complete DFAs and explain why an accepting pair in their symmetric difference supplies a language-equivalence counterexample. These are three different uses of finite-state machines: recognition, nondeterminism elimination, and exact comparison.

### Worked question: Trace a remainder DFA
A DFA reads binary digits from left to right and tracks the represented number modulo three. Trace input 1011 and determine acceptance for divisibility by three.

**State the formal contract**
Initialize remainder r=0. For a new bit b apply r←(2r+b) mod 3. The input 1011 is binary eleven, but compute from the transition invariant instead of trusting conversion.

**Derive the result**
The trace is: after 1, r=1; after 0, r=2; after 1, r=(4+1) mod 3=2; after final 1, r=(4+1) mod 3=2. The accepting remainder state is zero.

**Check the scope and a counterexample**
Check independently: eleven divided by three leaves remainder two. The machine rejects. Empty-input handling must be specified separately if the language requires a nonempty numeral.

**Answer:** Final remainder two; the DFA rejects 1011.

### Worked question: NFA subset acceptance
An NFA has states {q0,q1,q2}, start q0, accepting set {q2}, and on input 0 from q0 it may remain at q0 or move to q1; on input 1 from q1 it goes to q2. Given the additional self-loop on q2 for both symbols and q0 on 1, determine acceptance of 001.

**State the formal contract**
Begin with active-state set {q0}. On the first 0, possible destinations are {q0,q1}. On the second 0, q0 again yields {q0,q1}; q1 has no 0 transition.

**Derive the result**
On final 1, q0 can stay q0 and q1 can reach q2, so the active set becomes {q0,q2}. Since q2 is accepting, the NFA accepts on at least one possible run.

**Check the scope and a counterexample**
Rejecting or stuck alternatives do not defeat an accepting path. The corresponding subset DFA accepts exactly when its active set intersects the NFA final-state set.

**Answer:** 001 is accepted; the final active set contains q2.

### Worked question: State minimization witness
Two DFA states p and q are nonfinal. On input 0, δ(p,0) is final and δ(q,0) is nonfinal. Can p and q be merged?

**State the formal contract**
State equivalence requires that every continuation suffix produces the same acceptance outcome from both states. Choose the one-symbol suffix 0.

**Derive the result**
From p the suffix 0 reaches a final state, so it is accepted. From q the same suffix reaches a nonfinal state after input exhaustion, so it is rejected.

**Check the scope and a counterexample**
A single distinguishing suffix proves inequivalence; it is unnecessary to enumerate every longer suffix. Having identical current finality does not itself establish equivalent future behavior.

**Answer:** No. Suffix 0 distinguishes p and q.
