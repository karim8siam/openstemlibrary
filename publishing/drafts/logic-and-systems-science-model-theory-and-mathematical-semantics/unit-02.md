# Unit 2 — Isomorphisms, substructures and morphisms

**Learning objective.** Maps between structures reveal which features are genuinely structural rather than artifacts of element names.

**Running application.** A graph data migration should preserve the same relation, not merely keep the same number of records.

## Orientation: semantic commitments

The second unit uses renamings and inclusions of algebraic and relational structures. A relabeling of a graph preserves all information precisely when its relation is transported in both directions. An inclusion between groups is not automatically elementary; a new ambient solution to a polynomial or group equation can change the truth of an existential statement with parameters.

This lesson is about preservation rather than superficial resemblance. Before asking whether a map is structure-preserving, name the relation that must commute with the map. If a function is involved, compare the image of the function result with the result obtained after mapping its arguments. If a relation is involved, ask whether both preservation and reflection are required. The stronger conclusions need stronger hypotheses: cardinality equality, similar pictures or a few matching truth values cannot replace the appropriate algebraic definition.

A disciplined learning sequence begins with definitions, continues with a reproducible worked interpretation and ends with a search for a legitimate counterexample. You should be able to write a compact formal claim, list its hypotheses and decide whether it asserts satisfaction in one model, entailment by a theory, or a theorem about models. That choice determines the form of appropriate evidence. Keep one running example throughout the unit and modify its domain, relations, parameters or background theory only when you explicitly say so. Comparing these controlled interventions is more instructive than memorizing isolated definitions.

The five lessons proceed from a manageable definition to a mathematically consequential comparison. The first exercise of each lesson reconstructs its example; the second challenges an unjustified strengthening; the third transfers the idea to an applied specification. Each solution hint is guidance, not a substitute for checking the semantics line by line. Write formal answers with explicit witnesses or countermodels wherever possible.


## Lesson 2.1 — Isomorphisms and invariant truth

### The statement and its scope

**Core principle.** An isomorphism is a bijection preserving constants, functions and relations in both directions; first-order truth is invariant under isomorphism.

### A worked semantic construction

Let D={0,1}, E={(0,1)} and D′={red,blue}, E′={(red,blue)}. Map 0 to red and 1 to blue. Every formula is preserved under the induced change of assignment. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** A bijection alone is not an isomorphism: swapping red and blue would reverse this asymmetric edge. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

For each atomic symbol, verify preservation and reflection before using the induction on formulas. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Canonical labeling allows tests to compare data structures independent of identifiers. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 2.1a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: Let D={0,1}, E={(0,1)} and D′={red,blue}, E′={(red,blue)}. Map 0 to red and 1 to blue. Every formula is preserved under the induced change of assignment. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 2.1b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: A bijection alone is not an isomorphism: swapping red and blue would reverse this asymmetric edge. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 2.1c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Canonical labeling allows tests to compare data structures independent of identifiers. **Guidance:** State the proof obligation as: For each atomic symbol, verify preservation and reflection before using the induction on formulas. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 2.2 — Substructures and induced relations

### The statement and its scope

**Core principle.** A substructure is closed under all functions, includes interpretations of constants, and inherits the restricted relations.

### A worked semantic construction

For (Z,+,0), the even integers form a substructure in the language {+,0}; they are not closed under an added predecessor function n↦n−1. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Being a subset of the domain does not suffice; the chosen language changes whether the same subset is a substructure. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Check every symbol of the signature, not just one memorable operation. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Restricting a relational dataset may be harmless, while restricting a state-transition system can break closure. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 2.2a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: For (Z,+,0), the even integers form a substructure in the language {+,0}; they are not closed under an added predecessor function n↦n−1. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 2.2b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Being a subset of the domain does not suffice; the chosen language changes whether the same subset is a substructure. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 2.2c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Restricting a relational dataset may be harmless, while restricting a state-transition system can break closure. **Guidance:** State the proof obligation as: Check every symbol of the signature, not just one memorable operation. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 2.3 — Homomorphisms versus embeddings

### The statement and its scope

**Core principle.** A homomorphism preserves positive atomic structure; an embedding also reflects atomic relations and is injective, preventing some collapses.

### A worked semantic construction

A map taking both vertices of a graph to one vertex can preserve a loop edge in an appropriate target, but it is not injective and cannot support arbitrary formula transfer. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** A homomorphism does not in general preserve negated formulas, inequalities, or universal properties. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Construct a two-element counterexample whenever a map is called an embedding without proof. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Schema mappings often need explicit failure tests for lost negated information. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 2.3a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: A map taking both vertices of a graph to one vertex can preserve a loop edge in an appropriate target, but it is not injective and cannot support arbitrary formula transfer. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 2.3b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: A homomorphism does not in general preserve negated formulas, inequalities, or universal properties. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 2.3c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Schema mappings often need explicit failure tests for lost negated information. **Guidance:** State the proof obligation as: Construct a two-element counterexample whenever a map is called an embedding without proof. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 2.4 — Reducts and expansions

### The statement and its scope

**Core principle.** A reduct forgets interpretations of symbols; an expansion adds new symbols interpreted on the same domain.

### A worked semantic construction

The ordered additive group (Z,+,0,<) reduces to (Z,+,0); two order choices can have identical reducts while differing on formulas that use <. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** A property definable in an expansion need not be definable in the reduct; a new named predicate changes expressive power. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

State whether a transformation changes the language, the domain, or both. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Modeling tools often add auxiliary relations for debugging, but claims must specify which vocabulary is visible. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 2.4a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: The ordered additive group (Z,+,0,<) reduces to (Z,+,0); two order choices can have identical reducts while differing on formulas that use <. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 2.4b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: A property definable in an expansion need not be definable in the reduct; a new named predicate changes expressive power. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 2.4c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Modeling tools often add auxiliary relations for debugging, but claims must specify which vocabulary is visible. **Guidance:** State the proof obligation as: State whether a transformation changes the language, the domain, or both. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 2.5 — Elementary substructures

### The statement and its scope

**Core principle.** M≺N means that every first-order formula with parameters from M has the same truth in both structures. This is stronger than substructure.

### A worked semantic construction

The natural numbers sit inside the integers in the language {+,0}, but the formula ∃y(y+y=x) with a chosen parameter is sensitive to whether a half exists for some x; compare candidate substructures carefully. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** The inclusion Z⊂Q under addition preserves addition but is not elementary: ∃y(y+y=1) is true in Q and false in Z. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Use the Tarski–Vaught witness condition when attempting to prove elementarity. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

A cached small sample cannot automatically inherit every property of a full data universe. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 2.5a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: The natural numbers sit inside the integers in the language {+,0}, but the formula ∃y(y+y=x) with a chosen parameter is sensitive to whether a half exists for some x; compare candidate substructures carefully. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 2.5b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: The inclusion Z⊂Q under addition preserves addition but is not elementary: ∃y(y+y=1) is true in Q and false in Z. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 2.5c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** A cached small sample cannot automatically inherit every property of a full data universe. **Guidance:** State the proof obligation as: Use the Tarski–Vaught witness condition when attempting to prove elementarity. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Unit 2 capstone — Build, vary and defend one model

**Part A: specify the vocabulary.** From this unit's running application, choose one nonempty domain and a minimal signature. Interpret each constant, function and relation explicitly. Write at least two sentences: one intended to hold and one intended to fail. If the unit focuses on a metatheorem rather than one finite example, explain why the running finite structure is illustrative rather than the theorem's proof.

**Part B: produce a controlled comparison.** Construct a second structure, a second theory or a modified formula connected with one of this unit's five lessons. Change exactly one semantically significant feature and compute what happened to the truth conditions. If the proposed preservation theorem is invalid, supply a legal counterexample. If it is valid, outline the inductive or theorem-based reason that every relevant formula is preserved.

**Part C: critique the claim.** A hypothetical reviewer states that the exercise establishes the result 'for all structures of any size'. Explain whether that is justified, using this unit's central distinction: Maps between structures reveal which features are genuinely structural rather than artifacts of element names. State the strongest conclusion that the evidence supports. Identify one mathematical assumption and one practical assumption that would need separate checking before applying the result to the real-world scenario.

**Suggested response framework.** Include the written signature; a complete interpretation table; formulas with all quantifiers and parentheses; one explicit witness or countermodel; a short derivation of the outcome; and a paragraph describing the limitations. Students working collaboratively should swap their artifacts and test whether another reader can reproduce the same evaluation without informal clarification.

## Unit 2 mastery checklist

- I can restate the five definitions of this unit accurately, with all needed hypotheses.
- I can build a legitimate small example and evaluate its key formulas.
- I can name at least one tempting invalid strengthening and diagnose it.
- I can distinguish first-order truth from real-world empirical truth.
- I can identify which claims require proof beyond a finite simulation.
