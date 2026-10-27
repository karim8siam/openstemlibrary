# Unit 6: Formal Reasoning and Proof Construction

**Unit objective.** Use direct proof, contrapositive, contradiction, mathematical induction, and countermodels as distinct methods.

**Foundational distinction.** Choosing the right proof form is substantive work. For universal statements, ask what an arbitrary object must satisfy; for existential statements, provide a legitimate witness.

**Anchoring scenario.** For a claim about every natural number, compare tests of the first hundred inputs with a base case plus inductive step. The former provides evidence; the latter can establish a theorem.

**Interpretive boundary.** An invalid argument requires a countermodel, not merely a doubtful premise or an unrelated example.

## Core conceptual map

### Diagnostic lens 1: Assumptions and meaning

### Diagnostic lens 2: What an exact test establishes

### Diagnostic lens 3: Constructing a counterexample

An inductive step without a base case leaves an entire recursive family unsupported. Conversely checking the base case alone gives no guarantee about later inputs. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

A counterexample to a universal statement must actually lie within the quantified domain and violate the property. An out-of-domain exception is irrelevant. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

Classical contradiction proofs often rely on double-negation elimination; constructive work must mark that dependence explicitly rather than import a classical rule silently. A responsible solution states a semantic domain, separates definitions from empirical observations, and identifies the particular output that would refute the assertion. The student should carry this distinction forward to the worked cases rather than substitute confidence for a visible check.

## Unit opening investigation

Begin with the following problem: For a claim about every natural number, compare tests of the first hundred inputs with a base case plus inductive step. The former provides evidence; the latter can establish a theorem. Write the problem in ordinary language first. Identify which words introduce conjunctions, alternatives, negations, quantifiers, or claims of necessity. Then separate object-level statements from the evaluator's assumptions. State a proposed formalization and one plausible alternative. For each, ask what observation or interpretation would distinguish them. Finally, explain which parts can be checked by logic alone and which require additional factual or policy evidence. A correct formal answer must be precise enough for another student to reproduce without guessing the intended meanings.

## Lesson 6.1: Direct proofs and witness construction

### 1. Central idea and precise vocabulary

Start with the assumptions and derive a target through justified steps. A universal proof treats an arbitrary object; an existential proof supplies a witness that satisfies the declared conditions. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `From ∀x(P(x)→Q(x)) and P(a), derive Q(a)`.

**Worked example:** By universal instantiation obtain P(a)→Q(a). Together with P(a), implication elimination yields Q(a). The proof states both the instantiation and the rule. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** An example cannot establish a universal assertion unless a general argument explains why it applies to any element. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** If the domain changes, which premises need re-evaluation? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Prove a rule about each member of a validated dataset class. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Prove a rule about each member of a validated dataset class.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `From ∀x(P(x)→Q(x)) and P(a), derive Q(a)`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “An example cannot establish a universal assertion unless a general argument explains why it applies to any element.” and the question “If the domain changes, which premises need re-evaluation?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 6.2: Proof by contrapositive

### 1. Central idea and precise vocabulary

For classical material implication P→Q, the contrapositive ¬Q→¬P is equivalent. This provides a method when failure of Q reveals impossibility of P. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P→Q ≡ ¬Q→¬P`.

**Worked example:** If a number is divisible by four then it is even. Prove the contrapositive: if a number is odd, it cannot be divisible by four. State the integer definition used. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** The inverse ¬P→¬Q and converse Q→P are not contrapositives. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Does the equivalence persist for an intuitionistic treatment of all analogous transformations? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Explain a machine safety exclusion through contrapositive reasoning. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Explain a machine safety exclusion through contrapositive reasoning.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P→Q ≡ ¬Q→¬P`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “The inverse ¬P→¬Q and converse Q→P are not contrapositives.” and the question “Does the equivalence persist for an intuitionistic treatment of all analogous transformations?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 6.3: Contradiction and reductio

### 1. Central idea and precise vocabulary

A reductio argument introduces a temporary assumption and derives absurdity; the discharge rule depends on classical or constructive logic. Distinguish contradiction elimination from double-negation elimination. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `Assume ¬P; derive ⊥; infer ¬¬P (and P classically)`.

**Worked example:** Suppose two otherwise distinct integers are both claimed to be the unique minimum. Derive their mutual ≤ relations and antisymmetry to conclude equality, contradicting distinctness. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Do not invoke contradiction without identifying the pair of incompatible claims. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Would the same proof work without excluded middle or double-negation elimination? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Inspect an unsatisfiable requirements set and extract the conflict. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Inspect an unsatisfiable requirements set and extract the conflict.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `Assume ¬P; derive ⊥; infer ¬¬P (and P classically)`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Do not invoke contradiction without identifying the pair of incompatible claims.” and the question “Would the same proof work without excluded middle or double-negation elimination?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 6.4: Induction and recursive definitions

### 1. Central idea and precise vocabulary

Induction uses a base case and step from k to k+1 for a well-founded domain. Strong induction and structural induction generalize this pattern. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `Base P(0); ∀k(P(k)→P(k+1)) ⇒ ∀n P(n)`.

**Worked example:** Prove 1+2+…+n=n(n+1)/2: check n=1, assume the formula for k and add k+1, simplifying to (k+1)(k+2)/2. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** Checking many cases is not an inductive proof; the induction hypothesis must be used in the general step. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** Why does the base case matter even if the algebra in the induction step is flawless? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Reason about a recursively defined parser grammar. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Reason about a recursively defined parser grammar.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `Base P(0); ∀k(P(k)→P(k+1)) ⇒ ∀n P(n)`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “Checking many cases is not an inductive proof; the induction hypothesis must be used in the general step.” and the question “Why does the base case matter even if the algebra in the induction step is flawless?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Lesson 6.5: Counterexamples and proof review

### 1. Central idea and precise vocabulary

To refute ∀xP(x), identify a single domain element with ¬P. To refute entailment, exhibit a model with true premises and false conclusion. Proof review looks for hidden scope shifts. In this lesson, write down the syntax separately from the semantic interpretation. A notation choice should simplify comparison, not hide an extra premise. When a variable occurs more than once, keep its interpretation fixed within the test. If ordinary-language content is underspecified, state a working definition explicitly and report how a different definition could change the result. This practice matters most when a formula is later embedded in software and readers can no longer see the designer’s intention.

### 2. Formal object and worked walkthrough

**Canonical object:** `P→Q, Q ⊭ P`.

**Worked example:** Let P=F and Q=T. The conditional and Q are true while P is false; therefore the inference affirming the consequent is invalid. Start by naming the starting assumptions and the intended result. If this is an entailment claim, try to build an assignment or structure satisfying every premise while falsifying the conclusion. If this is a transformation, calculate both sides under an informative assignment before claiming equivalence, and give a general reason for all remaining cases. If this is a proof step, cite its legitimate introduction or elimination rule and keep the scope of assumptions visible. If it is an application rule, distinguish necessary from sufficient conditions. The same disciplined workflow should be usable by a reader who rejects the story but accepts the formal assumptions.

### 3. Analysis of the countercase

**Common failure:** A nonrepresentative anecdote does not refute a statement that was only probabilistic or restricted to a specific domain. Examine this failure in two deliberately separate ways. Semantically, ask whether an exact interpretation can expose the defect. Syntactically, ask whether the proposed step is a member of the permitted rule set. These answers are not always interchangeable: a specific valuation refutes an entailment, while a missing proof does not generally refute it. Do not count merely repeated numerical trials as a universal demonstration. Write a minimal countercase and then test it against each premise independently. If the attempt fails, explain which premise blocked the counterexample and whether it suggests a valid result or merely a poor choice of model.

**Boundary question:** What is the shortest independent check of a claimed countermodel? The answer should identify the exact condition being changed and the conclusion that may or may not survive. Consider domain restrictions, unavailable evidence, ambiguity of language, and the distinction between a pedagogical finite model and a theorem over all interpretations. Many logic mistakes are failures to track one of these four changes, even when every displayed formula looks plausible.

### 4. Transfer to a real reasoning workflow

**Applied scenario:** Create a counterexample log with valuation and decision rule. Draft a tiny audit trail containing a domain declaration, a glossary of symbols, the input facts, the inference or semantic test, and the final classification. State one observable that the formal tool does *not* calculate. For a database example, do not silently treat absence of a row as a false statement unless a closed-world convention has been adopted. For a scientific claim, distinguish the fact that a sentence was supplied as a premise from the independent evidence needed to establish it. For a system rule, show the outcome of an edge case and identify who is responsible for resolving the specification if two interpretations conflict.

### 5. Guided exercises with solution guidance

**Exercise A — identification and translation.** For the situation “Create a counterexample log with valuation and decision rule.”, write the assumptions as short declarative propositions or predicates. Include at least two alternative translations if the original wording is ambiguous. **Solution guidance:** first list the relevant people or system states and any excluded cases; next choose atomic predicates before adding connectives; finally identify what additional evidence would decide between rival translations. There may not be a unique answer until the context is fixed.

**Exercise B — exact check.** Analyze the displayed object `P→Q, Q ⊭ P`. Show a complete derivation if it is a consequence, an exhaustive valuation table if it has only a few propositional atoms, or a fully specified small structure when a semantic countermodel is more appropriate. **Solution guidance:** state which kind of claim is being assessed first. Then justify each inference, assignment, or interpretation. A correct table row must satisfy the stipulated meanings of each connective; a correct proof must not cross a discharged-assumption boundary.

**Exercise C — controlled perturbation.** Consider the error “A nonrepresentative anecdote does not refute a statement that was only probabilistic or restricted to a specific domain.” and the question “What is the shortest independent check of a claimed countermodel?”. Change exactly one assumption, connective, quantifier dependency, or rule of inference. Determine whether the original conclusion still holds. **Solution guidance:** make the changed hypothesis visible; compute the new test rather than assuming the old verdict transfers; explain why the result is sensitive or insensitive to the change. Where the statement becomes untestable from provided information, write **undetermined**, not true or false by guesswork.

## Unit 6 integrated capstone

**Challenge.** For a claim about every natural number, compare tests of the first hundred inputs with a base case plus inductive step. The former provides evidence; the latter can establish a theorem. Develop a short technical note with an exact formal statement, one chosen method of evaluation, and a counterexample search. The note should make at least one original decision-table row or proof trace available for checking. Explain why the result would be insufficient to justify a real-world institutional or engineering decision without premise validation. Attach a paragraph comparing the method used in this unit with a method from an earlier unit, or with a possible method to be learned later.

**Scoring rubric.** Allocate 20 points to definitions and domain, 25 to formalization, 25 to correct derivation or model checking, 15 to counterexamples and limitations, and 15 to clarity and reproducibility. A solution that asserts validity without a general argument or a complete finite enumeration receives at most partial credit. For a claim of invalidity, one genuine countermodel with all premise evaluations shown is decisive. For an application claim, assess the formal result and the evidence for inputs separately.

**Instructor follow-up.** Ask each student to change one premise and predict whether the final judgment flips. Comparison of predictions with actual outputs identifies memorization without semantic understanding. Archive the original translation, the revised translation, and the reason for revision; these form a transparent record of how the claim was sharpened.
