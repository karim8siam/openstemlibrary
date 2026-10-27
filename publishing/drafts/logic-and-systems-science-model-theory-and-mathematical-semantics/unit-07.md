# Unit 7 — Types, back-and-forth and finite comparisons

**Learning objective.** Local logical descriptions and partial maps expose the granularity of semantic comparison.

**Running application.** Two graph snapshots may be indistinguishable by simple tests yet diverge under more demanding queries.

## Orientation: semantic commitments

The seventh unit asks whether conditions imposed one by one can all be realized in a particular model, and what a bounded game can tell us. A statement such as x>n for every standard numeral can be finitely satisfiable while lacking a real witness in the standard reals; changing the structure can change whether the whole partial type is realized.

Types and game-theoretic comparisons provide local ways of describing potentially global semantic behavior. 'Consistent' is not synonymous with 'realized here'; a set of requirements may be finitely satisfiable yet omit a witness in the current structure. Likewise a finite-round semantic game captures formulas up to a specified quantifier rank, not every possible formula. Any claim based on finite resources must carry its resource bound alongside its conclusion. A valid small example becomes misleading precisely when that qualifier is silently dropped.

A disciplined learning sequence begins with definitions, continues with a reproducible worked interpretation and ends with a search for a legitimate counterexample. You should be able to write a compact formal claim, list its hypotheses and decide whether it asserts satisfaction in one model, entailment by a theory, or a theorem about models. That choice determines the form of appropriate evidence. Keep one running example throughout the unit and modify its domain, relations, parameters or background theory only when you explicitly say so. Comparing these controlled interventions is more instructive than memorizing isolated definitions.

The five lessons proceed from a manageable definition to a mathematically consequential comparison. The first exercise of each lesson reconstructs its example; the second challenges an unjustified strengthening; the third transfers the idea to an applied specification. Each solution hint is guidance, not a substitute for checking the semantics line by line. Write formal answers with explicit witnesses or countermodels wherever possible.


## Lesson 7.1 — Partial types and consistency

### The statement and its scope

**Core principle.** A partial n-type over a parameter set A is a consistent collection of formulas in n free variables, with parameters from A.

### A worked semantic construction

In ordered fields, p(x)={x>n:n∈N} is finitely satisfiable in R, but no real x realizes all its formulas; in an elementary extension a realization can exist. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Finite satisfiability of a type in a structure does not imply realization in that same structure. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Show consistency using compactness for the theory plus type, not by claiming a witness already exists. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Constraint systems should distinguish internal solutions from consistent requests requiring an extension. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 7.1a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: In ordered fields, p(x)={x>n:n∈N} is finitely satisfiable in R, but no real x realizes all its formulas; in an elementary extension a realization can exist. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 7.1b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Finite satisfiability of a type in a structure does not imply realization in that same structure. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 7.1c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Constraint systems should distinguish internal solutions from consistent requests requiring an extension. **Guidance:** State the proof obligation as: Show consistency using compactness for the theory plus type, not by claiming a witness already exists. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 7.2 — Realized, isolated and omitted types

### The statement and its scope

**Core principle.** A type is realized when some tuple satisfies every formula; isolation occurs when a single formula entails the type over the theory under suitable conventions.

### A worked semantic construction

Over the complete theory of dense linear orders without endpoints, the type asserting x>a for every named element a of a particular countable model can be realized in an elementary extension but is omitted in that named model. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Do not claim every nonisolated type is omitted in every model; omission depends on theory, language and model. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Define realization relative to a particular structure and parameter interpretation. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Parameterized recommendation constraints may be individually feasible without one local entity meeting all demands. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 7.2a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: Over the complete theory of dense linear orders without endpoints, the type asserting x>a for every named element a of a particular countable model can be realized in an elementary extension but is omitted in that named model. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 7.2b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Do not claim every nonisolated type is omitted in every model; omission depends on theory, language and model. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 7.2c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Parameterized recommendation constraints may be individually feasible without one local entity meeting all demands. **Guidance:** State the proof obligation as: Define realization relative to a particular structure and parameter interpretation. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 7.3 — Saturation and homogeneous behavior

### The statement and its scope

**Core principle.** Saturation means consistent types over small parameter sets have realizations, with exact cardinal thresholds made explicit.

### A worked semantic construction

A countably saturated structure realizes every type over a finite parameter set that is consistent with its theory and parameter diagram, whereas Q with all rational points named omits certain cut types. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Do not infer saturation from cardinality alone; being infinite or uncountable is not sufficient. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Specify the size of the parameter set and full type before claiming saturation. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Representative test worlds benefit from carefully chosen semantic coverage rather than large random populations. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 7.3a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: A countably saturated structure realizes every type over a finite parameter set that is consistent with its theory and parameter diagram, whereas Q with all rational points named omits certain cut types. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 7.3b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Do not infer saturation from cardinality alone; being infinite or uncountable is not sufficient. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 7.3c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Representative test worlds benefit from carefully chosen semantic coverage rather than large random populations. **Guidance:** State the proof obligation as: Specify the size of the parameter set and full type before claiming saturation. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 7.4 — Back-and-forth and partial isomorphisms

### The statement and its scope

**Core principle.** Back-and-forth methods extend finite partial isomorphisms alternately between countable structures; success can prove isomorphism.

### A worked semantic construction

For two countable dense orders with no endpoints, extend a finite order-preserving bijection by placing the next element into the matching interval in the other order; density supplies an unused point. Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** The construction depends on countability and an extension property; the same proof does not identify Q and R as isomorphic. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Demonstrate both forth and back stages, not only a one-way embedding. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Schema reconciliation can extend an identity mapping in small consistent steps. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 7.4a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: For two countable dense orders with no endpoints, extend a finite order-preserving bijection by placing the next element into the matching interval in the other order; density supplies an unused point. Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 7.4b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: The construction depends on countability and an extension property; the same proof does not identify Q and R as isomorphic. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 7.4c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Schema reconciliation can extend an identity mapping in small consistent steps. **Guidance:** State the proof obligation as: Demonstrate both forth and back stages, not only a one-way embedding. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Lesson 7.5 — Ehrenfeucht–Fraïssé games

### The statement and its scope

**Core principle.** In finite relational languages, Duplicator winning the r-round EF game characterizes agreement on first-order sentences of quantifier rank at most r.

### A worked semantic construction

With r=1 in a language containing only equality, any two nonempty domains are indistinguishable: Spoiler chooses one element and Duplicator can match it. With r=2, domains of sizes 1 and 2 can be distinguished by ∃x∃y(x≠y). Analyze this example systematically. Record the language first, then the nonempty domain, the interpretations of constant, function and relation symbols actually in use, and finally the formula under investigation. If no concrete relation is present, interpret the example as an argument about all structures meeting the stated hypotheses and write that change of level explicitly. Each step should say why the mathematical object exists, not merely report the eventual result.

### Counterexample discipline and boundary conditions

**Frequent mistake.** Do not generalize a finite-round game result into agreement on all first-order sentences without unbounded rounds. A meaningful counterexample preserves the hypotheses of the claim being tested while breaking only the proposed conclusion. If a supposed counterexample changes the language, silently changes its constants, or violates one of the axioms, it does not disprove the original claim. Conversely, when the claim is a universal assertion about all models, just one legal countermodel is decisive. Keep these two directions separate: finding a witness is enough for an existential conclusion in a fixed structure; proving universal entailment demands attention to every legal structure.

### Proof laboratory: what must be shown

Track the partial isomorphism condition after every round and match the claimed rank. One rigorous route is to write the target as a precise mathematical judgment and split the argument into sound subgoals. A constructive case should produce the structure, map, formula, or witness promised by the judgment. A negative case should produce a legal countermodel or identify an explicit theorem barring the proposed definition. If an implication is being established, prove the forward direction under named assumptions; for an equivalence, prove both directions independently. Do not let a numerical screen result replace a structural proof when the statement ranges over unbounded domains.

### Transfer to applied reasoning

Bounded semantic comparisons explain why limited regression tests miss deeper differences. The translation must include the mathematical object corresponding to a real-world identifier, the status of absent or unknown information, and a statement of what the formal model leaves unspecified. A theorem guarantees something *given* these premises. It cannot establish that the premises faithfully describe a laboratory, database or institutional policy without external evidence. Keep a record of unverifiable assumptions, because a formal derivation may be completely valid even when its data pipeline is flawed.

### Three exercises and instructor guidance

**Exercise 7.5a — Reconstruct.** Rebuild the worked example in the smallest signature needed. State the domain, all nonlogical interpretations and the central truth or preservation claim. Is the conclusion about a single structure or an entire class? **Guidance:** Begin from: With r=1 in a language containing only equality, any two nonempty domains are indistinguishable: Spoiler chooses one element and Duplicator can match it. With r=2, domains of sizes 1 and 2 can be distinguished by ∃x∃y(x≠y). Write a sentence or a formula-with-assignment, and justify the conclusion from the relevant recursive semantic clause or theorem. Name every free variable and every parameter.

**Exercise 7.5b — Find a boundary.** Test the tempting stronger claim that the principle automatically survives an arbitrary change of vocabulary, domain or interpretation. Give a specific change that would invalidate the inference or explain which hypotheses prevent such a change. **Guidance:** The primary hazard is: Do not generalize a finite-round game result into agreement on all first-order sentences without unbounded rounds. Construct a countermodel if a universal claim is false; if the claim is valid, identify the preserving map or model-theoretic theorem. A failure to find a counterexample by enumeration does not resolve an unbounded question.

**Exercise 7.5c — Apply and audit.** Design an audit record for the application scenario below. Include the signature, an intended model, a checkable formula, and one risk of interpreting the result as an external fact. **Scenario:** Bounded semantic comparisons explain why limited regression tests miss deeper differences. **Guidance:** State the proof obligation as: Track the partial isomorphism condition after every round and match the claimed rank. Then list the semantic evidence that a verifier can inspect and the external factual assumption that needs separate validation.


## Unit 7 capstone — Build, vary and defend one model

**Part A: specify the vocabulary.** From this unit's running application, choose one nonempty domain and a minimal signature. Interpret each constant, function and relation explicitly. Write at least two sentences: one intended to hold and one intended to fail. If the unit focuses on a metatheorem rather than one finite example, explain why the running finite structure is illustrative rather than the theorem's proof.

**Part B: produce a controlled comparison.** Construct a second structure, a second theory or a modified formula connected with one of this unit's five lessons. Change exactly one semantically significant feature and compute what happened to the truth conditions. If the proposed preservation theorem is invalid, supply a legal counterexample. If it is valid, outline the inductive or theorem-based reason that every relevant formula is preserved.

**Part C: critique the claim.** A hypothetical reviewer states that the exercise establishes the result 'for all structures of any size'. Explain whether that is justified, using this unit's central distinction: Local logical descriptions and partial maps expose the granularity of semantic comparison. State the strongest conclusion that the evidence supports. Identify one mathematical assumption and one practical assumption that would need separate checking before applying the result to the real-world scenario.

**Suggested response framework.** Include the written signature; a complete interpretation table; formulas with all quantifiers and parentheses; one explicit witness or countermodel; a short derivation of the outcome; and a paragraph describing the limitations. Students working collaboratively should swap their artifacts and test whether another reader can reproduce the same evaluation without informal clarification.

## Unit 7 mastery checklist

- I can restate the five definitions of this unit accurately, with all needed hypotheses.
- I can build a legitimate small example and evaluate its key formulas.
- I can name at least one tempting invalid strengthening and diagnose it.
- I can distinguish first-order truth from real-world empirical truth.
- I can identify which claims require proof beyond a finite simulation.
