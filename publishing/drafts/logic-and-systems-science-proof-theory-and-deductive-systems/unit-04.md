# Unit 4 — Sequent calculus and structural discipline

**Purpose.** Sequents expose assumptions on the left and conclusions on the right, enabling local proof search.

**Running application.** A static-analysis engine constructs inference trees from program contracts.

**Dangerous assumption.** Classical multiple-conclusion sequents and intuitionistic single-conclusion sequents differ.

## Research orientation and operational meaning

Sequent calculus reorganizes a proof into a tree where the principal connective in a sequent suggests the next backward step. It is valuable for automated proof search because there is usually a finite number of local patterns to try. However, the search tree may branch explosively. The calculus also makes differences between classical and intuitionistic derivability visible in their right-hand context structure.

Proof search should retain a precise rule set, not simply a bag of heuristics. For example, a goal of the form Γ⇒A∧B decomposes into Γ⇒A and Γ⇒B. A goal Γ⇒A→B reduces to Γ,A⇒B. A backwards tree that hits identity on all branches certifies the original sequent. An unclosed search frontier is unfinished business, not a countermodel.

The continuing case in this unit is **Static program contract checker**, specifically **search must respect the exact structural rules of the declared calculus**. The main complication is **a tool checking preconditions and postconditions using sequent rules**. A formal report should record what is defined inside the logic and what requires a separate observation or human specification. The expected deliverable is: **Every closed proof-search branch must end in an initial sequent or licensed rule.** This requirement makes the case genuinely useful rather than merely decorative; the proof language solves the implication problem only after the relevant facts have been expressed as formulas.

## Working with derivations rather than slogans

A sequent rule transforms a judgment into one or more simpler premise judgments. In backward proof search, this can be read as a branching instruction. Keep the antecedent and succedent side distinct: the same connective has different left and right rules because assuming a formula and trying to prove a formula are different tasks.

Structural rules govern usage rather than the meaning of connectives. You may weaken an assumption context in ordinary classical logic, but resource-sensitive systems change what operations are legal. A statement about cut elimination or identity expansion must always name the intended calculus, since different systems have different admissible rules.

A deliberately minimal audit record has five fields: formal premises, goal formula, inference-rule schema, concrete substitution into that schema, and remaining open obligations. The audit record should not confuse a witness term with an interpretation, a goal with an assumption, or a line of output with a theorem. When a rule has side conditions, record them just as carefully as the displayed conclusion. In a system that discharges assumptions, the scope of the discharge belongs to the proof object.

When the answer to a mathematical question is negative, supply evidence of the right kind. For finite propositional entailment, one satisfying valuation for the premises that falsifies the goal is decisive. For a claimed formula in a first-order setting, a legitimate structure and assignment can serve as a countermodel. For search failure on an undecidable class, however, no verdict follows. This evidence hierarchy will recur through every chapter, because it is central to responsible research and publication.

## Lesson 4.1 — Sequents and identity

### Exact rule or metatheorem

**Formal content.** A sequent Γ ⇒ Δ is read as: if every formula on the left is true, at least one on the right is true. For a single-succedent intuitionistic calculus Γ ⇒ A, the right side contains at most one formula. Identity is A ⇒ A.

### Worked argument with line-by-line reasoning

**Worked demonstration.** The identity sequent P ⇒ P is an initial derivation. By right conjunction, P,Q ⇒ P∧Q follows from P,Q ⇒ P and P,Q ⇒ Q. Contexts record dependencies explicitly.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **sequents and identity** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Conflating a sequent with a material implication formula in the object language, or assuming an empty succedent means a valid tautology.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Write the semantic reading of P,Q ⇒ R,S. **Solution or proof outline.** Every valuation satisfying P and Q satisfies at least one of R,S; equivalently (P∧Q)→(R∨S). The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** What is the reading of Γ ⇒ with an empty succedent in classical logic? **Expected explanation.** It expresses that Γ is jointly unsatisfiable. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **sequents and identity** to **static program contract checker** in the setting **search must respect the exact structural rules of the declared calculus**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool checking preconditions and postconditions using sequent rules**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 4.2 — Structural rules

### Exact rule or metatheorem

**Formal content.** Weakening permits extra assumptions; contraction merges duplicate assumptions; exchange reorders them if contexts are lists. Structural rules depend on the chosen calculus and are restricted in linear or relevant logics.

### Worked argument with line-by-line reasoning

**Worked demonstration.** From P ⇒ P obtain P,Q ⇒ P by left weakening. If contexts are multisets, exchange is implicit. From P,P ⇒ Q contraction allows P ⇒ Q only when the premise derivation is actually available.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **structural rules** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Using contraction or weakening silently in a resource-sensitive calculus that omits them.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Show how P ⇒ P gives P,R ⇒ P in classical LK. **Solution or proof outline.** Apply weakening-left to add R. The original derivation remains the premise of the new rule. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Why is resource logic different? **Expected explanation.** Linear logic treats repeated or discarded assumptions as meaningful; structural rules are controlled. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **structural rules** to **static program contract checker** in the setting **search must respect the exact structural rules of the declared calculus**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool checking preconditions and postconditions using sequent rules**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 4.3 — Conjunction left and right

### Exact rule or metatheorem

**Formal content.** For a standard single-conclusion intuitionistic calculus, ∧L replaces an assumed A∧B by assumptions A,B; ∧R combines proofs of Γ⇒A and Γ⇒B into Γ⇒A∧B.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Build P∧Q ⇒ Q∧P. Apply ∧L backwards to get P,Q ⇒ Q∧P; apply ∧R backwards, creating P,Q⇒Q and P,Q⇒P. Both are identity sequents plus weakening.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **conjunction left and right** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Taking Γ⇒A∧B from Γ⇒A alone, which overlooks the other ∧R premise.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Sketch a sequent proof of A∧B ⇒ A. **Solution or proof outline.** Use ∧L to reduce to A,B⇒A, then identity and weakening. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Does ∧R duplicate or consume a shared context? **Expected explanation.** In ordinary intuitionistic logic both premises may use the same Γ; resource-sensitive logics differ. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **conjunction left and right** to **static program contract checker** in the setting **search must respect the exact structural rules of the declared calculus**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool checking preconditions and postconditions using sequent rules**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 4.4 — Implication rules in sequents

### Exact rule or metatheorem

**Formal content.** Right implication moves an antecedent into the left context: Γ,A⇒B yields Γ⇒A→B. Left implication uses premises that establish A and use B, matching modus ponens operationally.

### Worked argument with line-by-line reasoning

**Worked demonstration.** Prove ⇒P→P: apply →R backwards, reducing to P⇒P, then identity. To prove P,P→Q⇒Q, →L combines P⇒P and Q⇒Q, respecting the calculus’s context conventions.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **implication rules in sequents** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Applying →R while keeping the temporary assumption A in the final open context.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** Derive ⇒P→(Q→P) with right rules. **Solution or proof outline.** Apply →R twice, producing P,Q⇒P; close by identity and weakening. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** How does →L differ from simply rewriting a formula? **Expected explanation.** →L is a two-premise inference requiring evidence for the antecedent and a continuation using the consequent. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **implication rules in sequents** to **static program contract checker** in the setting **search must respect the exact structural rules of the declared calculus**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool checking preconditions and postconditions using sequent rules**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Lesson 4.5 — Cut rule and proof search

### Exact rule or metatheorem

**Formal content.** Cut allows Γ⇒A and Δ,A⇒C to yield Γ,Δ⇒C. It names an intermediate lemma, which can greatly shorten reasoning. In appropriate pure logics, cut is admissible though not primitive.

### Worked argument with line-by-line reasoning

**Worked demonstration.** A proof of Γ⇒L and a proof of Δ,L⇒Goal combine by cut. If L=P∧Q, expansion can replace a cut by ∧L, ∧R and smaller derivations, but a genuine elimination proof must handle every last-rule case.

**Derivation check.** Begin by asking whether this demonstration establishes a theorem, an entailment from premises, a model property, or only a finite computational case. Reconstruct every line as a separate formula and annotate its dependencies. The critical proof move for **cut rule and proof search** is the one not already supplied by the syntax: its required premises must actually appear, and its side conditions must be recorded. In a physical or computational application, the validity of these formal moves should not be confused with the reliability of the measurements encoded as atomic claims.

### Stress test: invalid shortcuts and boundary conditions

**Invalid shortcut to avoid.** Claiming that a two-line toy transformation proves full first-order cut elimination, including contraction and quantifiers.

**Repair protocol.** Identify the smallest point where the shortcut changes the mathematical conclusion. If there is a propositional countervaluation, give atom assignments explicitly and check all premises. If a first-order countermodel is needed, declare the domain, constants and predicate interpretations. If the issue is rule bookkeeping, show the missing premise or escaping assumption label. Reject a proposed repair if it merely says that the result is “obvious.” In advanced proofs, record an unproved lemma as an obligation rather than presenting it as already discharged.

### Graded exercises and annotated solutions

**Exercise A — construct.** From ⇒P→P and (P→P)⇒R, infer ⇒R using cut; what must be supplied? **Solution or proof outline.** Both premises must genuinely have derivations; the cut step alone does not prove the second premise. The submitted solution should name each rule and write its dependency context, so that one does not have to rely on a prose paraphrase of the intended calculation.

**Exercise B — diagnose.** Can any asserted intermediate formula be cut into a proof? **Expected explanation.** No. It must be proved on the first side and legally used on the second. Separate an illegal inference from a fact that happens to be true in a special interpretation; a rule can be invalid even if a particular application produces a true sentence.

**Exercise C — adapt to the running case.** Apply **cut rule and proof search** to **static program contract checker** in the setting **search must respect the exact structural rules of the declared calculus**. Formulate a premise set and one exact goal. **Answer guidance.** A complete answer identifies the rule to be checked, the source of every open assumption, and which assertion requires independent evidence from the application. It should explicitly guard against **a tool checking preconditions and postconditions using sequent rules**. If your proposal uses proof search, specify what evidence is emitted on success and what output is displayed on timeout. The mathematical outcome must remain distinct from the organization’s policy judgment.

### Design review and independent verification

## Unit 4 capstone — Sequent calculus and structural discipline

**Design brief.** Build a reviewable specification for **Static program contract checker**. Begin with the formal vocabulary that represents **search must respect the exact structural rules of the declared calculus**. Use at least three of the unit’s five lesson rules in one coherent derivation and one adversarial countercase. Do not use a model screenshot as the sole supporting evidence for a general inference. Report the assumptions that can be checked mechanically and the application assumptions that cannot. The most important quality boundary is **a tool checking preconditions and postconditions using sequent rules**.

### Deliverables and answer checkpoints

1. Define the logical calculus, syntax and semantics you are using. This step prevents an unannounced change from classical to intuitionistic rules. 2. Construct a derivation with at least six labeled inference steps or give a checked proof-search tree where every leaf closes by a legitimate initial rule. 3. Provide a negative test case. For a propositional problem include a concrete valuation; for a rule-scope error show the illegal dependency; for a first-order issue give a finite countermodel when one exists. 4. Explain whether the produced artifact is a proof, refutation, illustrative simulation or incomplete search record. 5. Write a short assurance statement describing the remaining outside-the-logic questions.

**A sample critique.** A project report says that **static program contract checker** is correct because a demo displayed a green status and accepted two sample inputs. The critique should reject this as logically inadequate. The green status may show that the interface reacted, but not that the rule system is sound. Replace the vague claim with specific evidence: a formal statement of the goal, a complete proof trace, a verified derivation and an independent check of **a tool checking preconditions and postconditions using sequent rules**. The final write-up should make **every closed proof-search branch must end in an initial sequent or licensed rule.** clear.

### Rubric (100 points)

Formal statement and declared logic: 20. Complete rule-by-rule argument: 25. Correct assumption/freshness or structural bookkeeping: 20. Negative tests and countercases: 15. Honest evidence classification: 10. Clarity and reproducibility: 10. An elegant but unchecked demonstration cannot receive full correctness marks. A correct theorem about a visibly mistranslated real-world specification requires an explicit qualification.

### End-of-unit oral examination

**Question 1.** What would count as decisive evidence for the claim in **sequent calculus and structural discipline**, and what would be merely illustrative?

**Question 2.** Choose the unit’s most important side condition and construct a case that violates it. Explain what changes in the conclusion.

**Question 3.** Explain how you could independently audit **every closed proof-search branch must end in an initial sequent or licensed rule.** without trusting the original proof-search heuristic.
