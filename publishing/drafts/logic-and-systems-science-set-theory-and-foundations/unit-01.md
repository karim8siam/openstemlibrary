# Unit 1 — Sets, Membership, and Operations

**Core insight.** Extensionality makes membership conditions decisive: equivalent descriptions designate one set, but a set is not the same object as its elements.

**Running case.** Scientific sample inventory: three labs submit overlapping identifiers. Verify duplicates, subsets, complements and all derived sample groups without inventing a universal set.

**Restriction.** Declare a fixed ambient universe whenever you take a complement. A power set requires a set as its input; a proper class cannot be treated as a permissible universal set.

## Unit orientation: definition, construction, and evidence

A finite sample universe does not represent the set of all possible specimens. This matters in software: a complement operation performed in a registry means “not in the selected cohort among known identifiers,” not “does not exist anywhere.” When data scope changes, the result changes even if the recorded members of A do not.

A set identity may be proved by two inclusions: assume an arbitrary x is in the left side, derive membership on the right; reverse the implication. A Venn diagram or bit-mask table is valuable for checking a proposed identity but does not, by itself, substitute for the symbolic proof when the quantifiers range over every set.

The empty set illustrates a productive separation of notation and ontological claim. It is an object with no elements, while its singleton has one element, namely the empty set. Nesting braces changes the object, so the set {∅} must not be erased or simplified to ∅.

**Three questions before working.** (1) What exact members does the definition permit? (2) Which object is being selected: a member, a subset, or a set of subsets? (3) Can you prove the proposed identity by testing arbitrary element membership in both directions?

The unit is organized in a deliberate sequence. Start with a definition; derive consequences by matching the definition to its quantifiers; construct a worked finite or symbolic case; and then search for a boundary case. Mathematics offers different kinds of evidence. A direct proof establishes a result for all objects in the stated domain; a counterexample disproves such a result; an example only illustrates it. The accompanying model visualizations are transparent local computations. They can reveal errors and motivate a proof, but cannot establish set-theoretic independence, consistency, or claims about every possible infinite structure.

### Common vocabulary and a formal audit

In this unit, the word *construction* means a legitimate definition of an object in the chosen system, not just an algorithm that prints a plausible string. The running case is **Scientific sample inventory: three labs submit overlapping identifiers. Verify duplicates, subsets, complements and all derived sample groups without inventing a universal set.** A complete mathematical account begins by stating the source sets and background theory. Next specify what is asserted to exist, what equality means for these objects, and what properties need proof. Finally separate any domain facts collected from outside the mathematics. The last separation matters because an algorithm can be logically correct yet operate on incomplete or incorrectly classified entries.

A quick error audit starts from the restriction: **Declare a fixed ambient universe whenever you take a complement. A power set requires a set as its input; a proper class cannot be treated as a permissible universal set.** Try to invent a minimal counterexample to a stronger-sounding but invalid statement. If the counterexample is finite, list each member or ordered pair explicitly. If the statement concerns infinity or axioms, name the exact principle that would be required. Giving the missing hypothesis is a mathematically useful response: it tells the reader how the claim could be repaired without pretending it was already proved.

## Lesson 1.1 — Extensionality and equality

### Statement and formal objects

**Definition.** Sets A and B are equal precisely when ∀x(x∈A ↔ x∈B). The axiom of extensionality ensures there is no hidden ordering or multiplicity in an ordinary set. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** With A={1,2,2} and B={2,1}, both have exactly the elements 1 and 2; A=B. The sequence (1,2,2) is different because its duplicate and order are retained. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Confusing membership of an element with equality of a displayed list. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Prove {x∈Z:x²=1}={−1,1}; then compare {1} with {{1}}. **Worked answer or proof outline:** For x∈Z, x²−1=(x−1)(x+1)=0 implies x=1 or −1. In contrast 1∈{1}, whereas {1}∈{{1}}; equality fails by extensionality. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Confusing membership of an element with equality of a displayed list.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: Scientific sample inventory: three labs submit overlapping identifiers. Verify duplicates, subsets, complements and all derived sample groups without inventing a universal set. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 1.2 — Membership, subset, and empty set

### Statement and formal objects

**Definition.** A⊆B abbreviates ∀x(x∈A→x∈B); A∈B asserts an entirely different relation. The empty set ∅ has no members and is a subset of every set. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** For A={∅,{∅}}, we have ∅∈A and {∅}∈A. Moreover ∅⊆A and {∅}⊆A, but A∉A in the displayed well-founded construction. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Replacing ∈ with ⊆ because both appear to mean “contained in.” Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** List each subset of {{a}} and state whether {a}∈{{a}} when a is an atom-like identifier. **Worked answer or proof outline:** The subsets are ∅ and {{a}}. Its sole element is {a}, so {a}∈{{a}}; a∈{{a}} is false unless a happens to equal {a}. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Replacing ∈ with ⊆ because both appear to mean “contained in.”** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: Scientific sample inventory: three labs submit overlapping identifiers. Verify duplicates, subsets, complements and all derived sample groups without inventing a universal set. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 1.3 — Union, intersection, difference, complement

### Statement and formal objects

**Definition.** A∪B={x:x∈A or x∈B}, A∩B={x:x∈A and x∈B}, A\B={x∈A:x∉B}. Complement U\A always depends on the chosen ambient set U. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** With U={1,2,3,4,5}, A={1,2,3}, B={3,4}, A∪B={1,2,3,4}, A∩B={3}, A\B={1,2}, U\A={4,5}. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Claiming an absolute complement without defining an enclosing universe. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Prove A\(B∪C)=(A\B)∩(A\C), then test an example with overlapping B and C. **Worked answer or proof outline:** Elementwise proof: x belongs to the left iff x∈A, x∉B and x∉C, precisely the right-hand condition. No counting assumption is needed. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Claiming an absolute complement without defining an enclosing universe.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: Scientific sample inventory: three labs submit overlapping identifiers. Verify duplicates, subsets, complements and all derived sample groups without inventing a universal set. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 1.4 — Power sets and Boolean structure

### Statement and formal objects

**Definition.** P(A)={X:X⊆A}. When A has n distinct elements, P(A) has 2^n elements. Union and intersection make P(A) a Boolean algebra with ∅ and A. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** For A={a,b}, P(A)={∅,{a},{b},{a,b}}. Notice ∅ is a member of P(A), but ∅ is not a member of A under this example. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Thinking the power set consists of the elements of A rather than all its subsets. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** For A={p,q,r}, list eight subsets and identify all sets in P(A) containing p. **Worked answer or proof outline:** There are 2³=8 subsets. Exactly four contain p: {p},{p,q},{p,r},{p,q,r}; decide independently for q and r. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Thinking the power set consists of the elements of A rather than all its subsets.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: Scientific sample inventory: three labs submit overlapping identifiers. Verify duplicates, subsets, complements and all derived sample groups without inventing a universal set. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 1.5 — Cartesian products and set identities

### Statement and formal objects

**Definition.** A×B={(a,b):a∈A,b∈B}. The Kuratowski definition (a,b)={{a},{a,b}} permits ordered pairs to be represented as sets while preserving coordinate order. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** For A={1,2}, B={x,y}, A×B has four ordered pairs. But B×A contains (x,1) instead of (1,x) and generally differs from A×B. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Assuming cartesian products commute because ordinary products of integers do. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Verify (A∪B)×C=(A×C)∪(B×C), and explain why A×∅=∅. **Worked answer or proof outline:** A pair (x,c) has x∈A∪B iff x∈A or x∈B. No pair has second coordinate in ∅, so A×∅ is empty. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Assuming cartesian products commute because ordinary products of integers do.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: Scientific sample inventory: three labs submit overlapping identifiers. Verify duplicates, subsets, complements and all derived sample groups without inventing a universal set. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Unit 1 integrative capstone — Sets, Membership, and Operations

**Project brief.** Scientific sample inventory: three labs submit overlapping identifiers. Verify duplicates, subsets, complements and all derived sample groups without inventing a universal set. Draft a mathematics-first specification. Begin with the minimum object vocabulary for the case: distinguish an element, a collection of elements, a relation, a function and a predicate where relevant. Then select at least two of the five lesson theorems or constructions and explain precisely how they apply. Include one counterexample to a tempting informal rule. A valid submission must not imply that a finite output validates an unlimited set-theoretic law.

**Proof deliverables.** 1. A source-set and ambient-universe declaration that resolves **what exact members does the definition permit?** 2. A worked calculation that can be independently repeated without external data. 3. A statement of whether the central result is an identity, an existence claim, an injection, a well-ordering argument, an induction theorem, or an independence statement. 4. An edge-case analysis respecting the warning: **Declare a fixed ambient universe whenever you take a complement. A power set requires a set as its input; a proper class cannot be treated as a permissible universal set.** 5. A final paragraph explaining what remains outside the proof.

**Marking rubric (100 points).** Exact mathematical objects and domains: 20. Correct use of definitions: 20. Verifiable worked argument: 25. Counterexample and limitations: 20. Clarity, notation and citation of background assumptions: 15. An answer loses foundational credit when it conflates a set and its element, treats a limited search as a universal result, assumes a function is invertible without proof, or omits a limit-stage or choice assumption that affects the result.

### Unit-level short examination

**Question A.** Compare the hypotheses and conclusions of **Extensionality and equality** and **Cartesian products and set identities**. Give a concrete condition under which the second topic requires extra reasoning not supplied by the first.

**Question B.** Rebuild a nontrivial example from scratch while changing the original numerical identifiers or relation table. Check the result using the same definition, and explain why the identity of the symbols does not matter when an isomorphism or renaming preserves the relevant structure.

**Question C.** State which named axiom or principle would justify an existence statement in the unit and which statements can be proved from definitions alone. Carefully separate the informal application from a statement inside classical set theory.

**Question D.** Identify one realistic reason a software implementation of this unit’s ideas could be wrong even if its core mathematics is sound; propose a test for the implementation without claiming that the test proves a theorem about infinity.

