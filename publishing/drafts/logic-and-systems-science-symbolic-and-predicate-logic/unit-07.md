# Unit 7: Theories, Expressibility, and Model Limits

**Learning destination.** Formalize order and graph properties, analyze equality and definability, and understand compactness and expressiveness limitations.

**Guiding principle.** An axiom list describes a class of structures, not a particular data table. First-order formulas cannot generally express every global system property.

**Running case.** A research network tracks who collaborates with whom; distinguish a direct edge, two-step connection, and arbitrary-length reachability.

## Conceptual orientation

A useful way to begin this unit is to resist writing symbols immediately. Write defining axioms before testing examples, and identify the intended class of models. The first draft of any formal problem must identify what counts as an input, an allowed operation, a result, and an error. A research network tracks who collaborates with whom; distinguish a direct edge, two-step connection, and arbitrary-length reachability. If two readers obtain different formal sentences from the same English claim, the disagreement is often visible before either attempts a proof. A good analyst preserves both candidate translations until the intended interpretation can be resolved. The symbols do not decide the institutional meaning on their own.

In a complete solution: construct a finite positive example and a counterexample that fails one axiom; distinguish direct edges from fixed-length paths. The student should also be able to explain what this particular workflow cannot establish. A theory-analysis answer passes when it states which structures satisfy the axioms and what global claim is or is not definable. A finite battery of examples cannot establish compactness or a global expressibility theorem. These are not decorative limitations; they tell an independent reader when a result is strong enough to reuse and when it should remain a hypothesis pending additional evidence.

## Diagnostic pretest

Take the following situation in isolation: A research network tracks who collaborates with whom; distinguish a direct edge, two-step connection, and arbitrary-length reachability. State three things that are known, two things that would need additional facts, and one piece of evidence that could falsify a tempting interpretation. Label each claim as *syntax*, *truth in a model*, *derivability*, *semantic consequence*, or *external factual premise*. If you cannot confidently assign a label, carry the question into the individual lessons rather than quietly collapsing the categories. A convincing formal report will make uncertainty legible.

## Lesson 7.1: Uniqueness and cardinality restrictions

### Core definition and significance

With identity, first-order logic can express “there exists exactly one” and fixed finite bounds. It cannot simply count via a database aggregation primitive; its formulation uses equality and explicitly quantified witnesses. 

### Exact symbolic object and derivation

The central formal object is `∃x(P(x)∧∀y(P(y)→y=x))`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** To assert exactly two P-objects, write ∃x∃y(x≠y∧P(x)∧P(y)∧∀z(P(z)→(z=x∨z=y))). The two witnesses are required to differ, and every P-object must equal one of them. 

### Why the distinction matters

One common failure is **Writing two existential quantifiers without inequality and assuming they designate different things.** 

**Boundary probe.** A finite fixed cardinality bound is first-order expressible; “finitely many” over arbitrary structures is a different, non-first-order property. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Encode a safety constraint requiring exactly two independent approvers. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∃x(P(x)∧∀y(P(y)→y=x))` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Writing two existential quantifiers without inequality and assuming they designate different things.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Encode a safety constraint requiring exactly two independent approvers. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A finite fixed cardinality bound is first-order expressible; “finitely many” over arbitrary structures is a different, non-first-order property.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 7.2: Partial orders and equivalence relations

### Core definition and significance

An axiomatic theory describes constraints that all acceptable interpretations must satisfy. A partial order is reflexive, antisymmetric, and transitive; a strict order is usually irreflexive and transitive. An equivalence relation is reflexive, symmetric, and transitive. 

### Exact symbolic object and derivation

The central formal object is `∀xR(x,x); ∀xy(R(x,y)∧R(y,x)→x=y); ∀xyz(R(x,y)∧R(y,z)→R(x,z))`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** For a prerequisite relation ≤ on courses, verify reflexivity, antisymmetry, and transitivity. Course A≤B and B≤A forces identity under antisymmetry; “can be cross-listed with” instead might be an equivalence relation. 

### Why the distinction matters

One common failure is **Confusing antisymmetry with the negation of symmetry.** 

**Boundary probe.** A finite test of one graph confirms the axioms in that graph, not that every graph with the chosen label obeys them. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Develop machine-checkable invariants for a department’s dependency graph. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀xR(x,x); ∀xy(R(x,y)∧R(y,x)→x=y); ∀xyz(R(x,y)∧R(y,z)→R(x,z))` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Confusing antisymmetry with the negation of symmetry.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Develop machine-checkable invariants for a department’s dependency graph. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A finite test of one graph confirms the axioms in that graph, not that every graph with the chosen label obeys them.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 7.3: Functions represented by relations

### Core definition and significance

A binary relation defines the graph of a total function precisely when every input has exactly one related output. This is useful when data initially arrive as rows and one wishes to impose functional consistency rather than assume it. 

### Exact symbolic object and derivation

The central formal object is `∀x∃y(F(x,y)∧∀z(F(x,z)→z=y))`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Represent AssignedAdvisor(student,advisor). Existence is ∀s(Student(s)→∃a AssignedAdvisor(s,a)); uniqueness is ∀s∀a∀b((AssignedAdvisor(s,a)∧AssignedAdvisor(s,b))→a=b). The two conditions jointly yield a single advisor for every student. 

### Why the distinction matters

One common failure is **Conflating “every student has an advisor” with “every student has exactly one advisor.”** 

**Boundary probe.** If some students may have no advisor, model a partial function rather than hiding missingness behind an arbitrary null object. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Compare a SQL uniqueness constraint with an existence constraint and describe what each fails to guarantee alone. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀x∃y(F(x,y)∧∀z(F(x,z)→z=y))` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Conflating “every student has an advisor” with “every student has exactly one advisor.”” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Compare a SQL uniqueness constraint with an existence constraint and describe what each fails to guarantee alone. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “If some students may have no advisor, model a partial function rather than hiding missingness behind an arbitrary null object.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 7.4: Graphs and bounded reachability

### Core definition and significance

A fixed-length path can be described with finitely many intermediate variables. The transitive closure relation—existence of a path of arbitrary length—is not generally definable by one first-order formula over arbitrary finite directed graphs with only the edge relation. 

### Exact symbolic object and derivation

The central formal object is `∃z(E(x,z)∧E(z,y)) expresses a length-two path`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** For nodes a,b,c, edges a→b and b→c imply a length-two path a→c, expressible by ∃z(E(a,z)∧E(z,c)). A graph with an a→c path of length five cannot be captured by that exact two-step formula. 

### Why the distinction matters

One common failure is **Interpreting two-step connectivity as arbitrary reachability.** 

**Boundary probe.** On a fixed finite graph size bound, a bounded disjunction of path lengths can encode reachability, but the bound matters. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Contrast logical specification with a recursive graph algorithm and record their domains of validity. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∃z(E(x,z)∧E(z,y)) expresses a length-two path` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Interpreting two-step connectivity as arbitrary reachability.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Contrast logical specification with a recursive graph algorithm and record their domains of validity. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “On a fixed finite graph size bound, a bounded disjunction of path lengths can encode reachability, but the bound matters.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 7.5: Compactness and model-size cautions

### Core definition and significance

Compactness concerns arbitrary collections of first-order sentences under standard semantics: if every finite subset has a model, the whole set has a model. It reveals why certain global claims about all finite structures cannot be captured by a single first-order theory in the intended way. 

### Exact symbolic object and derivation

The central formal object is `Every finite subset satisfiable ⇒ whole first-order theory satisfiable (compactness)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Add a different-objects sentence for each positive integer n asserting at least n domain elements. Every finite subset admits a sufficiently large finite model; compactness gives a model for the entire theory, necessarily infinite. This does not claim that a computer can construct it. 

### Why the distinction matters

One common failure is **Assuming finite-model checks decide satisfiability of an unrestricted theory.** 

**Boundary probe.** Use compactness only with its exact hypothesis and classical first-order framework; finite model theory has different tools. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Explain why a sequence of larger test graphs does not prove a universal finite-only theorem. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `Every finite subset satisfiable ⇒ whole first-order theory satisfiable (compactness)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Assuming finite-model checks decide satisfiability of an unrestricted theory.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Explain why a sequence of larger test graphs does not prove a universal finite-only theorem. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Use compactness only with its exact hypothesis and classical first-order framework; finite model theory has different tools.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Unit 7 capstone — independent specification review

**Case study.** A research network tracks who collaborates with whom; distinguish a direct edge, two-step connection, and arbitrary-length reachability. Produce a two-page formal reasoning memo. The opening paragraph must distinguish the original communication from the interpretation chosen for checking. Provide the signature with arities, a formula or axiom set, and at least two tests: one representative positive interpretation and one boundary or negative interpretation. When claiming an entailment, include a valid derivation or a checked countermodel. State exactly which hypotheses are independent of the formal result and how the real project would validate them. Conclude by explaining how the result would change if a key premise were relaxed.

**Evidence standard.** Write defining axioms before testing examples, and identify the intended class of models. Construct a finite positive example and a counterexample that fails one axiom; distinguish direct edges from fixed-length paths. A theory-analysis answer passes when it states which structures satisfy the axioms and what global claim is or is not definable. A finite battery of examples cannot establish compactness or a global expressibility theorem. A good submission includes a machine-readable artifact where practical: a tiny truth table, predicate relation matrix, proof trace, or set of syntactically valid clauses. If a negative example fails to satisfy all premises, it is not evidence against the claimed entailment; correct the example before making the conclusion.

**Marking rubric (100 points).** Formal vocabulary and precise domain: 20. Faithful translation and variable scope: 20. Semantic or proof certificate: 25. Adversarial countercase and scope limitations: 20. Reproducibility and clear writing: 15. Instructors should award no proof credit for fluent prose that hides an invalid inference. Conversely, a correct formula accompanied by an inadequate plain-language explanation should not receive full communication credit. Use student-reported uncertainty as evidence of intellectual discipline when it is accurately justified.

### Unit closeout questions

1. Identify the difference between the main claim in **Uniqueness and cardinality restrictions** and **Compactness and model-size cautions**. How would a careless reader mistakenly combine them?

2. Construct a concrete countercase to one of the unit’s tempting informal inferences, naming each interpreted symbol.

3. Explain whether the unit’s interactive models could prove a universal first-order result. State the exact finite guarantee, if any, and the evidence needed for a broader theorem.

4. Revise the running case after one relevant premise changes. Record the old and new expressions side by side.
