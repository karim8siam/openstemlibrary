# Database Systems — Unit 1: Data modeling

**OpenSTEM original educational manuscript. Review draft; not an academic certification.**

## 1.1 Entities

**Core model — Entities**

An entity type represents a distinguishable class of real-world objects, with attributes and keys. A sound model separates conceptual identity from current descriptive values.

**Original worked illustration**

Student(student_id,name) uses a stable student_id to identify a student; name alone is not a safe key because names can repeat.

**Boundary conditions and checks**

Overloaded identifiers and missing lifecycle rules cause duplicate records and difficult merges later.

### Domain model and precise assumptions

A database entity is not merely a noun discovered in an interview. It is an object whose identity the application must retain while descriptive values change. Consider a university where a learner can change a legal name, preferred name, email address, program, and campus without becoming a new learner. An assigned learner identifier therefore plays a different role from every descriptive attribute. Identity should survive those changes, but identity itself needs an issuance policy: imported student numbers may collide, external systems may recycle identifiers, and accounts may be merged. A conceptual model says what persists, whereas its relational implementation says which values identify a row. Treat those as distinct design questions. In an entity–relationship diagram distinguish an entity type, its instances, the attributes recorded for each instance, and the conditions under which an instance begins or ends. Do not place a mutable name in a primary key just because humans recognize names.

### Worked field scenario

Suppose a registrar has student records (s17, Amina Rahman, old@example.test) and (s18, Amin Rahman, new@example.test). Before deduplicating, staff must establish whether there are two people or two records for one person. A name similarity heuristic cannot resolve identity: two different people can share a name and one person can use several names. A safe merge procedure preserves both original identifiers in an alias or merge-audit relation, reassigns dependent enrollments transactionally, and records who approved the merge. If an application simply deletes s18 and changes the email on s17, historic references to s18 may fail. Conversely, retaining both may double-count tuition. The conceptual model therefore benefits from Person, StudentRole, and ExternalIdentifier as separate entities when one person can hold several institutional roles.

### Counterexample and limits

Entity granularity matters. A CourseOffering in a particular term is not the same as a CourseCatalog entry that describes a reusable curriculum topic. The offering can have a room, schedule and lecturer, while the catalog entry carries a title and credit value. Mixing the two causes updates to a catalog title to look like changes to past offerings. Likewise a payment attempt and a successful payment are separate facts. Distinguish snapshots from current state, mutable from immutable attributes, and a durable event from the object it affects.

### Investigation and self-check

Draw three candidate diagrams: one in which Student owns email, one with Person owning email, and one with a separate verified ContactPoint relation. For each, ask whether a student may have multiple emails, whether another account can use a shared family email, and whether contact history must be retained. Construct an example with a name change and a duplicate external identifier. Explain precisely which diagram can represent both facts without overwriting history.

### Engineering verification

A review should inspect cardinality assumptions, not only field lists. Check that a synthetic stable key never appears before it is allocated, that imported identities are constrained by a source-specific uniqueness rule, and that deletion does not orphan dependent records. Record a legitimate retention policy before implementing physical deletion. Audit trails frequently require immutable event IDs even when account information is later corrected.

## 1.2 Relationships

**Core model — Relationships**

A relationship associates entities with cardinality and optionality. One-to-many relations often become a foreign key on the many side; many-to-many relations require a junction table.

**Original worked illustration**

Enrollments(student_id,course_id,grade) relates many students to many courses; the pair can form a composite primary key if repeat attempts are excluded.

**Boundary conditions and checks**

A foreign key alone does not encode every business rule, such as maximum concurrent enrollments or prerequisites.

### Domain model and precise assumptions

Relationships express claims about possible combinations of entities rather than just drawing connecting lines. The phrase “a student enrolls in a course” leaves at least three questions unanswered: can a student enroll in many courses, can a course have many students, and can the same pair recur in another term? A naïve Student(course_id) column forces one course per student. A comma-separated course_ids field destroys relational composition. The usual many-to-many solution is a junction relation Enrollment(student_id,offering_id,attempt_number,grade), where foreign keys refer to Student and CourseOffering. If repeat attempts are permitted, the composite key must include an attempt or independent enrollment identifier. Optionality also matters: a student with no enrollments must remain a valid row even when a join produces no match.

### Worked field scenario

Consider students S1 and S2, and offerings O11 and O12. The intended edges are (S1,O11), (S1,O12), and (S2,O11). Storing these edges in Enrollment produces three rows, regardless of the number of students and offerings. Joining Student to Enrollment and then Offering recovers offering details, but the join multiplies Student rows where there are multiple enrollments. That multiplication is correct for a listing of enrollments and incorrect for a raw count of unique learners. `COUNT(*)` counts joined rows; `COUNT(DISTINCT student_id)` counts distinct students under the corresponding join. If a waitlist membership is a separate relationship with a different lifecycle, do not silently coerce a waitlist row into an enrollment row.

### Counterexample and limits

Relationship attributes belong to the occurrence of the relationship. A grade is not a property of a person in general or a course catalog entry in general; it is a property of a particular enrollment attempt. Assignment of a teacher to an offering can carry a workload percentage or role. Ternary relationships are not always decomposable without introducing spurious combinations: supplier, part, and project may determine a single contractual agreement that cannot be accurately represented by every pair alone.

### Investigation and self-check

Model an equipment checkout system with Borrower, Item, Checkout and ReturnEvent. Decide whether simultaneous active checkouts of the same physical item are possible. Specify which relation represents the transaction and which attributes belong to that relation. Write a uniqueness rule that rejects two active checkouts for one item, while allowing many historic checkouts. A simple globally unique (borrower,item) key would incorrectly prevent legitimate repeated borrowing.

### Engineering verification

Test a relationship by inserting a subject with zero related rows, one related row, multiple related rows and a deleted parent. Document whether cascading deletion is appropriate or dangerous: deleting a course catalog entry should rarely erase transcript history. Use referential integrity and transactional business logic together rather than expecting cardinality labels in a diagram to enforce every lifecycle rule.

## 1.3 Constraints

**Core model — Constraints**

Constraints formalize allowable database states: domain rules, uniqueness, referential integrity and check predicates. They should be enforced at the strongest reliable boundary.

**Original worked illustration**

A UNIQUE(email) constraint prevents two rows with the same non-null email under the database's comparison rules; a foreign key prevents references to nonexistent parent IDs.

**Boundary conditions and checks**

Null handling and collation vary by engine, so apparent duplicate behavior must be tested on the actual database product.

### Domain model and precise assumptions

A constraint is a statement that must hold for every committed valid database state. Domain constraints restrict values, keys restrict identifiers, foreign keys restrict cross-table references, and check predicates capture row-level requirements. Write the invariant in ordinary language before selecting syntax. For instance, a percentage grade has to be between zero and one hundred when it is present, an enrollment must reference an existing offering, and an examination attempt cannot be awarded to an absent learner. Those are different kinds of rule and may require different mechanisms. Nullable columns require special care because the SQL expression `NULL = NULL` evaluates to unknown, not true. A CHECK predicate ordinarily rejects false; unknown need not be rejected. To prohibit missing values, use NOT NULL explicitly.

### Worked field scenario

Take an Order table with `quantity INTEGER NOT NULL CHECK(quantity > 0)` and `customer_id` referring to Customer(id). Attempting to insert quantity zero should fail even if the application forgot validation. Attempting to insert a nonexistent customer must also fail when the engine actually enforces foreign keys. SQLite, for example, documents enabling its foreign-key pragma for each connection; do not assume the same default as another engine. An email uniqueness requirement is less straightforward: engines vary in collation rules and treatment of multiple NULLs, and an address can change. Normalization, lowercasing or domain-specific canonicalization is a policy choice, not a consequence of SQL syntax.

### Counterexample and limits

Not every invariant fits a single row. “No more than 40 admitted students per offering” depends on the count of several rows and concurrent inserts. A CHECK on one Enrollment row cannot ordinarily enforce it. A capacity procedure must use an appropriate lock, serializable execution or carefully protected counter to prevent two sessions from observing one remaining seat and both committing. The application should convert an integrity error into a meaningful message, not suppress the database constraint.

### Investigation and self-check

For a booking system, list four invariants: positive price, valid customer, non-overlapping use of the same room, and immutable payment-event ID. Classify each as column-local, foreign-key, cross-row or event-identity invariant. Explain which constraints can be expressed using plain standard SQL and which require an engine feature or transaction protocol. Try concurrent bookings in two connections rather than testing only sequential inserts.

### Engineering verification

Build a negative-test table: invalid quantity, missing parent, duplicate key, null required field and simultaneous capacity claims. Record the expected SQLSTATE or documented error category without hardcoding a vendor-specific message. When migrating an existing table, verify old rows before enabling a new constraint; successful schema creation does not prove historical data are consistent.

## 1.4 Normalization

**Core model — Normalization**

Normalization decomposes relations to reduce update anomalies using functional dependencies. BCNF requires every nontrivial determinant to be a superkey.

**Original worked illustration**

If Course(course_id,instructor,office) has instructor->office, repeatedly storing an office for each course risks inconsistent updates; separate Instructor(instructor,office) when constraints justify it.

**Boundary conditions and checks**

Not every decomposition preserves all dependencies or is lossless; prove joins reconstruct the original before migrating data.

### Domain model and precise assumptions

Normalization is a method of reasoning about dependencies, not a demand that every database have the largest possible number of tables. A functional dependency X→Y means that any two valid rows agreeing on X must agree on Y. The dependence is a domain assertion, not an accident of the current sample. From Course(course_id, lecturer_id, lecturer_office), if lecturer_id→lecturer_office holds, duplicating an office over courses introduces an update anomaly. A separate Lecturer(lecturer_id,office) and Course(course_id,lecturer_id) can avoid it, assuming lecturer offices are truly fixed per lecturer and not per campus or semester. A design must not invent a functional dependency that the real world does not guarantee.

### Worked field scenario

To analyze a relation, identify candidate keys, calculate closures of determinants and inspect nontrivial functional dependencies. In BCNF, every nontrivial determinant must be a superkey. For a relation R(A,B,C) with A→B and B→C, A is a key, but B→C violates BCNF if B is not a superkey. Decompose into R1(B,C) and R2(A,B). Joining on B recovers the original under the stated dependencies; proving a lossless join matters because a poor decomposition could generate combinations never present in the source. The procedure is not merely splitting a table by subjective “topic.”

### Counterexample and limits

Third normal form permits certain dependencies involving prime attributes that BCNF does not, which can preserve dependencies more conveniently. Another common error is denormalizing before identifying the source of truth. A summary table may improve a reporting query but then it requires a refresh, invalidation or transaction strategy. The normalized model states the authoritative facts; materialized projections are controlled derived data. JSON documents can also be normalized conceptually even though the physical representation is not a set of relational tables.

### Investigation and self-check

Derive the closure of A under {A→B,B→C} step by step. Next suppose a lecturer can have a different office on each campus. Show why `lecturer_id→office` is false while `(lecturer_id,campus_id)→office` may hold. Rewrite the decomposition accordingly and explain what evidence from administrators is needed before migration. Design a test inserting two offices on different campuses and verify the schema does not incorrectly reject it.

### Engineering verification

A migration from one table to several requires backfilling and counts. Validate that every old course resolves to exactly one expected lecturer and that row multiplicities do not silently increase after joins. Verify foreign keys before dropping the source columns. Normalization can increase joins and require indexes, so benchmark representative requests without sacrificing integrity to solve an unmeasured performance problem.

### Integrated unit case study

**Unit case study: registrar data model with durable enrollment history.**

The design team is asked to maintain a catalog of courses, dated teaching offerings, student identities and attempts at enrollment. Write a relationship diagram before writing CREATE TABLE statements. `Student(student_id,display_name)` identifies the learner; `Course(course_id,title,credits)` identifies a reusable course; `Offering(offering_id,course_id,term,instructor_id,capacity)` identifies a scheduled instance; `Enrollment(enrollment_id,student_id,offering_id,attempt_no,status,grade)` records one attempt. Decide whether students can repeat the same offering or only retake the catalog course in a later term. Under the common assumption that an offering can be enrolled once by each learner, `UNIQUE(student_id,offering_id)` is appropriate; if a formal withdraw-and-reapply workflow creates separate attempts, the uniqueness rule must be revised before implementation.

Begin by adding parent rows: student s100, course CS101, offering o500 in term T1. Insert enrollment e1 and check the foreign key path. In a separate test, try to insert enrollment e2 for nonexistent offering o999. The database should reject it. Add a second valid enrollment for another student to the same offering; that should succeed. Then test the enrollment cap by simulating two connections racing for one remaining seat. A foreign key cannot protect a count constraint. Use a serialized capacity reservation or a database isolation strategy with explicit conflict handling, and verify that the committed total never exceeds the stated capacity. Treat waitlist membership as a separately defined state; it should not consume a confirmed seat unless the policy explicitly says so.

Next introduce a course title correction. It should modify the Course row, not overwrite historic student enrollment records. Introduce a student legal-name change, a failed email delivery and a merged duplicate identity. Account for these cases without changing primary keys. Historical reports can join current names or preserve a snapshot of the name printed on an official transcript; that choice is a product requirement rather than a universal database truth. Specify retention and access boundaries for sensitive student data before deciding which values should be deleted, pseudonymized or retained for audit.

A model review has three deliverables. First provide the entity diagram with cardinality and optionality marked on every edge. Second supply functional dependencies and a justification for each key; do not infer dependencies solely from a tiny example. Third give a small executable set of valid and invalid inserts whose outcomes distinguish the proposed model from its plausible alternatives. Correctness is established by those explicit behavioral tests, not by the number of arrows in the diagram.

**Design trade-off.** An enrollment identifier is a convenient single-column primary key, but it does not replace business uniqueness constraints. Surrogate identifiers and natural domain constraints solve different problems. The former support durable references; the latter prevent logically duplicated facts. The exact balance depends on retake rules, legal retention and application access patterns.

### Extended executable laboratory

**Extended laboratory: identifying anomalies by counterexample.**

Begin with a deliberately flawed spreadsheet-shaped table `Teaching(student_name,email,course_title,term,lecturer,office,grade)`. Insert two rows for the same lecturer teaching two different courses and three rows for one student taking three courses. First identify the intended keys in the source institution. Without them, the table cannot reliably distinguish two learners with the same display name. Change the lecturer's office in only one row, leaving the other unchanged; this produces an update anomaly if an office truly depends solely on lecturer. Remove the only enrollment row for a one-course lecturer; if that row was also the only place storing the lecturer, a deletion has destroyed an unrelated person record. Explain how these observations reveal an undesirable coupling of facts.

Refactor into Student, Lecturer, Course, Offering and Enrollment. At each step, state which functional dependency or relationship assumption justifies the separation. A student_id now identifies Student independently of enrollment history. A lecturer_id identifies Lecturer, but the office field may still need a CampusLocation child relation if an individual uses several offices. Reconstruct the former report with joins and compare row counts. All rows representing legitimate enrollments must remain; a decomposition that loses enrollment occurrences is incorrect even if it reduces duplicate columns.

Create negative tests. Attempt an Enrollment with an unknown student ID, an unknown offering ID and a duplicate legitimate key. These should be rejected according to the chosen schema's explicit constraints. Then create a learner with no enrollments and verify the Student row still exists and appears in an appropriate left-joined report. Decide what happens if a course is retired: the catalog may be flagged as inactive while historic transcript records remain immutable.

In the written report distinguish three notions of correctness: structural correctness of the diagram, logical correctness of its constraints and operational correctness under concurrent updates. The first two can be checked using symbols and small tables; the third requires multiple database connections and an actual transaction schedule. An ER diagram drawn neatly cannot by itself guarantee that a seat-capacity invariant survives concurrent insertions. The output of the experiment should include a diagram, CREATE TABLE definitions, inserted sample rows, a table of expected rejection results and a reconciliation query for migrated data.

### Connections and deeper pitfalls

**Further investigation: missing identity and time.** An effective database design records not just objects but when facts were true. A student's current program may differ from their program at the time a course was taken. If a report must reproduce a historic degree audit, joining a transcript to a current Program table can give the wrong result unless catalog versions and effective dates are represented. One approach assigns an immutable catalog_version identifier to each CourseOffering. Another represents program membership as intervals: Membership(student_id,program_id,valid_from,valid_to). Define whether endpoints are inclusive, and prevent overlapping intervals if a student can have only one major during any instant. The correctness test is temporal: querying at T1 should recover the version effective at T1 even after administrators publish version T2.

Soft deletion is another form of time and identity confusion. A row with `deleted_at` may remain physically present for retention or auditing, yet should usually disappear from active-user listings. Enforce uniqueness with awareness of whether retired identifiers can be reused. Two active users sharing the same username may be forbidden, while two historic rows bearing the same old username might be allowed in a system with partial uniqueness or an explicitly staged retirement rule. A simplistic globally unique username key can block legitimate recycling; an unrestricted unique rule can let active conflicts slip in. Write the policy first and choose an engine-specific implementation afterward.

A useful examination asks whether two databases with the same current rows can differ in behavior because their event history differs. If the business cares about the order or cause of changes, model events explicitly rather than hoping that updated timestamps reconstruct the full history. A last_modified field records only one moment and cannot answer who approved a merge or whether two separate corrections occurred. Data minimization applies here too: keeping every historic personal field forever is not automatically justified. Design retention with domain and legal review as required.

## Three worked questions

### Problem 1: Entities: worked verification
Students has IDs 1,2,3 and Enrollments IDs 1,1,3. Count equijoin result rows.

**Set up the model and conditions**
Student 1 matches two enrollment rows.

**Carry out the calculation or proof**
Student 2 matches none; student 3 matches one.

**State the result and its scope**
Inner join returns three rows under bag semantics.

**Detailed reasoning and validation.** Count the multiplicities by student identifier, not by distinct names. For ID 1 the enrollment multiset contains two records, so the join emits two copies of the Student 1 tuple combined with the different enrollment rows. ID 2 emits zero rows in an inner join because there is no enrollment; ID 3 emits one. Summation gives 2+0+1=3. If a projection drops every enrollment-specific attribute, the resulting displayed rows could appear repeated, but SQL does not remove them unless DISTINCT is used. Validate with a three-row Student table and a three-row Enrollment table. An exact row-count check after an unrelated column is added should still return three. If `COUNT(DISTINCT Student.id)` is requested, the result would instead be two students with enrollments, answering a different question.

**Answer:** Inner join returns three rows under bag semantics.

### Problem 2: Relationships: worked verification
Explain why Enrollment(student_id,course_id,grade) needs a junction table.

**Set up the model and conditions**
Students and courses can each participate in many enrollments.

**Carry out the calculation or proof**
A junction table holds each pair and attributes like grade.

**State the result and its scope**
A composite key can prevent duplicate pairs when repeats are prohibited.

**Detailed reasoning and validation.** Start from functional roles: neither Student nor Course alone uniquely determines an Enrollment because each student may attend several courses and each course may be attended by several students. Grade depends on the relationship instance, so putting grade inside Student repeats course-dependent attributes, while putting it in Course repeats student-dependent attributes. A junction relation makes the pair explicit and allows foreign keys to reject nonexistent participants. To permit retakes in a later term, associate an Offering or attempt identifier; do not blindly enforce uniqueness on student_id and course_id across the learner's entire history. Test S1 taking C1 and C2, S2 taking C1, and S1 retaking C1 in another term. A good schema represents exactly the legitimate occurrences and rejects only genuinely invalid duplicates.

**Answer:** A composite key can prevent duplicate pairs when repeats are prohibited.

### Problem 3: Constraints: worked verification
Find the anomaly when instructor→office is repeated in Course(course_id,instructor,office).

**Set up the model and conditions**
The same instructor's office appears in several course rows.

**Carry out the calculation or proof**
Changing the office in only one row creates contradictory data for the same instructor.

**State the result and its scope**
Separate Instructor(instructor,office) after checking the dependency and lossless join.

**Detailed reasoning and validation.** The update anomaly is observable with two course rows: (C1,L7,Room21) and (C2,L7,Room21). Changing only C1 to Room37 creates a relation that violates L7→office because the determinant L7 now corresponds to two values. If the office truly belongs to lecturer L7, move the office attribute to Lecturer(L7,Room37) and have courses reference L7. The join of Course with Lecturer reconstructs the office for reporting. This design presupposes lecturer identity is stable and each lecturer has one relevant office. If location depends on campus or term, the dependency must include that context; normalization based on a false assumption simply replaces one modeling problem with another.

**Answer:** Separate Instructor(instructor,office) after checking the dependency and lossless join.
