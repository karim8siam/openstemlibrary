# Database Systems — Unit 2: Relational systems

**OpenSTEM original educational manuscript. Review draft; not an academic certification.**

## 2.1 Relational Algebra

**Core model — Relational Algebra**

Relational algebra models queries using selection, projection, joins, unions and related operators. It has set semantics, unlike default SQL bag semantics.

**Original worked illustration**

Selecting students with year=3, then projecting names returns a set of distinct names in classical relational algebra.

**Boundary conditions and checks**

SQL SELECT name without DISTINCT may return duplicate names, so algebraic equivalences need bag-aware interpretation.

### Domain model and precise assumptions

Relational algebra gives a precise language for expressing database queries. A relation is mathematically a set of tuples, although SQL often operates with bags of rows. Selection σ filters tuples according to a predicate, projection π retains named attributes, and join combines compatible tuples. Renaming avoids ambiguity when the same relation occurs twice. To read an algebra expression, start with the innermost relations and identify the attributes available after every operator. A relational operator changes both the row set and the schema; dropping an attribute too early can make a subsequent join impossible. This careful trace is a foundation for reasoning about query correctness and optimizer transformations.

### Worked field scenario

Suppose Student(sid,name), Enrollment(sid,oid), and Offering(oid,term) contain registrations. To find names enrolled in term `2026F`, first select that term from Offering, join the selected offerings to Enrollment on oid, join the result to Student on sid, and project the name or, preferably, (sid,name) to preserve identity. Under set relational algebra, duplicate identical tuples disappear. Under SQL bag semantics, multiple matching registrations can produce duplicate names unless DISTINCT is requested. Replacing a join with a cross product and a later selection is algebraically possible but may yield an expensive intermediate result; a real optimizer often recognizes equivalent forms.

### Counterexample and limits

Relational division expresses “for all” requirements, such as learners who completed every compulsory lab. Simply counting rows equals the number of labs is unsafe if duplicates exist or if the relation being counted omits relevant lab identifiers. A robust SQL formulation uses nested NOT EXISTS to show that no required lab is missing. The domain of quantification matters: if the required set is empty, universal quantification is true for each candidate learner, whereas an inner join can accidentally drop everybody.

### Investigation and self-check

Translate the query “return student IDs registered in every required offering” into a NOT EXISTS formulation and test it with three students and two offerings. Add a student who has no registrations and test the result when the required offering set is empty. Explain how SQL NULL complicates NOT IN compared with NOT EXISTS. Then derive a selection-pushdown transformation and state the conditions under which it preserves the query's meaning.

### Engineering verification

Use a tiny data set to validate algebra before benchmarking large data. Write out intermediate tuple sets by hand for a five-row example and compare with an executable query. In SQL, make the intended duplicate semantics explicit and avoid projecting away keys during debugging. A query that looks plausible but returns the wrong set is a more serious failure than one that happens to run slowly.

## 2.2 Sql

**Core model — Sql**

SQL is declarative: a query specifies the desired result while the optimizer chooses a physical execution strategy. NULL introduces three-valued logic.

**Original worked illustration**

SELECT * FROM Enrollment WHERE grade >= 80 excludes rows for which grade is NULL because the predicate evaluates UNKNOWN, not TRUE.

**Boundary conditions and checks**

WHERE grade <> 80 also excludes NULL values; special handling requires IS NULL or another explicit predicate.

### Domain model and precise assumptions

SQL combines data definition, retrieval and transaction commands but its surface syntax hides evaluation rules that matter. In a typical SELECT query, the logical operations include FROM/JOIN, WHERE, GROUP BY, HAVING, SELECT and ORDER BY, although optimizers are free to use other physical execution orders that preserve semantics. WHERE removes individual rows before grouping; HAVING tests groups after aggregation. `COUNT(*)` counts rows, `COUNT(column)` ignores null values in that expression, and `COUNT(DISTINCT column)` counts distinct non-null values. Quoting and case folding of identifiers vary by database; parameterized SQL is necessary for data values supplied by users.

### Worked field scenario

Imagine an exam platform containing Attempts(attempt_id,student_id,exam_id,score). To compute average score per exam among completed attempts, filter the appropriate completion state, GROUP BY exam_id, then AVG(score). If score is nullable, AVG ignores those missing scores. That is often correct for “graded attempts” and incorrect for “all assigned attempts.” State which population the denominator represents. Use `WHERE score IS NOT NULL` for clarity, and check whether repeated attempts per student should all count. Choosing a single most recent attempt requires a deterministic tie-breaker; simply joining against MAX(time) can return two rows when timestamps tie.

### Counterexample and limits

Transactions also matter for SQL scripts. A sequence of insertions that establishes several foreign-key-linked records must either commit together or roll back together. A `BEGIN` without an error-handling and rollback strategy may leave a connection inside a failed transaction depending on the engine. Schema changes can have different transactional behavior across engines. Never use dynamic string concatenation to insert user text into a SQL statement; binding parameters prevents the text being interpreted as executable syntax. Identifiers such as column names cannot normally be passed as bound values, so whitelist them when dynamic selection is necessary.

### Investigation and self-check

Write a query that returns each exam ID with the number of graded attempts, their mean score, and a condition requiring at least three graded attempts. Test a null score, a repeated candidate, and an exam with zero attempts. Next return all exams including empty ones using LEFT JOIN, keeping right-table filters in the ON clause when needed so the outer join remains outer. Explain why moving a filter from ON to WHERE can change the row set.

### Engineering verification

Check execution results and their interpretation separately. Record column types, nullability, expected sorting, row multiplicity and how empty tables behave. An ORDER BY belongs in the query that is actually delivered to users; physical row order or an index scan does not promise stable presentation order without an explicit sort instruction.

## 2.3 Joins

**Core model — Joins**

Joins combine rows using predicates. Inner joins discard nonmatches, outer joins retain certain nonmatches with null-filled columns.

**Original worked illustration**

Students IDs [1,2,3] joined with Enrollment IDs [1,1,3] by student ID yields three inner-join rows; student 2 has no matching enrollment.

**Boundary conditions and checks**

A join without a valid predicate can create a Cartesian product that multiplies row counts and resource cost.

### Domain model and precise assumptions

A join associates tuples according to a condition, but choosing a join type determines what happens to unmatched tuples. INNER JOIN retains matches; LEFT JOIN retains every left row and extends unmatched rows with null right-side fields. FULL OUTER JOIN retains unmatched rows from both sides in systems supporting it. A CROSS JOIN produces the Cartesian product, which can be useful for systematic test combinations but disastrous when accidentally applied to production-sized data. An equijoin predicate usually compares identifiers; joining on a nonunique descriptive attribute can silently multiply matches. Distinguish a logical join's result from its physical implementation, since nested-loop, hash, and merge joins can all implement the same equijoin under appropriate conditions.

### Worked field scenario

Given Students(sid) containing 1, 2, 3 and Enrollment(sid,oid) containing (1,10),(1,11),(3,10), an inner join on sid returns three rows; a LEFT JOIN returns four rows because student 2 gets one null-extended match. If the query then adds `WHERE Enrollment.oid=10`, the null-extended row disappears, making the output equivalent to an inner join for that predicate. To keep students with zero enrollments, put a restrictive matching condition in the ON clause, or use a conditional aggregate that explicitly handles nulls.

### Counterexample and limits

Joining three tables can amplify duplicates in non-obvious ways. If a student has three enrollments and two contact methods, independently joining both child relations to Student creates six rows for that student. Summing tuition after the join would triple or double-count values depending on where the sums came from. Aggregate each child relation to one row per parent first, or design the query around the intended grain. State the grain of every query result: one row per student, one row per enrollment, or one row per student–contact combination.

### Investigation and self-check

Produce a row-count table for zero, one and two matches in each joined child relation. Compute the multiplicity for two independent one-to-many joins and show how to restore one row per parent using separate common table expressions. Also inspect whether an equality predicate can match nulls: standard `NULL=NULL` is unknown, so records requiring “null-safe” matching need an intentional engine-supported condition.

### Engineering verification

Use EXPLAIN to locate unexpected row multiplication and compare estimated versus actual cardinalities where supported. Indexing a join key can improve some algorithms but cannot fix logically incorrect multiplicity. Test outer joins using parents with no children; most happy-path test data lacks these critical cases.

## 2.4 Views

**Core model — Views**

Views expose a named query and can protect or simplify interfaces, but they do not automatically materialize results.

**Original worked illustration**

CREATE VIEW ActiveStudents AS SELECT ... WHERE status='active' exposes a reusable projection of underlying data.

**Boundary conditions and checks**

A regular view's performance depends on its expansion and query plan; security barriers and updateability are engine-specific.

### Domain model and precise assumptions

A view is a named query that defines a logical interface over underlying relations. It can reduce repeated query text, standardize a calculation and hide columns that consumers should not see. An ordinary view generally does not store a separate copy of its result; a materialized view is a persisted projection requiring a refresh or maintenance strategy. Consumers must understand whether they are reading current committed base data or a possibly stale materialization. A view is not automatically a security boundary: permissions, security-definer behavior and evaluation semantics vary, and side channels may still exist.

### Worked field scenario

Consider a university dashboard that requires the count of active enrollments per offering. A view `EnrollmentCounts(offering_id,n)` can group the Enrollment relation while exposing a stable column contract. If the enrollment status taxonomy changes, a single reviewed view definition can keep several clients consistent. But an interface view that lists student names is not automatically safe to expose publicly. Grant only the necessary SELECT permissions, filter sensitive rows in an appropriate enforced layer, and test with the actual low-privilege identity. Avoid using a view as a substitute for thoughtful row-level authorization.

### Counterexample and limits

Views simplify schema migrations when the physical base tables change but old queries must continue briefly. A compatibility view might retain an old column name while reading a renamed column. That can be a bridge, not a permanent guarantee: inserts through views have engine-specific restrictions, and some views are not updatable. Materialized summaries can improve repeated expensive analytics at the cost of stale data and extra storage. The operational contract must specify refresh frequency, acceptable lag and behavior when refresh fails.

### Investigation and self-check

Design a secure view that exposes student ID and enrollment count but not email, telephone or address. Query the view with an account that has no direct SELECT access to the sensitive base table, and document whether the particular engine permits the expected view behavior. Next compare live and materialized versions after inserting another enrollment. Determine whether the user needs transactionally current data or whether an explicitly labeled delayed summary is acceptable.

### Engineering verification

Review dependencies before dropping or renaming base columns. A stored view definition is code and deserves migrations, version control and regression tests. Test both authorized and unauthorized access, because data visibility and logical query correctness are separate properties.

### Integrated unit case study

**Unit case study: grade reporting under bag semantics.**

Assume an application stores Students(sid,name), Exams(eid,title), and Attempts(aid,sid,eid,score,submitted_at). Each attempt has a distinct aid; a student may take an exam repeatedly. The goal is a report listing each exam, its number of graded attempts and the mean grade of those attempts. The word "attempt" is important: this is not automatically the number of distinct students. A precise SQL sketch is `SELECT e.eid, COUNT(a.score) AS graded, AVG(a.score) AS mean_score FROM Exams e LEFT JOIN Attempts a ON a.eid=e.eid GROUP BY e.eid`. The left join preserves exams with no attempts, the count ignores missing score values, and AVG produces NULL rather than zero for an exam with no graded attempts.

Populate two exams E1 and E2. Give E1 attempts (A1,S1,80), (A2,S1,90), (A3,S2,NULL) and no attempts to E2. For E1, graded=2 and mean_score=85; for E2, graded=0 and mean_score=NULL. A query computing COUNT(*) would produce a different number: for E1 it counts three rows, and for E2 the LEFT JOIN creates one null-extended row. `COUNT(*)` would report one for E2, so it is the wrong measure. For "number of participants", count distinct non-null student IDs instead. For "latest grade per student", first rank or otherwise identify the latest attempt per student–exam pair with a deterministic tie rule, then aggregate that restricted relation.

A second report requests students who have never attempted E1. An anti-join can use NOT EXISTS with a correlated subquery; it avoids one set of NULL complications associated with NOT IN. Include students with no Attempts rows at all. Explain why `LEFT JOIN Attempts a ... WHERE a.eid IS NULL` can work only if the matching condition and non-null identifier are chosen correctly. A filter `WHERE a.eid='E1'` after the outer join will exclude unmatched students and fail the requirement.

Now add a ContactMethod(sid,type,value) table. Student S1 has two contact methods; each exam attempt joined to ContactMethod appears twice. Aggregating scores across that join duplicates contributions. To repair it, compute exam aggregates in a subquery at the intended grain before joining any contact methods. This design choice can be checked by comparing results for the original data with results after adding another irrelevant phone number. The grade report should not change when contact information changes.

**Performance study.** Compare a query that scans every attempt with one using an index on (eid,score) or (eid,sid,submitted_at), conditional on what the report actually filters and sorts. Read EXPLAIN output without treating cost units as milliseconds. Document which index helps a particular query and which update overhead it adds. Parameterize exam IDs and test unauthorized access separately from aggregation correctness.

### Extended executable laboratory

**Extended laboratory: a reproducible SQL result oracle.**

Populate a small disposable SQLite database with four students: IDs 1,2,3,4. Create Courses 10,20,30 and Enrollment entries (1,10), (1,20), (2,10), (3,20), (3,30). Student 4 has no enrollments. Calculate, on paper, the number of inner-join rows: five. A left join from Students to Enrollment yields six because student 4 contributes one null-extended row. Count unique enrolled students using `COUNT(DISTINCT student_id)` on the enrollment table: three. List all students with a left join and group by student ID, using `COUNT(Enrollment.course_id)` rather than `COUNT(*)`, which would incorrectly count student 4's null-extended row as one enrollment.

Next change the question: which students took both courses 10 and 20? One solution uses grouping with conditional counts, but ensure each course is counted only once for a student. Another uses two correlated EXISTS subqueries. For the sample data, only student 1 qualifies. Compare the two approaches after deliberately adding a duplicate enrollment row in a second experiment without a uniqueness constraint. If the grouping query mistakenly counts duplicate course 10 rows as separate required courses, it can produce a false positive. `COUNT(DISTINCT course_id)` addresses one type of duplicate, but a proper uniqueness constraint prevents the impossible state when duplicates violate the domain model.

Analyze three-valued logic. Add a nullable score field and set some scores to NULL. A predicate `score >= 80` excludes missing scores because UNKNOWN is not accepted by WHERE. `COUNT(score)` omits NULL scores; `COUNT(*)` counts all rows. An aggregate over a group with no non-null scores produces a NULL average. Make the reporting label explain the population and missingness policy. Replacing every missing score with zero may depress averages and misrepresent unanswered versus ungraded work.

Finally verify one anti-join for students without any enrollment. The expected set is exactly {4}. Write both a NOT EXISTS expression and a LEFT JOIN ... IS NULL expression and compare their outputs. Test a student with a NULL email to confirm the anti-join is based on the stable student identifier rather than nullable descriptive values. Preserve the SQL script and expected result tables so later changes to the schema or query can be tested against the same oracle.

### Connections and deeper pitfalls

**Further investigation: NULL, duplication and reporting questions.** A report that returns “students with the highest scores” needs a tie policy. If two attempts share the maximum score, should both be returned? A top-one query without an ORDER BY tie-breaker may select an arbitrary row. A window function such as ROW_NUMBER can rank within each student group, but the application must specify the ordering of tied timestamps. RANK and DENSE_RANK answer different ranking questions. Stable public reporting needs deterministic order and a written definition of attempts, candidates and completions.

Numeric aggregates must also be interpreted carefully. `AVG(score)` ignores NULL scores; if an exam has ten assigned students but only four grades recorded, it reports the mean of four scores, not a mean of ten students. `COUNT(*)`, `COUNT(score)`, `COUNT(DISTINCT student_id)` and `COUNT(DISTINCT CASE WHEN score IS NOT NULL THEN student_id END)` can represent four different measures. An author should annotate the population and denominator on every chart. A query can be syntactically valid and still support a false statement if its population was misunderstood.

Even straightforward SQL can have portability limits. Boolean syntax, date arithmetic, ordered aggregates, JSON operators, generated columns and some outer-join constructs differ across engines. Learning ANSI-style relational semantics is foundational, but production examples should label their tested engine. Prefer parameter binding for user values, and escape object identifiers only by a whitelisted transformation. A test oracle built with actual rows is stronger than asserting that two query texts “look equivalent.” Compare output multiplicity and NULL behavior before optimizing.

## Three worked questions

### Problem 1: Relational Algebra: worked verification
Evaluate selection year=3 followed by projection name in relational algebra versus SQL SELECT name without DISTINCT.

**Set up the model and conditions**
Relational algebra traditionally uses sets, eliminating duplicate projected names.

**Carry out the calculation or proof**
Default SQL uses bag semantics, preserving repeated values.

**State the result and its scope**
To mimic set projection in SQL, request SELECT DISTINCT name.

**Detailed reasoning and validation.** Use a relation with learners (S1,Alex,3), (S2,Alex,3) and (S3,Sam,2). Selection year=3 yields the first two student rows. Set projection of name gives the one-element set {Alex}, since two identical projected tuples collapse. SQL `SELECT name FROM Student WHERE year=3` normally returns two Alex rows because SQL preserves duplicates unless instructed otherwise. `SELECT DISTINCT name` returns one Alex row. Neither result by itself tells us how many people share the name; if the use case is unique students, project the stable ID as well. This difference becomes important when COUNT is used, when rows are joined later, and when pagination depends on stable ordering.

**Answer:** To mimic set projection in SQL, request SELECT DISTINCT name.

### Problem 2: Sql: worked verification
For a SQL predicate grade>=80 with grade NULL, determine whether a row passes WHERE.

**Set up the model and conditions**
Comparing NULL with 80 yields UNKNOWN under SQL three-valued logic.

**Carry out the calculation or proof**
WHERE retains only rows for which predicate is TRUE.

**State the result and its scope**
The NULL-grade row is excluded.

**Detailed reasoning and validation.** For grade NULL, the comparison `grade>=80` is neither true nor false in ordinary two-valued logic; it is UNKNOWN in SQL's three-valued logic. WHERE accepts only TRUE, so the row is excluded. A row with grade 80 is included; one with grade 79 is not. `WHERE grade IS NULL` deliberately finds missing grades. Replacing a null with zero via COALESCE is a modeling decision: a missing grade may mean not submitted, not assessed, or deliberately withheld, which is not equivalent to a scored zero. For aggregate AVG, null grades are ignored by default; verify the denominator and make the reporting definition explicit.

**Answer:** The NULL-grade row is excluded.

### Problem 3: Joins: worked verification
With students IDs 1,2,3 and enrollment IDs 1,1,3, how many rows does a left join produce?

**Set up the model and conditions**
Student 1 contributes two joined rows; student 3 contributes one.

**Carry out the calculation or proof**
Student 2 contributes one unmatched row filled with NULL enrollment fields.

**State the result and its scope**
The LEFT JOIN yields four rows.

**Detailed reasoning and validation.** An inner join would produce three matches because student 2 has no Enrollment row. A LEFT JOIN adds one null-extended row for student 2, yielding four in total: (1,Ea), (1,Eb), (2,NULL), (3,Ec). It does not add a single synthetic row for every nonmatching enrollment, because Enrollment is on the right side. Confirm what happens after `WHERE enrollment.offer_id = 10`: the student with no enrollment disappears, since UNKNOWN fails WHERE. To retain that student while selecting offering 10 matches, move the filter to the JOIN's ON condition. Counting students with `COUNT(*)` after a left join is not equivalent to counting distinct student IDs when the left table has one-to-many matches.

**Answer:** The LEFT JOIN yields four rows.
