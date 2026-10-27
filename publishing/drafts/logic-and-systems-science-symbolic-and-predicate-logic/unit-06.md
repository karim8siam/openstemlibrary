# Unit 6: Normal Forms and Automated Inference

**Learning destination.** Derive prenex and clausal transformations; distinguish equivalence from equisatisfiability; perform unification and first-order resolution.

**Guiding principle.** A reliable automated pipeline records every transformation and its logical guarantee, rather than labeling all normalization steps “equivalent.”

**Running case.** A proof assistant encodes “every project has a supervisor” and tries to search for a contradiction with a denied candidate conclusion.

## Conceptual orientation

A useful way to begin this unit is to resist writing symbols immediately. Record all formula transformations together with the precise guarantee. The first draft of any formal problem must identify what counts as an input, an allowed operation, a result, and an error. A proof assistant encodes “every project has a supervisor” and tries to search for a contradiction with a denied candidate conclusion. If two readers obtain different formal sentences from the same English claim, the disagreement is often visible before either attempts a proof. A good analyst preserves both candidate translations until the intended interpretation can be resolved. The symbols do not decide the institutional meaning on their own.

In a complete solution: check a standardization step, a Skolem step, and a resolution step separately; verify substitutions and do not elide the occurs check. The student should also be able to explain what this particular workflow cannot establish. A refutation passes when the negated target and clauses are displayed and the empty clause is derived from properly prepared premises. Equisatisfiability is weaker than equivalence in the unchanged signature; failed unbounded search is not a proof of invalidity. These are not decorative limitations; they tell an independent reader when a result is strong enough to reuse and when it should remain a hypothesis pending additional evidence.

## Diagnostic pretest

Take the following situation in isolation: A proof assistant encodes “every project has a supervisor” and tries to search for a contradiction with a denied candidate conclusion. State three things that are known, two things that would need additional facts, and one piece of evidence that could falsify a tempting interpretation. Label each claim as *syntax*, *truth in a model*, *derivability*, *semantic consequence*, or *external factual premise*. If you cannot confidently assign a label, carry the question into the individual lessons rather than quietly collapsing the categories. A convincing formal report will make uncertainty legible.

## Lesson 6.1: Quantifier pushing and prenex forms

### Core definition and significance

Quantifier transformations require exact side conditions. A prenex form moves quantifiers to the beginning while preserving semantics under valid equivalences. Alphabetic renaming prevents collisions between originally independent binders. 

### Exact symbolic object and derivation

The central formal object is `¬∀xP(x) ≡ ∃x¬P(x); (∀xP(x))∧Q ≡ ∀x(P(x)∧Q) if x∉FV(Q)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Rewrite ¬∃x(P(x)∧Q(x)) as ∀x¬(P(x)∧Q(x)), then as ∀x(¬P(x)∨¬Q(x)). But moving ∀x across a formula that has x free can alter its meaning; first inspect the free-variable sets. 

### Why the distinction matters

One common failure is **Performing a quantifier move based on visual proximity alone.** 

**Boundary probe.** Equivalences can depend on a nonempty-domain convention and free-variable side conditions. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Prepare logic formulas for a theorem prover while retaining a transformation audit log. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `¬∀xP(x) ≡ ∃x¬P(x); (∀xP(x))∧Q ≡ ∀x(P(x)∧Q) if x∉FV(Q)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Performing a quantifier move based on visual proximity alone.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Prepare logic formulas for a theorem prover while retaining a transformation audit log. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Equivalences can depend on a nonempty-domain convention and free-variable side conditions.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 6.2: Skolem witnesses and satisfiability

### Core definition and significance

Skolemization replaces an existential witness with a fresh constant or function whose arguments reflect surrounding universal variables. This is generally equisatisfiability of suitable formulas, not ordinary equivalence in the same unchanged signature. 

### Exact symbolic object and derivation

The central formal object is `∀x∃yR(x,y) ↝ ∀xR(x,f(x))`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** The requirement ∀x∃yR(x,y) can be represented after Skolemization by ∀xR(x,f(x)). Each input x may choose its own f(x). For ∃y∀xR(x,y), a fresh constant c gives ∀xR(x,c) instead. 

### Why the distinction matters

One common failure is **Using one Skolem constant for an existential whose witness depends on an earlier universal.** 

**Boundary probe.** The introduced symbol expands the signature; record that change when explaining the logical guarantee. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Encode subject-specific reviewer assignment versus a universal reviewer in a solver. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀x∃yR(x,y) ↝ ∀xR(x,f(x))` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Using one Skolem constant for an existential whose witness depends on an earlier universal.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Encode subject-specific reviewer assignment versus a universal reviewer in a solver. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “The introduced symbol expands the signature; record that change when explaining the logical guarantee.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 6.3: Clausal form and variable standardization

### Core definition and significance

Resolution operates on clauses: disjunctions of literals whose variables are conventionally universally quantified. Eliminating implication, pushing negations inward, standardizing variables apart, Skolemizing, and distributing connectives are different stages with different requirements. 

### Exact symbolic object and derivation

The central formal object is `P(x)→Q(x) ⇝ ¬P(x)∨Q(x)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Translate ∀x(P(x)→Q(x)) into the single clause {¬P(x),Q(x)}. Combine with {P(a)} and the negation {¬Q(a)} of a goal. Resolution produces {Q(a)}, then the empty clause, showing the assumptions contradict the denied goal. 

### Why the distinction matters

One common failure is **Treating a comma between clauses as another disjunction rather than a conjunction of clauses.** 

**Boundary probe.** Converting a large expression to distributed CNF may blow up size; proof engines manage this with transformations and representations. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Trace clause preparation for a small grant eligibility rule. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `P(x)→Q(x) ⇝ ¬P(x)∨Q(x)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Treating a comma between clauses as another disjunction rather than a conjunction of clauses.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Trace clause preparation for a small grant eligibility rule. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Converting a large expression to distributed CNF may blow up size; proof engines manage this with transformations and representations.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 6.4: Unification and the occurs check

### Core definition and significance

Unification finds a substitution making two predicate expressions syntactically identical. It must respect function symbols, arity, consistency of repeated occurrences, and an occurs check to avoid illegal infinite terms in ordinary first-order syntax. 

### Exact symbolic object and derivation

The central formal object is `unify(P(f(x),x), P(f(a),a)) = {x↦a}`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** P(f(x),x) and P(f(a),a) unify with x=a. But unifying x and f(x) should fail the occurs check for finite first-order terms; accepting it silently changes the term universe to rational trees. 

### Why the distinction matters

One common failure is **Choosing substitutions independently for repeated occurrences of the same variable.** 

**Boundary probe.** Matching with domain-specific equality theories is more complex than free syntactic unification. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Implement a pattern matcher for a restricted automated proof demonstration. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `unify(P(f(x),x), P(f(a),a)) = {x↦a}` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Choosing substitutions independently for repeated occurrences of the same variable.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Implement a pattern matcher for a restricted automated proof demonstration. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Matching with domain-specific equality theories is more complex than free syntactic unification.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 6.5: First-order resolution and refutation

### Core definition and significance

Resolution derives a resolvent after complementary literals have been unified; refutation proves entailment by showing the premises together with the negated target are unsatisfiable. A claimed proof must expose the substitutions, parent clauses, and derived clauses. 

### Exact symbolic object and derivation

The central formal object is `{¬P(x),Q(x)}, {P(a)}, {¬Q(a)} ⊢ □`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Resolve {¬P(x),Q(x)} with {P(a)} under x=a to obtain {Q(a)}. Resolve with {¬Q(a)} to obtain the empty clause. This certifies contradiction under the resolution calculus, assuming the clausification pipeline was correct. 

### Why the distinction matters

One common failure is **Confusing the empty clause with an empty set of clauses: the former is false, the latter trivially satisfiable.** 

**Boundary probe.** First-order resolution is refutation-complete with fair search, not a terminating decision procedure for arbitrary invalid conjectures. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Build a small derivation viewer with hyperlinks between clauses and their parents. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `{¬P(x),Q(x)}, {P(a)}, {¬Q(a)} ⊢ □` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Confusing the empty clause with an empty set of clauses: the former is false, the latter trivially satisfiable.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Build a small derivation viewer with hyperlinks between clauses and their parents. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “First-order resolution is refutation-complete with fair search, not a terminating decision procedure for arbitrary invalid conjectures.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Unit 6 capstone — independent specification review

**Case study.** A proof assistant encodes “every project has a supervisor” and tries to search for a contradiction with a denied candidate conclusion. Produce a two-page formal reasoning memo. The opening paragraph must distinguish the original communication from the interpretation chosen for checking. Provide the signature with arities, a formula or axiom set, and at least two tests: one representative positive interpretation and one boundary or negative interpretation. When claiming an entailment, include a valid derivation or a checked countermodel. State exactly which hypotheses are independent of the formal result and how the real project would validate them. Conclude by explaining how the result would change if a key premise were relaxed.

**Evidence standard.** Record all formula transformations together with the precise guarantee. Check a standardization step, a Skolem step, and a resolution step separately; verify substitutions and do not elide the occurs check. A refutation passes when the negated target and clauses are displayed and the empty clause is derived from properly prepared premises. Equisatisfiability is weaker than equivalence in the unchanged signature; failed unbounded search is not a proof of invalidity. A good submission includes a machine-readable artifact where practical: a tiny truth table, predicate relation matrix, proof trace, or set of syntactically valid clauses. If a negative example fails to satisfy all premises, it is not evidence against the claimed entailment; correct the example before making the conclusion.

**Marking rubric (100 points).** Formal vocabulary and precise domain: 20. Faithful translation and variable scope: 20. Semantic or proof certificate: 25. Adversarial countercase and scope limitations: 20. Reproducibility and clear writing: 15. Instructors should award no proof credit for fluent prose that hides an invalid inference. Conversely, a correct formula accompanied by an inadequate plain-language explanation should not receive full communication credit. Use student-reported uncertainty as evidence of intellectual discipline when it is accurately justified.

### Unit closeout questions

1. Identify the difference between the main claim in **Quantifier pushing and prenex forms** and **First-order resolution and refutation**. How would a careless reader mistakenly combine them?

2. Construct a concrete countercase to one of the unit’s tempting informal inferences, naming each interpreted symbol.

3. Explain whether the unit’s interactive models could prove a universal first-order result. State the exact finite guarantee, if any, and the evidence needed for a broader theorem.

4. Revise the running case after one relevant premise changes. Record the old and new expressions side by side.
