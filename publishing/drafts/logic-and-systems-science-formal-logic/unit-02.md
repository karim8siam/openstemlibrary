# Unit 2: Propositional Semantics and Truth Tables

**Unit objective.** Evaluate connectives using assignments, determine satisfiability and logical consequence, and detect equivalent formulas by complete comparison.

**Foundational distinction.** A single successful assignment establishes satisfiability but not validity. Conversely one assignment with true premises and false conclusion disproves consequence immediately.

**Anchoring scenario.** A lab controller must sound an alarm when heating is active and coolant is absent. Enumerate states and compare the rule with an attractive but mistaken converse.

**Interpretive boundary.** An English conditional may carry expectations of relevance or causation not represented by material implication.

## Core conceptual map

### Diagnostic lens 1: Assumptions and meaning

### Diagnostic lens 2: What an exact test establishes

### Diagnostic lens 3: Constructing a counterexample

Under ordinary inclusive disjunction, the state P=T,Q=T makes P∨Q true. Many interface labels suggest exclusive choices, so their software specifications must not borrow inclusive semantics carelessly. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

The conditional P→Q has no causal content. One can assign P=F and Q=T and make the formula true even when no physical process links P to Q. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

A truth table with three atoms has eight assignments. This is finite and supports exhaustive semantic checking. With many atoms, a naive table grows exponentially and becomes unsuitable for large production policies. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

## Unit opening investigation

Begin with the following problem: A lab controller must sound an alarm when heating is active and coolant is absent. Enumerate states and compare the rule with an attractive but mistaken converse. Write the problem in ordinary language first. Identify which words introduce conjunctions, alternatives, negations, quantifiers, or claims of necessity. Then separate object-level statements from the evaluator's assumptions. State a proposed formalization and one plausible alternative. For each, ask what observation or interpretation would distinguish them. Finally, explain which parts can be checked by logic alone and which require additional factual or policy evidence. A correct formal answer must be precise enough for another student to reproduce without guessing the intended meanings.

## Lesson 2.1: Valuations and truth functions

### 1. Central idea and precise vocabulary

A valuation assigns T or F to each atomic proposition. Complex truth values are recursively determined by connective tables. With n independent atoms there are 2^n distinct assignments. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `v(P)=T, v(Q)=F; v(P∧Q)=F`.

**Worked example:** For P true and Q false, P∧Q is false and P∨Q is true. The difference expresses two requirements versus an alternative. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not replace inclusive or with exclusive or without an explicit rule. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** At what row does the conjunction first fail, and what independent data are needed to evaluate atoms? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Enumerate four states for two laboratory interlocks. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Enumerate four states for two laboratory interlocks.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `v(P)=T, v(Q)=F; v(P∧Q)=F`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not replace inclusive or with exclusive or without an explicit rule.” and the question “At what row does the conjunction first fail, and what independent data are needed to evaluate atoms?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 2.2: Negation, conjunction and disjunction

### 1. Central idea and precise vocabulary

Classical negation reverses truth values; a conjunction is true only if every conjunct is true; inclusive disjunction is true if at least one disjunct is true. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `¬(P∧Q) ≡ (¬P∨¬Q)`.

**Worked example:** A machine cannot be both powered and open under a safety prohibition. Denying their conjunction is weaker than saying neither condition ever holds. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not apply De Morgan transformations by keeping the same connective. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** How does “either but not both” differ from the inclusive disjunction in the row T,T? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Represent a safety policy with parentheses, then make a truth table. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Represent a safety policy with parentheses, then make a truth table.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `¬(P∧Q) ≡ (¬P∨¬Q)`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not apply De Morgan transformations by keeping the same connective.” and the question “How does “either but not both” differ from the inclusive disjunction in the row T,T?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 2.3: Conditionals and biconditionals

### 1. Central idea and precise vocabulary

Material implication P→Q is false only when P is true and Q false. The biconditional P↔Q requires equal values. This is a semantic definition rather than proof of physical causation. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P→Q ≡ ¬P∨Q`.

**Worked example:** If entry is approved, a token is issued. If entry is not approved, the material conditional is true regardless of token status, so the rule alone cannot guarantee token uniqueness. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Affirming the consequent and denying the antecedent are invalid inference forms. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** What additional premise would make an observed token sufficient to infer approval? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Check an API rule for necessary versus sufficient conditions. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Check an API rule for necessary versus sufficient conditions.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P→Q ≡ ¬P∨Q`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Affirming the consequent and denying the antecedent are invalid inference forms.” and the question “What additional premise would make an observed token sufficient to infer approval?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 2.4: Satisfiability, tautology and contradiction

### 1. Central idea and precise vocabulary

Satisfiability asks for at least one truth assignment. A tautology holds under all assignments; a contradiction holds under none. These are three different semantic classifications. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P∨¬P tautology; P∧¬P contradiction`.

**Worked example:** A configuration demands P and not P simultaneously, making it unsatisfiable. Replacing the contradictory requirement with P∨¬P removes the conflict but adds no practical restriction. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not call a merely satisfiable formula a theorem or universal law. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Provide an actual satisfying assignment or explain why every assignment fails. The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Determine whether a policy conjunction admits any user state. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Determine whether a policy conjunction admits any user state.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P∨¬P tautology; P∧¬P contradiction`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not call a merely satisfiable formula a theorem or universal law.” and the question “Provide an actual satisfying assignment or explain why every assignment fails.”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 2.5: Equivalence and normal forms

### 1. Central idea and precise vocabulary

Two formulas are semantically equivalent if they agree on every valuation. Normal forms expose structure for SAT solvers and proofs, but distributive expansion can increase size. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P→(Q∧R) ≡ (¬P∨Q)∧(¬P∨R)`.

**Worked example:** An implication with a conjunctive consequent becomes two clauses. Test all eight assignments to confirm the transformation, then note that equivalence is stronger than matching on one row. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not assume a shortened formula is equivalent because a few sampled cases coincide. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** When might exhaustive enumeration become computationally expensive as atom count increases? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Reduce a small equipment access rule to CNF. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Reduce a small equipment access rule to CNF.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P→(Q∧R) ≡ (¬P∨Q)∧(¬P∨R)`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not assume a shortened formula is equivalent because a few sampled cases coincide.” and the question “When might exhaustive enumeration become computationally expensive as atom count increases?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Unit 2 integrated capstone

**Challenge.** A lab controller must sound an alarm when heating is active and coolant is absent. Enumerate states and compare the rule with an attractive but mistaken converse. Develop a short technical note with an exact formal statement, one chosen method of evaluation, and a counterexample search. The note should make at least one original decision-table row or proof trace available for checking. Explain why the result would be insufficient to justify a real-world institutional or engineering decision without premise validation. Attach a paragraph comparing the method used in this unit with a method from an earlier unit, or with a possible method to be learned later.

**Scoring rubric.** Allocate 20 points to definitions and domain, 25 to formalization, 25 to correct derivation or model checking, 15 to counterexamples and limitations, and 15 to clarity and reproducibility. A solution that asserts validity without a general argument or a complete finite enumeration receives at most partial credit. For a claim of invalidity, one genuine countermodel with all premise evaluations shown is decisive. For an application claim, assess the formal result and the evidence for inputs separately.

**Instructor follow-up.** Ask each student to change one premise and predict whether the final judgment flips. Comparison of predictions with actual outputs identifies memorization without semantic understanding. Archive the original translation, the revised translation, and the reason for revision; these form a transparent record of how the claim was sharpened.
