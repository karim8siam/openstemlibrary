# Unit 3: Proof Systems and Derivations

**Unit objective.** Apply introduction and elimination rules, understand subproof discharge, compare deduction with semantic checking, and record every inference.

**Foundational distinction.** A written proof is a finite certificate whose local steps can be checked. A line that merely seems plausible is not certified until its premises and rule are identified.

**Anchoring scenario.** A system description supplies A→B and A. A correct derivation obtains B by implication elimination; it does not infer A from B without an additional premise.

**Interpretive boundary.** Different proof systems may require different formatting, even when they derive the same logical consequences.

## Core conceptual map

### Diagnostic lens 1: Assumptions and meaning

### Diagnostic lens 2: What an exact test establishes

### Diagnostic lens 3: Constructing a counterexample

The natural-deduction rule for implication introduction closes an assumption box. If a student keeps using that assumption globally, the claimed conclusion may no longer follow from the original premises. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

Semantic tableaux begin with the premises and the negation of the conclusion. A fully expanded open branch is valuable: it provides a specific model that defeats the entailment. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

A sequent system can be proof-theoretically different from Fitch natural deduction yet sound and complete for the same classical consequence relation; checking requires respecting the particular rule set. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

## Unit opening investigation

Begin with the following problem: A system description supplies A→B and A. A correct derivation obtains B by implication elimination; it does not infer A from B without an additional premise. Write the problem in ordinary language first. Identify which words introduce conjunctions, alternatives, negations, quantifiers, or claims of necessity. Then separate object-level statements from the evaluator's assumptions. State a proposed formalization and one plausible alternative. For each, ask what observation or interpretation would distinguish them. Finally, explain which parts can be checked by logic alone and which require additional factual or policy evidence. A correct formal answer must be precise enough for another student to reproduce without guessing the intended meanings.

## Lesson 3.1: Inference rules and proof certificates

### 1. Central idea and precise vocabulary

An inference rule licenses a conclusion from premises with a specific form. A certificate should record each step and its supporting lines. Rule soundness means each permitted step preserves truth. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P, P→Q ⊢ Q (→-elimination)`.

**Worked example:** From A and A→B, write line 1 A, line 2 A→B, line 3 B, justified by lines 1 and 2. A checker needs no guess about intended meaning. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not cite a conclusion as its own justification or silently invoke an unstated premise. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Can the same trace be audited if every proposition is renamed consistently? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Design a three-line proof trace for a deployment rule. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Design a three-line proof trace for a deployment rule.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P, P→Q ⊢ Q (→-elimination)`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not cite a conclusion as its own justification or silently invoke an unstated premise.” and the question “Can the same trace be audited if every proposition is renamed consistently?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 3.2: Conjunction and disjunction in natural deduction

### 1. Central idea and precise vocabulary

Conjunction introduction combines two established results; elimination extracts either component. Disjunction introduction weakens a claim, while elimination requires treating each possible case. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P,Q ⊢ P∧Q; P∧Q ⊢ P`.

**Worked example:** Given P∧Q, deriving P is immediate. Deriving an unrelated R is not. For P∨Q and both P→R and Q→R, reason by cases to derive R. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** A disjunction does not authorize choosing whichever disjunct is convenient. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** What must be shown separately in both branches of a proof by cases? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Show how an incident report combines two verified conditions. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Show how an incident report combines two verified conditions.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P,Q ⊢ P∧Q; P∧Q ⊢ P`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “A disjunction does not authorize choosing whichever disjunct is convenient.” and the question “What must be shown separately in both branches of a proof by cases?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 3.3: Implication introduction and assumption scope

### 1. Central idea and precise vocabulary

To prove P→Q, temporarily assume P and derive Q; then discharge the assumption. The conclusion outside the subproof must not rely on the discharged assumption except through the conditional. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `From [P] ... Q infer P→Q`.

**Worked example:** Suppose P∧Q. Extract Q and close the scope to obtain (P∧Q)→Q. If P∧Q were merely hypothesized, claiming Q without the conditional would be illicit. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Never export a sentence from a closed scope as if it were globally established. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** How is a temporary premise different from an empirical assertion about the application? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Use an assumption box to justify a conditional in a program invariant. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Use an assumption box to justify a conditional in a program invariant.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `From [P] ... Q infer P→Q`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Never export a sentence from a closed scope as if it were globally established.” and the question “How is a temporary premise different from an empirical assertion about the application?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 3.4: Sequents and structural reasoning

### 1. Central idea and precise vocabulary

A sequent Γ ⊢ φ expresses derivability from assumptions. Weakening, contraction and exchange handle contexts in classical sequent systems; left and right rules expose connectives. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P∧Q ⊢ P`.

**Worked example:** For Γ containing P∧Q, a left-conjunction rule makes P and Q available. Compare this symbolic maneuver with semantic reasoning about what truth of a conjunction entails. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not interpret every sequent as a material implication formula without stating the translation and system. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** How do context rules change under resource-sensitive logical systems? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Relate proof trees to a static analyzer diagnostic. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Relate proof trees to a static analyzer diagnostic.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P∧Q ⊢ P`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not interpret every sequent as a material implication formula without stating the translation and system.” and the question “How do context rules change under resource-sensitive logical systems?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 3.5: Tableaux and counterbranches

### 1. Central idea and precise vocabulary

A semantic tableau expands complex formulas into constraints on branches. A branch closes when it contains a literal and its negation. An open completed branch can exhibit a countermodel. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `To test Γ⊨C, start with Γ and ¬C`.

**Worked example:** Test P→Q, P ⊨ Q by assuming P→Q, P and ¬Q. The implication splits into ¬P or Q; both branches contradict existing literals. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** An open unfinished branch does not establish a countermodel until the remaining formulas have been expanded. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Can the countermodel from an open branch be independently confirmed by direct evaluation? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Trace a small automated validity checker. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Trace a small automated validity checker.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `To test Γ⊨C, start with Γ and ¬C`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “An open unfinished branch does not establish a countermodel until the remaining formulas have been expanded.” and the question “Can the countermodel from an open branch be independently confirmed by direct evaluation?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Unit 3 integrated capstone

**Challenge.** A system description supplies A→B and A. A correct derivation obtains B by implication elimination; it does not infer A from B without an additional premise. Develop a short technical note with an exact formal statement, one chosen method of evaluation, and a counterexample search. The note should make at least one original decision-table row or proof trace available for checking. Explain why the result would be insufficient to justify a real-world institutional or engineering decision without premise validation. Attach a paragraph comparing the method used in this unit with a method from an earlier unit, or with a possible method to be learned later.

**Scoring rubric.** Allocate 20 points to definitions and domain, 25 to formalization, 25 to correct derivation or model checking, 15 to counterexamples and limitations, and 15 to clarity and reproducibility. A solution that asserts validity without a general argument or a complete finite enumeration receives at most partial credit. For a claim of invalidity, one genuine countermodel with all premise evaluations shown is decisive. For an application claim, assess the formal result and the evidence for inputs separately.

**Instructor follow-up.** Ask each student to change one premise and predict whether the final judgment flips. Comparison of predictions with actual outputs identifies memorization without semantic understanding. Archive the original translation, the revised translation, and the reason for revision; these form a transparent record of how the claim was sharpened.
