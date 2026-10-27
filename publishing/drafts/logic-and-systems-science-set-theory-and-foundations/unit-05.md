# Unit 5 — Countability, Cardinality, and Diagonalization

**Core insight.** Finite strings, rational numbers, infinite binary sequences and real intervals do not all have the same cardinality.

**Running case.** A data scientist asserts that all infinite datasets can be indexed by an ordinary list of integers. Test the claim on rational values and infinite bit streams.

**Restriction.** A diagonal argument must define an object within the claimed codomain that differs from the nth candidate at a definite coordinate.

## Unit orientation: definition, construction, and evidence

Countably many finite descriptions do not capture every infinite information stream. Length-first enumeration covers each finite string at some finite stage. Cantor’s diagonal method constructs an infinite string that differs from every row of any proposed enumeration of infinite binary sequences.

Cantor’s theorem is a structural obstruction: no map from A onto P(A) can cover all subsets. It applies independently of whether A is finite, countable or uncountable. The diagonal subset depends on f but is still a legitimate subset of A, so it lies in the codomain that the alleged map was meant to cover.

Cardinal arithmetic requires named axioms and careful representation. The inequality ℵ₀<2^{ℵ₀} is established, whereas the assertion that 2^{ℵ₀}=ℵ₁ is not settled by ZFC. Computational sampling of finite bit strings does not decide a statement about possible intermediate infinite cardinals.

**Three questions before working.** (1) Is the object finite, a finite description, or an infinite sequence? (2) How does the diagonal differ from the indexed candidate? (3) Which conclusion follows in ZFC and which does not?

The unit is organized in a deliberate sequence. Start with a definition; derive consequences by matching the definition to its quantifiers; construct a worked finite or symbolic case; and then search for a boundary case. Mathematics offers different kinds of evidence. A direct proof establishes a result for all objects in the stated domain; a counterexample disproves such a result; an example only illustrates it. The accompanying model visualizations are transparent local computations. They can reveal errors and motivate a proof, but cannot establish set-theoretic independence, consistency, or claims about every possible infinite structure.

### Common vocabulary and a formal audit

In this unit, the word *construction* means a legitimate definition of an object in the chosen system, not just an algorithm that prints a plausible string. The running case is **A data scientist asserts that all infinite datasets can be indexed by an ordinary list of integers. Test the claim on rational values and infinite bit streams.** A complete mathematical account begins by stating the source sets and background theory. Next specify what is asserted to exist, what equality means for these objects, and what properties need proof. Finally separate any domain facts collected from outside the mathematics. The last separation matters because an algorithm can be logically correct yet operate on incomplete or incorrectly classified entries.

A quick error audit starts from the restriction: **A diagonal argument must define an object within the claimed codomain that differs from the nth candidate at a definite coordinate.** Try to invent a minimal counterexample to a stronger-sounding but invalid statement. If the counterexample is finite, list each member or ordered pair explicitly. If the statement concerns infinity or axioms, name the exact principle that would be required. Giving the missing hypothesis is a mathematically useful response: it tells the reader how the claim could be repaired without pretending it was already proved.

## Lesson 5.1 — Cantor diagonal and binary sequences

### Statement and formal objects

**Definition.** The set {0,1}^N of infinite binary sequences is uncountable. If sequences s₀,s₁,... were listed, t(n)=1−sₙ(n) differs from sₙ at position n. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Given purported rows 000…,101…,110…,… form a new row by flipping each diagonal bit; whatever the remaining rows are, the new sequence disagrees with row n at digit n. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Claiming the diagonal object is absent without checking it belongs to the same set of binary sequences. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Explain why a finite 5×5 matrix diagonal flip does not prove infinitely many sequences are uncountable. **Worked answer or proof outline:** It constructs an omitted length-5 string from five candidate strings, but all 2^5 finite strings can still be listed; infinitude is essential. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Claiming the diagonal object is absent without checking it belongs to the same set of binary sequences.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A data scientist asserts that all infinite datasets can be indexed by an ordinary list of integers. Test the claim on rational values and infinite bit streams. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 5.2 — Countable unions and finite strings

### Statement and formal objects

**Definition.** A finite product of countable sets is countable; a countable union of countable sets is countable in ZFC, with choice subtleties for arbitrary countable families in ZF. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Binary strings of length n number 2^n. Their union over finite lengths can be listed by length and lexicographic order, so all finite binary strings are countable. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Equating all finite strings with infinite binary streams simply because both use only zeros and ones. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Construct an enumeration that lists ε, 0, 1, 00, 01, 10, 11 and continues. **Worked answer or proof outline:** Order by length, then lexicographically. Every finite string has finite length and finite position among strings of that length, ensuring eventual appearance. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Equating all finite strings with infinite binary streams simply because both use only zeros and ones.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A data scientist asserts that all infinite datasets can be indexed by an ordinary list of integers. Test the claim on rational values and infinite bit streams. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 5.3 — Cantor theorem: no set surjects onto its powerset

### Statement and formal objects

**Definition.** For every set A and f:A→P(A), define D={a∈A:a∉f(a)}. D∈P(A) but D≠f(a) for each a∈A, so no surjection A→P(A) exists. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Assume f(a₀)=D. Then a₀∈D iff a₀∉f(a₀)=D, contradiction. The proof does not rely on finite examples or a preferred listing. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Using Russell’s paradox directly as though D were an unrestricted set of all sets. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Give a full proof that |A|<|P(A)| in the sense of an injection A→P(A) but no bijection. **Worked answer or proof outline:** The singleton map a↦{a} is injective. Cantor’s diagonal subset excludes any surjection from A onto P(A). Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Using Russell’s paradox directly as though D were an unrestricted set of all sets.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A data scientist asserts that all infinite datasets can be indexed by an ordinary list of integers. Test the claim on rational values and infinite bit streams. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 5.4 — Reals and decimal representation caveats

### Statement and formal objects

**Definition.** The interval (0,1) is uncountable; a diagonal construction works with base digits if nonunique expansions such as 0.4999…=0.5000… are handled. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Choose each diagonal digit from {1,2} against a displayed decimal digit using 1 if the digit is 2 and 2 otherwise. Only digits 1 and 2 appear, avoiding terminating/nines ambiguity. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Flipping digits by a rule that can create two decimal expansions for the same real and then claiming distinctness without qualification. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Explain why the base-2 sequence diagonal proof is cleaner for Cantor space than arbitrary decimal real expansions. **Worked answer or proof outline:** Infinite bit sequences are primitive elements of {0,1}^N and differ at a coordinate by definition; representing real numbers adds an identification issue at dyadic rationals. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Flipping digits by a rule that can create two decimal expansions for the same real and then claiming distinctness without qualification.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A data scientist asserts that all infinite datasets can be indexed by an ordinary list of integers. Test the claim on rational values and infinite bit streams. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 5.5 — Cardinal arithmetic, CH, and independence

### Statement and formal objects

**Definition.** Cardinals classify equipotent sets. In ZFC, |N|=ℵ₀, |P(N)|=2^{ℵ₀}; the continuum hypothesis asserts no cardinal strictly between these and is independent of ZFC if ZFC is consistent. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** For finite A of size 4, |P(A)|=16. For infinite A=N, Cantor still proves |P(N)|>|N|, but does not decide whether an intermediate infinite cardinal exists. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Treating Cantor’s theorem as a proof of the continuum hypothesis. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Distinguish the claims “2^{ℵ₀}>ℵ₀” and “2^{ℵ₀}=ℵ₁.” **Worked answer or proof outline:** The former follows from Cantor’s theorem. The latter is CH; Gödel and Cohen established relative consistency and independence results over ZFC. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Treating Cantor’s theorem as a proof of the continuum hypothesis.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A data scientist asserts that all infinite datasets can be indexed by an ordinary list of integers. Test the claim on rational values and infinite bit streams. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Unit 5 integrative capstone — Countability, Cardinality, and Diagonalization

**Project brief.** A data scientist asserts that all infinite datasets can be indexed by an ordinary list of integers. Test the claim on rational values and infinite bit streams. Draft a mathematics-first specification. Begin with the minimum object vocabulary for the case: distinguish an element, a collection of elements, a relation, a function and a predicate where relevant. Then select at least two of the five lesson theorems or constructions and explain precisely how they apply. Include one counterexample to a tempting informal rule. A valid submission must not imply that a finite output validates an unlimited set-theoretic law.

**Proof deliverables.** 1. A source-set and ambient-universe declaration that resolves **is the object finite, a finite description, or an infinite sequence?** 2. A worked calculation that can be independently repeated without external data. 3. A statement of whether the central result is an identity, an existence claim, an injection, a well-ordering argument, an induction theorem, or an independence statement. 4. An edge-case analysis respecting the warning: **A diagonal argument must define an object within the claimed codomain that differs from the nth candidate at a definite coordinate.** 5. A final paragraph explaining what remains outside the proof.

**Marking rubric (100 points).** Exact mathematical objects and domains: 20. Correct use of definitions: 20. Verifiable worked argument: 25. Counterexample and limitations: 20. Clarity, notation and citation of background assumptions: 15. An answer loses foundational credit when it conflates a set and its element, treats a limited search as a universal result, assumes a function is invertible without proof, or omits a limit-stage or choice assumption that affects the result.

### Unit-level short examination

**Question A.** Compare the hypotheses and conclusions of **Cantor diagonal and binary sequences** and **Cardinal arithmetic, CH, and independence**. Give a concrete condition under which the second topic requires extra reasoning not supplied by the first.

**Question B.** Rebuild a nontrivial example from scratch while changing the original numerical identifiers or relation table. Check the result using the same definition, and explain why the identity of the symbols does not matter when an isomorphism or renaming preserves the relevant structure.

**Question C.** State which named axiom or principle would justify an existence statement in the unit and which statements can be proved from definitions alone. Carefully separate the informal application from a statement inside classical set theory.

**Question D.** Identify one realistic reason a software implementation of this unit’s ideas could be wrong even if its core mathematics is sound; propose a test for the implementation without claiming that the test proves a theorem about infinity.

