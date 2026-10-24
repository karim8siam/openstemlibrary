# Database Systems — Unit 3: Storage engines

**OpenSTEM original educational manuscript. Review draft; not an academic certification.**

## 3.1 Pages

**Core model — Pages**

Database pages are fixed-sized transfer and caching units containing headers, slot arrays and records. Slotted pages allow records to move inside a page while stable slot identifiers remain.

**Original worked illustration**

An 8 KiB page with 512 bytes of header and slot overhead can fit at most floor((8192-512)/128)=60 fixed 128-byte records under this simplified model.

**Boundary conditions and checks**

Real record layouts have null maps, variable-length fields, free-space fragmentation and MVCC metadata; the simple capacity estimate is an upper bound.

### Domain model and precise assumptions

A database page is the fundamental fixed-size unit through which many storage engines organize reads, writes, free space and recovery records. The fact that a query returns one logical row does not mean the storage system reads one row's bytes from disk. If rows are clustered into pages, obtaining a single row can involve bringing an entire page into memory; scanning a table can touch every page even when most rows fail a predicate. Page size, internal headers, visibility metadata, slot directories and fill factors influence capacity. Storage pages are not identical to operating-system memory pages, although both may use page-based mechanisms. A page can hold variable-length tuples and free-space bookkeeping, so naïvely dividing the page size by the nominal row size often overstates capacity.

### Worked field scenario

Suppose a simplified heap page has 8,192 bytes, a fixed 192-byte header and 16-byte slot metadata per record. If each record payload occupies exactly 128 bytes, the ideal capacity is floor((8192−192)/(128+16)) = 55 records. At 1,000 records, a lower bound is ceil(1000/55)=19 pages. This estimate ignores alignment, variable-length encodings, page fragmentation and reserved free space. Those omissions should be written beside the answer. If a workload frequently updates rows to larger payloads, filling pages to the theoretical maximum can cause fragmentation or moves. Storage design balances density against update headroom.

### Counterexample and limits

Page-level observability helps diagnose slow full scans. Compare logical page reads to physical reads: a logical read served from cache need not involve storage hardware, but it still consumes CPU and memory bandwidth. On solid-state hardware, random versus sequential I/O costs differ from older magnetic-disk assumptions, although sequential access and prefetching can still matter. An application developer should resist inferring actual I/O from an abstract page-count exercise without examining an engine's storage instrumentation.

### Investigation and self-check

Design a page-capacity calculator for 4 KiB, 8 KiB and 16 KiB pages with variable record sizes. Explicitly include header and slot overhead. Derive the capacity by requiring `header + n*(payload+slot) <= page_size`. Test zero payload, oversized payload and a record that just fits. Explain why compression or overflow storage would change the model and why real fill factors are configuration and workload decisions.

### Engineering verification

Check that page-count estimates always round upward for partial pages, and document whether the estimate is an initial bulk load or a long-lived table with deletes and updates. Use actual buffer-hit and I/O metrics to make performance decisions, not uncalibrated theoretical constants.

## 3.2 Records

**Core model — Records**

Records encode fields and metadata in binary structures. Physical layout affects scanning, updates and clustering.

**Original worked illustration**

A record containing a 4-byte key and 16-byte payload might occupy more than 20 bytes after alignment and a transaction header.

**Boundary conditions and checks**

Logical schema types are not always equal to stored byte counts; compression and encoding can dramatically change actual size.

### Domain model and precise assumptions

Record layout translates columns into bytes: fixed-size fields, variable-length payloads, null bitmaps, tuple headers and alignment may all contribute. A logical schema can declare a variable-length text field without deciding where every long string lives on disk. Engines may store some values out of line or compress them; the details are product- and version-specific. Slotted pages enable records to move within a page while preserving a stable slot reference, but this is an implementation technique rather than a requirement of the relational model. Row-oriented storage often favors retrieving several attributes of one tuple. Column-oriented storage can accelerate scans over a few fields by compressing similar adjacent values and avoiding unrelated columns.

### Worked field scenario

Imagine a reporting workload that sums invoice totals over ten million orders without examining postal addresses. A row store may have to read pages carrying totals alongside addresses and descriptions, whereas a column store can concentrate bytes from the numeric total column. By contrast, an online checkout that fetches one customer's current cart may benefit from a row representation and an index on cart ID. Hybrid systems and columnar extensions complicate this simplistic contrast. The critical design exercise is to describe access patterns and data freshness, not to label one storage organization universally superior.

### Counterexample and limits

An update to an indexed column also affects index maintenance. If an engine uses multiversion row versions, updates may create additional physical versions and require vacuuming or garbage collection. That maintenance can change the relationship between a table's logical row count and its physical footprint. Statistics such as dead tuple counts or compaction backlog should be monitored where available. A row's storage format and its transactional visibility are distinct layers of the engine.

### Investigation and self-check

Estimate the lower bound for storing one million records with a 24-byte fixed portion, average 40-byte text payload and 20-byte per-record overhead. Then vary the average text length and compute the total difference. Calculate percentages carefully and state why external payload storage or compression can invalidate the arithmetic. Draw a slotted page showing header, slot directory, free space and record bodies after one deletion and insertion.

### Engineering verification

Measure real space usage after a representative load, delete and update cycle. Compare logical counts with storage allocation, check whether the table has bloated after repeated updates, and avoid using rough average-row estimates as a guaranteed disk budget. Persist source data types and character encodings during exports and migrations.

## 3.3 Indexes

**Core model — Indexes**

Indexes map search keys to locations or records. B+ trees support ordered range scans; hash indexes suit equality lookups but not ordered traversal.

**Original worked illustration**

With a branching factor of 100, a three-level tree can address roughly a million leaf-entry positions in the idealized full-tree model.

**Boundary conditions and checks**

Fanout and depth estimates ignore fill factors, leaf chaining and I/O cache effects; indexes also increase insert and update cost.

### Domain model and precise assumptions

An index is a secondary access path, not a promise that every query becomes faster. In a B+ tree, sorted keys support point lookups and ordered range scans through a hierarchy of internal nodes and leaf pages. Height depends on fanout, page size, key length, fill factor and total entries. A low height makes point access efficient, but looking up a large fraction of a table can require so many scattered fetches that a sequential scan wins. A composite index on (student_id, term) can serve predicates anchored on student_id, while a predicate only on term may not obtain the same benefit from its leading key arrangement. Engines differ in their support for skip scans, included columns and index-only scans.

### Worked field scenario

Take an index where each leaf stores up to 64 entries. For 12,800 entries, at least 200 full leaves are needed if every leaf is packed. A realistic 75% average fill yields roughly ceil(12800/(64×0.75)) = 267 leaf pages. Internal-page capacity and pointer sizes determine additional levels. These are planning estimates; an actual engine may split pages and leave gaps. Under a workload updating student grades, an index on every column multiplies write work, memory occupancy and maintenance cost. Index only measured query needs and constraints, not every possible predicate.

### Counterexample and limits

Hash indexes can support equality but not general ordered ranges in the same way as B+ trees. Bitmap structures can suit low-cardinality analytical dimensions, and full-text or spatial indexes have specialized operators. Index semantics also require collation, null positioning and expression behavior. An index on lower(email) may help a query applying precisely that expression, subject to engine rules; it cannot make unsafe address canonicalization correct.

### Investigation and self-check

Compare candidate indexes for queries filtering by `student_id`, `term`, and both together. Show a counterexample where an index `(student_id,term)` fails to prune most keys when only term is bound. For an equality predicate followed by a sorting requirement, explain when index key order may reduce sorting. Create sample skew, with one student responsible for many enrollments, and explain why uniform-selectivity assumptions could underestimate rows.

### Engineering verification

Use an actual execution plan to inspect whether the index is used and how many rows are touched. Track index size and write overhead. The absence of index usage does not prove a planner defect: a small table or unselective predicate is often better scanned.

## 3.4 Buffer Management

**Core model — Buffer Management**

Buffer managers retain frequently accessed pages and control pinning, eviction and dirty writes. Effective hit ratio depends on access locality and buffer pool size.

**Original worked illustration**

For 1000 page requests with 900 hits, the observed hit ratio is 90%; if a disk miss costs 5 ms, misses alone contribute about 500 ms of service work.

**Boundary conditions and checks**

Pinning prevents eviction of an in-use page. Confusing dirty and pinned states can corrupt data or block progress.

### Domain model and precise assumptions

A buffer manager keeps disk-backed pages in a finite memory pool so repeated accesses can avoid physical I/O. Each frame can store one page and metadata identifying its owning page; the manager tracks dirty state, pin counts and replacement candidates. A pinned page cannot safely be evicted while a consumer still needs it. A dirty page may need logging constraints satisfied before being written to storage. A simplistic LRU policy evicts the least recently referenced page, but production engines often use clock-like approximations, scan-resistant policies or multiple queues because maintaining exact global LRU can be expensive and sequential scans can pollute the cache.

### Worked field scenario

Consider three empty frames and the reference sequence A,B,C,A,D,B,A. Under a textbook LRU rule, the first three references miss and fill the cache. The next A hits and becomes most recent. D misses and evicts B; B then misses and evicts C; the final A hits. The sequence has five misses and two hits. It is easy to make an implementation error by updating recency only on misses, which would evict the wrong page after a hit. FIFO would make different choices because it ignores hits when ordering victims.

### Counterexample and limits

A larger buffer pool is not a substitute for an index or sound access plan. If a query touches ten million distinct pages and the buffer holds a tiny portion, most pages may still be read from storage. Conversely, repeated reads of a hot working set can achieve high cache-hit rates. Distinguish a buffer cache miss from a query latency failure: CPU calculations, locks, network transfers and slow clients also affect response time. Be cautious interpreting hit ratios without workload size and underlying I/O context.

### Investigation and self-check

Execute LRU and FIFO on the trace A,B,C,A,D,B,A with frame counts two, three and four. Record every hit, miss, eviction and frame contents. Explain whether more frames always reduce faults for LRU and why FIFO can exhibit Belady's anomaly on certain traces. Repeat after pinning a page and specify what a replacement algorithm may do when no unpinned frame exists.

### Engineering verification

Instrument buffer hit/miss counts and physical reads for repeated and cold-cache runs. State whether prewarming or OS caches were present. Verify dirty-page flush ordering with the engine's logging protocol rather than treating cache eviction as an unconstrained write.

### Integrated unit case study

**Unit case study: persistent bookstore storage.**

A bookstore holds four million BookStock rows keyed by SKU, and each row includes a small numeric count and a potentially large description. The application performs two types of access: point lookups by SKU at checkout and nightly analytics that sum quantities by category. These workloads stress different storage patterns. Begin with a page-level model. At 8 KiB pages, an assumed fixed overhead of 192 bytes and 16-byte slot per record, a 128-byte tuple payload admits floor((8192−192)/(128+16))=55 tuples per page. For four million tuples, a purely packed lower bound is ceil(4000000/55)=72,728 pages. This is not an engine capacity guarantee; free space, alignment and variable-length descriptions can change the physical row footprint.

Design an index on SKU for point lookup, and identify what happens when a query selects the large description. An index that stores only SKU and an internal row reference may require an additional heap lookup. Some engines can use covering indexes for selected queries, but adding every description to an index could make the index enormous and slow down writes. When daily inventory updates touch a hot subset of rows, the buffer pool can hide many physical reads. Contrast this with a cold batch scan of all stock; it may read pages that the point-lookup workload almost never uses.

Simulate a three-frame buffer with page trace A,B,C,A,D,B,A. Under LRU the hits occur on the second A and final A; under FIFO the eviction order is controlled by insertion, not recency. Record frame contents after each access. The exercise reveals why a buffer hit policy cannot be reasoned about merely from the number of unique pages. Extend the example with a pinned page and note that a pinned frame cannot be chosen as a normal eviction victim.

Estimate storage for a record whose description grows from 80 to 1,000 bytes. Variable-length fields may be compressed or moved to overflow storage, which changes the cost of fetching a single row. Write a small instrumentation plan: load representative catalog data, execute warm and cold SKU lookups, update 1% of rows, and compare reported page reads, index size and allocated table space. Add realistic skew rather than a perfectly uniform synthetic distribution. In production, ten popular items could generate most checkout reads.

**Design trade-off.** A row store supports the checkout path, while a column-oriented export or analytical projection may help the nightly report. That does not require changing the transaction database into a column store. A managed derived analytics table could be maintained periodically, with an explicit staleness label. The team should prefer measured query improvements and clear consistency semantics over an assumption that one physical format is ideal for every purpose.

### Extended executable laboratory

**Extended laboratory: compare access patterns rather than brands.**

Create a simple heap file simulator with 8 KiB pages and rows of several sizes. Let the page header consume 192 bytes, each slot 16 bytes and the payload 128 bytes in the initial experiment. The formula floor((8192−192)/(128+16)) yields 55 rows per page. For 1,000 rows, the minimum packed page count is 19. Increase payload to 256 bytes, reducing capacity to floor(8000/272)=29, so at least 35 pages are required. Record both results and the simplifying assumptions. This is not a benchmark of an actual production engine; its purpose is to explain why a schema choice changes I/O demand.

Give the simulator a three-frame buffer and a deterministic reference trace. Verify LRU against a hand-worked table. Change the number of frames and compare fault counts; then change the workload from repeated hot pages to a sequential scan. When the trace streams through more unique pages than the pool holds, repeated page misses can dominate. An index may help selective queries avoid many cold pages, but an index scan that fetches a large fraction of rows can incur more random page accesses than a sequential scan. There is no contradiction: the logical query and the physical access strategy differ.

Add an ordered B+ tree leaf-capacity toy model: 64 entries per fully packed leaf. For 10,000 entries the theoretical minimum is ceil(10000/64)=157 leaf pages. If average occupancy is only 75 percent, a planning estimate becomes ceil(10000/48)=209 pages. The experiment deliberately excludes internal index pages, overflow, split history and transaction metadata. Write the missing assumptions in a separate column; they help explain why estimates differ from real storage instrumentation.

Run a representative query in a database with EXPLAIN and measured buffer counters if supported. Save the exact SQL, table row count, index definition, cold/warm cache status and observed plan. Then change one factor at a time: an index, the predicate selectivity or the row payload. Keep the output rows identical. Conclude with a distinction among page-count arithmetic, an instrumented local observation and a performance claim that might generalize to a larger service.

### Connections and deeper pitfalls

**Further investigation: row growth and index lifecycle.** An index usually has operational costs during insert and update, even when a SELECT becomes faster. Every inserted row must be represented in the relevant secondary indexes. In workloads with random key insertion and frequent deletes, leaf splits and fragmentation can lower average occupancy. A bulk-built index with dense leaves can look very different from the same index after months of modifications. Do not use the original bulk-load leaf count as a permanent bound on file size.

A frequently updated text column might not belong in every covering index. If the index stores a copy of the column, an update could enlarge index maintenance even when the indexed search key is unchanged; exact behavior depends on the engine. Conversely, retrieving an occasional large document through a separate table or object store changes read patterns and transactional boundaries. An application must choose whether those documents must commit atomically with metadata, whether old versions must remain retrievable, and what happens when a remote blob upload succeeds but the relational transaction aborts.

A storage estimate should separate capacity planning from latency measurement. Estimating 50,000 pages says little about milliseconds without IOPS, throughput, cache state, concurrency and access order. Use page-count models as sanity checks: they explain scale and lower bounds. Then collect actual engine measurements for the exact workload. When page and index sizes unexpectedly grow, examine the update/delete history and maintenance state before assuming the cloud disk is defective.

## Three worked questions

### Problem 1: Pages: worked verification
A page has 8192 bytes, of which 512 is metadata. Fixed records are 128 bytes. Find maximum records.

**Set up the model and conditions**
Usable bytes=8192−512=7680.

**Carry out the calculation or proof**
Divide by record size 128: 7680/128=60.

**State the result and its scope**
At most sixty records fit in this idealized fixed-length model.

**Detailed reasoning and validation.** Derive available payload 8192−512=7680 bytes. Divide exactly by 128 to get 60 records. The calculation deliberately folds all overhead into 512 bytes; if each record also requires an 8-byte slot, capacity would instead be floor(7680/136)=56. It matters which model is being used. A single long variable-length string could reduce the actual capacity further, while external storage or compression could change the size relationship. Report 60 as a theoretical upper bound under the question's stipulated fixed-length layout, not as a guaranteed PostgreSQL or SQLite page capacity. Test that 60×128+512 fits exactly and 61×128+512 exceeds the page.

**Answer:** At most sixty records fit in this idealized fixed-length model.

### Problem 2: Records: worked verification
A record has 4-byte key and 16-byte payload. Can one infer an exact 20-byte disk footprint?

**Set up the model and conditions**
The logical field sizes add to twenty bytes.

**Carry out the calculation or proof**
Page slots, alignment, transaction metadata and compression may modify physical size.

**State the result and its scope**
No exact footprint follows without a particular storage layout.

**Detailed reasoning and validation.** A four-byte integer and a sixteen-byte fixed payload total twenty logical bytes before physical metadata. A page may require a slot entry, row version header, null bitmap or alignment padding; a variable-length value might be compressed, moved out of line, or placed behind a pointer. Those choices are not specified in the question. A defensible estimate lists the assumed encoding and overhead, then calculates a range or a conditional number. For example, adding 24 bytes of hypothetical header and 8 bytes of slot metadata yields 52 bytes before any padding, but that is explicitly a toy implementation rather than a fact about a named engine. Distinguish logical schema size, allocated pages and bytes sent over the network.

**Answer:** No exact footprint follows without a particular storage layout.

### Problem 3: Indexes: worked verification
For 1000 page accesses of which 900 hit a buffer, compute hit ratio and disk misses.

**Set up the model and conditions**
Hits=900 and total=1000, so hit ratio=900/1000=0.9.

**Carry out the calculation or proof**
Misses are the remaining 100 requests.

**State the result and its scope**
Observed hit ratio is 90% with 100 misses.

**Detailed reasoning and validation.** The hit fraction is 900/1000=0.9, or 90 percent. The remaining 100 references are buffer misses; a miss does not always imply a physical disk read if another cache layer can serve the page, and not every miss has identical latency. A high hit ratio may be satisfactory for a large reporting scan or inadequate for a latency-critical workload depending on miss cost. Compare the count with a trace that accesses 100 distinct pages ten times each; if references cluster by page, a small buffer may produce many hits, whereas alternating through a working set larger than the buffer can cause repeated misses. Hit ratio is a workload observation, not a standalone performance guarantee.

**Answer:** Observed hit ratio is 90% with 100 misses.
