# Unit 1: Logical Language and Arguments

**Unit objective.** Distinguish sentences from propositions, recognize premises and conclusions, and examine validity without confusing truth with good reasoning.

**Foundational distinction.** A mathematical proof cannot repair an ambiguity in the claim being proved. The first obligation is to establish the intended vocabulary and the role of each sentence in the argument.

**Anchoring scenario.** Admissions policy: A requirement says that a candidate qualifies if they possess a degree and a language certificate. Does this mean both certificates are necessary, or only sufficient? Write two rival interpretations before evaluating a decision.

**Interpretive boundary.** Formalization records logical structure; it does not establish that the nonlogical descriptions accurately portray the world.

## Core conceptual map

### Diagnostic lens 1: Assumptions and meaning

### Diagnostic lens 2: What an exact test establishes

### Diagnostic lens 3: Constructing a counterexample

If a report says that all candidates with verified IDs can register, being registered does not prove that the ID was verified. This reverses the stated conditional. The missing biconditional should not be silently supplied. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

A scientific instrument can have true output by coincidence despite unreliable calibration. Similarly a deductively invalid argument can have a true conclusion. Evaluate evidence for the conclusion and relation of premises separately. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

A material defect log states that either the sensor drifted or the sample was mislabeled. A later measurement rules out drift. The inference to mislabeling depends on whether the original disjunction was intended as exhaustive; otherwise an omitted third explanation remains possible. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

## Unit opening investigation

Begin with the following problem: Admissions policy: A requirement says that a candidate qualifies if they possess a degree and a language certificate. Does this mean both certificates are necessary, or only sufficient? Write two rival interpretations before evaluating a decision. Write the problem in ordinary language first. Identify which words introduce conjunctions, alternatives, negations, quantifiers, or claims of necessity. Then separate object-level statements from the evaluator's assumptions. State a proposed formalization and one plausible alternative. For each, ask what observation or interpretation would distinguish them. Finally, explain which parts can be checked by logic alone and which require additional factual or policy evidence. A correct formal answer must be precise enough for another student to reproduce without guessing the intended meanings.

## Lesson 1.1: Premises and conclusions

### 1. Central idea and precise vocabulary

An argument is a directed relationship between assertions: certain sentences are offered as reasons and another is presented as what follows. Indicator words help but do not determine the structure. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P, P→Q ⊢ Q`.

**Worked example:** If the instrument is calibrated, its error certificate is current. The instrument is calibrated. Therefore its certificate is current. The inference is a valid modus ponens form. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not treat a rhetorical question or a mere list of observations as an argument. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** What if the first conditional is false in the actual laboratory? The form remains valid but the argument may not be sound. The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Audit a short laboratory report and mark the hidden conclusion. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Audit a short laboratory report and mark the hidden conclusion.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P, P→Q ⊢ Q`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not treat a rhetorical question or a mere list of observations as an argument.” and the question “What if the first conditional is false in the actual laboratory? The form remains valid but the argument may not be sound.”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 1.2: Statements, propositions and context

### 1. Central idea and precise vocabulary

A proposition has a determinate truth condition after relevant context is fixed. An instruction, question, vague comparison or sentence with an unresolved indexical may not express a single proposition. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P = “the reading exceeds 50 °C at 12:00 UTC”`.

**Worked example:** “It is hot here” lacks a fixed location and threshold. Replace it with a timestamp, place, measurable quantity and comparison. Now different auditors can evaluate the same claim. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not mistake grammatical declarative mood for unambiguous truth conditions. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** How could a different reference time or measurement method change the proposition without changing its grammar? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Rewrite two research hypotheses as testable propositions with explicit units. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Rewrite two research hypotheses as testable propositions with explicit units.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P = “the reading exceeds 50 °C at 12:00 UTC”`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not mistake grammatical declarative mood for unambiguous truth conditions.” and the question “How could a different reference time or measurement method change the proposition without changing its grammar?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 1.3: Logical form and substitution

### 1. Central idea and precise vocabulary

An argument form displays what remains invariant when content terms are replaced consistently. Repeated occurrences of P must represent the same whole claim. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P∨Q, ¬P ⊢ Q`.

**Worked example:** Either the server is offline or the sensor has failed. The server is not offline. Therefore the sensor has failed. Abstracting leaves a valid disjunctive syllogism. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** It is illegal to replace one occurrence of P with a new meaning halfway through a proof. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Does the result survive every interpretation of the atomic propositions? Show why it must. The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Classify the form of a safety alert using only P and Q. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Classify the form of a safety alert using only P and Q.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P∨Q, ¬P ⊢ Q`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “It is illegal to replace one occurrence of P with a new meaning halfway through a proof.” and the question “Does the result survive every interpretation of the atomic propositions? Show why it must.”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 1.4: Validity versus truth

### 1. Central idea and precise vocabulary

Validity excludes the configuration where all premises are true and the conclusion false. It does not say whether the premises or conclusion are actually true. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `Γ ⊨ C iff no valuation makes Γ true and C false`.

**Worked example:** All metal samples are edible; this coupon is a metal sample; so this coupon is edible. The premises are unreliable, yet the syllogistic structure preserves truth under every interpretation. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not label an argument invalid merely because the conclusion sounds absurd or undesirable. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Construct an argument with a true conclusion but invalid form. The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Separate logical assessment from empirical checking in a product claim. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Separate logical assessment from empirical checking in a product claim.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `Γ ⊨ C iff no valuation makes Γ true and C false`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not label an argument invalid merely because the conclusion sounds absurd or undesirable.” and the question “Construct an argument with a true conclusion but invalid form.”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 1.5: Soundness, strength and charitable reconstruction

### 1. Central idea and precise vocabulary

A deductively sound argument is valid and has true premises. Inductive strength is a different assessment. Charitable reconstruction supplies plausible missing premises without smuggling in a conclusion. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `Sound argument = valid form + true premises`.

**Worked example:** A brochure says “qualified applicants have references; Mira has references; therefore Mira is qualified.” This affirms the consequent. A repair might add a biconditional, but that is a new empirical assumption. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not confuse making an argument valid with proving its newly added premise. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** What additional evidence, not rhetorical confidence, would establish the repaired premise? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Write an argument map separating assumptions from evidence. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Write an argument map separating assumptions from evidence.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `Sound argument = valid form + true premises`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not confuse making an argument valid with proving its newly added premise.” and the question “What additional evidence, not rhetorical confidence, would establish the repaired premise?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Unit 1 integrated capstone

**Challenge.** Admissions policy: A requirement says that a candidate qualifies if they possess a degree and a language certificate. Does this mean both certificates are necessary, or only sufficient? Write two rival interpretations before evaluating a decision. Develop a short technical note with an exact formal statement, one chosen method of evaluation, and a counterexample search. The note should make at least one original decision-table row or proof trace available for checking. Explain why the result would be insufficient to justify a real-world institutional or engineering decision without premise validation. Attach a paragraph comparing the method used in this unit with a method from an earlier unit, or with a possible method to be learned later.

**Scoring rubric.** Allocate 20 points to definitions and domain, 25 to formalization, 25 to correct derivation or model checking, 15 to counterexamples and limitations, and 15 to clarity and reproducibility. A solution that asserts validity without a general argument or a complete finite enumeration receives at most partial credit. For a claim of invalidity, one genuine countermodel with all premise evaluations shown is decisive. For an application claim, assess the formal result and the evidence for inputs separately.

**Instructor follow-up.** Ask each student to change one premise and predict whether the final judgment flips. Comparison of predictions with actual outputs identifies memorization without semantic understanding. Archive the original translation, the revised translation, and the reason for revision; these form a transparent record of how the claim was sharpened.
