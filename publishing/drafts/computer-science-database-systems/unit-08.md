# Database Systems — Unit 8: Application databases

**OpenSTEM original educational manuscript. Review draft; not an academic certification.**

## 8.1 Document Stores

**Core model — Document Stores**

Document stores keep records as structured documents and may favor aggregate-oriented reads. Schema flexibility transfers some validation responsibility to applications.

**Original worked illustration**

An order document can embed a small array of line items to retrieve the whole order in one read, avoiding a join for that access pattern.

**Boundary conditions and checks**

Unbounded embedded arrays create large documents and costly updates; relationships and validation still require design.

### Domain model and precise assumptions

Document stores group related information into hierarchical values such as JSON-like objects. They suit cases where one aggregate is usually read and modified together, but that does not eliminate schema design. A document is an application data model with structure and compatibility obligations even if its database accepts flexible fields. Embedding can make a single read convenient; referencing avoids duplicating large or shared objects. The central question is the boundary of an aggregate that must remain consistent. Document storage cannot substitute for transaction requirements or carefully chosen indexes.

### Worked field scenario

Imagine a library book document containing title, authors, tags and a small set of edition metadata. Embedding an author's biographical profile in every book would repeat mutable information and create inconsistent copies when the author updates it. Referencing a separate author record can preserve one source of truth, but now a book page may require additional fetches or application-side joins. In a curriculum platform, embedding a few unit headings with a book may be reasonable, while storing thousands of evolving student annotations inside one book document can create contention and oversized records.

### Counterexample and limits

Flexible schema complicates evolution when some documents use `studentName`, others use `full_name`, and old readers assume one field. Validate data at application boundaries and consider database-enforced schema validation if supported. Index nested fields that correspond to measured query patterns. Arrays can produce multikey indexing effects and query semantics that differ from simple scalar fields. Denormalization reduces some joins but increases update coordination and data duplication.

### Investigation and self-check

Compare two document designs for Course: one embeds all enrollment records and one stores enrollments separately by student and offering. Evaluate update frequency, maximum size, required aggregate consistency, queries by student and deletion requirements. Explain which reads favor embedding and which independent updates favor referencing. Draft a versioned JSON schema and a compatibility reader for an old field name.

### Engineering verification

Benchmark actual document sizes, update conflicts, index amplification and validation failures. A JSON document with no agreed structure is not automatically more adaptable than a normalized table; migration effort has merely moved into application code.

## 8.2 Key–Value Systems

**Core model — Key–Value Systems**

Key-value systems access opaque values by key and are well suited to caches, sessions and lookups. Rich predicates may require secondary structures or external indexes.

**Original worked illustration**

A key user:42 can map to a serialized session record, retrieved with one exact-key operation in the abstract model.

**Boundary conditions and checks**

Cache eviction and expiry mean a key-value cache cannot be treated as the only durable copy of important application state.

### Domain model and precise assumptions

A key–value database presents access through a key and an associated value, often with optional expiration and atomic operations. Its apparent simplicity is powerful for direct lookup, caches, sessions and counters, but it does not imply rich joins or complex constraints. Keys need stable namespaces that distinguish object type, tenant and identifier; otherwise unrelated data can collide. A cache is a derived copy whose invalidation and staleness behavior must be specified. TTL expiration is generally a cleanup and freshness mechanism, not a hard real-time promise that data vanish at an exact microsecond.

### Worked field scenario

Suppose application sessions are stored under `session:{opaque_id}` with an expiry. The session key must be unguessable; users must not be able to choose another person's session identifier. Changing access privileges may require immediate revocation, and waiting for the TTL to expire is not always safe. A course-catalog cache under `book:{id}:v{revision}` can avoid serving stale schema versions when a revision changes, at the cost of extra storage for old keys until cleanup. A write to the authoritative database and a cache update are not normally one atomic operation.

### Counterexample and limits

For a shared counter, check whether the engine supplies an atomic INCR-like command instead of implementing GET then SET. Atomicity of one key says nothing about a transaction spanning many keys. High-frequency counters can create a hot key; partitioning counters across keys introduces aggregation and staleness trade-offs. Memory eviction policies may remove values independently of TTL and must be accounted for when using a cache as an optimization.

### Investigation and self-check

Design keys for tenants, student sessions and resource metadata. Distinguish user data from cache-derived data and decide which keys may be rebuilt after eviction. Simulate two clients incrementing a counter first with read-then-write and then with a documented atomic primitive. Define what should happen when the cache is unavailable or data in the cache disagree with the authoritative database.

### Engineering verification

Monitor hit ratio, memory usage, eviction count, latency and key cardinality. A high hit ratio can coexist with poor tail latency if expensive misses occur at critical times. Do not put secrets in easily enumerated keys or log full session tokens during troubleshooting.

## 8.3 Schema Migration

**Core model — Schema Migration**

Schema migrations modify production structures and data while preserving availability and compatibility. Expand/backfill/contract is safer than simultaneous breaking changes.

**Original worked illustration**

Add a nullable new column, deploy writers that populate it, backfill old rows, switch readers, then enforce NOT NULL after verifying coverage.

**Boundary conditions and checks**

A large backfill can block hot tables or saturate replication; plan batch size, rollbacks and version coexistence.

### Domain model and precise assumptions

Schema migration changes an application's storage contract while existing code and data continue to exist. A safe rollout usually separates expanding compatibility, moving data, switching reads and writes, and eventually contracting old structures. For example, rename a column by first adding the new column, writing both values during transition, backfilling existing rows in batches, updating readers and then removing the old column only after verification. The exact algorithm depends on data volume, transaction guarantees and whether writes can continue during backfill. “ALTER TABLE is one command” does not imply that the whole application migration is instantaneous or risk-free.

### Worked field scenario

Imagine 20 million Student rows that currently store `full_name` and must move to `given_name` plus `family_name`. Automatic splitting is not reliable for all naming systems; a migration must avoid assuming every name follows one Western naming pattern. An alternative could preserve display_name while introducing optional structured components. If two application versions run simultaneously during deployment, both must accept the staged schema. A migration can be technically reversible while having irreversible information loss if a dropped field was the only copy of some data.

### Counterexample and limits

Operational migrations should measure backfill progress, lock duration, replication lag and row-level validation failures. Large updates can create WAL volume, index churn and replication delay. Smaller batches with checkpoints reduce blast radius but increase complexity. A feature flag can enable the new read path after both old and new data are available. A rollback plan must describe how writes made under the new schema remain visible to old code.

### Investigation and self-check

Plan the migration of Enrollment.status from free text to an enum-like controlled domain. Inventory existing spellings and unknown values, define an explicit mapping, create a compatible new field, backfill under a measurable count, and validate the totals. Demonstrate rollback after the new writer has accepted a previously unseen status; explain why a simple schema revert could lose meaning.

### Engineering verification

Include forward and backward compatibility tests in CI against a disposable database. Never rely solely on a successful migration command; test actual application queries and prepared statements against the changed schema. Keep backups and restore instructions independent of the migration code.

## 8.4 Access Control

**Core model — Access Control**

Database access control uses roles, grants, row policies and audit records. Least privilege limits the damage from a compromised application component.

**Original worked illustration**

A reporting account granted SELECT on a restricted view should not hold schema-altering permissions in the same database.

**Boundary conditions and checks**

Filtering rows only in front-end JavaScript is not a security boundary; server/database authorization must enforce the policy.

### Domain model and precise assumptions

Access control determines which identities can read, write or administer data. Authentication establishes an identity; authorization evaluates that identity's privileges on a particular operation and object. Least privilege gives each role only what it requires. At the database layer, table, column, schema, function and sometimes row-level permissions can protect data even when an application contains a bug. However, database roles do not automatically solve every tenant-boundary problem, and administrative or owner privileges may bypass ordinary policies. Authorization must be tested using real low-privilege accounts, not only a superuser connection.

### Worked field scenario

Suppose a multi-tenant teaching service has organizations O1 and O2. Every enrollment belongs to one organization through an authoritative tenant identifier. A web request for O1 must never read O2's enrollments even if the caller guesses O2's record ID. Filtering by tenant_id in application queries can be necessary but is fragile if one endpoint forgets the predicate. Engine-supported row-level security can offer defense in depth if session identity is propagated securely and the policy is configured and tested. Using a single privileged service account that bypasses all policy can nullify the intended protection.

### Counterexample and limits

Permission grants need operational hygiene: schema migrations may introduce new tables without the expected restrictions; temporary diagnostic access may persist; database backups expose content outside normal query paths. Encryption at rest protects storage media under certain threat models but does not prevent an authenticated database account from reading rows it is authorized to query. Auditing sensitive accesses and keeping credentials out of source files are separate duties.

### Investigation and self-check

Construct a permission matrix with roles student, instructor, registrar and analytics_reader. Define which role may see a grade, update a grade, export an entire cohort or alter schema. Test one permitted and one forbidden action for every role. Add a second tenant to every test to catch cross-tenant leakage. Explain why column masking is not the same as preventing inference through aggregates or error messages.

### Engineering verification

Review privileges whenever the schema changes, not only at initial deployment. Monitor failed access attempts, privileged role usage, stale credentials and backup access. Ensure that the application's error messages do not reveal whether another tenant's private record exists.

### Integrated unit case study

**Unit case study: evolving a multi-tenant academic portal.**

A teaching platform initially uses a relational Students table and a simple cache for course descriptions. It will introduce rich book metadata, tenant-specific settings, and a renamed enrollment status field. Rather than move every object to one fashionable data store, analyze each data access pattern. Relational constraints are valuable for enrollment identity and payment references. Document-style storage can group evolving book descriptors, but book IDs and author identities should still have clear uniqueness and reference rules. A key–value cache can reduce repeated reads for popular public descriptions without becoming the canonical record.

Suppose the cache stores `book:CS101:v4` as a JSON value. An editor publishes version v5 in the authoritative store but a service still serves v4 under a stale pointer. An immutable versioned key plus an updated current-version reference can make invalidation tractable, but clients must decide how much staleness is acceptable. Do not place private student progress inside a public cache namespace. Namespaces should include tenant and privilege scopes where appropriate; cache key design is part of access control when data are shared among users.

The schema migration renames `Enrollment.state` to `Enrollment.status`. Begin with an expand step: introduce status while keeping state readable. Backfill historical rows, use application compatibility code to keep both fields synchronized during the transition, test readers on both application versions, then switch reads to status. Only after traffic confirms that no old reader requires state should the column be contracted. A reversible DDL statement is not enough for rollback if a new status value has no representation in the old schema. Preserve an explicit mapping policy and count unmapped values.

A second tenant is then onboarded. Every enrollment must be tied to an authoritative tenant or institutional boundary. Test access with three principals: a learner from tenant A, a learner from tenant B, and an admin permitted only inside tenant A. A guessable enrollment ID from tenant B must not expose data when requested by tenant A. SQL row-level policies can help where supported and correctly configured, but a highly privileged connection may bypass intended restrictions. Application-level validation and database authorization should reinforce one another. Analytics exports and backups need their own access controls.

**Release gate.** In a staging system, deploy old and new application versions against the expanded schema, write and read both old and new status values, and validate row counts after backfill. Simulate cache loss and confirm the portal can still fetch authoritative data. Run negative authorization tests for cross-tenant access. Only then remove the old column and stale cache keys. Keep rollback procedures, data backups and migration SQL in version control, and monitor errors and performance during the cutover.

### Extended executable laboratory

**Extended laboratory: safe evolution and tenant isolation.**

Create a tenant-aware Enrollment table with IDs, tenant_id, learner_id, offering_id and state. Populate two tenants, each with an enrollment bearing a similar human-readable reference. Begin with a negative authorization test: a user authenticated for tenant A requests a known record from tenant B. The correct API response must reveal no confidential data and must not allow modification, regardless of whether the identifier is guessed or read from an old link. Test the same endpoint under a normal application role and under an administrative maintenance role; explain why the latter may intentionally have broader access and requires a separate audit path.

Stage a schema migration from `state` to `status`. Deploy a new nullable column first. Backfill old data with a validated mapping, including records whose legacy values are unknown. During a mixed-version release, use compatible reads and writes or a deliberate transition mechanism. Measure the number of rows where old and new fields disagree. Only remove the old column after all active services and background jobs have switched and the mismatch count is acceptably resolved. Include tests for rollback after a new status value appears, because the old schema may lack a representation for that value.

Add a key–value cache for public book metadata. Set a stable `book:{id}:{revision}` key for versioned data, and keep the authoritative value in the database. Evict the cache and show the application can rebuild the value; change the revision and prove clients do not inadvertently receive stale content from an old key. Inject cache unavailability and ensure enrollment writes remain correct. A cache miss may increase latency, but it should not corrupt canonical enrollment data.

Finish with a deployment checklist that includes a backup restore rehearsal, application compatibility matrix, privileged role audit, cross-tenant negative tests, old-client reads, new-client reads and metrics for long-running migrations. A feature cannot be declared complete merely because every file compiles. The final artifact must demonstrate behavior on valid data, invalid data, concurrent access and interrupted operations under the explicitly chosen engine.

### Connections and deeper pitfalls

**Further investigation: choosing the right persistence boundary.** A document store, relational store and key–value store can coexist in a service, but every additional technology creates another failure mode and operational skill requirement. First determine whether a real workload needs another storage model. A relational database with JSON columns can support flexible descriptors without adding a separate cluster, while an in-process cache may be sufficient for small public datasets. Introducing a new database solely because a content format is JSON is not a meaningful architectural criterion.

For a migration, estimate operational impact before implementation. Backfilling ten million rows means write amplification, possible replication lag and long-running transactions if batching is careless. Add metrics for rows scanned, rows converted, rows rejected and time spent holding locks. Test compatibility with the oldest application process still permitted to run. Changing the contract too early can break delayed queue consumers even when the web application deployment appears successful.

Security review must include alternative access paths. Analytics exports, backup readers, customer-support tools and administrator scripts may hold broad privileges that bypass normal application filters. A least-privilege design distinguishes roles and includes revocation for temporary access. Row-level filtering is helpful but should be verified with the actual connection identity, including any database-owner bypass rules. When data are cached, ensure tenant and authorization boundaries survive the cache key scheme. A migration is complete only when old, new and privileged access paths have been reviewed.

## Three worked questions

### Problem 1: Document Stores: worked verification
An app stores orders and line items together as one document. What is the benefit and the danger?

**Set up the model and conditions**
The app can read one order aggregate without performing a separate join.

**Carry out the calculation or proof**
A very large or frequently changing item array expands the write and storage cost of that aggregate.

**State the result and its scope**
Embedding helps bounded aggregates but should be reconsidered for unbounded growth.

**Detailed reasoning and validation.** Embedding all line items with their parent order can make the whole aggregate easy to retrieve and update when item counts remain modest. The risk is that an unbounded array grows large and forces repeated rewrites or creates contention when independently edited. Suppose an order has six items and is almost always read as a whole; embedding may suit that use case. If an account has hundreds of thousands of audit events, embedding all events in one account document is likely an inappropriate aggregate boundary. Referencing those events separately can support pagination and independently indexed searches. The decision follows lifecycle and access patterns, not a blanket preference for relational or document storage.

**Answer:** Embedding helps bounded aggregates but should be reconsidered for unbounded growth.

### Problem 2: Key–Value Systems: worked verification
A cache maps user:42 to a session, then evicts it. May this be the only durable copy?

**Set up the model and conditions**
Eviction removes the key without any authoritative application-level delete.

**Carry out the calculation or proof**
Important session state needs a durable source or explicit regeneration semantics.

**State the result and its scope**
No: an evictable cache is not a suitable sole durable store by default.

**Detailed reasoning and validation.** An evictable cache can discard `user:42` without any domain-level logout action, according to its memory policy. Therefore it must not be assumed to be the only persistent record of a business-critical session unless the application explicitly accepts losing the session and can recover safely. The cache may hold regenerable derived data or an expiring session token, but its failure semantics need design. A cache hit is not proof of authorization: secrets can be revoked or privileges changed in the authoritative identity store. Define the consequence of eviction, stale data and outage, then test the application against all three rather than only the happy-path cache hit.

**Answer:** No: an evictable cache is not a suitable sole durable store by default.

### Problem 3: Schema Migration: worked verification
Describe a safe expand/backfill/contract migration for a new required column.

**Set up the model and conditions**
Add the column in a backward-compatible nullable form and deploy dual-compatible readers/writers.

**Carry out the calculation or proof**
Backfill old rows in controlled batches, verify counts, and update all clients.

**State the result and its scope**
Only then enforce NOT NULL and remove compatibility code.

**Detailed reasoning and validation.** First expand the schema with a nullable column so existing clients keep working. Introduce compatible writers/readers, backfill historical rows, and verify counts and unmapped values. Only after every active writer is known to populate the new field should the deployment enforce NOT NULL and remove compatibility code. A single large UPDATE may hold locks, generate substantial logs or strain replicas; batch it under an idempotent migration process with progress checkpoints. Rollback is not simply the reverse DDL command if the new system has stored values the old schema cannot represent. Test mixed-version application rollout before contracting the old schema.

**Answer:** Only then enforce NOT NULL and remove compatibility code.
