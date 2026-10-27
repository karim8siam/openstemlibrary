# Unit 3 — Natural Numbers and Inductive Constructions

**Core insight.** Set-theoretic natural numbers admit recursion and induction, but the precise definition of the number system and the proof obligations must be given.

**Running case.** A laboratory numbering convention starts from the empty set, constructs finite ordinals, and uses induction to certify batch-count formulas.

**Restriction.** Checking the first five cases is not induction; an induction proof establishes the initial step and a universally applicable successor step.

## Unit orientation: definition, construction, and evidence

Counting can be treated axiomatically or via canonical sets. The von Neumann convention makes each natural number contain its predecessors. It is a representation supported by set-theoretic axioms, not evidence that familiar arithmetic arose historically by writing nested braces.

A genuine induction argument has a dependency: the successor case must derive P(n+1) assuming P(n) for an arbitrary n. A list of numerical checks, no matter how long, can be fooled by a claim engineered to fail outside that range. This is a general verification lesson for mathematics and software testing.

Recursion must identify a base object, an operation that computes the next stage, and a theorem guaranteeing uniqueness. If the “next stage” requires a value not already assigned, the definition may be circular rather than recursive. For the natural numbers, the well-ordered succession makes the dependency legitimate.

**Three questions before working.** (1) What is the initial object and the successor construction? (2) Where is the induction hypothesis actually applied? (3) Would the argument still work if the defining operation were not uniquely specified?

The unit is organized in a deliberate sequence. Start with a definition; derive consequences by matching the definition to its quantifiers; construct a worked finite or symbolic case; and then search for a boundary case. Mathematics offers different kinds of evidence. A direct proof establishes a result for all objects in the stated domain; a counterexample disproves such a result; an example only illustrates it. The accompanying model visualizations are transparent local computations. They can reveal errors and motivate a proof, but cannot establish set-theoretic independence, consistency, or claims about every possible infinite structure.

### Common vocabulary and a formal audit

In this unit, the word *construction* means a legitimate definition of an object in the chosen system, not just an algorithm that prints a plausible string. The running case is **A laboratory numbering convention starts from the empty set, constructs finite ordinals, and uses induction to certify batch-count formulas.** A complete mathematical account begins by stating the source sets and background theory. Next specify what is asserted to exist, what equality means for these objects, and what properties need proof. Finally separate any domain facts collected from outside the mathematics. The last separation matters because an algorithm can be logically correct yet operate on incomplete or incorrectly classified entries.

A quick error audit starts from the restriction: **Checking the first five cases is not induction; an induction proof establishes the initial step and a universally applicable successor step.** Try to invent a minimal counterexample to a stronger-sounding but invalid statement. If the counterexample is finite, list each member or ordered pair explicitly. If the statement concerns infinity or axioms, name the exact principle that would be required. Giving the missing hypothesis is a mathematically useful response: it tells the reader how the claim could be repaired without pretending it was already proved.

## Lesson 3.1 — Finite ordinals and the von Neumann naturals

### Statement and formal objects

**Definition.** Define 0=∅ and n+1=n∪{n}; thus 1={0}, 2={0,1}, 3={0,1,2}. For natural ordinals, m<n precisely when m∈n. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Expand 3= {∅,{∅},{∅,{∅}}}. The members of 3 are exactly 0,1,2, reflecting the predecessors of 3. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Treating the numeral 3 as a primitive symbol rather than a canonical set representation within the construction. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Write 4 as a set of its predecessors and verify 2∈4 but 4∉2. **Worked answer or proof outline:** By the successor definition, 4={0,1,2,3}. Since 2 is one of its members, 2∈4; 4 cannot be an earlier ordinal member of 2. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Treating the numeral 3 as a primitive symbol rather than a canonical set representation within the construction.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A laboratory numbering convention starts from the empty set, constructs finite ordinals, and uses induction to certify batch-count formulas. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 3.2 — Infinity and the smallest inductive set

### Statement and formal objects

**Definition.** A set I is inductive when ∅∈I and x∈I⇒x∪{x}∈I. The axiom of infinity gives at least one inductive set; ω is the intersection of all inductive subsets of a suitable I. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Given any inductive I, every finite ordinal 0,1,2,... belongs to I. Defining ω as the minimal inductive subset makes induction and arithmetic possible. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Assuming the existence of an infinite set follows from the other basic ZF formation axioms without using infinity. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Explain why ω is inductive and why every inductive set contains ω. **Worked answer or proof outline:** Zero belongs to every inductive set and successors are preserved; the intersection construction preserves both properties. Minimality follows directly from membership in every inductive set. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Assuming the existence of an infinite set follows from the other basic ZF formation axioms without using infinity.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A laboratory numbering convention starts from the empty set, constructs finite ordinals, and uses induction to certify batch-count formulas. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 3.3 — Ordinary mathematical induction

### Statement and formal objects

**Definition.** To prove ∀n∈ω P(n), show P(0) and ∀n(P(n)⇒P(n+1)); the induction principle follows from minimality of ω. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** For S(n)=0+1+⋯+n, base S(0)=0. If S(n)=n(n+1)/2, adding n+1 gives S(n+1)=(n+1)(n+2)/2. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Extrapolating after testing n=0,1,2 without proving the successor implication. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Inductively show 1+3+⋯+(2n−1)=n² for all n≥1. **Worked answer or proof outline:** Base n=1 is 1=1². Step adds 2(n+1)−1=2n+1 to n² and yields (n+1)². Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Extrapolating after testing n=0,1,2 without proving the successor implication.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A laboratory numbering convention starts from the empty set, constructs finite ordinals, and uses induction to certify batch-count formulas. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 3.4 — Strong induction and minimal counterexample

### Statement and formal objects

**Definition.** Strong induction assumes P(k) for every k<n when proving P(n). It is equivalent to ordinary induction for statements over ω, not a stronger axiom. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Every integer n≥2 factors into primes: either n is prime, or n=ab with 2≤a,b<n; by strong induction both factors split into primes. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Appealing to strong induction while allowing factors equal to n, thereby making the reasoning circular. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Show every positive integer is expressible as a sum of distinct powers of two. **Worked answer or proof outline:** Take the largest power 2^k≤n. The remainder r=n−2^k is smaller than 2^k; induct on r and ensure no repeated use of 2^k. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Appealing to strong induction while allowing factors equal to n, thereby making the reasoning circular.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A laboratory numbering convention starts from the empty set, constructs finite ordinals, and uses induction to certify batch-count formulas. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Lesson 3.5 — Primitive recursion and arithmetic

### Statement and formal objects

**Definition.** A recursion theorem on ω provides a unique f from an initial value a and a step rule F. Addition and multiplication arise by recursive equations on a chosen argument. The object under discussion is not a mere metaphor: its elements, domain, equality condition, and allowable constructions determine what can be deduced. In particular, a statement with a universal quantifier must be justified for every member of its stated domain. A statement of existence requires an actual object or a valid existence theorem. Wherever notation abbreviates a more detailed membership claim, unfold it before applying a familiar algebraic rule.

### Fully worked example

**Worked case.** Define n+0=n and n+S(m)=S(n+m). Then 2+2=S(2+1)=S(S(2+0))=4; multiplication follows by n·0=0, n·S(m)=n·m+n. To check this example, first record exactly the input set or structure. Then perform each step under the definition rather than under a visual intuition. If the result is a set, an elementwise membership test is the primary certificate; if it is a map, check both uniqueness and totality; if it is a formal theorem, identify the inference used. The example shows the stated calculation in this setting. It does not, by itself, justify replacing finite inputs with arbitrary infinite ones.

**A tempting error.** Treating recursion as circular because the value at n+1 refers to the already defined value at n. Diagnose it by writing the disputed expression and the legal definition next to each other. Test a small counterexample when one exists; otherwise state the missing justification. A successful correction is not simply a more forceful verbal explanation. It should alter a quantified claim, a domain declaration, an equality condition, or a proof step that has been shown to be wrong. If the same error can survive the revised formulation, the repair is not complete.

### Three graded exercises and answer guidance

**Exercise 1 — derive.** Derive 3·2 using multiplication recursion and justify that the rules determine a unique output. **Worked answer or proof outline:** 3·2=3·1+3=(3·0+3)+3=6. Uniqueness comes from recursion over the well-ordered natural index. Check each intermediate membership or mapping fact. If more than one construction is possible, explain what property the chosen one has that matters for the problem. A good answer can be verified by somebody who does not know the intended conclusion in advance: the definition and the visible steps suffice.

**Exercise 2 — find a countercase.** Analyze the claim implicit in the mistake: **Treating recursion as circular because the value at n+1 refers to the already defined value at n.** Construct the smallest useful finite case or supply an axiom-level diagnosis. **Answer check:** the proposed failure must share the same domain and hypotheses as the original claim. A picture with omitted cases is not a counterexample. When no counterexample is appropriate because the result is itself a theorem, explain why the attempted move is invalid without asserting a fabricated example. Describe which condition is essential to the valid statement.

**Exercise 3 — transfer.** Apply the definition to the unit project: A laboratory numbering convention starts from the empty set, constructs finite ordinals, and uses induction to certify batch-count formulas. Start by assigning mathematical types to the represented objects, then state whether the operation being requested preserves those types. **Answer check:** identify one ordinary input and one edge case, such as an empty relation, duplicate identifier, missing output, undefined ambient set or a new ordinal stage. If a conclusion depends on a model of real-world data, state that dependency; do not silently turn a record-management decision into a set-theoretic fact.

## Unit 3 integrative capstone — Natural Numbers and Inductive Constructions

**Project brief.** A laboratory numbering convention starts from the empty set, constructs finite ordinals, and uses induction to certify batch-count formulas. Draft a mathematics-first specification. Begin with the minimum object vocabulary for the case: distinguish an element, a collection of elements, a relation, a function and a predicate where relevant. Then select at least two of the five lesson theorems or constructions and explain precisely how they apply. Include one counterexample to a tempting informal rule. A valid submission must not imply that a finite output validates an unlimited set-theoretic law.

**Proof deliverables.** 1. A source-set and ambient-universe declaration that resolves **what is the initial object and the successor construction?** 2. A worked calculation that can be independently repeated without external data. 3. A statement of whether the central result is an identity, an existence claim, an injection, a well-ordering argument, an induction theorem, or an independence statement. 4. An edge-case analysis respecting the warning: **Checking the first five cases is not induction; an induction proof establishes the initial step and a universally applicable successor step.** 5. A final paragraph explaining what remains outside the proof.

**Marking rubric (100 points).** Exact mathematical objects and domains: 20. Correct use of definitions: 20. Verifiable worked argument: 25. Counterexample and limitations: 20. Clarity, notation and citation of background assumptions: 15. An answer loses foundational credit when it conflates a set and its element, treats a limited search as a universal result, assumes a function is invertible without proof, or omits a limit-stage or choice assumption that affects the result.

### Unit-level short examination

**Question A.** Compare the hypotheses and conclusions of **Finite ordinals and the von Neumann naturals** and **Primitive recursion and arithmetic**. Give a concrete condition under which the second topic requires extra reasoning not supplied by the first.

**Question B.** Rebuild a nontrivial example from scratch while changing the original numerical identifiers or relation table. Check the result using the same definition, and explain why the identity of the symbols does not matter when an isomorphism or renaming preserves the relevant structure.

**Question C.** State which named axiom or principle would justify an existence statement in the unit and which statements can be proved from definitions alone. Carefully separate the informal application from a statement inside classical set theory.

**Question D.** Identify one realistic reason a software implementation of this unit’s ideas could be wrong even if its core mathematics is sound; propose a test for the implementation without claiming that the test proves a theorem about infinity.

