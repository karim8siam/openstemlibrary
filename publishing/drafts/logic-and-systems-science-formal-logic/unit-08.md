# Unit 8: Applications and Responsible Formalization

**Unit objective.** Use logic for specifications, decision tables, automated reasoning, model checking, rule systems, and critical argument analysis.

**Foundational distinction.** A formally correct system can enforce the wrong requirement. Validation of the translation from stakeholders to logical sentences is separate from correctness of the proof engine.

**Anchoring scenario.** An access-control policy grants data access under a conjunction of authorized role, consent, and active membership. Test ordinary, exceptional, and missing-information cases.

**Interpretive boundary.** Passing a finite demonstration is not evidence that a production system is secure, fair, complete, or compliant.

## Core conceptual map

### Diagnostic lens 1: Assumptions and meaning

### Diagnostic lens 2: What an exact test establishes

### Diagnostic lens 3: Constructing a counterexample

An authorization invariant specifies a condition on every reachable state; testing one screenshot does not prove preservation under every possible transition. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

A satisfiability solver may find an assignment satisfying a defective requirement specification. Requirements validation is distinct from solver correctness. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

A decision rule can be logically unambiguous but still introduce unacceptable discrimination or operational harm. Policy review is a separate responsibility. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

## Unit opening investigation

Begin with the following problem: An access-control policy grants data access under a conjunction of authorized role, consent, and active membership. Test ordinary, exceptional, and missing-information cases. Write the problem in ordinary language first. Identify which words introduce conjunctions, alternatives, negations, quantifiers, or claims of necessity. Then separate object-level statements from the evaluator's assumptions. State a proposed formalization and one plausible alternative. For each, ask what observation or interpretation would distinguish them. Finally, explain which parts can be checked by logic alone and which require additional factual or policy evidence. A correct formal answer must be precise enough for another student to reproduce without guessing the intended meanings.

## Lesson 8.1: Specification and invariants

### 1. Central idea and precise vocabulary

A specification states the behaviors permitted or required by a system. An invariant is a condition intended to hold in every reachable state, not just in an example run. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `Invariant: access ⇒ authorized∧consented`.

**Worked example:** For a request with authorization T and consent F, access must be F. This is a necessary condition, not sufficient for service availability. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** A passing unit test is not a general proof that an invariant holds after every transition. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Could a new background process invalidate the invariant even if the user interface appears correct? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Convert a short product requirement into a predicate with explicitly defined variables. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Convert a short product requirement into a predicate with explicitly defined variables.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `Invariant: access ⇒ authorized∧consented`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “A passing unit test is not a general proof that an invariant holds after every transition.” and the question “Could a new background process invalidate the invariant even if the user interface appears correct?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 8.2: SAT and constraint encodings

### 1. Central idea and precise vocabulary

Propositional satisfiability solves whether a finite Boolean formula admits an assignment. Conjunctive normal form is standard for many SAT procedures; encodings must preserve the intended model. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `(P∨Q)∧(¬P∨R)∧¬R`.

**Worked example:** With R false, the second clause forces ¬P. The first clause then forces Q. Assignment P=F,Q=T,R=F satisfies the system. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** A solver reports satisfiable formulas, not whether the underlying requirements are ethically or empirically acceptable. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** How can one independently test the solver output against every original clause? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Encode a simple course scheduling restriction as Boolean clauses. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Encode a simple course scheduling restriction as Boolean clauses.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `(P∨Q)∧(¬P∨R)∧¬R`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “A solver reports satisfiable formulas, not whether the underlying requirements are ethically or empirically acceptable.” and the question “How can one independently test the solver output against every original clause?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 8.3: Decision tables and rule engines

### 1. Central idea and precise vocabulary

Decision tables enumerate relevant conditions and outcomes. Rule priority and incomplete inputs must be explicit, or unexpected overlaps can produce inconsistent behavior. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `Role∧Consent∧Active → Permit`.

**Worked example:** If Role=T, Consent=T, Active=F, a policy requiring all three must deny. A table also needs a decision for incomplete or unknown consent. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not infer Permit from one requirement unless the full conjunction is satisfied. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Are there condition combinations left without any specified result? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Audit a student application routing rule. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Audit a student application routing rule.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `Role∧Consent∧Active → Permit`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not infer Permit from one requirement unless the full conjunction is satisfied.” and the question “Are there condition combinations left without any specified result?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 8.4: Temporal and transition reasoning

### 1. Central idea and precise vocabulary

System behavior unfolds as state transitions. A state invariant differs from a liveness condition: “never enter error” and “eventually respond” have different temporal meanings. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `Safety: G¬Error; liveness: FRespond (LTL notation)`.

**Worked example:** A model checker examines a transition structure. A server that never fails but remains idle forever may meet a safety rule yet violate a timely-response goal. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** A finite trace cannot by itself prove an unbounded liveness property for every path. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** What assumptions about fairness or scheduling are hidden in “eventually”? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Sketch states of an admission portal during submission. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Sketch states of an admission portal during submission.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `Safety: G¬Error; liveness: FRespond (LTL notation)`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “A finite trace cannot by itself prove an unbounded liveness property for every path.” and the question “What assumptions about fairness or scheduling are hidden in “eventually”?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 8.5: Auditability, bias and model limits

### 1. Central idea and precise vocabulary

Formalization is one layer of assurance. Stakeholder interpretations, data quality, access rights, disparate impacts and update control require additional checks outside logical validity alone. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `Verified proof ≠ validated requirement`.

**Worked example:** An eligibility rule is implemented exactly, but its eligibility category was imported from an obsolete source. The derivation can be correct while the operational outcome is wrong. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not advertise a finite toy checker as a security audit or legal compliance evaluation. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Which evidence would justify accepting a production rule after formal verification? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Prepare a change log that records requirements, translations, tests and human sign-off. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Prepare a change log that records requirements, translations, tests and human sign-off.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `Verified proof ≠ validated requirement`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not advertise a finite toy checker as a security audit or legal compliance evaluation.” and the question “Which evidence would justify accepting a production rule after formal verification?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Unit 8 integrated capstone

**Challenge.** An access-control policy grants data access under a conjunction of authorized role, consent, and active membership. Test ordinary, exceptional, and missing-information cases. Develop a short technical note with an exact formal statement, one chosen method of evaluation, and a counterexample search. The note should make at least one original decision-table row or proof trace available for checking. Explain why the result would be insufficient to justify a real-world institutional or engineering decision without premise validation. Attach a paragraph comparing the method used in this unit with a method from an earlier unit, or with a possible method to be learned later.

**Scoring rubric.** Allocate 20 points to definitions and domain, 25 to formalization, 25 to correct derivation or model checking, 15 to counterexamples and limitations, and 15 to clarity and reproducibility. A solution that asserts validity without a general argument or a complete finite enumeration receives at most partial credit. For a claim of invalidity, one genuine countermodel with all premise evaluations shown is decisive. For an application claim, assess the formal result and the evidence for inputs separately.

**Instructor follow-up.** Ask each student to change one premise and predict whether the final judgment flips. Comparison of predictions with actual outputs identifies memorization without semantic understanding. Archive the original translation, the revised translation, and the reason for revision; these form a transparent record of how the claim was sharpened.
