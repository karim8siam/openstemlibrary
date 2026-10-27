# Unit 8: Practical Logic Systems and Validation

**Learning destination.** Connect first-order logic to databases, typed policies, Datalog, software specifications, and reproducible reasoning audits.

**Guiding principle.** A correct formula over inaccurate records remains a correct formula over inaccurate records. Data semantics and operational obligations must be validated separately.

**Running case.** An internship matching system applies supervisor eligibility, student consent, project capacity, and approval checks.

## Conceptual orientation

A useful way to begin this unit is to resist writing symbols immediately. Separate logical rules, data collection, identity, security, and human approval. The first draft of any formal problem must identify what counts as an input, an allowed operation, a result, and an error. An internship matching system applies supervisor eligibility, student consent, project capacity, and approval checks. If two readers obtain different formal sentences from the same English claim, the disagreement is often visible before either attempts a proof. A good analyst preserves both candidate translations until the intended interpretation can be resolved. The symbols do not decide the institutional meaning on their own.

In a complete solution, Create an evaluation record with timestamped inputs, exact formula version, uncertainty conditions, and expected counterexamples; use honest timeout labeling. The student should also be able to explain what this particular workflow cannot establish. An application passes when reproducible checks and operational caveats are recorded independently. Neither a formal proof nor a toy widget authorizes a real-world decision. These are not decorative limitations; they tell an independent reader when a result is strong enough to reuse and when it should remain a hypothesis pending additional evidence.

## Diagnostic pretest

Take the following situation in isolation: An internship matching system applies supervisor eligibility, student consent, project capacity, and approval checks. State three things that are known, two things that would need additional facts, and one piece of evidence that could falsify a tempting interpretation. Label each claim as *syntax*, *truth in a model*, *derivability*, *semantic consequence*, or *external factual premise*. If you cannot confidently assign a label, carry the question into the individual lessons rather than quietly collapsing the categories. A convincing formal report will make uncertainty legible.

## Lesson 8.1: First-order queries and database assumptions

### Core definition and significance

Relational databases resemble finite first-order structures, but SQL adds bags, null markers, and three-valued logic. The closed-world assumption for missing tuples is a convention of a database environment, not a theorem of first-order logic. 

### Exact symbolic object and derivation

The central formal object is `∀x(Student(x)→Enrolled(x))`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** If the Student table contains a and b, but Enrolled contains only a, the universal enrollment rule fails at b in the modeled snapshot. If b has a NULL enrollment status, a literal SQL predicate may yield UNKNOWN rather than classical false, so translation needs an explicit policy. 

### Why the distinction matters

One common failure is **Assuming SQL NOT EXISTS and logical negation always coincide regardless of null semantics.** 

**Boundary probe.** A query passing today does not prove the live database will preserve the invariant after concurrent writes. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Prepare an integrity check for a student registry and document how unknown statuses are classified. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀x(Student(x)→Enrolled(x))` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Assuming SQL NOT EXISTS and logical negation always coincide regardless of null semantics.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Prepare an integrity check for a student registry and document how unknown statuses are classified. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A query passing today does not prove the live database will preserve the invariant after concurrent writes.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 8.2: Sorts and type-sensitive quantification

### Core definition and significance

Many-sorted first-order logic assigns variables to types or sorts. This prevents accidental quantification over ill-typed objects; it can be translated to one-sorted logic using unary sort predicates and appropriate restrictions. 

### Exact symbolic object and derivation

The central formal object is `∀s:Student ∃p:Project Applied(s,p)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** “Each student applies to a project” becomes ∀s(Student(s)→∃p(Project(p)∧Applied(s,p))) in one-sorted form. The sorted notation is shorter but requires the same interpretation of Student and Project. 

### Why the distinction matters

One common failure is **Using an unrestricted quantifier where only a named category is eligible.** 

**Boundary probe.** Sorting does not ensure the data entered under a type are trustworthy or that types reflect reality. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Specify distinct types for student, supervisor, opportunity, and institution in a scholarship system. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀s:Student ∃p:Project Applied(s,p)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Using an unrestricted quantifier where only a named category is eligible.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Specify distinct types for student, supervisor, opportunity, and institution in a scholarship system. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Sorting does not ensure the data entered under a type are trustworthy or that types reflect reality.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 8.3: Datalog rules and recursion

### Core definition and significance

Datalog uses Horn-style rules over a database, frequently with a least-fixed-point semantics. Recursion can compute reachability in finite graphs even though arbitrary transitive closure is not expressible by a single first-order formula over all finite graphs. 

### Exact symbolic object and derivation

The central formal object is `Reach(x,z) :- Edge(x,z). Reach(x,z) :- Edge(x,y), Reach(y,z).`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Given Edge(a,b) and Edge(b,c), the base rule gives Reach(a,b),Reach(b,c); the recursive rule adds Reach(a,c). Continue until no new facts are produced. A safe rule restricts variables so evaluation is well-defined over its intended active domain. 

### Why the distinction matters

One common failure is **Treating procedural recursion as identical to a quantifier nesting of fixed depth.** 

**Boundary probe.** Rules with negation need additional stratification or semantic conventions; positive Datalog alone is monotonic. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Prototype a research-collaboration graph with explicit explainable path evidence. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `Reach(x,z) :- Edge(x,z). Reach(x,z) :- Edge(x,y), Reach(y,z).` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Treating procedural recursion as identical to a quantifier nesting of fixed depth.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Prototype a research-collaboration graph with explicit explainable path evidence. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Rules with negation need additional stratification or semantic conventions; positive Datalog alone is monotonic.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 8.4: Verification of policy engines

### Core definition and significance

A formal policy can enforce prerequisites, prevent forbidden assignments, and generate counterexample records. It cannot determine whether the policy itself is fair, legally compliant, or appropriate to its institutional setting. 

### Exact symbolic object and derivation

The central formal object is `∀s∀p(Assigned(s,p)→Consented(s,p)∧Eligible(s,p))`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** For s1,p1, if Assigned(s1,p1) is true but Consented(s1,p1) false, the universal policy fails immediately. If both booleans are true but the consent record was forged, the logical model still evaluates true; data provenance is not built into the formula. 

### Why the distinction matters

One common failure is **Equating theorem-prover acceptance with authorization from the real user.** 

**Boundary probe.** A secure implementation requires identity, logging, threat modeling, and privacy controls not supplied by a logic widget. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Construct test cases for research matching: missing consent, changed capacity, outdated supervisor status. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀s∀p(Assigned(s,p)→Consented(s,p)∧Eligible(s,p))` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Equating theorem-prover acceptance with authorization from the real user.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Construct test cases for research matching: missing consent, changed capacity, outdated supervisor status. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A secure implementation requires identity, logging, threat modeling, and privacy controls not supplied by a logic widget.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 8.5: Limits, auditability, and reproducible research

### Core definition and significance

Classical first-order validity is semi-decidable: sound and complete proof search can eventually derive valid consequences, but no general algorithm decides every formula in finite time. A finite model finder may disprove entailment early while proving all cases is harder. 

### Exact symbolic object and derivation

The central formal object is `Γ⊨φ iff Γ∪{¬φ} is unsatisfiable`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Report a toy solver result with signature, premises, negated claim, preprocessing steps, bounded-model options, and proof trace or explicit countermodel. If the search times out, report “unknown under these resources,” never “false.” 

### Why the distinction matters

One common failure is **Reporting a timeout or failed bounded search as mathematical invalidity.** 

**Boundary probe.** Proof soundness, database correctness, stakeholder acceptance, accessibility, and safety are separate quality dimensions. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Develop publication standards for a research-logic demonstration: versioned inputs, unit tests, limitations, reproducible notebooks, and independent review. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `Γ⊨φ iff Γ∪{¬φ} is unsatisfiable` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Reporting a timeout or failed bounded search as mathematical invalidity.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Develop publication standards for a research-logic demonstration: versioned inputs, unit tests, limitations, reproducible notebooks, and independent review. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Proof soundness, database correctness, stakeholder acceptance, accessibility, and safety are separate quality dimensions.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Unit 8 capstone — independent specification review

**Case study.** An internship matching system applies supervisor eligibility, student consent, project capacity, and approval checks. Produce a two-page formal reasoning memo. The opening paragraph must distinguish the original communication from the interpretation chosen for checking. Provide the signature with arities, a formula or axiom set, and at least two tests: one representative positive interpretation and one boundary or negative interpretation. When claiming an entailment, include a valid derivation or a checked countermodel. State exactly which hypotheses are independent of the formal result and how the real project would validate them. Conclude by explaining how the result would change if a key premise were relaxed.

**Evidence standard.** Separate logical rules, data collection, identity, security, and human approval. Create an evaluation record with timestamped inputs, exact formula version, uncertainty conditions, and expected counterexamples; use honest timeout labeling. An application passes when reproducible checks and operational caveats are recorded independently. Neither a formal proof nor a toy widget authorizes a real-world decision. A good submission includes a machine-readable artifact where practical: a tiny truth table, predicate relation matrix, proof trace, or set of syntactically valid clauses. If a negative example fails to satisfy all premises, it is not evidence against the claimed entailment; correct the example before making the conclusion.

**Marking rubric (100 points).** Formal vocabulary and precise domain: 20. Faithful translation and variable scope: 20. Semantic or proof certificate: 25. Adversarial countercase and scope limitations: 20. Reproducibility and clear writing: 15. Instructors should award no proof credit for fluent prose that hides an invalid inference. Conversely, a correct formula accompanied by an inadequate plain-language explanation should not receive full communication credit. Use student-reported uncertainty as evidence of intellectual discipline when it is accurately justified.

### Unit closeout questions

1. Identify the difference between the main claim in **First-order queries and database assumptions** and **Limits, auditability, and reproducible research**. How would a careless reader mistakenly combine them?

2. Construct a concrete countercase to one of the unit’s tempting informal inferences, naming each interpreted symbol.

3. Explain whether the unit’s interactive models could prove a universal first-order result. State the exact finite guarantee, if any, and the evidence needed for a broader theorem.

4. Revise the running case after one relevant premise changes. Record the old and new expressions side by side.
