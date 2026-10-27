# Unit 8 — Realizations, Models, and Proof Audits

**Core insight.** Set-theoretic definitions support analysis, computing and structural mathematics; reliable reasoning also recognizes independence and formal-system limits.

**Running case.** A STEM repository tries to standardize real-number encodings, graph relations and formal claims about infinite objects. Separate representation from underlying mathematics.

**Restriction.** An accurate computation of finite examples is not a proof of a theorem about all sets. Statements of independence need explicit theories and assumptions.

## Unit orientation: definition, construction, and evidence

Constructing real numbers from rational approximations requires identifying when two representations encode the same object. A Cauchy-sequence quotient demands a carefully defined equivalence relation and a proof that arithmetic respects it. Simply storing approximations in floating-point form skips these foundational tasks.

A graph may be encoded as a pair of sets or as relations inside a larger system; its exact encoding is rarely the most important practical property. Mathematical structure is preserved under suitable isomorphisms, while a software serialization imposes additional decisions about identifiers and storage.

When publishing an educational proof or computation, label evidence honestly: tested instance, counterexample, general theorem, or statement independent relative to an axiom system. A reader should never have to guess which kind of support backs a claim. This principle is essential when interactive visuals accompany logic and set theory.

**Three questions before working.** (1) Is the mathematical object being confused with its chosen encoding? (2) What invariant connects the implementation to the definition? (3) Does the claim require a proof beyond finite tests?

The unit is organized in a deliberate sequence. Start with a definition; derive consequences by matching the definition to its quantifiers; construct a worked finite or symbolic case; and then search for a boundary case. Mathematics offers different kinds of evidence. A direct proof establishes a result for all objects in the stated domain; a counterexample disproves such a result; an example only illustrates it. The accompanying model visualizations are transparent local computations. They can reveal errors and motivate a proof, but cannot establish set-theoretic independence, consistency, or claims about every possible infinite structure.

### Common vocabulary and a formal audit

In this unit, the word *construction* means a legitimate definition of an object in the chosen system, not just an algorithm that prints a plausible string. The running case is **A STEM repository tries to standardize real-number encodings, graph relations and formal claims about infinite objects. Separate representation from underlying mathematics.** A complete mathematical account begins by stating the source sets and background theory. Next specify what is asserted to exist, what equality means for these objects, and what properties need proof. Finally separate any domain facts collected from outside the mathematics. The last separation matters because an algorithm can be logically correct yet operate on incomplete or incorrectly classified entries.

A quick error audit starts from the restriction: **An accurate computation of finite examples is not a proof of a theorem about all sets. Statements of independence need explicit theories and assumptions.** Try to invent a minimal counterexample to a stronger-sounding but invalid statement. If the counterexample is finite, list each member or ordered pair explicitly. If the statement concerns infinity or axioms, name the exact principle that would be required. Giving the missing hypothesis is a mathematically useful response: it tells the reader how the claim could be repaired without pretending it was already proved.

## Lesson 8.1 — Real numbers via cuts and Cauchy sequences

### Statement and formal objects

**Definition.** The real line can be constructed from suitable Dedekind cuts of Q or equivalence classes of rational Cauchy sequences. Either route demands a precise equivalence and completeness argument. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** The rational approximations 1,1.4,1.41,... suggest √2 but the limit is not a rational fraction. A Cauchy-sequence construction supplies an object representing that limit. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Defining the reals as decimal notation and assuming representation ambiguities settle themselves. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Sketch an equivalence condition on two rational Cauchy sequences representing the same real. **Worked answer or proof outline:** Two Cauchy sequences (a_n),(b_n) are equivalent when a_n−b_n→0; the quotient identifies different rational approximation schemes. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Defining the reals as decimal notation and assuming representation ambiguities settle themselves.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A STEM repository tries to standardize real-number encodings, graph relations and formal claims about infinite objects. Separate representation from underlying mathematics. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 8.2 — Sequences, function spaces, and products

### Statement and formal objects

**Definition.** A^I denotes the set of functions I→A. A sequence in A is an element of A^N; an infinite product captures coordinated choices indexed by an infinite set. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Finite strings in {0,1}^{<ω} are countable, while infinite sequences {0,1}^N have the cardinality of P(N) by mapping s to {n:s(n)=1}. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Collapsing the union over finite lengths with the set of all infinite sequences. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Give inverse maps between subsets S⊆N and characteristic sequences χ_S∈{0,1}^N. **Worked answer or proof outline:** Set χ_S(n)=1 exactly for n∈S. Recover S={n:χ_S(n)=1}; the constructions are mutually inverse. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Collapsing the union over finite lengths with the set of all infinite sequences.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A STEM repository tries to standardize real-number encodings, graph relations and formal claims about infinite objects. Separate representation from underlying mathematics. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 8.3 — Graphs, quotient types, and structure

### Statement and formal objects

**Definition.** Graph theory can encode vertices and edges as sets. Quotients identify elements under equivalence; the properties of the quotient depend on proving the relation is an equivalence. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** A network with vertex set V and edge relation E⊆V×V can be directed or undirected. Connected components of an undirected graph form equivalence classes under path connectivity. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Calling an edge relation itself an equivalence: a single direct edge need not be transitive. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** For V={a,b,c} and edges a–b and b–c, compare direct adjacency with path connectivity. **Worked answer or proof outline:** a and c are not adjacent, but a path a–b–c connects them. Connectivity is transitive when paths can be concatenated. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Calling an edge relation itself an equivalence: a single direct edge need not be transitive.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A STEM repository tries to standardize real-number encodings, graph relations and formal claims about infinite objects. Separate representation from underlying mathematics. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 8.4 — Finite representations and proof obligations

### Statement and formal objects

**Definition.** A finite encoding is an implementation of a mathematical definition, not the object itself. To justify an algorithm, prove a specification invariant and distinguish termination from correctness. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** A program enumerates P({a,b,c}) by looping over masks 000,...,111. The invariant maps one mask to exactly one subset; 2³=8 total masks guarantee completeness without duplicates. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Inferring a theorem about arbitrary infinite sets from a finite exhaustive search over small cardinalities. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Describe a correct finite powerset algorithm and state which part of the result remains valid for infinite sets. **Worked answer or proof outline:** Every subset corresponds to one binary membership assignment for finite A. The general cardinal theorem requires Cantor’s argument; finite enumeration does not extend directly. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Inferring a theorem about arbitrary infinite sets from a finite exhaustive search over small cardinalities.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A STEM repository tries to standardize real-number encodings, graph relations and formal claims about infinite objects. Separate representation from underlying mathematics. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 8.5 — Proof auditing and independent claims

### Statement and formal objects

**Definition.** Foundational claims must say which axioms, representations and logical rules are being used. Verified computation, derivation, relative consistency, and independence are different evidence types. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** An educational tool reports “the continuum hypothesis was validated on sets of size at most 12.” That sentence is categorically misleading: CH concerns infinite cardinals, not small finite examples. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Using impressive runtime logs as a replacement for an argument at the necessary mathematical level. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Design a checklist for any digital demonstration purporting to establish a theorem about infinite structures. **Worked answer or proof outline:** Record formal statement and background theory; verify implementation of finite case; identify whether a finite counterexample is relevant; demand a general proof or an appropriately cited independence theorem. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Using impressive runtime logs as a replacement for an argument at the necessary mathematical level.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A STEM repository tries to standardize real-number encodings, graph relations and formal claims about infinite objects. Separate representation from underlying mathematics. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Unit 8 integrative capstone — Realizations, Models, and Proof Audits

**Project brief.** A STEM repository tries to standardize real-number encodings, graph relations and formal claims about infinite objects. Separate representation from underlying mathematics. Draft a mathematics-first specification. Begin with the minimum object vocabulary for the case: distinguish an element, a collection of elements, a relation, a function and a predicate where relevant. Then select at least two of the five lesson theorems or constructions and explain precisely how they apply. Include one counterexample to a tempting informal rule. A valid submission must not imply that a finite output validates an unlimited set-theoretic law.

**Proof deliverables.** 1. A source-set and ambient-universe declaration that resolves **is the mathematical object being confused with its chosen encoding?** 2. A worked calculation that can be independently repeated without external data. 3. A statement of whether the central result is an identity, an existence claim, an injection, a well-ordering argument, an induction theorem, or an independence statement. 4. An edge-case analysis respecting the warning: **An accurate computation of finite examples is not a proof of a theorem about all sets. Statements of independence need explicit theories and assumptions.** 5. A final paragraph explaining what remains outside the proof.

**Marking rubric (100 points).** Exact mathematical objects and domains: 20. Correct use of definitions: 20. Verifiable worked argument: 25. Counterexample and limitations: 20. Clarity, notation and citation of background assumptions: 15. An answer loses foundational credit when it conflates a set and its element, treats a limited search as a universal result, assumes a function is invertible without proof, or omits a limit-stage or choice assumption that affects the result.

### Unit-level short examination

**Question A.** Compare the hypotheses and conclusions of **Real numbers via cuts and Cauchy sequences** and **Proof auditing and independent claims**. Give a concrete condition under which the second topic requires extra reasoning not supplied by the first.

**Question B.** Rebuild a nontrivial example from scratch while changing the original numerical identifiers or relation table. Check the result using the same definition, and explain why the identity of the symbols does not matter when an isomorphism or renaming preserves the relevant structure.

**Question C.** State which named axiom or principle would justify an existence statement in the unit and which statements can be proved from definitions alone. Carefully separate the informal application from a statement inside classical set theory.

**Question D.** Identify one realistic reason a software implementation of this unit’s ideas could be wrong even if its core mathematics is sound; propose a test for the implementation without claiming that the test proves a theorem about infinity.

