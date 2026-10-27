# Unit 3: Structures and Compositional Semantics

**Learning destination.** Evaluate terms and formulas using nonempty domains, interpretations of symbols, variable assignments, and recursive semantic clauses.

**Guiding principle.** Satisfaction is defined relative to a structure and, for open formulas, an assignment; truth of a sentence needs no external variable assignment.

**Running case.** A two-researcher model has several supervisor relations. Use its explicit relation table to determine whether each quantified assertion holds.

## Conceptual orientation

A useful way to begin this unit is to resist writing symbols immediately. Construct a finite structure as tables, then evaluate terms before formulas. The first draft of any formal problem must identify what counts as an input, an allowed operation, a result, and an error. A two-researcher model has several supervisor relations. Use its explicit relation table to determine whether each quantified assertion holds. If two readers obtain different formal sentences from the same English claim, the disagreement is often visible before either attempts a proof. A good analyst preserves both candidate translations until the intended interpretation can be resolved. The symbols do not decide the institutional meaning on their own.

In a complete solution: for each quantifier, update the assignment for only its bound variable and recursively check the body; preserve all other variable values. The student should also be able to explain what this particular workflow cannot establish. A semantic test passes when a witness, falsifying element, or complete table is visible and consistent with the declared interpretation. Truth in one structure is not validity across all structures. These are not decorative limitations; they tell an independent reader when a result is strong enough to reuse and when it should remain a hypothesis pending additional evidence.

## Diagnostic pretest

Take the following situation in isolation: A two-researcher model has several supervisor relations. Use its explicit relation table to determine whether each quantified assertion holds. State three things that are known, two things that would need additional facts, and one piece of evidence that could falsify a tempting interpretation. Label each claim as *syntax*, *truth in a model*, *derivability*, *semantic consequence*, or *external factual premise*. If you cannot confidently assign a label, carry the question into the individual lessons rather than quietly collapsing the categories. A convincing formal report will make uncertainty legible.

## Lesson 3.1: Domains and interpretations

### Core definition and significance

A first-order structure assigns nonlogical meaning: a nonempty domain, an element to each constant, a function on the domain to each function symbol, and a relation of the correct arity to each predicate. Logical symbols have their fixed semantics. 

### Exact symbolic object and derivation

The central formal object is `M=(D,I); D={a,b}; I(P)={a}`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Let D={a,b}, P={a}, and c interpreted as a. Then P(c) is true and ∀xP(x) false. Reinterpreting c as b changes P(c) but not the truth of the universal sentence. 

### Why the distinction matters

One common failure is **Confusing the name of a constant with its denoted domain object.** 

**Boundary probe.** The same abstract formula can be true in one structure and false in another without logical contradiction. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Create a tiny data model with projects p1,p2 and a set of accepted projects. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `M=(D,I); D={a,b}; I(P)={a}` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Confusing the name of a constant with its denoted domain object.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Create a tiny data model with projects p1,p2 and a set of accepted projects. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “The same abstract formula can be true in one structure and false in another without logical contradiction.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 3.2: Relations, arity, and tuples

### Core definition and significance

A binary predicate is interpreted as a set of ordered pairs. A relation may be reflexive, symmetric, transitive, or none of these; such properties come from explicit axioms or recorded tuples, not from the English name “collaborates.” 

### Exact symbolic object and derivation

The central formal object is `I(R)⊆D×D; R(a,b) not necessarily R(b,a)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** For D={a,b}, let R={(a,b)}. R(a,b) is true but R(b,a) is false. ∀xR(x,x) is false. Symmetry fails, and adding (b,a) fixes that one condition without necessarily adding either self-loop. 

### Why the distinction matters

One common failure is **Assuming that all relations that sound mutual are represented as symmetric.** 

**Boundary probe.** A graph view is a visual encoding of selected tuples, not evidence that a chosen relation is actually complete. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Test whether research mentorship, collaboration, and supervision require different relation properties. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `I(R)⊆D×D; R(a,b) not necessarily R(b,a)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Assuming that all relations that sound mutual are represented as symmetric.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Test whether research mentorship, collaboration, and supervision require different relation properties. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A graph view is a visual encoding of selected tuples, not evidence that a chosen relation is actually complete.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 3.3: Constants and function symbols

### Core definition and significance

A total function symbol must map each n-tuple of domain elements to exactly one domain element. Real-world “supervisor of” may be partial or multivalued and therefore cannot automatically be represented by a total unary function without extra modeling assumptions. 

### Exact symbolic object and derivation

The central formal object is `f:D→D; f(c) denotes an element, not a truth value`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** For D={a,b}, c=a, f(a)=b and f(b)=b. f(f(c))=b. If f models a “primary mentor” and an applicant lacks a mentor, the model needs a sentinel object, restricted domain, or a relation rather than a total function. 

### Why the distinction matters

One common failure is **Declaring a function even when the intended relation returns zero or multiple values.** 

**Boundary probe.** A domain extension can preserve the grammar while changing the truth of formulas containing function terms. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Compare one-to-many supervision with a declared single primary contact. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `f:D→D; f(c) denotes an element, not a truth value` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Declaring a function even when the intended relation returns zero or multiple values.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Compare one-to-many supervision with a declared single primary contact. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A domain extension can preserve the grammar while changing the truth of formulas containing function terms.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 3.4: Assignments and open formulas

### Core definition and significance

An open formula is evaluated under a variable assignment. Only sentences—formulas without free variables—have truth independent of assignments for a fixed structure. Updating an assignment for the bound variable is central to quantifier semantics. 

### Exact symbolic object and derivation

The central formal object is `M,s ⊨ R(x,c); s(x)=a`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** With R={(a,b)}, c=b: R(x,c) is true under s(x)=a and false under s(x)=b. But ∃xR(x,c) is true under every assignment of unrelated variables, since a is an available witness. 

### Why the distinction matters

One common failure is **Saying R(x,c) is simply true without naming the value of x.** 

**Boundary probe.** The distinction between formulas and sentences matters whenever a system stores partially filled logical templates. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Inspect an API rule template before and after its user parameter is supplied. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `M,s ⊨ R(x,c); s(x)=a` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Saying R(x,c) is simply true without naming the value of x.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Inspect an API rule template before and after its user parameter is supplied. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “The distinction between formulas and sentences matters whenever a system stores partially filled logical templates.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 3.5: Recursive satisfaction clauses

### Core definition and significance

Semantics is defined by recursion on formula structure. For conjunction both conjuncts must hold; for negation the embedded formula must fail; for a universal quantifier every assignment update must satisfy the body. 

### Exact symbolic object and derivation

The central formal object is `M,s⊨∀xφ iff for every d∈D, M,s[x↦d]⊨φ`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Let D={a,b}, P={a}. To test ∀x(P(x)→Q(x)), evaluate the body with x=a then x=b. If Q={a}, the first implication holds and the second has false antecedent, so the universal is true; ∀xQ(x) is false. 

### Why the distinction matters

One common failure is **Testing only objects in P and claiming to have verified ∀xQ(x).** 

**Boundary probe.** This executable recursion establishes truth only for the supplied finite structure, not validity in all structures. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Write an exact finite evaluator that displays each quantified substitution. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `M,s⊨∀xφ iff for every d∈D, M,s[x↦d]⊨φ` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Testing only objects in P and claiming to have verified ∀xQ(x).” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Write an exact finite evaluator that displays each quantified substitution. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “This executable recursion establishes truth only for the supplied finite structure, not validity in all structures.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Unit 3 capstone — independent specification review

**Case study.** A two-researcher model has several supervisor relations. Use its explicit relation table to determine whether each quantified assertion holds. Produce a two-page formal reasoning memo. The opening paragraph must distinguish the original communication from the interpretation chosen for checking. Provide the signature with arities, a formula or axiom set, and at least two tests: one representative positive interpretation and one boundary or negative interpretation. When claiming an entailment, include a valid derivation or a checked countermodel. State exactly which hypotheses are independent of the formal result and how the real project would validate them. Conclude by explaining how the result would change if a key premise were relaxed.

**Evidence standard.** Construct a finite structure as tables, then evaluate terms before formulas. For each quantifier, update the assignment for only its bound variable and recursively check the body; preserve all other variable values. A semantic test passes when a witness, falsifying element, or complete table is visible and consistent with the declared interpretation. Truth in one structure is not validity across all structures. A good submission includes a machine-readable artifact where practical: a tiny truth table, predicate relation matrix, proof trace, or set of syntactically valid clauses. If a negative example fails to satisfy all premises, it is not evidence against the claimed entailment; correct the example before making the conclusion.

**Marking rubric (100 points).** Formal vocabulary and precise domain: 20. Faithful translation and variable scope: 20. Semantic or proof certificate: 25. Adversarial countercase and scope limitations: 20. Reproducibility and clear writing: 15. Instructors should award no proof credit for fluent prose that hides an invalid inference. Conversely, a correct formula accompanied by an inadequate plain-language explanation should not receive full communication credit. Use student-reported uncertainty as evidence of intellectual discipline when it is accurately justified.

### Unit closeout questions

1. Identify the difference between the main claim in **Domains and interpretations** and **Recursive satisfaction clauses**. How would a careless reader mistakenly combine them?

2. Construct a concrete countercase to one of the unit’s tempting informal inferences, naming each interpreted symbol.

3. Explain whether the unit’s interactive models could prove a universal first-order result. State the exact finite guarantee, if any, and the evidence needed for a broader theorem.

4. Revise the running case after one relevant premise changes. Record the old and new expressions side by side.
