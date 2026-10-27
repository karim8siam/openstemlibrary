# Unit 6 — Löwenheim–Skolem and elementary extensions

**Learning objective.** Countability, elementary embeddings and chains constrain how much an axiomatization can control model size.

**Running application.** A model-building experiment must not mistake one countable simulation for the only possible infinite world.

## Orientation: semantic commitments

The sixth unit compares countable and uncountable linear orders, and uses elementary chains. The rational and real orders satisfy the same first-order sentences in the pure order language, but there is no bijection from Q onto R. Their agreement on sentences therefore does not identify them as the same structure. Elementary inclusion, where available, must be justified with the parameter-sensitive definition.

The cardinality of the language as well as of the domain can affect the theorem. The word elementary signifies agreement in truth for first-order formulas with parameters from the smaller structure, which is a much stronger property than closure under algebraic operations. When building chains, keep track of embeddings and their compatibility across successive stages. At each move between finite, countable and uncountable settings, identify what is known to exist, what is preserved, and what is not promised by the theorem.

A disciplined learning sequence begins with definitions, continues with a reproducible worked interpretation and ends with a search for a legitimate counterexample. You should be able to write a compact formal claim, list its hypotheses and decide whether it asserts satisfaction in one model, entailment by a theory, or a theorem about models. That choice determines the form of appropriate evidence. Keep one running example throughout the unit and modify its domain, relations, parameters or background theory only when you explicitly say so. Comparing these controlled interventions is more instructive than memorizing isolated definitions.

The five lessons proceed from a manageable definition to a mathematically consequential comparison. The first exercise of each lesson reconstructs its example; the second challenges an unjustified strengthening; the third transfers the idea to an applied specification. Each solution hint is guidance, not a substitute for checking the semantics line by line. Write formal answers with explicit witnesses or countermodels wherever possible.


## Lesson 6.1 — Downward Löwenheim–Skolem

### The statement and its scope

**Core principle.** For an infinite structure in a countable first-order language, there is a countable elementary substructure; more generally account for language and parameter-set cardinalities.

### A worked semantic construction

Starting from R as a pure linear order, there is a countable elementary substructure, even though the real line itself is uncountable. This substructure is not obtained by selecting arbitrary rationals without proof of elementarity. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** The theorem does not produce a finite elementary substructure for every infinite structure, and the size bound requires language assumptions. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Explain the Skolem-hull strategy without equating an elementary submodel with a random subset. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

A sample of representatives must satisfy witness-closure tests, not merely look statistically representative. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 6.1a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: Starting from R as a pure linear order, there is a countable elementary substructure, even though the real line itself is uncountable. This substructure is not obtained by selecting arbitrary rationals without proof of elementarity. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 6.1b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: The theorem does not produce a finite elementary substructure for every infinite structure, and the size bound requires language assumptions. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 6.1c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** A sample of representatives must satisfy witness-closure tests, not merely look statistically representative. **Guidance:** State the proof obligation as: Explain the Skolem-hull strategy without equating an elementary submodel with a random subset. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 6.2 — Upward Löwenheim–Skolem

### The statement and its scope

**Core principle.** An infinite model of a first-order theory admits arbitrarily large models in cardinals at least the relevant language size, under standard cardinality hypotheses.

### A worked semantic construction

For the theory of dense linear orders without endpoints, Q provides a countable model and R is an uncountable model of the same sentences. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** This does not say that arbitrary finite theories have models of all sizes; existence of an infinite model matters. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Separate model existence from an assertion of isomorphism. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Architecture specifications should not claim a unique storage capacity solely from first-order axioms. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 6.2a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: For the theory of dense linear orders without endpoints, Q provides a countable model and R is an uncountable model of the same sentences. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 6.2b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: This does not say that arbitrary finite theories have models of all sizes; existence of an infinite model matters. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 6.2c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Architecture specifications should not claim a unique storage capacity solely from first-order axioms. **Guidance:** State the proof obligation as: Separate model existence from an assertion of isomorphism. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 6.3 — Tarski–Vaught test

### The statement and its scope

**Core principle.** For M⊆N to be elementary, every formula ∃x φ(x,ā) with parameters ā from M that has a witness in N must have a witness in M.

### A worked semantic construction

For Q⊆R in the pure order language {<}, any finite interval constraints on rationals satisfiable in R are satisfiable in Q; stronger formulas require the full criterion. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Checking one particular existential formula is necessary but not sufficient for elementarity across the whole language. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Record the formula, parameters, and witness replacement, then cite the complete test for the general claim. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Data submodeling needs a coverage condition for all definable witness requests, not just for observed queries. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 6.3a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: For Q⊆R in the pure order language {<}, any finite interval constraints on rationals satisfiable in R are satisfiable in Q; stronger formulas require the full criterion. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 6.3b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Checking one particular existential formula is necessary but not sufficient for elementarity across the whole language. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 6.3c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Data submodeling needs a coverage condition for all definable witness requests, not just for observed queries. **Guidance:** State the proof obligation as: Record the formula, parameters, and witness replacement, then cite the complete test for the general claim. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 6.4 — Elementary chains and unions

### The statement and its scope

**Core principle.** The union of an increasing elementary chain is an elementary extension of each member, by the elementary-chain theorem.

### A worked semantic construction

Let M₀≺M₁≺… . To check an existential formula in the union with parameters in Mᵢ, locate a later stage witnessing it and then transfer via elementarity. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Unions of arbitrary substructures are not automatically elementary, and a family lacking a chain order requires extra work. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Use induction and Tarski–Vaught or the standard chain theorem with its hypotheses stated. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Incrementally grown formal knowledge bases need stability under the query language, not merely expanding records. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 6.4a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: Let M₀≺M₁≺… . To check an existential formula in the union with parameters in Mᵢ, locate a later stage witnessing it and then transfer via elementarity. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 6.4b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Unions of arbitrary substructures are not automatically elementary, and a family lacking a chain order requires extra work. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 6.4c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Incrementally grown formal knowledge bases need stability under the query language, not merely expanding records. **Guidance:** State the proof obligation as: Use induction and Tarski–Vaught or the standard chain theorem with its hypotheses stated. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 6.5 — Categoricity and the Skolem phenomenon

### The statement and its scope

**Core principle.** A theory can be categorical in one infinite cardinal but have other nonisomorphic models at different cardinalities.

### A worked semantic construction

The first-order theory of dense linear orders without endpoints is ℵ₀-categorical: every two countable models are isomorphic by back-and-forth. It also has uncountable models. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Categoricity must name the cardinality, and a first-order theory with an infinite model cannot force only countable models in all cardinalities. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

State the cardinal and language, then distinguish categoricity from completeness. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

A unique canonical small implementation may not imply a unique unbounded mathematical realization. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 6.5a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: The first-order theory of dense linear orders without endpoints is ℵ₀-categorical: every two countable models are isomorphic by back-and-forth. It also has uncountable models. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 6.5b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Categoricity must name the cardinality, and a first-order theory with an infinite model cannot force only countable models in all cardinalities. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 6.5c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** A unique canonical small implementation may not imply a unique unbounded mathematical realization. **Guidance:** State the proof obligation as: State the cardinal and language, then distinguish categoricity from completeness. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Unit 6 capstone — Build, vary and defend one model

**Part A: specify the vocabulary.** From this unit's running application, choose one nonempty domain and a minimal signature. Interpret each constant, function and relation explicitly. Write at least two sentences: one intended to hold and one intended to fail. If the unit focuses on a metatheorem rather than one finite example, explain why the running finite structure is illustrative rather than the theorem's proof.

**Part B: produce a controlled comparison.** Construct a second structure, a second theory or a modified formula connected with one of this unit's five lessons. Change exactly one semantically significant feature and compute what happened to the truth conditions. If the proposed preservation theorem is invalid, supply a legal counterexample. If it is valid, outline the inductive or theorem-based reason that every relevant formula is preserved.

**Part C: critique the claim.** A hypothetical reviewer states that the exercise establishes the result 'for all structures of any size'. Explain whether that is justified, using this unit's central distinction: Countability, elementary embeddings and chains constrain how much an axiomatization can control model size. State the strongest conclusion that the evidence supports. Identify one mathematical assumption and one practical assumption that would need separate checking before applying the result to the real-world scenario.

**Suggested response framework.** Include the written signature; a complete interpretation table; formulas with all quantifiers and parentheses; one explicit witness or countermodel; a short derivation of the outcome; and a paragraph describing the limitations. Students working collaboratively should swap their artifacts and test whether another reader can reproduce the same evaluation without informal clarification.

## Unit 6 mastery checklist

- I can restate the five definitions of this unit accurately, with all needed hypotheses.
- I can build a legitimate small example and evaluate its key formulas.
- I can name at least one tempting invalid strengthening and diagnose it.
- I can distinguish first-order truth from real-world empirical truth.
- I can identify which claims require proof beyond a finite simulation.
