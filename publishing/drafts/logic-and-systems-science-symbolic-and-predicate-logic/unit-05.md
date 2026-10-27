# Unit 5: Deduction and Proof Discipline

**Learning destination.** Develop natural-deduction proofs for universal and existential statements while enforcing eigenvariable and assumption-scope restrictions.

**Guiding principle.** First-order inference rules carry conditions about arbitrary parameters and fresh witnesses; overlooking them makes unsound arguments look like proofs.

**Running case.** A grant-selection assistant tries to conclude that all students were approved after proving approval for one named student.

## Conceptual orientation

A useful way to begin this unit is to resist writing symbols immediately. List active assumptions and parameters on every proof line. The first draft of any formal problem must identify what counts as an input, an allowed operation, a result, and an error. A grant-selection assistant tries to conclude that all students were approved after proving approval for one named student. If two readers obtain different formal sentences from the same English claim, the disagreement is often visible before either attempts a proof. A good analyst preserves both candidate translations until the intended interpretation can be resolved. The symbols do not decide the institutional meaning on their own.

In a complete solution, Apply quantifier rules with freshness and arbitrary-parameter checks; discharge temporary assumptions correctly; avoid an existential witness escaping its subproof. The student should also be able to explain what this particular workflow cannot establish. A deduction passes when each line follows by an admissible rule from earlier lines and its listed side conditions hold. A derivation of a mistaken real-world premise says nothing about that premise’s factual accuracy. These are not decorative limitations; they tell an independent reader when a result is strong enough to reuse and when it should remain a hypothesis pending additional evidence.

## Diagnostic pretest

Take the following situation in isolation: A grant-selection assistant tries to conclude that all students were approved after proving approval for one named student. State three things that are known, two things that would need additional facts, and one piece of evidence that could falsify a tempting interpretation. Label each claim as *syntax*, *truth in a model*, *derivability*, *semantic consequence*, or *external factual premise*. If you cannot confidently assign a label, carry the question into the individual lessons rather than quietly collapsing the categories. A convincing formal report will make uncertainty legible.

## Lesson 5.1: Universal elimination and introduction

### Core definition and significance

Universal elimination substitutes a suitable term for a universally bound variable. Universal introduction requires the chosen parameter to be arbitrary with respect to undischarged assumptions; a property of a particular named person is insufficient. 

### Exact symbolic object and derivation

The central formal object is `∀xP(x) ⊢ P(c); P(a) ⊢ ∀xP(x) only if a arbitrary`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** From ∀x(Student(x)→Eligible(x)), instantiate at candidate c to derive Student(c)→Eligible(c). If also Student(c), modus ponens yields Eligible(c). But you cannot conclude ∀xEligible(x) from that particular case. 

### Why the distinction matters

One common failure is **Generalizing from one named individual whose properties were used as assumptions.** 

**Boundary probe.** The side condition may vary in presentation across proof systems but protects the same semantic dependence. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Have a proof checker list open assumptions before applying ∀-introduction. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀xP(x) ⊢ P(c); P(a) ⊢ ∀xP(x) only if a arbitrary` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Generalizing from one named individual whose properties were used as assumptions.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Have a proof checker list open assumptions before applying ∀-introduction. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “The side condition may vary in presentation across proof systems but protects the same semantic dependence.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 5.2: Existential introduction

### Core definition and significance

Existential introduction needs a concrete witness. The introduced variable is bound and does not name one permanent object; different demonstrations of the same existential may have different witnesses. 

### Exact symbolic object and derivation

The central formal object is `P(c) ⊢ ∃xP(x)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** If Mentor(r) and Supervises(r,p), then ∃x(Mentor(x)∧Supervises(x,p)). The proof uses r as a witness, but the conclusion does not claim that r is the only suitable mentor. 

### Why the distinction matters

One common failure is **Treating existential introduction as a uniqueness or universal claim.** 

**Boundary probe.** This rule is sound in standard nonempty-domain first-order semantics; disclosure policy is a separate issue. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Derive a safe reporting rule from one approved record without disclosing a permanent identifier. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `P(c) ⊢ ∃xP(x)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Treating existential introduction as a uniqueness or universal claim.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Derive a safe reporting rule from one approved record without disclosing a permanent identifier. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “This rule is sound in standard nonempty-domain first-order semantics; disclosure policy is a separate issue.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 5.3: Existential elimination and freshness

### Core definition and significance

Existential elimination temporarily chooses a fresh symbol to represent an unknown witness; the final conclusion must not depend on which witness was chosen. Carrying the temporary label outside its subproof invalidates the reasoning. 

### Exact symbolic object and derivation

The central formal object is `∃xP(x), ∀x(P(x)→Q(x)) ⊢ ∃xQ(x)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** From ∃xP(x), assume P(k) for a fresh k. Instantiate ∀x(P(x)→Q(x)) to P(k)→Q(k), get Q(k), infer ∃xQ(x), then discharge the temporary assumption. The conclusion never mentions k. 

### Why the distinction matters

One common failure is **Concluding Q(k) globally or assigning the existential witness a privileged permanent name.** 

**Boundary probe.** A witness label must be fresh relative to the relevant assumptions and conclusion under the selected calculus. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Audit a grant application proof that derives existence of a qualified supervisor from existence of a trained supervisor. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∃xP(x), ∀x(P(x)→Q(x)) ⊢ ∃xQ(x)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Concluding Q(k) globally or assigning the existential witness a privileged permanent name.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Audit a grant application proof that derives existence of a qualified supervisor from existence of a trained supervisor. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A witness label must be fresh relative to the relevant assumptions and conclusion under the selected calculus.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 5.4: Proof by cases and conditional subproofs

### Core definition and significance

First-order deductions reuse the same structural machinery as propositional logic. Subproof assumptions are temporary and must be discharged by their correct introduction or elimination rules; quantifier steps add variable restrictions. 

### Exact symbolic object and derivation

The central formal object is `(A→C)∧(B→C), A∨B ⊢ C`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Suppose every approved project is funded and every emergency project is funded. If a given project is either approved or emergency, split on the disjunction and derive funded in each branch; the combined result follows by disjunction elimination. 

### Why the distinction matters

One common failure is **Applying universal introduction while a branch-specific property of the generalized object remains open.** 

**Boundary probe.** Natural-deduction notation varies by textbook; track assumptions rather than copying visual indentation alone. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Write a proof certificate with numbered lines for a two-route approval system. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `(A→C)∧(B→C), A∨B ⊢ C` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Applying universal introduction while a branch-specific property of the generalized object remains open.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Write a proof certificate with numbered lines for a two-route approval system. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Natural-deduction notation varies by textbook; track assumptions rather than copying visual indentation alone.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 5.5: Identity introduction and substitution

### Core definition and significance

Reflexivity of identity holds in every structure. Substitution of identicals preserves truth for formulas when substitution is performed correctly without variable capture. It does not license swapping unrelated entities with similar labels. 

### Exact symbolic object and derivation

The central formal object is `a=a; a=b, P(a) ⊢ P(b)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Given r1=r2 and Qualified(r1), infer Qualified(r2). If r1 and r2 are different strings naming a single researcher, the formula remains correct. It does not prove that the real database has de-duplicated those profiles reliably. 

### Why the distinction matters

One common failure is **Applying equality substitution to a similarity score or fuzzy string match.** 

**Boundary probe.** Some programming languages treat object equality differently; this is a model choice rather than a change to logical identity. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Separate entity-resolution confidence from deductive substitution in a researcher-profile catalog. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `a=a; a=b, P(a) ⊢ P(b)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Applying equality substitution to a similarity score or fuzzy string match.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Separate entity-resolution confidence from deductive substitution in a researcher-profile catalog. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Some programming languages treat object equality differently; this is a model choice rather than a change to logical identity.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Unit 5 capstone — independent specification review

**Case study.** A grant-selection assistant tries to conclude that all students were approved after proving approval for one named student. Produce a two-page formal reasoning memo. The opening paragraph must distinguish the original communication from the interpretation chosen for checking. Provide the signature with arities, a formula or axiom set, and at least two tests: one representative positive interpretation and one boundary or negative interpretation. When claiming an entailment, include a valid derivation or a checked countermodel. State exactly which hypotheses are independent of the formal result and how the real project would validate them. Conclude by explaining how the result would change if a key premise were relaxed.

**Evidence standard.** List active assumptions and parameters on every proof line. Apply quantifier rules with freshness and arbitrary-parameter checks; discharge temporary assumptions correctly; avoid an existential witness escaping its subproof. A deduction passes when each line follows by an admissible rule from earlier lines and its listed side conditions hold. A derivation of a mistaken real-world premise says nothing about that premise’s factual accuracy. A good submission includes a machine-readable artifact where practical: a tiny truth table, predicate relation matrix, proof trace, or set of syntactically valid clauses. If a negative example fails to satisfy all premises, it is not evidence against the claimed entailment; correct the example before making the conclusion.

**Marking rubric (100 points).** Formal vocabulary and precise domain: 20. Faithful translation and variable scope: 20. Semantic or proof certificate: 25. Adversarial countercase and scope limitations: 20. Reproducibility and clear writing: 15. Instructors should award no proof credit for fluent prose that hides an invalid inference. Conversely, a correct formula accompanied by an inadequate plain-language explanation should not receive full communication credit. Use student-reported uncertainty as evidence of intellectual discipline when it is accurately justified.

### Unit closeout questions

1. Identify the difference between the main claim in **Universal elimination and introduction** and **Identity introduction and substitution**. How would a careless reader mistakenly combine them?

2. Construct a concrete countercase to one of the unit’s tempting informal inferences, naming each interpreted symbol.

3. Explain whether the unit’s interactive models could prove a universal first-order result. State the exact finite guarantee, if any, and the evidence needed for a broader theorem.

4. Revise the running case after one relevant premise changes. Record the old and new expressions side by side.
