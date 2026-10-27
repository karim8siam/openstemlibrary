# Unit 1: Formal Symbols, Parsing, and Substitution

**Learning destination.** Distinguish well-formed first-order formulas from plausible strings; track free occurrences and compute substitutions without capture.

**Guiding principle.** An automated checker can never recover the author’s quantifier scope from indentation or good intentions. A syntax specification must define it.

**Running case.** A reviewer asks whether changing a variable name preserves the assertion, and whether replacing a free variable with a term accidentally makes it bound.

## Conceptual orientation

A useful way to begin this unit is to resist writing symbols immediately. Build an abstract syntax tree and a free-variable ledger before evaluating. The first draft of any formal problem must identify what counts as an input, an allowed operation, a result, and an error. A reviewer asks whether changing a variable name preserves the assertion, and whether replacing a free variable with a term accidentally makes it bound. If two readers obtain different formal sentences from the same English claim, the disagreement is often visible before either attempts a proof. A good analyst preserves both candidate translations until the intended interpretation can be resolved. The symbols do not decide the institutional meaning on their own.

In a complete solution: for each variable occurrence, write the nearest binding quantifier or label it free. When replacing terms, verify no free variable from the replacement enters the reach of a new binder. The student should also be able to explain what this particular workflow cannot establish. A parser test passes only when it establishes unique construction under the grammar and the arity constraints. Malformed notation is not a false logical sentence; it is outside the specified language. These are not decorative limitations; they tell an independent reader when a result is strong enough to reuse and when it should remain a hypothesis pending additional evidence.

## Diagnostic pretest

Take the following situation in isolation: A reviewer asks whether changing a variable name preserves the assertion, and whether replacing a free variable with a term accidentally makes it bound. State three things that are known, two things that would need additional facts, and one piece of evidence that could falsify a tempting interpretation. Label each claim as *syntax*, *truth in a model*, *derivability*, *semantic consequence*, or *external factual premise*. If you cannot confidently assign a label, carry the question into the individual lessons rather than quietly collapsing the categories. A convincing formal report will make uncertainty legible.

## Lesson 1.1: Alphabet and signatures

### Core definition and significance

A signature lists relation arities, function arities and constants before a grammar is introduced. Symbols of different arity cannot silently replace one another. Atomic formulas are built from appropriately formed terms; conjunctions and quantified expressions then produce larger formulas. 

### Exact symbolic object and derivation

The central formal object is `L={R^2,f^1,c,P^1}; x,y,z ∈ Var`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** With c a constant and f unary, f(f(c)) is a term, P(f(c)) is a formula, and R(c,f(c)) is an atomic formula. R(c) is ill-formed because the declared relation expects two arguments. 

### Why the distinction matters

One common failure is **Treating a predicate as if it returns a domain object.** 

**Boundary probe.** Changing the domain does not change grammatical well-formedness; changing the signature can. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Design a vocabulary for students, projects, and a supervision relation; explain why one predicate can be binary and another unary. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `L={R^2,f^1,c,P^1}; x,y,z ∈ Var` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Treating a predicate as if it returns a domain object.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Design a vocabulary for students, projects, and a supervision relation; explain why one predicate can be binary and another unary. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Changing the domain does not change grammatical well-formedness; changing the signature can.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 1.2: Inductive formation rules

### Core definition and significance

An inductive grammar describes the smallest collection closed under specific constructors. This makes structural recursion possible: a property of all formulas is checked at the atomic case and then at each legal constructor. 

### Exact symbolic object and derivation

The central formal object is `φ ::= P(t) | ¬φ | (φ∧ψ) | ∀x φ`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Derive ∀x(P(x)→∃yR(x,y)) by constructing P(x), R(x,y), the existential, the conditional, and finally the universal quantifier. A string with an unpaired quantifier does not have such a construction tree. 

### Why the distinction matters

One common failure is **Saying a formula is valid because it looks like mathematical notation, without constructing a parse.** 

**Boundary probe.** A malformed formula has no truth value under the standard recursive satisfaction definition. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Specify grammar productions in a small parser for an online research-policy editor. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `φ ::= P(t) | ¬φ | (φ∧ψ) | ∀x φ` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Saying a formula is valid because it looks like mathematical notation, without constructing a parse.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Specify grammar productions in a small parser for an online research-policy editor. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A malformed formula has no truth value under the standard recursive satisfaction definition.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 1.3: Scopes, precedence, and parse trees

### Core definition and significance

Parentheses remove scope ambiguity; quantifiers bind only occurrences within their syntactic scope. Some texts use precedence conventions, but a cross-institutional formal specification should not rely on readers guessing those conventions. 

### Exact symbolic object and derivation

The central formal object is `∀x(P(x)→Q(x)) versus (∀xP(x))→Q(x)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** In ∀x(P(x)→Q(x)), x is bound in both atoms. In (∀xP(x))→Q(x), x in Q(x) remains free, so evaluation needs an assignment. These are different kinds of expressions even though their symbols are similar. 

### Why the distinction matters

One common failure is **Letting a quantifier reach past the subformula it governs.** 

**Boundary probe.** A parser tree certifies structure, not the appropriateness of the translation. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Audit a student-submission rule that contains a parenthetical exception and an “or” clause. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀x(P(x)→Q(x)) versus (∀xP(x))→Q(x)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Letting a quantifier reach past the subformula it governs.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Audit a student-submission rule that contains a parenthetical exception and an “or” clause. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A parser tree certifies structure, not the appropriateness of the translation.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 1.4: Free variables and alpha-renaming

### Core definition and significance

An occurrence of a variable is free unless enclosed by a quantifier binding that variable. Renaming bound variables is harmless when the renamed variable does not collide with a free occurrence or an intervening binder. 

### Exact symbolic object and derivation

The central formal object is `FV(∀x R(x,y))={y}; ∀xR(x,y) ≡α ∀zR(z,y)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** In ∃x(P(x)∧∀yR(x,y)), all occurrences are bound. Rename the outer x to z to get ∃z(P(z)∧∀yR(z,y)). But renaming that x to y would change which quantifier governs R’s second argument. 

### Why the distinction matters

One common failure is **Assuming a bound-variable change is valid whenever the new letter is different.** 

**Boundary probe.** Two alpha-equivalent formulas have the same satisfaction behavior under corresponding interpretations; a captured formula need not. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Prepare pseudocode for variable analysis in a symbolic proof editor. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `FV(∀x R(x,y))={y}; ∀xR(x,y) ≡α ∀zR(z,y)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Assuming a bound-variable change is valid whenever the new letter is different.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Prepare pseudocode for variable analysis in a symbolic proof editor. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Two alpha-equivalent formulas have the same satisfaction behavior under corresponding interpretations; a captured formula need not.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 1.5: Capture-avoiding substitution

### Core definition and significance

Substituting a term for free occurrences is more delicate than textual search-and-replace. If a variable in the incoming term would be bound by an enclosing quantifier, first alpha-rename the conflicting bound variable. 

### Exact symbolic object and derivation

The central formal object is `(∀yR(x,y))[y/x] requires renaming bound y first`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Start with ∀yR(x,y). To substitute y for free x, rename bound y to fresh z, yielding ∀zR(x,z), then substitute to obtain ∀zR(y,z). Naively replacing x by y gives ∀yR(y,y), which changes the meaning. 

### Why the distinction matters

One common failure is **Replacing substrings rather than free occurrences with scope-aware renaming.** 

**Boundary probe.** A substitution algorithm must also track function symbols and the free variables inside complex terms. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Debug a rule editor that instantiates an eligibility predicate with a user-selected variable. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `(∀yR(x,y))[y/x] requires renaming bound y first` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Replacing substrings rather than free occurrences with scope-aware renaming.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Debug a rule editor that instantiates an eligibility predicate with a user-selected variable. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A substitution algorithm must also track function symbols and the free variables inside complex terms.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Unit 1 capstone — independent specification review

**Case study.** A reviewer asks whether changing a variable name preserves the assertion, and whether replacing a free variable with a term accidentally makes it bound. Produce a two-page formal reasoning memo. The opening paragraph must distinguish the original communication from the interpretation chosen for checking. Provide the signature with arities, a formula or axiom set, and at least two tests: one representative positive interpretation and one boundary or negative interpretation. When claiming an entailment, include a valid derivation or a checked countermodel. State exactly which hypotheses are independent of the formal result and how the real project would validate them. Conclude by explaining how the result would change if a key premise were relaxed.

**Evidence standard.** Build an abstract syntax tree and a free-variable ledger before evaluating. For each variable occurrence, write the nearest binding quantifier or label it free. When replacing terms, verify no free variable from the replacement enters the reach of a new binder. A parser test passes only when it establishes unique construction under the grammar and the arity constraints. Malformed notation is not a false logical sentence; it is outside the specified language. A good submission includes a machine-readable artifact where practical: a tiny truth table, predicate relation matrix, proof trace, or set of syntactically valid clauses. If a negative example fails to satisfy all premises, it is not evidence against the claimed entailment; correct the example before making the conclusion.

**Marking rubric (100 points).** Formal vocabulary and precise domain: 20. Faithful translation and variable scope: 20. Semantic or proof certificate: 25. Adversarial countercase and scope limitations: 20. Reproducibility and clear writing: 15. Instructors should award no proof credit for fluent prose that hides an invalid inference. Conversely, a correct formula accompanied by an inadequate plain-language explanation should not receive full communication credit. Use student-reported uncertainty as evidence of intellectual discipline when it is accurately justified.

### Unit closeout questions

1. Identify the difference between the main claim in **Alphabet and signatures** and **Capture-avoiding substitution**. How would a careless reader mistakenly combine them?

2. Construct a concrete countercase to one of the unit’s tempting informal inferences, naming each interpreted symbol.

3. Explain whether the unit’s interactive models could prove a universal first-order result. State the exact finite guarantee, if any, and the evidence needed for a broader theorem.

4. Revise the running case after one relevant premise changes. Record the old and new expressions side by side.
