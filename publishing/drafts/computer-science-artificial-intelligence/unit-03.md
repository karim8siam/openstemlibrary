# Unit 3: Knowledge representation

*Editorial draft; not approved for live publication.*

## Logic
**Logic: conceptual explanation**

### Propositional logic and satisfiable knowledge bases
Knowledge representation makes explicit claims that an inference system may use. In propositional logic, atomic symbols represent true-or-false statements, and connectives such as NOT, AND, OR and implication build more complicated formulas. An interpretation assigns Boolean values to atoms. A formula is satisfiable if at least one interpretation makes it true, valid if every interpretation does, and contradictory if none does. These distinctions matter: a system that finds one plausible interpretation has not proved that a statement follows from a knowledge base.

An inference claim KB⊨q means that every model of KB is also a model of q. It can be checked in the finite propositional case by asking whether KB∧¬q is unsatisfiable. For example, let R mean 'the road is wet' and P mean 'it rained'. From P→R and P, the query R follows by modus ponens. But from P→R and R, P does not follow: a sprinkler could make the road wet. The latter error is affirming the consequent. A toy rule system should display its inference steps and show a countermodel for unsupported conclusions.

Conjunctive normal form is an AND of clauses, each an OR of literals. SAT algorithms search for truth assignments satisfying all clauses. A clause (A∨B) asserts that at least one literal is true. The conjunction (A∨B)∧(¬A∨B)∧(A∨¬B) has satisfying assignment A=true,B=true; evaluate all four assignments as a baseline check. Unit propagation assigns a forced literal when a clause has only one unassigned literal and all others are false. Backtracking combined with propagation underlies DPLL and more sophisticated SAT methods, which can solve many practical instances despite worst-case exponential complexity.

A knowledge base can be internally inconsistent, making every statement a classical logical consequence under the principle of explosion. For a practical rule engine this is usually a data-quality failure, not a desirable behavior. Record provenance, consistency status and conflicting assertions rather than silently emitting arbitrary conclusions. Open-world reasoning, common in semantic web representations, differs from the closed-world database assumption that unrecorded facts are treated as false. State the chosen semantics in a course example: absence of a medical allergy record must not be interpreted as proof that no allergy exists.

As a laboratory, encode five building-access rules as clauses. Ask which staff roles may open which doors and which permissions are not entailed. Inject a contradictory rule and demonstrate that model enumeration detects inconsistency. A useful explanation includes the actual premises used and a counterexample interpretation where possible. Truth-table completeness works on a small number of atoms, but enumeration scales as 2^n; the simulation should not advertise brute-force checking as a general industrial reasoner.

## Ontologies
**Ontologies: conceptual explanation**

### Ontologies, knowledge graphs and identity
An ontology specifies classes, relations and constraints about a domain. A knowledge graph stores entities and relation instances, often as directed labeled edges. For a campus knowledge base, 'Laboratory' may be a subclass of 'Building', 'contains' may link buildings to rooms, and 'worksIn' may connect staff to departments. Declaring a subclass relation means every instance of the subclass belongs to the superclass; it does not mean that all buildings are laboratories. Choosing a relation vocabulary correctly is essential for reliable queries, data integration and downstream reasoning.

Identity errors create serious knowledge-graph failures. The label 'Physics Lab' might refer to a room, a course, or a research group. A robust system uses stable entity identifiers, records the type of each identifier and tracks aliases separately. Do not merge two entities merely because their names match. Conversely, two records with different names may represent the same real object after verified reconciliation. Schema constraints can disallow a room from simultaneously being typed as a person, but real ontologies often allow multiple compatible types. The constraint must be domain justified rather than mechanically applied.

Description logics provide formal semantics for parts of ontology languages. A simple example is ResearchRoom⊑Room and ResearchRoom⊑∃hasEquipment.Instrument, expressing that research rooms are rooms and have at least one piece of equipment. The existence statement need not identify a named instrument; this is an important feature of existential semantics. Under open-world reasoning, a missing equipment record does not establish that no such equipment exists. Under a closed-world database rule, a service may instead require a recorded instrument before marking the room ready. Those are different operational interpretations of the same incomplete data.

Knowledge graphs also need temporal validity. A staff member can change departments, a room can be repurposed and permissions can expire. Store the time interval to which a relation applies and avoid applying historical facts to today's actions. Provenance matters when sources disagree: record whether an affiliation came from HR, a self-reported profile or an outdated scraped webpage. A query result can include supporting edges and their sources, making error correction possible.

For a laboratory, create ten entities and at least four relation types. Write queries answering 'Which instruments are located in rooms managed by Department X?' and compare results before and after a room is transferred. Deliberately insert an ambiguous label and show why identifier-based joins remain reliable. Measure retrieval accuracy against a hand-authored reference graph. The graph's completeness cannot be inferred from the number of edges: missing relations and false equivalences have different consequences.

## Inference
**Inference: conceptual explanation**

### Sound inference, resolution and proof traces
An inference procedure is sound if every derived statement is entailed by its premises. It is complete relative to a language and proof system if it can derive every entailed statement when sufficient computation is allowed. Soundness and completeness are mathematical properties of the inference rules, not guarantees that the premises are factually correct. An inference engine can be perfectly sound and still deliver an incorrect answer about the world if the input knowledge base contains false facts.

Resolution operates on clauses. From (A∨B) and (¬A∨C), one may infer (B∨C). To see why it is valid, consider any interpretation satisfying both premises: if A is true then the second clause forces C; if A is false then the first forces B. Either way B∨C holds. In a refutation proof, add the negation of the query to the knowledge base, convert statements into clauses, and derive the empty clause. The empty clause represents contradiction, establishing that the query follows, assuming the conversion preserved satisfiability appropriately.

Forward chaining applies rules as their premises become known. Backward chaining begins with a query and recursively seeks rules that can establish it. In a finite Horn-rule system, these methods can be efficient, but recursive rules require cycle management and a defined semantics. Suppose 'mentor(x,y)' and 'mentor(y,z)' imply 'indirectMentor(x,z)'. A backward reasoner may need bindings for x,y,z and must avoid treating variables with the same printed name from different rule invocations as automatically identical. This is the role of variable standardization and unification.

A concrete access-control example uses facts Employee(Ada), Trained(Ada), and a rule Employee(x)∧Trained(x)→MayEnterLab(x). Forward chaining derives MayEnterLab(Ada). If TrainingExpired(Ada) is later learned, naive monotonic logic does not automatically retract MayEnterLab(Ada) unless the validity rule explicitly includes the absence of expiry under an appropriate nonmonotonic semantics or time-indexed conditions. Defeasible and rule-based production systems need well-defined conflict handling rather than assuming all facts remain valid forever.

In a proof-tracing laboratory, record every derived clause or fact with its parent premises, rule name and substitution. Confirm that a small consequence is derivable by two independent strategies. For a nonconsequence, provide a satisfying countermodel to KB∧¬q if practical. Add an inconsistent knowledge base and observe the behavior instead of suppressing it. A visual simulation can teach proof search, but displaying one valid proof does not establish that all needed domain facts were supplied.

## Rule Systems
**Rule Systems: conceptual explanation**

### Production rules and operational decision engines
A production rule has a condition and an action or conclusion. A typical rule says, 'if a server exceeds a load threshold and a healthy replica is available, propose rerouting traffic.' Unlike a purely declarative theorem, such a rule may trigger external side effects. Rule engines therefore need conflict resolution, priorities, safeguards, event deduplication and rollback procedures. Combining logical inference and operations without distinguishing them can produce an agent that repeatedly triggers expensive actions every time a fact is reasserted.

Compare two systems. In a deductive knowledge base, adding a fact often increases the set of classical consequences; the system is monotonic. In a business workflow, adding 'authorization revoked' should remove a previously valid permission. This is a nonmonotonic update, whether implemented by explicit validity periods, prioritized exceptions, or a model of defaults. For example, a default rule 'registered users may download' and exception 'users with a suspended account may not download' requires a conflict policy. If the engine merely fires both rules, the application may produce contradictory outputs. Define precedence in the specification and test both events arriving in different orders.

Rule systems can chain: a temperature threshold produces Alarm, Alarm produces Escalation, and Escalation sends a notification. A circular rule such as Alarm→Urgent and Urgent→Alarm should not run indefinitely. One strategy evaluates rules to a fixed point over a finite set of facts, adding each fact only once; another keeps an event queue with identifiers to suppress duplicate actions. For side-effecting rules, idempotency keys and transactional outbox patterns can prevent duplicate messages after retries. These implementation concerns are part of deploying an 'intelligent' rule system rather than optional details.

The representational language also constrains what is possible. Simple Boolean rules cannot naturally express uncertain sensor readings without additional probabilistic structure. A rule 'if temperature > 80 then fail' has a crisp boundary and may oscillate when noisy measurements cross the threshold. Hysteresis can use separate activation and clearing thresholds, such as alarm at 82 and clear below 78, reducing chattering. The simulation should show that hysteresis changes behavior through state, not through a mysterious smoothing constant.

Build a miniature rule engine with six rules and explicit timestamps. Test rule conflicts, circular dependencies, missing facts, unauthorized actions and event replay. For every output store the exact triggering facts and policy version. Verify that replaying the same event does not duplicate an external action when idempotency is claimed. Report which inference properties are mathematically established and which reliability properties depend on the implementation and its storage guarantees.

## Integrated Case Study and Model Limitations
**Integrated investigation for Knowledge representation.** The examples below illustrate the precise mathematical and operational constraints of the unit.

### Case study: explainable course-advising knowledge base
A university advising system recommends whether a student may enroll in a specialized course. The knowledge base contains facts about completed prerequisites, waivers, current catalog version, course availability and degree requirements. A naive system might use name matching to conclude that 'Probability' and 'Probability and Statistics' are identical. A better schema distinguishes a course identifier from its title and records institution-specific equivalence decisions as sourced assertions.

Write the rule Eligible(student,course) when the student has fulfilled every required prerequisite or an explicitly authorized waiver, and when the course is offered in the intended semester. In a classical logic setting, an absent prerequisite record does not prove the student lacks the course. Operationally, the advising service may mark eligibility 'unverified' and request a transcript rather than deciding 'ineligible'. A three-valued result of eligible, ineligible and unresolved is often more faithful than a Boolean answer derived from incomplete documents.

Suppose AdvancedAI requires Algorithms and LinearAlgebra. Student Noor has a verified Algorithms credit, an unverified transfer Linear Algebra course, and no waiver. The correct result is not automatically yes or no. A course-equivalence review may validate the transfer, after which the rule succeeds. If the course is not offered, eligibility to register this semester still fails despite academic readiness. Track that distinction in the data model instead of hiding both under one yes/no field.

The lab should include a provenance graph for one recommendation: each supporting requirement, the evidence record, evidence freshness and the catalog version. Change a prerequisite in the new catalog and show that the recommendation for the previous catalog remains reproducible. Inject an expired waiver and confirm that it cannot authorize a future term. Unit tests should cover contradictory transcripts, duplicate course identifiers, changing titles and partial records.

Ethically, the system must not fabricate an enrollment decision or claim institutional authority. It is an explanatory decision aid subject to official policy and human review. This case connects logical inference to concrete engineering: good representations and proof traces help users identify where knowledge is missing, while rules with uncontrolled side effects could incorrectly deny or grant access to essential educational opportunities.

### Research exercise: conflicting evidence, consistency and provenance
Imagine two university databases disagree about whether a student has completed a laboratory safety course. An HR system records Trained(Ari), while a recent safety-audit system records TrainingExpired(Ari). A classical deductive knowledge base can represent both statements without logical contradiction if the predicates are distinct, but a rule that ignores expiry may still infer MayEnterLab(Ari). The problem is not merely a weak theorem prover. The vocabulary and decision rule omit a temporal precondition that matters to real access. Add a date-indexed predicate ValidTraining(person,date) or an explicitly evaluated current authorization event, and distinguish the historical fact 'training occurred' from the operational fact 'training is valid now.'

This motivates provenance records. Every assertion should carry a source, observation date, effective interval, and method of verification. If multiple sources disagree, a policy may rank an official audited record above an informal self-report. That ranking itself is an organizational rule and can be wrong if the official record lags; the system must record exceptions and a human correction path. A knowledge graph storing provenance as first-class edges can help trace why an inference changed after an update. For example, a derived access permission might depend on Staff(Ari), HasTraining(Ari,Course1), CourseEquivalent(Course1,Safety2026) and NotRevoked(Ari). The inference trace should identify which evidence establishes each prerequisite.

### Failure of a naive open-world assumption
Open-world logic treats absent facts as unknown rather than automatically false. That property is valuable for web-scale data integration but creates operational questions. A hospital knowledge graph missing an allergy entry should not tell a prescribing system 'allergy=false.' A customer directory lacking a phone number cannot infer that the customer owns no telephone. When a procedure needs a total Boolean answer, the application layer must define what to do with unknown information, perhaps abstain, ask a person, or block an action until verified evidence arrives. Forcing unknown into false may simplify implementation but changes the semantics and potentially the risk profile.

Students can implement three truth statuses: supported true, supported false and unresolved. This is a simplified operational three-valued interface; it should not be confused with every formal three-valued logic, which may assign different truth tables. Enter a fact P, an explicit negation ¬P, neither, or both and observe how the conflict policy handles each situation. A truthful simulator should not hide the inconsistent-both state if its input design permits conflicting sources. Separately show how classical propositional entailment works on a consistent subset, avoiding the inaccurate claim that the operational conflict handler is classical theorem proving.

### Quantified rules and variable binding
Rules with variables require careful scope. Suppose WorksIn(x,d)∧DepartmentBuilding(d,b)→CanRequestAccess(x,b). With WorksIn(Mina,Physics) and DepartmentBuilding(Physics,ScienceHall), substitution yields CanRequestAccess(Mina,ScienceHall). But the rule grants a request opportunity, not automatic permission to open doors. A reasoner using predicates with overly strong names can convert a harmless eligibility statement into an unjustified operational command. Derive conclusions only with the exact rule semantics supplied.

In a small lab, implement forward chaining over ground facts and range-restricted Horn rules. Normalize variable names between rule invocations, deduplicate derived facts, and terminate at a fixed point on a finite domain. Check that every derived fact has a proof trace. Feed deliberately cyclic rules and ensure the implementation terminates when no new facts are added. Use an independent exhaustive model check for a tiny propositional subset to verify selected entailments.

### Communicating a nonconclusion
A knowledge system earns trust by saying what does not follow. Given an applicant recorded as 'completed Calculus' and a course prerequisite 'completed Linear Algebra,' the system cannot conclude eligibility merely because Calculus appears adjacent to Linear Algebra in an ontology. Relatedness is not equivalence. The system should return 'prerequisite not verified' rather than fabricate an equivalency. Likewise, lack of proof of a prerequisite is not automatically proof of its absence. An educational report should include one valid derivation, one explicit countermodel showing a query is not entailed, one inconsistency diagnosis and one operational abstention case. These are four different outcomes that a polished interface must not collapse into a single confident answer.

### Distinguish database truth from justified consequences
A database stores observations and administrative claims; a reasoner derives consequences under explicit rules. These should be logged separately so an inferred statement is not confused with a source document. For instance, if an institution's policy states that training completed less than one year ago permits a laboratory access request, the system must evaluate the actual date of the training against the policy's effective term. A rule engine that treats 'Trained' as an eternal Boolean fact loses that distinction. Construct two facts with identical training labels but different dates and check that only one qualifies when all other requirements are met. Record the policy version; if the validity period changes next year, prior decisions remain reproducible under the earlier rule rather than silently rewritten.

### Worked question: Logical entailment and countermodel
Given P→Q and Q, does P necessarily follow? Provide a countermodel if not.

**Model the question**
To test entailment, find an interpretation where both premises hold but the proposed conclusion fails. The implication P→Q is logically equivalent to not P or Q.

**Calculate or derive**
Choose P=false and Q=true. Then P→Q evaluates true, and Q is true, yet P is false. This single interpretation disproves entailment.

**Check assumptions and boundaries**
Do not infer that P is always false: other models also satisfy the premises. We have shown only that the conclusion P is not forced by the given knowledge base.

**Answer:** No; P is not entailed. Countermodel: P=false, Q=true.

### Worked question: SAT model enumeration
For formula (A∨B)∧(¬A∨B), list all satisfying assignments of Boolean variables A and B.

**Model the question**
Evaluate the four assignments (F,F), (F,T), (T,F), (T,T). The first clause requires at least one of A,B; the second requires at least one of not A,B.

**Calculate or derive**
If B=true, both clauses hold regardless of A. If B=false, the first forces A=true and the second forces A=false simultaneously, impossible.

**Check assumptions and boundaries**
Thus exactly two assignments satisfy the conjunction: A=false,B=true and A=true,B=true. The formula is equivalent to B and does not imply a fixed value for A.

**Answer:** Exactly two satisfying assignments, both with B=true.

### Worked question: Forward-chaining trace
Given facts Student(Lee), Trained(Lee), and a rule Student(x)∧Trained(x)→MayUseLab(x), what follows? Does this prove Lee has a valid safety authorization today?

**Model the question**
Match x to Lee. The premises Student(Lee) and Trained(Lee) both appear among the given facts, so the Horn rule can fire once.

**Calculate or derive**
Derive MayUseLab(Lee) within this particular logic model. Record the supporting premises and the rule identifier so the derivation can be reproduced.

**Check assumptions and boundaries**
The model omits training expiry, current enrollment and institutional access policies. The logical consequence is sound relative to the premises but may not justify actual door authorization.

**Answer:** MayUseLab(Lee) follows in the toy knowledge base; current real-world authorization is not established.
