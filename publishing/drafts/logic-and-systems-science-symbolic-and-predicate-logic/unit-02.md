# Unit 2: Precision in Natural-Language Translation

**Learning destination.** Translate restricted quantifiers, relative clauses, uniqueness, and scope-sensitive claims without smuggling assumptions into the vocabulary.

**Guiding principle.** A correct translation preserves an agreed interpretation; the shortest symbolic sentence is not necessarily the best translation.

**Running case.** A university funding rule says every applicant must have one supervisor and no two applicants may share the same award.

## Conceptual orientation

A useful way to begin this unit is to resist writing symbols immediately. Declare the universe of discourse, relation argument order, and qualification predicates first. The first draft of any formal problem must identify what counts as an input, an allowed operation, a result, and an error. A university funding rule says every applicant must have one supervisor and no two applicants may share the same award. If two readers obtain different formal sentences from the same English claim, the disagreement is often visible before either attempts a proof. A good analyst preserves both candidate translations until the intended interpretation can be resolved. The symbols do not decide the institutional meaning on their own.

In a complete solution: check a universal on a zero-member restricted class, then provide a positive existential example. For a uniqueness rule, separately test missing witness and duplicated witnesses. The student should also be able to explain what this particular workflow cannot establish. A translation test passes when the symbolic and stated natural-language readings agree on both positive and negative edge cases. A formula may be logically precise while encoding the wrong practical meaning of “eligible” or “approved.” These are not decorative limitations; they tell an independent reader when a result is strong enough to reuse and when it should remain a hypothesis pending additional evidence.

## Diagnostic pretest

Take the following situation in isolation: A university funding rule says every applicant must have one supervisor and no two applicants may share the same award. State three things that are known, two things that would need additional facts, and one piece of evidence that could falsify a tempting interpretation. Label each claim as *syntax*, *truth in a model*, *derivability*, *semantic consequence*, or *external factual premise*. If you cannot confidently assign a label, carry the question into the individual lessons rather than quietly collapsing the categories. A convincing formal report will make uncertainty legible.

## Lesson 2.1: Conditionals in institutional rules

### Core definition and significance

Natural language distinguishes a sufficient condition from a necessary condition. “If A then B” makes A sufficient for B; “A only if B” makes B necessary for A; neither licenses the converse by itself. 

### Exact symbolic object and derivation

The central formal object is `Student(x)→Eligible(x); Eligible(x)→Student(x)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** “A person is funded only if enrolled” translates ∀x(Funded(x)→Enrolled(x)). A non-funded enrolled person is consistent with this. “Enrolled only if funded” would reverse the conditional and impose a very different rule. 

### Why the distinction matters

One common failure is **Translating “only if” backward because the word “if” appears near the second clause.** 

**Boundary probe.** Eligibility logic does not establish that a person’s supporting documents are authentic. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Translate three actual policy-style sentences before writing automated eligibility decisions. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `Student(x)→Eligible(x); Eligible(x)→Student(x)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Translating “only if” backward because the word “if” appears near the second clause.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Translate three actual policy-style sentences before writing automated eligibility decisions. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Eligibility logic does not establish that a person’s supporting documents are authentic.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 2.2: Restricted universal and existential claims

### Core definition and significance

Restriction on a universal is usually expressed by implication; restriction on an existential is usually expressed by conjunction. Replacing these patterns with one another radically changes cases outside the intended subject category. 

### Exact symbolic object and derivation

The central formal object is `∀x(Student(x)→Registered(x)); ∃x(Student(x)∧Registered(x))`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** “Every registered researcher has consent” is ∀x(Researcher(x)∧Registered(x)→Consented(x)). “A registered researcher has consent” is ∃x(Researcher(x)∧Registered(x)∧Consented(x)). If there are no registered researchers, the universal is true and the existential false. 

### Why the distinction matters

One common failure is **Writing ∀x(Student(x)∧Admitted(x)) for “every student was admitted.”** 

**Boundary probe.** A domain model that omits unregistered individuals can make a restriction redundant, but that choice must be explicit. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Formalize how a scholarship portal checks an applicant subset without making claims about outsiders. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀x(Student(x)→Registered(x)); ∃x(Student(x)∧Registered(x))` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Writing ∀x(Student(x)∧Admitted(x)) for “every student was admitted.”” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Formalize how a scholarship portal checks an applicant subset without making claims about outsiders. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A domain model that omits unregistered individuals can make a restriction redundant, but that choice must be explicit.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 2.3: Negative statements and De Morgan duality

### Core definition and significance

Negation applied to a quantified sentence reverses the quantifier while moving inward. This syntactic law matches the witness-based semantics: failure of “all” needs a counterexample; failure of “some” means every candidate fails. 

### Exact symbolic object and derivation

The central formal object is `¬∀xP(x) ≡ ∃x¬P(x); ¬∃xP(x) ≡ ∀x¬P(x)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Negate “every student passed an ethics review”: ∃x(Student(x)∧¬Passed(x)). Negating “some student passed” gives ∀x(Student(x)→¬Passed(x)). A missing review record is not automatically evidence of a failed review. 

### Why the distinction matters

One common failure is **Confusing “not everyone” with “no one.”** 

**Boundary probe.** Classical negation presupposes a two-valued semantic model; missing database fields need additional treatment. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Convert requirements into explicit audit queries: which individual could witness a violation? Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `¬∀xP(x) ≡ ∃x¬P(x); ¬∃xP(x) ≡ ∀x¬P(x)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Confusing “not everyone” with “no one.”” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Convert requirements into explicit audit queries: which individual could witness a violation? **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “Classical negation presupposes a two-valued semantic model; missing database fields need additional treatment.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 2.4: Exactly one and at most one

### Core definition and significance

A uniqueness claim combines existence with the exclusion of distinct alternative witnesses. “At most one” omits the existence clause; “exactly one” cannot be established by merely finding a candidate. 

### Exact symbolic object and derivation

The central formal object is `∃x(P(x)∧∀y(P(y)→y=x))`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Exactly one supervisor per project: ∀p(Project(p)→∃s(Supervisor(s,p)∧∀t(Supervisor(t,p)→t=s))). A project with no supervisor violates this, and one with two distinct supervisors also violates it. 

### Why the distinction matters

One common failure is **Treating “unique” as though it means “the first result returned.”** 

**Boundary probe.** If supervisor identifiers can refer to the same person, the identity policy becomes part of the model. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Encode a matching rule that forbids duplicated award assignments and flags projects without mentors. Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∃x(P(x)∧∀y(P(y)→y=x))` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Treating “unique” as though it means “the first result returned.”” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Encode a matching rule that forbids duplicated award assignments and flags projects without mentors. **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “If supervisor identifiers can refer to the same person, the identity policy becomes part of the model.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Lesson 2.5: Alternating quantifiers in translation

### Core definition and significance

Quantifier order is a formal representation of who may depend on whom. A witness chosen after x can vary with x; an early witness must work for every x. The two orders generally cannot be exchanged. 

### Exact symbolic object and derivation

The central formal object is `∀x∃yR(x,y) versus ∃y∀xR(x,y)`. Read it in full, including all quantifier scopes, function arities, and any dependence on an intended domain. **Worked construction:** Two applicants a,b each have a different mentor m,n. Relation R={(a,m),(b,n)} satisfies ∀x(Applicant(x)→∃y(Mentor(y)∧R(x,y))), but no common mentor serves both; the unrestricted forms require domain restrictions. 

### Why the distinction matters

One common failure is **Using an unrestricted ∀x when the intended objects are applicants and mentors.** 

**Boundary probe.** A finite model clarifies dependency but does not determine what an ambiguous English sentence was intended to require. The probe is best answered by keeping the original expression next to its proposed revision. Compare their free variables, bound variables, domains, and truth conditions; do not assume that superficially similar symbols denote the same property. When a proof step is at issue, inspect every live assumption. When a semantics result is at issue, present one satisfying assignment or one falsifying tuple. A student who cannot supply either should qualify the claim as provisional rather than assert that it has been established.

### Worked application and audit record

**Transfer problem:** Translate “each student follows a researcher” and “a researcher is followed by each student.” Create a four-part audit: (1) plain-language requirement, (2) symbol table and domain, (3) exact formal representation, and (4) output with its limits. Check at least one ordinary case and one intentionally awkward case: zero eligible subjects, a shared witness, contradictory records, duplicate identifiers, or a free-variable collision—whichever exposes the subject of the lesson most sharply. If the output differs, explain which condition caused the difference. A reliable application should not hide a failed edge case; it should make the discrepancy easy to reproduce and correct.

### Practice: three graded problems

**Problem A — reconstruct.** Rebuild `∀x∃yR(x,y) versus ∃y∀xR(x,y)` without looking at it: define its atomic components, describe the argument positions in every predicate and function, and write the fully parenthesized expression where relevant. **Answer guide:** a reconstruction is correct when its parse and scopes agree with the original. If it produces a different sentence, provide a structure or interpretation that can separate the two when possible. If the object contains a transformation marker, specify the original and transformed languages separately. Merely reproducing a string does not establish understanding; explain the meaning of each operator.

**Problem B — adversarial test.** Attempt the error “Using an unrestricted ∀x when the intended objects are applicants and mentors.” on the worked example, then show why the corrected reasoning is required. **Answer guide:** first state the purported rule and how it would modify the original claim. Second, test a minimal finite case or inspect the proof side condition. Third, repair the reasoning without adding hidden premises. For a model-based test, record the actual domain and truth assignments; for a substitution, list free variables; for a proof, show which assumption is open at each step. The answer is incomplete if the purported countermodel violates a premise.

**Problem C — controlled generalization.** Apply the idea to this task: Translate “each student follows a researcher” and “a researcher is followed by each student.” **Answer guide:** write down the input data model, the exact claim being established, and one falsification attempt. Then address the qualification “A finite model clarifies dependency but does not determine what an ambiguous English sentence was intended to require.” without declaring the original result universally valid unless a general proof supports it. If the task cannot be decided from given information, identify the missing element rather than invent one. A rigorous “undetermined” is better than a confident answer to a different question.

## Unit 2 capstone — independent specification review

**Case study.** A university funding rule says every applicant must have one supervisor and no two applicants may share the same award. Produce a two-page formal reasoning memo. The opening paragraph must distinguish the original communication from the interpretation chosen for checking. Provide the signature with arities, a formula or axiom set, and at least two tests: one representative positive interpretation and one boundary or negative interpretation. When claiming an entailment, include a valid derivation or a checked countermodel. State exactly which hypotheses are independent of the formal result and how the real project would validate them. Conclude by explaining how the result would change if a key premise were relaxed.

**Evidence standard.** Declare the universe of discourse, relation argument order, and qualification predicates first. Check a universal on a zero-member restricted class, then provide a positive existential example. For a uniqueness rule, separately test missing witness and duplicated witnesses. A translation test passes when the symbolic and stated natural-language readings agree on both positive and negative edge cases. A formula may be logically precise while encoding the wrong practical meaning of “eligible” or “approved.” A good submission includes a machine-readable artifact where practical: a tiny truth table, predicate relation matrix, proof trace, or set of syntactically valid clauses. If a negative example fails to satisfy all premises, it is not evidence against the claimed entailment; correct the example before making the conclusion.

**Marking rubric (100 points).** Formal vocabulary and precise domain: 20. Faithful translation and variable scope: 20. Semantic or proof certificate: 25. Adversarial countercase and scope limitations: 20. Reproducibility and clear writing: 15. Instructors should award no proof credit for fluent prose that hides an invalid inference. Conversely, a correct formula accompanied by an inadequate plain-language explanation should not receive full communication credit. Use student-reported uncertainty as evidence of intellectual discipline when it is accurately justified.

### Unit closeout questions

1. Identify the difference between the main claim in **Conditionals in institutional rules** and **Alternating quantifiers in translation**. How would a careless reader mistakenly combine them?

2. Construct a concrete countercase to one of the unit’s tempting informal inferences, naming each interpreted symbol.

3. Explain whether the unit’s interactive models could prove a universal first-order result. State the exact finite guarantee, if any, and the evidence needed for a broader theorem.

4. Revise the running case after one relevant premise changes. Record the old and new expressions side by side.
