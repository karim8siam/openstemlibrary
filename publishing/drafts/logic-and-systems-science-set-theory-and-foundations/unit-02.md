# Unit 2 — Relations, Functions, and Structures

**Core insight.** Relations are sets of tuples. Functions are special relations with an existence-and-uniqueness rule at every input in the domain.

**Running case.** A researcher matching platform represents eligibility as a binary relation, mentor assignment as a function, and equivalence of qualifications as a partition.

**Restriction.** A many-to-many eligibility graph is generally not a function. A partial map is a function only when its declared domain is restricted accordingly.

## Unit orientation: definition, construction, and evidence

Eligibility, mentorship and equivalence are not interchangeable even if they are all stored as database tables. Eligibility can be many-to-many; assignment can be a total or partial function; membership in a qualification class uses an equivalence relation; prerequisite ordering usually produces a partial order rather than a ranking.

To establish a function f:A→B, prove totality on A and unique output in B. To establish injectivity, derive x=y from f(x)=f(y). To establish surjectivity, take arbitrary y∈B and construct x∈A mapping to it. These checks have distinct failures; an algorithm can pass the first two and still omit some codomain elements.

A quotient collapses multiple elements into one class, but equivalence classes do not mix arbitrarily. If two classes overlap at one element, symmetry and transitivity force them to coincide. This is why classes constitute a partition rather than merely a family of intersecting clusters.

**Three questions before working.** (1) What is the declared domain and what is the codomain? (2) Does the relation satisfy the global rule or merely some of its instances? (3) Which property fails first under a minimal counterexample?

The unit is organized in a deliberate sequence. Start with a definition; derive consequences by matching the definition to its quantifiers; construct a worked finite or symbolic case; and then search for a boundary case. Mathematics offers different kinds of evidence. A direct proof establishes a result for all objects in the stated domain; a counterexample disproves such a result; an example only illustrates it. The accompanying model visualizations are transparent local computations. They can reveal errors and motivate a proof, but cannot establish set-theoretic independence, consistency, or claims about every possible infinite structure.

### Common vocabulary and a formal audit

In this unit, the word *construction* means a legitimate definition of an object in the chosen system, not just an algorithm that prints a plausible string. The running case is **A researcher matching platform represents eligibility as a binary relation, mentor assignment as a function, and equivalence of qualifications as a partition.** A complete mathematical account begins by stating the source sets and background theory. Next specify what is asserted to exist, what equality means for these objects, and what properties need proof. Finally separate any domain facts collected from outside the mathematics. The last separation matters because an algorithm can be logically correct yet operate on incomplete or incorrectly classified entries.

A quick error audit starts from the restriction: **A many-to-many eligibility graph is generally not a function. A partial map is a function only when its declared domain is restricted accordingly.** Try to invent a minimal counterexample to a stronger-sounding but invalid statement. If the counterexample is finite, list each member or ordered pair explicitly. If the statement concerns infinity or axioms, name the exact principle that would be required. Giving the missing hypothesis is a mathematically useful response: it tells the reader how the claim could be repaired without pretending it was already proved.

## Lesson 2.1 — Relations as sets of ordered pairs

### Statement and formal objects

**Definition.** A binary relation R from A to B is any subset of A×B. Its domain is {a∈A:∃b(a,b)∈R} and range {b∈B:∃a(a,b)∈R}. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Let A={1,2,3}, B={x,y}, R={(1,x),(2,x),(2,y)}. Domain(R)={1,2}, range(R)={x,y}; 3 has no outgoing pair. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Calling a relation a total function because some pairs appear for every selected item in a sample. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Give a relation on A={0,1,2} that is symmetric but not transitive. **Worked answer or proof outline:** Use R={(0,1),(1,0),(1,2),(2,1)}. Symmetry holds; (0,1) and (1,2) would require (0,2) for transitivity, which is missing. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Calling a relation a total function because some pairs appear for every selected item in a sample.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A researcher matching platform represents eligibility as a binary relation, mentor assignment as a function, and equivalence of qualifications as a partition. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 2.2 — Reflexivity, symmetry, transitivity

### Statement and formal objects

**Definition.** For R⊆A×A: reflexivity requires (a,a) for all a; symmetry requires aRb⇒bRa; transitivity requires aRb∧bRc⇒aRc. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** On A={a,b}, R={(a,a),(b,b),(a,b)} is reflexive and transitive but not symmetric; the reverse edge (b,a) is absent. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Confusing antisymmetry with failure of symmetry. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Assess R={(a,a),(a,b),(b,b)} for reflexivity, antisymmetry, and transitivity. **Worked answer or proof outline:** It is a partial order: each diagonal exists, no distinct pair points in both directions, and all possible length-two compositions are already present. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Confusing antisymmetry with failure of symmetry.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A researcher matching platform represents eligibility as a binary relation, mentor assignment as a function, and equivalence of qualifications as a partition. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 2.3 — Equivalence relations and quotient sets

### Statement and formal objects

**Definition.** An equivalence relation is reflexive, symmetric and transitive. For a∈A, [a]={x∈A:x~a}; equivalence classes partition A and each partition induces an equivalence relation. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Define x~y on Z when x−y is divisible by 3. The classes [0],[1],[2] exhaust Z and are pairwise disjoint. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Treating “similar to” as an equivalence without testing transitivity. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** On students with same final grade, explain why the relation is an equivalence even if some students are personally unrelated. **Worked answer or proof outline:** Equal grades are reflexive, symmetric and transitive. The quotient groups students by grade value; the relation makes no claim about friendships. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Treating “similar to” as an equivalence without testing transitivity.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A researcher matching platform represents eligibility as a binary relation, mentor assignment as a function, and equivalence of qualifications as a partition. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 2.4 — Orders, bounds, and chains

### Statement and formal objects

**Definition.** A partial order is reflexive, antisymmetric and transitive. A chain has comparable elements; an upper bound of S satisfies s≤u for all s∈S; a greatest element belongs to S and dominates it. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** In P({a,b}) ordered by inclusion, {a} and {b} are incomparable; {a,b} is their least upper bound and ∅ their greatest lower bound. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Assuming every partially ordered set is a linear order, or that maximal means greatest. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Produce two incomparable maximal elements in a poset and show it has no greatest element. **Worked answer or proof outline:** On {{a},{b}} ordered by inclusion, both elements are maximal, neither contains the other; there is no greatest element inside that poset. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Assuming every partially ordered set is a linear order, or that maximal means greatest.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A researcher matching platform represents eligibility as a binary relation, mentor assignment as a function, and equivalence of qualifications as a partition. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 2.5 — Functions, images, and inverse images

### Statement and formal objects

**Definition.** A function f:A→B is a relation assigning exactly one value in B to each a∈A. The image f[S]={f(x):x∈S}; preimage f⁻¹[T]={x∈A:f(x)∈T} need not assume f invertible. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Let f:Z→Z be f(x)=x². Then f[{−2,−1,0,1,2}]={0,1,4}, and f⁻¹[{1,4}]={−2,−1,1,2}. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Writing f⁻¹(y) as an inverse function when the original f is not injective. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Find f⁻¹[{0,1}] and show f[X∩Y] need not equal f[X]∩f[Y]. **Worked answer or proof outline:** Preimage is {−1,0,1}. For X={−1}, Y={1}, X∩Y=∅ yet f[X]∩f[Y]={1}; equality fails. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Writing f⁻¹(y) as an inverse function when the original f is not injective.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A researcher matching platform represents eligibility as a binary relation, mentor assignment as a function, and equivalence of qualifications as a partition. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Unit 2 integrative capstone — Relations, Functions, and Structures

**Project brief.** A researcher matching platform represents eligibility as a binary relation, mentor assignment as a function, and equivalence of qualifications as a partition. Draft a mathematics-first specification. Begin with the minimum object vocabulary for the case: distinguish an element, a collection of elements, a relation, a function and a predicate where relevant. Then select at least two of the five lesson theorems or constructions and explain precisely how they apply. Include one counterexample to a tempting informal rule. A valid submission must not imply that a finite output validates an unlimited set-theoretic law.

**Proof deliverables.** 1. A source-set and ambient-universe declaration that resolves **what is the declared domain and what is the codomain?** 2. A worked calculation that can be independently repeated without external data. 3. A statement of whether the central result is an identity, an existence claim, an injection, a well-ordering argument, an induction theorem, or an independence statement. 4. An edge-case analysis respecting the warning: **A many-to-many eligibility graph is generally not a function. A partial map is a function only when its declared domain is restricted accordingly.** 5. A final paragraph explaining what remains outside the proof.

**Marking rubric (100 points).** Exact mathematical objects and domains: 20. Correct use of definitions: 20. Verifiable worked argument: 25. Counterexample and limitations: 20. Clarity, notation and citation of background assumptions: 15. An answer loses foundational credit when it conflates a set and its element, treats a limited search as a universal result, assumes a function is invertible without proof, or omits a limit-stage or choice assumption that affects the result.

### Unit-level short examination

**Question A.** Compare the hypotheses and conclusions of **Relations as sets of ordered pairs** and **Functions, images, and inverse images**. Give a concrete condition under which the second topic requires extra reasoning not supplied by the first.

**Question B.** Rebuild a nontrivial example from scratch while changing the original numerical identifiers or relation table. Check the result using the same definition, and explain why the identity of the symbols does not matter when an isomorphism or renaming preserves the relevant structure.

**Question C.** State which named axiom or principle would justify an existence statement in the unit and which statements can be proved from definitions alone. Carefully separate the informal application from a statement inside classical set theory.

**Question D.** Identify one realistic reason a software implementation of this unit’s ideas could be wrong even if its core mathematics is sound; propose a test for the implementation without claiming that the test proves a theorem about infinity.

