# Unit 1: Formal languages

*Editorial draft; not approved for live publication.*

## Alphabets
**Alphabets: conceptual explanation**

### Alphabet as a modeling decision
A formal alphabet is finite, and its members are atomic symbols by convention, even if a symbol is printed using several characters. A tokenizer may define IF as one token while the input characters `i` and `f` constitute two separate characters. Confusing the lexical alphabet with a grammar's terminal alphabet leads to invalid counts. Let A={red,blue,green}. The sequence red-blue contains two symbols in A*, despite the larger number of characters needed to print it. The empty word belongs to A* because it is the result of concatenating zero symbols. It does not belong to A+ unless the language designer expressly includes it in a separate rule.

If |A|=k, the map from a word of length n to its ordered n-tuple of symbols is a bijection between A^n and the Cartesian product of n copies of A. The multiplication rule therefore gives |A^n|=k^n, including |A^0|=1. For k=3, there are 27 length-three words; the empty word is the unique length-zero word. Infinite A* is nevertheless countable when A is finite: enumerate words by increasing length and, within a length, lexicographically. This construction matters when algorithms enumerate all possible input strings. It does not permit a terminating finite search over A* without a separate bound.

Think of a real protocol whose messages are represented by symbols START, DATA, ACK, and END. These four types are a logical alphabet, but their binary encodings may have variable lengths. If encodings overlap without a framing rule, a byte stream may admit multiple tokenizations. A formal grammar cannot compensate for an ambiguous physical encoding unless the lexer supplies a deterministic boundary policy. Verify the mapping between raw bytes and alphabet elements before counting messages. Unicode introduces an analogous distinction between bytes, code points, and user-perceived graphemes; do not silently change the underlying alphabet halfway through an argument.

### Why symbol coding cannot be ignored
Suppose an alphabet contains the tokens {A, AB, B}. If a source text contains characters AB, it could denote the one-token word [AB] or the two-token word [A,B]. A lexer must establish a unique tokenization rule, such as maximal munch with priority or a prefix-free encoding. Under a prefix-free code no codeword prefixes another, which lets the receiver parse token boundaries without external separators. The set {0,10,11} is prefix-free: every encoded symbol can be recognized after reading at most two bits. By contrast, {0,01,1} is not prefix-free because 0 prefixes 01. It is not enough to call an encoding 'binary' and then apply a simple k^n count: k^n describes abstract length-n symbol sequences, whose physical bit lengths may vary.

If the codewords have lengths ℓ_1,...,ℓ_k, the bit length of an encoded symbolic word is the sum of lengths for its component symbols. A length-n symbolic word need not correspond to an n-bit transmission. This distinction matters when estimating brute-force input spaces or expressing complexity in terms of bytes. Consider five abstract symbols chosen from an alphabet of eight. There are 8^5=32768 possibilities, but a fixed three-bit encoding requires fifteen bits for each. With a variable-length encoding, different choices can yield different physical lengths. The correct count depends on whether the exercise constrains symbols, codewords, or bytes.

An edge case concerns the empty alphabet. Some formal conventions permit Σ=∅, in which case Σ*={ε}; many introductory texts choose a nonempty alphabet to simplify statements. If you rely on k≥1, say so. The identity |Σ^0|=1 still holds, because the empty word is the unique sequence of length zero even when no symbols are available. This is a useful example of how an apparently harmless definition changes the meaning of boundary examples. In course exercises, require students to write both the logical alphabet and its representation before deriving storage costs.

## Strings
**Strings: conceptual explanation**

### Words, positions and closure
Define a word w of length n as a function from {1,...,n} into the alphabet. This position-based definition makes indexing and substring claims precise. With zero-based programming notation the same positions are 0 through n-1. Write |w| for the length, w^R for reversal, and ε for the empty word. Concatenation uv first copies every position of u and then appends v, giving |uv|=|u|+|v|. This establishes associativity: both (uv)z and u(vz) contain the symbols of u, v, and z in the same order. It does not establish commutativity. For example, ab differs from ba even though they have the same length.

The set A* with concatenation is a free monoid: it has an associative operation with identity ε, and every element is uniquely decomposable into a sequence of generators from A. The term free is important. Relations such as ab=ba are not built into strings. If an application requires order-insensitive collections, its mathematical model is a multiset or a quotient structure, not an unrestricted word. Prefixes and suffixes include ε and the entire word. For a word of length n there are n+1 different prefix positions, but fewer than n+1 distinct prefix strings is not possible: each prefix has a unique length. Substrings are indexed by start and end positions and can repeat as values.

For a binary alphabet, the cumulative number of words up to length n is 1+2+...+2^n=2^(n+1)-1. The formula includes ε. A language of palindromes is an infinite proper subset of A*. Reversal preserves word length but changes left and right concatenation: (uv)^R=v^R u^R. Checking this identity on examples is a useful first exercise, but an inductive proof on the length of v gives a general result. Distinguish a property holding for every word from an observed property of a finite sample.

### Induction on strings: a reusable proof method
Prove that reverse(reverse(w))=w for every word w over Σ. Start with ε: reversing ε does nothing, so the identity holds. Suppose it holds for a word v. Append a symbol a to produce va. Using reverse(va)=a reverse(v), reverse(reverse(va)) equals reverse(a reverse(v)); reversal of a concatenation reverses its factors, producing reverse(reverse(v)) a=va by the induction hypothesis. A proof by induction on length covers every finite word, regardless of what particular symbols are present.

A common mistake is to attempt induction over the number of distinct letters. A word may repeat symbols many times, so the number of distinct symbols does not follow the structural construction. Another mistake is stating the induction hypothesis for a single chosen string v but using it for arbitrary pieces later without justification. Structural induction on the recursive word construction, w=ε or w=va, makes the legal inference rule explicit. In programming, recursive functions on lists follow exactly this reasoning when list concatenation and reverse are implemented consistently.

Now analyze the classic recursive reversal routine reverse(va)=a+reverse(v) when concatenation copies its left argument. If adding a character to the front of a string is O(|v|), the resulting implementation may use Θ(n²) time; if a list representation permits O(1) cons, construction may be linear, with an additional pass to materialize an array. Both compute the same mathematical reversal. Correctness and complexity are separate proof obligations. Asking only whether the output string is right misses a significant engineering consequence of representation.

For testing, enumerate binary words through length eight and check involution, length preservation, and anti-homomorphism (uv)^R=v^R u^R for selected pairs. Property-based tests can reveal a bug such as reversing Unicode bytes rather than code points, while the mathematical proof covers only the intended alphabet abstraction. Record this abstraction boundary in the lab report.

## Operations
**Operations: conceptual explanation**

### Language operations as constructive rules
A language is a set of words. Union and intersection use ordinary set operations, while concatenation is defined by LR={uv: u∈L and v∈R}. A word in LR may admit multiple decompositions, so simply multiplying the numbers of words in L and R can overcount. For L={ε,a} and R={ε,a}, the four pairs produce ε,a,a,aa, so LR has only three elements. Kleene closure L* is the union of all finite powers L^i, with L^0={ε}. This definition makes ε∈L* unavoidable, even if ε∉L. Positive closure L+ is the union over i≥1; when ε∈L the two closures may coincide.

Language complementation requires an explicit universe. For a binary language, `not L` generally means A*\L with A={0,1}; if the alphabet silently changes to {0,1,2}, the complement changes. Reversal of languages applies reversal to every member and distributes over union. Its interaction with concatenation reverses order: (LR)^R=R^R L^R. A proof has two inclusions. If w∈(LR)^R then w=(uv)^R=v^R u^R for some u∈L and v∈R, so w∈R^R L^R; the reverse inclusion applies the same identity backwards.

Quotients are essential for automata theory. The left quotient w^-1 L={x:wx∈L} captures possible continuations after reading prefix w. Two prefixes are behaviorally indistinguishable for L when their quotients agree. This observation leads directly to the Myhill–Nerode relation and minimal DFA states. A student should practice computing quotients for languages such as strings ending in 01, comparing the residual requirement after prefixes ε,0, and 01. Algebraic language identities become useful when they suggest an actual algorithm or an invariant.

### Derive algebraic counterexamples before writing code
The identity (L∪R)S=LS∪RS follows directly from quantifiers. A word belongs to the left side exactly when it has a decomposition uv with u in L or R and v in S. This is equivalent to a decomposition with u in L and v in S, or one with u in R and v in S. Both directions hold without finiteness assumptions. Similarly, L(R∪S)=LR∪LS. But replacing concatenation by an arbitrary multiplication rule can tempt invalid cancellations. From LA=LB it need not follow that A=B: choose L=∅, and both products are empty regardless of A and B.

Kleene star supplies another trap: (L∪R)* generally differs from L*∪R*. Let L={a}, R={b}. The left language contains ab because it may concatenate an a and a b from different choices; the right contains only words made exclusively of a or exclusively of b. Star's union behavior permits interleaving between factors. Notice also that L*L*=L* because concatenating two sequences of L-words is still a sequence of L-words; the empty-factor case handles zero repetitions.

The left quotient has a useful derivative property. For w=ab and language K, (ab)^-1 K=b^-1(a^-1 K) under the convention w^-1K={x:wx∈K}. To verify, x is in b^-1(a^-1K) precisely when bx is in a^-1K, meaning abx∈K. This computation mirrors how a DFA updates its residual future requirement after each newly read symbol. It can be used to construct a minimal automaton conceptually by identifying distinct residual languages.

A careful exercise should distinguish operations on words from operations on languages. The concatenation of one word u with another word v is itself one word uv; concatenating singleton languages {u}{v} yields singleton language {uv}. Confusing the types can hide errors in derivations that appear syntactically plausible. Introduce notation checks as part of proofs, not merely style preferences.

## Language Classes
**Language Classes: conceptual explanation**

### Four language families and evidence
A regular language is recognized by a finite automaton, generated by a regular expression, or described by a right-linear grammar under the standard equivalence theorems. A context-free language is generated by a context-free grammar and recognized by a nondeterministic pushdown automaton. A context-sensitive language is recognized by a suitably bounded linear-space machine, while recursively enumerable languages are accepted by Turing machines that may run forever on nonmembers. These inclusions are proper, but proving a proper inclusion requires a separating language and a theorem, not an intuition that a machine feels stronger.

For example, L={0^n1^n:n≥0} is context-free: a stack can push one symbol per 0 and pop one per 1. It is not regular, because a DFA with finitely many states must repeat a state while scanning sufficiently many initial zeros. The repeated-state argument yields distinct prefixes that the machine cannot distinguish, yet a suitable suffix of ones must distinguish them. The language {0^n1^n2^n:n≥0} is not context-free under a standard pumping argument, even though a context-sensitive recognizer can check three counters within linear tape space. Each separation comes with hypotheses that need to be stated carefully.

Do not confuse the class of a problem with a particular implementation's speed. A context-free parser can be inefficient if built poorly; a DFA can still have a huge state graph. Likewise, a non-context-free language may have a fast membership algorithm using a richer computational model. Complexity measures time and space once the model and input encoding are fixed. Expressiveness concerns which languages a model can recognize at all. Build a classification table with an explicit witness method and at least one boundary counterexample for every row.

### How to prove a language is nonregular
Use the pumping lemma as a necessary property of regular languages, not as a test that automatically establishes regularity when it appears to hold. Suppose L={0^n1^n:n≥0} were regular with pumping length p. Choose word s=0^p1^p. Any permitted split s=xyz satisfying |xy|≤p and |y|>0 places y entirely among zeros. Pumping y down to zero copies yields xz with fewer zeros than ones, outside L. But the pumping lemma would require xy^i z∈L for every i≥0. This contradiction proves L nonregular.

The quantifiers matter: after choosing the long word s, the pumping lemma permits some suitable split; to refute the lemma, the proof must handle every split meeting its constraints, not one convenient split. Taking y to be the entire initial block is not justified unless that choice follows from the assumed automaton. Another standard strategy uses the Myhill–Nerode theorem: for every i≠j, prefixes 0^i and 0^j are distinguished by suffix 1^i, because one yields equal counts and the other does not. There are infinitely many equivalence classes, so no finite DFA exists.

The Myhill–Nerode argument is often stronger pedagogically because it exhibits the unbounded memory required: after reading i zeros, the recognizer needs to distinguish infinitely many possible i values to know which number of ones is acceptable. A finite control cannot do so. The conclusion does not say the language is undecidable or computationally infeasible. A pushdown automaton decides it using a stack, and a conventional program decides it by counting. Nonregularity is a limitation of a specific memory model.

When classifying a less familiar language, seek both an upper bound and a lower bound. Give a machine or grammar proving membership in a class, then a separating argument ruling out a weaker class. One direction alone is not a full classification.

## Integrated Case Study and Model Limitations
**Unit synthesis: Formal languages.** The following case study integrates formal definitions, correctness reasoning, limitations and realistic testing.

### A finite protocol-language investigation
Design a protocol where packets begin with OPEN, continue with zero or more DATA messages, and end with CLOSE. The allowed messages form OPEN DATA* CLOSE. A finite automaton needs an initial state, an active state, an accepting closed state, and a rejecting sink if the transition function is total. After OPEN the automaton loops on DATA, and CLOSE moves it to the accepting state. Any subsequent DATA or CLOSE must fail. If a client can cancel before CLOSE, the language changes: specify CANCEL as an alternative terminal rather than adding an undocumented transition.

Now extend the protocol to nested BEGIN and END blocks. If arbitrary nesting is legal and every BEGIN must match an END, a finite-state model cannot maintain an unbounded depth counter. A pushdown model can push on BEGIN and pop on END. Real services often enforce a finite maximum nesting depth, in which case a large but finite automaton could represent every depth. State the bound before saying the service truly needs a pushdown automaton. This distinction shows why finite test cases cannot prove an unbounded language property.

For a lab, enumerate all strings of up to length five over the alphabet {OPEN,DATA,CLOSE} and compare acceptance with a direct specification checker. Ensure the empty string and malformed leading CLOSE are rejected. Record exact intended traces for OPEN-CLOSE, OPEN-DATA-CLOSE, OPEN-DATA-DATA-CLOSE, and OPEN-CLOSE-DATA. Then modify the grammar with nested blocks and show the failure of a finite-depth model on an input just beyond its limit. The point of the exercise is specification fidelity: enumerate within a bound, give a rigorous explanation beyond it, and do not mistake tested cases for a proof.

### Bounded exhaustive checks versus an unbounded theorem
Extend the packet-language experiment by allowing zero or more nested groups: START, followed by possibly nested OPEN ... CLOSE segments, then END. A depth-limited validator can be represented by a finite automaton with a state for each legal depth up to bound d plus status and error states. For d=2, test a string containing three nested OPEN tokens followed by three CLOSE tokens. The validator rejects by resource policy, although an unbounded stack-based grammar would accept that nested structure. The example shows that the language of implemented software may intentionally differ from the ideal formal grammar.

A compiler's parser may use an ordinary call stack as its nesting memory. Even if the grammar is context-free, an actual recursive-descent implementation can fail for deep inputs because its runtime stack is finite. Classify this as resource exhaustion rather than syntactic invalidity if the user-facing specification promises arbitrary nesting. A safer implementation may use an explicit heap-allocated stack with a configured limit. The limit is still finite but can produce an informative outcome and avoid crashing.

For the lab record, store the grammar version, tokenization policy, maximum depth and the expected result for every test. Generate all length-≤d token strings over a tiny alphabet to compare the recognizer against a direct reference predicate; then use an induction proof for general balanced nesting. Extend the test generator with malformed cases that contain an extra CLOSE, omit a final END, or close a group in the wrong order. The implementation should reject those for a semantic reason independent of the depth limit.

Finally, connect language design to security. Ambiguity between the gateway's parser and the backend's parser can cause inconsistent interpretation of the same bytes. In a specification-first design, both components should agree on framing and grammar, or reject ambiguous encodings. Formal language theory does not itself prevent an exploit, but it gives precise tools to identify parser disagreement.

### Proof notebook: alphabet, concatenation and physical encoding
Create two representations of a language of binary messages: one treats the entire message as a word over {0,1}, and another treats consecutive pairs as tokens over {00,01,10,11}. The second representation applies directly only to even-length messages unless a remainder symbol is introduced. A count of k^n has meaning only once k and n refer to one consistent tokenization. Derive the number of even-length messages up to ten bits, and explain why adding odd-length encodings requires another rule. The exercise forces a learner to label an abstract symbol versus the bytes used to represent it.

Add a prefix-free code exercise. Choose codewords 0,10,11 and decode 01110 from left to right as 0,11,10. Now choose ambiguous codewords 0,01,1; show that the string 01 admits both 01 and 0 followed by 1. Instead of saying the implementation 'failed', identify the missing unique-decoding property. Finally, use the regular packet language to verify which lexed symbols may occur in sequence. Separate errors into physical framing, lexical decoding, and grammatical membership; an end-to-end message can fail at any of those layers. This is the practical reason formal descriptions begin with precise alphabets.

### Independent self-check: choose the right mathematical object
Classify each object in a packet decoder as raw byte, code point, alphabet symbol, string, or language. Write down why bytes and graphemes need not correspond one-for-one. Then decide whether one protocol record is modeled by one long string or by a sequence of typed tokens. The result controls whether a string-count formula should be expressed in terms of packet types, characters, or bits. Recompute one enumeration under an intentionally changed encoding and state why the number of abstract messages does not necessarily change. This exercise prevents representation mistakes that often invalidate otherwise correct proofs.

### Worked question: Count short DNA words
For alphabet Σ={A,C,G,T}, count words of length exactly five and of length at most five, including the empty word.

**State the formal contract**
Each of five positions offers four choices, so the number of length-five words is 4^5=1024. The choices multiply because a symbol at one position does not constrain another position.

**Derive the result**
For lengths zero through five the count is 1+4+16+64+256+1024=1365, by the geometric-series identity (4^6-1)/(4-1). The length-zero term is the unique empty word ε.

**Check the scope and a counterexample**
Check by direct enumeration for lengths zero, one, and two: 1+4+16=21. The formula predicts 21. Do not count physical byte encodings as additional alphabet symbols.

**Answer:** Exactly five: 1024. Up to five: 1365.

### Worked question: Concatenation and duplicate products
Let L={ε,a} and R={ε,a}. Calculate the language product LR and explain why |LR| differs from |L||R|.

**State the formal contract**
List the four ordered choices from L×R: (ε,ε), (ε,a), (a,ε), and (a,a). Concatenate each pair, yielding ε, a, a, and aa.

**Derive the result**
Languages are sets rather than multisets, so the duplicate a is counted once. Consequently LR={ε,a,aa} and |LR|=3, whereas |L||R|=2×2=4.

**Check the scope and a counterexample**
The counting shortcut works only if the concatenation map from L×R into LR is injective. Here it is not, because εa=aε. A counterexample disproves the unrestricted multiplication claim.

**Answer:** LR contains three distinct words; four pairs do not imply four outcomes.

### Worked question: Infinite language versus finite test
A tester enumerates all binary strings up to length twelve and finds that a validator accepts exactly the strings ending in 01. Has the tester proved equivalence to (0|1)*01?

**State the formal contract**
The bounded set has 2^13−1=8191 strings. Agreement on this finite collection checks only inputs with length at most twelve; infinitely many longer inputs remain unexamined.

**Derive the result**
A validator that behaves correctly on every tested input but deliberately flips its answer for one specific thirteen-symbol word is a counterexample to the proposed inference.

**Check the scope and a counterexample**
A proof could instead construct a DFA from the validator if its finite-state semantics are known, form the symmetric difference against the reference DFA, and check reachability of an accepting state.

**Answer:** No. Finite exhaustive testing without a proved completeness bound cannot establish equivalence over Σ*.
