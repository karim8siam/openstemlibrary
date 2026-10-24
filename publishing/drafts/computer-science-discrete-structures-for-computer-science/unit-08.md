# Unit 8: Formal structures


## Languages

**Core model — Languages**

A formal language is a subset of all finite strings over an alphabet. Membership and generation are distinct but related viewpoints.

**Original worked illustration**

Over alphabet {0,1}, the language of strings with even number of 1 symbols includes the empty string, 00, 11, 101 and excludes 1.

**Boundary conditions and checks**

A natural-language description such as 'balanced' needs a precise grammar or decision procedure to avoid ambiguity.

### Languages are sets of finite strings
An alphabet Σ is a finite set of symbols. The set Σ* contains all finite strings formed from Σ, including the empty string ε. A formal language L is a subset of Σ*. The language of binary strings ending in 01 is {w01 : w∈{0,1}*}. It includes 01, 001 and 10101 but not ε, 10 or 010. A language definition must distinguish strings from numerical values: the string '001' contains leading zeros and is different from '1' even if both denote the same integer under binary interpretation.

### Operations on languages
For languages A and B, their union contains strings belonging to either, and their concatenation AB contains every string xy where x∈A and y∈B. Kleene star A* contains concatenations of zero or more strings from A, always including ε. For A={a,b}, A* is the set of all strings over that two-symbol alphabet. For A={ab}, A* contains ε, ab, abab, ... but not a or abb. These operations underpin regular expressions and abstract language recognition.

### Regular expressions as mathematical models
A mathematical regular expression denotes a regular language by union, concatenation and star. Practical regex engines may add backreferences, lookarounds and other features that exceed classical regular-language power or change performance properties. When a theoretical result says every regular expression can be recognized by a finite automaton, confirm that the syntax being discussed is the mathematical one. Matching against external Unicode text also raises normalization and encoding questions absent from the simple finite-alphabet model.

### Pumping lemma: what it can and cannot show
The regular-language pumping lemma states that a sufficiently long string in a regular language can be decomposed xyz with |xy| bounded, |y|>0, and xy^iz in the language for every i≥0. To prove L={0^n1^n:n≥0} is not regular, assume it is and choose 0^p1^p for pumping length p. Every permitted y within the first p characters consists only of zeros. Pumping y twice produces more zeros than ones, contradicting language membership. The lemma gives a necessary property of regular languages; satisfying a few pumping tests does not prove that a language is regular.

### Security-relevant parsing distinctions
A string that matches a permissive prefix regex is not necessarily a valid full input. Use anchored whole-string recognition when the specification requires it, and define whether whitespace, separators and escape sequences are accepted. Lexical validity does not by itself guarantee semantic safety: a syntactically valid numeric value might be out of range, and a syntactically valid command might be unauthorized. Language recognition belongs inside a layered input-validation design.



## Grammars

**Core model — Grammars**

A grammar uses productions to generate strings from a start symbol. Regular, context-free and more general grammar classes have different expressive powers.

**Original worked illustration**

Grammar S->aSb or S->epsilon generates a^n b^n. The derivation S=>aSb=>aaSbb=>aabb exhibits n=2.

**Boundary conditions and checks**

A finite-state automaton cannot recognize arbitrary matched counts a^n b^n, so a regular expression is insufficient for this language.

### Grammars generate structured expressions
A context-free grammar consists of nonterminal symbols, terminal symbols, production rules and a start symbol. For arithmetic expressions, one might use E→E+T | T, T→T×F | F, F→(E) | id. Derivations replace nonterminals by right-hand sides until only terminals remain. The grammar's structure expresses intended precedence: multiplication is grouped under T while addition combines E and T. A parser produces a tree that records how the input was derived, allowing later stages to evaluate or compile the expression.

### Ambiguity and multiple parse trees
The naive grammar E→E+E | E×E | id is ambiguous because id+id×id has a parse grouping addition first and another grouping multiplication first. If interpretation assigns ordinary arithmetic meaning, the two trees can produce different results. Ambiguity is a property of a grammar, not simply a typo in a token sequence. Grammar refactoring, precedence declarations, or disambiguation rules can impose a single intended interpretation. The parser's acceptance decision and the semantic tree it constructs are separate outputs deserving independent tests.

### Balanced parentheses
The language of correctly nested parentheses is context-free. A grammar S→(S)S | ε generates ε, (), ()(), (()), and so on. To check a candidate string, scan left to right with a counter initialized at zero. Increase on '(' and decrease on ')'. Reject if the counter becomes negative; accept at the end only if it returns to zero. This linear-time algorithm recognizes the single-parenthesis-type language using an unbounded integer counter. For several bracket types, a stack is needed to remember which opening bracket should match each closing one.

### Parse-tree induction
Grammar derivations support structural induction. To show that every string generated by S→(S)S | ε contains equally many opening and closing parentheses, prove the empty-string case and the production step. If the first S contributes equal numbers and the second S also contributes equal numbers, wrapping the first part with one '(' and one ')' preserves equality; concatenating the second part preserves it again. This necessary balance property alone does not characterize correct nesting: ')(' has equal counts but cannot be derived.

### Parser engineering limitations
Recursive-descent parsers cannot directly implement arbitrary left-recursive grammar rules without transformation, because E→E+T calls E again before consuming input. LL and LR parsing methods handle different grammar families and lookahead constraints. Error messages are part of the reader experience: a parser that only outputs 'invalid' may meet recognition correctness yet be difficult to debug. Provide token positions, expected categories, and recovery behavior without fabricating certainty about which edit the user intended.



## Automata Models

**Core model — Automata Models**

A deterministic finite automaton consists of a finite state set, input alphabet, transition function, start state and accepting states. Every input symbol leads to exactly one next state.

**Original worked illustration**

For parity of ones, two states Even and Odd suffice: reading 1 toggles the state, reading 0 preserves it. The word 1011 ends Odd and is rejected by an even-parity recognizer.

**Boundary conditions and checks**

Missing transitions make an automaton incomplete; informal state sketches may conceal edge cases like the empty word.

### Finite automata make state explicit
A deterministic finite automaton consists of a finite state set Q, alphabet Σ, transition function δ:Q×Σ→Q, start state q0, and accepting states F⊆Q. It reads a string left to right, updating state according to δ. A string is accepted if the final state belongs to F. For binary strings having an even number of ones, use states E and O, start E, accept E, and toggle on input 1 while remaining unchanged on input 0. The empty string is accepted because the initial count of ones is even.

### Invariants explain DFA correctness
After reading any prefix w, the automaton's state is E exactly when w contains an even number of ones. Prove this by induction on prefix length. The base prefix ε has zero ones and state E. Appending 0 does not change either parity or state; appending 1 toggles both. The invariant directly proves recognition correctness for every input string, more reliably than testing only several examples. Tests still help uncover implementation mistakes such as an incorrect transition on a zero.

### Nondeterminism and subset construction
A nondeterministic finite automaton may have several possible next states, possibly including epsilon transitions. A string is accepted when at least one path through the machine ends in an accepting state. A deterministic machine can simulate an NFA by representing its current state as a subset of NFA states and updating the subset after each symbol. The subset construction may create up to 2^{|Q|} DFA states in the worst case, though many may be unreachable in a particular input machine. Nondeterminism in this model does not mean that hardware literally explores all paths at once.

### DFA minimization
Two states are equivalent when no possible suffix can distinguish them by acceptance. Partition-refinement algorithms group states with the same future behavior and combine equivalent states to form a minimal DFA. If two states have different acceptance status, the empty suffix already distinguishes them. If both agree on acceptance but some symbol leads to states in different classes, that symbol followed by a distinguishing suffix separates them. This gives a behavioral interpretation of minimization, not merely a table manipulation.

### Pushdown automata and model limits
A DFA has only finitely many states and cannot recognize the unbounded language {0^n1^n:n≥0}. A pushdown automaton adds a stack and can recognize that language by pushing symbols for zeros and popping one for each one, with guards preventing new zeros after ones begin. A Turing machine has still more general computational power through unbounded tape access. The hierarchy describes classes of languages and computational models; it does not assert that finite-state machines are useless in real software. Protocol handlers, tokenizers and many validators are naturally finite-state.



## Specification Foundations

**Core model — Specification Foundations**

Formal specification defines permissible behaviors and invariants before implementation. State-transition systems turn requirements into properties that can be checked against traces.

**Original worked illustration**

For a lock with states Free and Held, acquire must transition Free->Held and release Held->Free. A trace acquire,acquire violates the transition contract.

**Boundary conditions and checks**

A tested sample trace cannot demonstrate invariance over all possible traces; model-checking claims require declared finite state bounds and exploration assumptions.

### Specifications are mathematical contracts for programs
A precondition describes what must be true before a program fragment runs, while a postcondition describes the state afterward. Hoare notation {P} C {Q} means that if P holds and command C terminates, then Q holds; this is a partial-correctness interpretation unless termination is also proved. Consider command x:=x+1. With precondition x=4 and exact integer arithmetic, the postcondition x=5 follows directly. With fixed-width overflow near the maximum value, the same mathematical argument may no longer describe the executed program.

### Loop invariants carry facts across iterations
A loop invariant I should hold before the first iteration, be preserved by each iteration, and combine with the loop's exit condition to imply the desired postcondition. For finding the maximum of a nonempty list, initialize current maximum to the first element and process subsequent elements. An invariant is: after k elements have been processed, current maximum equals the maximum of those k elements. Initialization is immediate for k=1. When the next element arrives, replacing the stored maximum by max(old,new) preserves the property. On termination k=n, the postcondition follows.

### Model checking on bounded state systems
A transition system defines states, initial states and allowed transitions. A safety property says something bad never occurs; a liveness property says something good eventually occurs under specified fairness assumptions. For a finite bounded model, exhaustive reachability exploration can find a counterexample path to an unsafe state if one exists. State explosion is a major limit: n independent Boolean flags alone can produce 2^n states before the control state is counted. Abstraction, symmetry reductions and symbolic methods aim to preserve important properties while reducing explored state space.

### Temporal logic and the meaning of eventually
A formula informally written 'always not error' concerns every state along a path, while 'eventually response' concerns at least one future state. The latter may require assumptions that the scheduler actually executes pending work and that the environment does not permanently block I/O. Without fairness, a valid execution might indefinitely postpone a ready task. Formal verification must state which executions are considered; otherwise claims of eventual response may be stronger than the system guarantees.

### Testing, proof and real-world trust
Unit tests establish behavior for selected inputs. Property-based tests sample many inputs from a generator. Formal proofs establish properties for all inputs within a model, provided the proof and model are correct. None of these alone guarantees that a deployed service behaves as intended when compilers, network protocols, hardware faults, human procedures or data assumptions are wrong. An engineering release combines clear specifications, static reasoning, automated tests, operational monitoring and incident response. A textbook should teach the interfaces between these forms of evidence rather than presenting one as a complete substitute for the others.

### Extended laboratory: building and checking a tiny command language
Define a command protocol with alphabet of tokens OPEN, READ, CLOSE. A valid command session consists of OPEN followed by zero or more READ commands and finally CLOSE. In formal-language notation, L={OPEN READ^k CLOSE : k≥0}. The empty string is not valid, and neither is READ OPEN CLOSE. The protocol can be recognized by a DFA with states Start, Open, Done, Reject. From Start, OPEN moves to Open and everything else rejects. From Open, READ stays Open and CLOSE moves to Done. From Done, any further token rejects. Done is the only accepting state after the full input.

Test the language using concrete traces. OPEN CLOSE is accepted with k=0. OPEN READ READ CLOSE is accepted with k=2. OPEN READ never reaches Done, so it is rejected as an incomplete session. OPEN CLOSE READ enters Reject when the unexpected read follows closure. A useful invariant for state Open is that the prefix consists of OPEN followed by some number of READ tokens. For state Done, the whole accepted prefix has the required pattern. The invariant proves that the DFA accepts no invalid sequence and that all valid sequences follow its transitions to Done.

Now design a grammar S→OPEN R CLOSE and R→READ R | ε. The nonterminal R generates any finite list of READ tokens. Derive OPEN READ READ CLOSE by replacing S, expanding R twice with READ R, then replacing R by ε. The grammar and DFA describe the same toy language; the grammar's parse tree additionally exposes the recursive structure of the read sequence. This is an example of a regular language that is also context-free. Being context-free does not imply a language requires a stack for recognition.

Change the protocol so that operations may nest: OPEN OPEN CLOSE CLOSE is legal, while OPEN CLOSE CLOSE is not. The language of correctly nested OPEN and CLOSE operations can be expressed with grammar S→OPEN S CLOSE S | ε. An unbounded nesting depth cannot be recognized by a finite-state machine with a fixed number of states, because the checker must remember how many unmatched OPEN tokens remain. A pushdown automaton uses a stack to match these openings; a bounded-depth deployment could instead encode depths 0 through k in a DFA, but it would reject valid traces requiring more than k levels.

In an implementation, tokenization happens before grammar recognition. A string such as 'OPENREADCLOSE' must be split according to declared lexical rules or rejected if tokens require separators. A correct parser cannot compensate for a lexer that silently accepts illegal encodings. Similarly, recognizing a syntactically valid OPEN-READ-CLOSE trace does not prove that the user is authorized to read the resource. Access control and business semantics remain additional layers.

Specify safety properties for the protocol: 'READ never occurs before OPEN' and 'READ never occurs after CLOSE.' The DFA enforces both on accepted traces. A liveness property such as 'every OPEN is eventually followed by CLOSE' requires reasoning about potentially infinite executions; rejecting a finite incomplete trace is a parser decision, while proving eventual closure in a running concurrent system needs scheduler and environment assumptions. These claims live at different levels of abstraction.

Finally add a verifier that enumerates all token sequences of length at most five. For each sequence, compare the DFA's result against a direct pattern predicate: length at least two, first token OPEN, last token CLOSE, and every interior token READ. The outputs should match. This bounded exhaustive test can discover bad transitions such as allowing READ in Done. It does not establish the equivalence for strings of every possible length; the state invariant and grammar derivation provide the general argument. Document the accepted alphabet, treatment of malformed tokens, and reset behavior so simulation users know precisely what model is being demonstrated.

### Experiment card: parity and remainder automata
The primary automaton model reads the binary representation of input integer n and accepts when its number of one bits is even. For n=3, binary 11 contains two ones and is accepted. For n=5, binary 101 contains two ones and is accepted. For n=7, binary 111 contains three ones and is rejected. An independent checker can count bits with a loop that repeatedly examines the least significant bit and shifts the integer right. The expected acceptance decision is the parity of that count. The model is a DFA for parity of ones, not a DFA recognizing even numerical values; a binary number may be even while containing an odd number of ones.

The companion model reads the fixed binary word 1101 (decimal thirteen) through a remainder-tracking automaton, varying the modulus n. Its state update after bit b is r'=(2r+b) mod n. Starting from residue zero, reading 1,1,0,1 yields a final remainder 13 mod n. For n=1 the remainder is zero and every string is accepted. For n=2 the remainder is one, so the word is rejected by the divisible-by-two language. The simulation is not parsing an arbitrary user-entered binary word; it is a controlled experiment with one fixed word and a changing modulus.

Verify the result using ordinary integer arithmetic: compute 13%n for each supported n and compare with the automaton's final state. Also inspect the transition invariant. After consuming a prefix whose binary numerical value is v, the current state equals v mod n. Appending bit b changes the number to 2v+b, so the update formula preserves the invariant. The base empty prefix has value zero and state zero, completing an inductive correctness proof.

For student exercises, change the accepting set from {0} to {1} for modulus three. The automaton now recognizes binary representations whose value leaves remainder one, not divisible values. Keep the transition function unchanged. Then ask why a fixed finite automaton cannot recognize arbitrarily nested parentheses, whereas a stack-based parser can. Both machines process sequences symbol by symbol, but one has bounded memory and the other can retain unbounded nesting information. The comparison links a concrete simulator to a central limitation of finite-state computation.



## Fully worked questions

### Question 1: Languages: worked application 1

Build a two-state DFA accepting binary strings with an even number of ones, and test 1011.


**Set up the model and conditions:** Create states E (start, accepting) and O (nonaccepting); 0 preserves state and 1 toggles.


**Carry out the calculation or proof:** Trace 1:E→O, 0:O→O, 1:O→E, 1:E→O.


**State the result and its scope:** The final state O rejects 1011.


**Independent reasoning check and edge conditions:** Use states E for even parity and O for odd parity. Start in E and accept only in E. Reading a zero keeps the current state while reading a one toggles between E and O. For input 1011, the states after each character are O, O, E, O, so the final state O rejects. The string contains three ones, confirming the direct parity check. The empty string would be accepted because it contains zero ones; if the specification requires a nonempty string, it must add a separate rule or state.


**Answer:** The final state O rejects 1011.


### Question 2: Grammars: worked application 2

Derive the string aabb from grammar S→aSb | ε.


**Set up the model and conditions:** Use S⇒aSb by the recursive production once.


**Carry out the calculation or proof:** Use the same production again to get aaSbb, then S→ε.


**State the result and its scope:** The result is aabb.


**Independent reasoning check and edge conditions:** Start with S and apply S→aSb once to obtain aSb. Apply the same production to the remaining S, giving aaSbb. Finally replace S by ε to obtain aabb. Each derivation step changes one nonterminal according to a declared production, and the final string has no nonterminals. The grammar generates a^n b^n for n≥0, including the empty string. It does not generate abab, because all a tokens must precede the corresponding b tokens. This language is context-free but not regular.


**Answer:** The result is aabb.


### Question 3: Automata Models: worked application 3

Explain why a lock protocol allowing acquire only in Free state rejects acquire,acquire.


**Set up the model and conditions:** Start in Free; first acquire takes the system to Held.


**Carry out the calculation or proof:** A second acquire has no enabled Held→Held acquire transition in this specification.


**State the result and its scope:** The trace is rejected at its second step.


**Independent reasoning check and edge conditions:** Represent the lock by states Free and Held. The transition acquire is defined from Free to Held; the protocol does not permit acquire from Held without an intervening release. Starting Free, the first acquire moves to Held. The second acquire has no valid transition, so the trace is rejected. To test the intended policy, also verify acquire,release,acquire,release succeeds and release in Free is rejected. If a real lock supports reentrancy, it needs a different state model, such as an ownership counter, rather than forcing the simple two-state protocol to represent it.


**Answer:** The trace is rejected at its second step.

