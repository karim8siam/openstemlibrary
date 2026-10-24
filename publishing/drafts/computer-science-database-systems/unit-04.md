# Database Systems — Unit 4: Query processing

**OpenSTEM original educational manuscript. Review draft; not an academic certification.**

## 4.1 Query Plans

**Core model — Query Plans**

A query plan is a tree or DAG of physical operators such as scans, filters, joins and sorts. Operator order can change intermediate result sizes by orders of magnitude.

**Original worked illustration**

Filtering a million-row table to 100 rows before joining can be much cheaper than materializing a million-row cross-product.

**Boundary conditions and checks**

Relational rewrites must respect outer-join, NULL, aggregation and bag semantics; not every algebraic pushdown is valid.

### Domain model and precise assumptions

A query plan is an executable tree of operators chosen to implement a logical SQL request. Scans produce rows, filters reject rows, joins combine row streams, aggregates summarize them, and sorts reorder results. Some operators pipeline tuples one at a time; blocking operators may materialize input before producing a result. Physical plan selection depends on index availability, data distribution, estimated cardinality, memory, parallelism and optimizer assumptions. A plan with fewer operators can still be slower if it processes much more data. When learning to read plans, identify the result cardinality at each node and whether a filter is applied before or after an expensive join.

### Worked field scenario

Suppose a report joins ten million sales to 500 stores but only requests one store for one day. Filtering Store and Sale early can greatly reduce intermediate rows, yet moving a predicate across an outer join might change meaning. If an index on (store_id, sale_date) exists, an index range scan may be efficient. Without it, a sequential scan and hash join can be sensible. Compare alternatives with concrete assumptions about number of matching sales rather than announcing a universal “index scan is better” rule.

### Counterexample and limits

EXPLAIN commonly shows optimizer estimates; an analyzed execution plan may show measured row counts and timings, which can itself add overhead. Confusing estimate with measurement is a frequent diagnostic error. When observed rows differ sharply from estimates, inspect stale statistics, skew, correlated predicates or parameter-sensitive plans. A significant mismatch can propagate upward and cause an inappropriate join choice. Diagnose the earliest large cardinality surprise rather than randomly toggling optimizer settings.

### Investigation and self-check

Draw two physical plans for filtering orders to one day and joining Customers. In the first, scan Orders then join; in the second, use an indexed date range and join. Assume 100,000 orders, 1,000 on the selected day and 500 customers. Estimate rows under an explicit uniqueness assumption on customer_id, and mark which operators can stream. Then add a nullable customer reference and discuss how an outer join changes correctness.

### Engineering verification

Collect the query text, parameter values, table sizes, statistics age, actual plan and resource metrics. Change one variable at a time when benchmarking. A copied EXPLAIN screenshot without workload context is evidence of one execution path, not evidence of a generally faster schema.

## 4.2 Cost Estimates

**Core model — Cost Estimates**

Cost estimation predicts rows, I/O and CPU work from table statistics and assumptions about correlation. Incorrect cardinality estimates can select poor plans.

**Original worked illustration**

If two predicates are each estimated to keep 10% of rows and treated independent, the optimizer predicts 1% combined selectivity.

**Boundary conditions and checks**

Highly correlated predicates can violate independence dramatically; sampling and histograms help but do not guarantee exactness.

### Domain model and precise assumptions

Cost estimation converts possible plans into comparable forecasts, usually measured in an engine-specific abstract unit rather than currency or actual milliseconds. A simple model can combine pages read, tuples processed, random access and sorting work: cost ≈ pages×page_cost + tuples×cpu_cost. The exact constants differ across engines and hardware. Selectivity is the fraction of rows expected to satisfy a predicate. For 200,000 records and an estimated selectivity of 0.01, a planner expects about 2,000 qualifying records before other filters. If predicates are correlated, multiplying independent selectivities can give a bad estimate.

### Worked field scenario

Imagine users choosing a campus and a department. Suppose 80% of one campus's students take a particular program but only 5% of all students take it. Treating campus and program as independent could underestimate the matching rows substantially. Statistics describing joint distributions, histograms or most-common-value lists can improve a plan, but a planner has finite knowledge and a sampling error. On one index-based plan, each qualifying row may require a heap fetch; at high selectivity those scattered fetches overwhelm the benefit of avoiding a full scan.

### Counterexample and limits

Query costs must include memory-sensitive operations. A hash join may spill partitions to storage when its hash table exceeds available memory; an external merge sort requires extra passes as the input grows. Relative estimates can reverse when cache state or runtime concurrency changes. A carefully measured query tuning process inspects both estimated and actual cardinalities and keeps the required result set fixed. Optimizing a subtly different query to get a faster time is not a valid comparison.

### Investigation and self-check

For a table with 12,000 pages and an assumed 1.0 cost per sequential page, estimate a full scan as 12,000 page-cost units before CPU. Estimate an indexed alternative touching 300 index pages and 600 randomly accessed heap pages if each random page costs 3.0 units. Compute 300+1,800=2,100 plus CPU, and explain why those assumptions favor the index. Increase qualifying rows until heap page accesses approach the full table; discuss when the comparison may reverse.

### Engineering verification

Tune estimates using measured evidence rather than magic multipliers. Report whether buffers were warm, whether a prepared statement used a generic or custom plan, and whether observed variance comes from concurrent workloads. Keep a baseline query output checksum so performance changes cannot silently drop rows.

## 4.3 Join Algorithms

**Core model — Join Algorithms**

Join algorithms include nested loops, sorting/merging and hashing. Their relative costs depend on data sizes, available memory, indexes and whether sorted output is valuable.

**Original worked illustration**

A naive nested-loop comparison of 100 rows against 200 rows performs up to 20,000 predicate comparisons. An in-memory hash join can be near linear expected work under favorable hashing assumptions.

**Boundary conditions and checks**

Hash joins may spill; sort-merge joins can reuse existing order; indexed nested loops can outperform hashing when outer input is tiny.

### Domain model and precise assumptions

Join algorithms implement the same logical operation with different computational access patterns. A basic nested-loop join checks every pair of rows, requiring approximately |R|×|S| comparisons when no index or other shortcut exists. An indexed nested loop probes an index on S for each row of R; it can work well when R is small and S has a selective access path. A hash join builds a hash table for one input and probes it with the other, usually suited to equality conditions. A merge join streams through already sorted inputs, accommodating ordered comparisons and sometimes avoiding a separate sort if useful order already exists.

### Worked field scenario

Assume R has 400 rows and S has 2,000 rows. A naive pairwise nested loop performs 800,000 predicate evaluations. A hash join can process approximately 2,400 rows' worth of build/probe work in a simplified in-memory model, plus hashing and output costs. But if almost every R row matches 1,000 S rows, the result itself has 400,000 tuples. No algorithm avoids constructing or aggregating that logical output merely by changing its join strategy. Memory spills, hash collisions and skew matter in practice.

### Counterexample and limits

For an indexed nested loop, the index lookup cost repeats once per outer row. An apparently small outer input can become expensive when it has hundreds of thousands of rows; a scan-based strategy may win. Merge join requires compatible ordering and special handling of duplicate join keys, since a group of equal keys can produce a Cartesian product within that key. Outer joins add work to preserve unmatched rows and constrain some transformations.

### Investigation and self-check

Trace nested loop, hash join and merge join on R={(1,a),(1,b),(3,c)} and S={(1,x),(2,y),(1,z)}. Show four matches for key 1 and none for key 3. Identify why duplicate-key handling matters in merge join. Next describe how an index on S.key changes indexed nested-loop access. Note which techniques require equality predicates and which can support a less-than condition directly.

### Engineering verification

Compare implementations with identical inputs, selected columns and join semantics. Include output cardinality and memory usage. An optimizer's ability to select the algorithm cannot repair a wrong join predicate, especially when a missing predicate creates an accidental cross join.

## 4.4 Optimization

**Core model — Optimization**

Query optimization enumerates alternative access paths and join orders subject to semantic equivalence. Search-space restrictions balance planning time against plan quality.

**Original worked illustration**

Joining three relations permits different binary join trees; joining the most selective pair first may reduce intermediate rows considerably.

**Boundary conditions and checks**

Small estimated cost differences are not proof of actual speedups. Use EXPLAIN and measured execution plans on realistic data.

### Domain model and precise assumptions

Query optimization searches among equivalent relational expressions and physical implementations. Algebraic rewrites include predicate pushdown, projection pruning, join reordering and subquery decorrelation when semantic conditions permit. Cost-based systems typically explore a constrained plan space using dynamic programming, heuristics or memo structures; exhaustively enumerating every plan is impractical for large queries. Common table expressions may be inlined or materialized depending on the engine and query. A developer should examine the actual implementation rather than assuming that query text order forces join execution order.

### Worked field scenario

Join order can have a dramatic effect on intermediate results. In a three-way join of Orders, Customers and a tiny Region filter, joining a prefiltered Region to Customers before touching a huge Orders table may limit rows early. Yet join order is not entirely free: outer joins must retain unmatched tuples according to their null-extension semantics, and volatile functions can restrict rewrites. A predicate that references only one base table may be pushed toward that table, but a predicate depending on a window function or aggregate cannot generally move before its own computation.

### Counterexample and limits

Hints and configuration switches can force a plan that happened to work on one data snapshot but becomes inferior as distribution changes. Index creation, query rewriting and statistics maintenance should be justified with reproducible before-and-after measurements. A SELECT DISTINCT added merely to hide duplicate rows can turn a logical error into a costly sort or hash aggregate; it is not a substitute for understanding the join grain.

### Investigation and self-check

Given 1,000,000 Orders, 20,000 Customers and 10 Regions, sketch two possible join orders under the assumption that a requested region contains 5% of customers and orders are evenly spread by customer. Work through expected intermediate sizes and identify where independence assumptions could fail. Then change the query to a LEFT JOIN and explain which reordering might alter preservation of unmatched customers.

### Engineering verification

Retain correctness tests while optimizing. Compare row identifiers, aggregates and order-sensitive output where applicable, not just execution time. Recheck plans after data growth and engine upgrades; cost estimates and plan choices are not permanent properties of an SQL string.

### Integrated unit case study

**Unit case study: choosing a plan for regional sales.**

Imagine Orders(order_id,customer_id,created_at,amount) with 2,000,000 rows and Customer(customer_id,region_id) with 50,000 rows. A dashboard requests total sales for one region during one week. First clarify the query's grain: the final result has one row for the region, not one row per order. An incorrect join to an independently one-to-many CustomerContact table could multiply order amounts; therefore CustomerContact does not belong in the reporting plan unless the question expressly needs it.

Sketch a plan that scans Orders, joins Customer on customer_id, filters region and date, then aggregates. Sketch another that identifies customers from the target region and uses an index to find their dated orders. Under a uniform approximation, if the region has 5% of customers and the target week has 1% of orders, about 1,000 orders may match. But the independence approximation can be false if the region's customers have unusually heavy activity. Record both assumptions and the estimated row counts at each node. Compare the plans using page and tuple costs rather than claiming that selecting the smallest intermediate relation always produces the fastest physical plan.

Introduce physical indexes. An index on Orders(customer_id,created_at) can help probes for known customers within a date range. An index on Orders(created_at,customer_id) helps date-first access. The preferred key order depends on whether the query arrives with customers or dates constrained most selectively and on the downstream grouping. Neither index is universally superior. A hash join after date filtering can be efficient if a week still contains too many rows for repeated index probes. A nested loop on 5,000 qualifying customers may cause thousands of lookups; an index probe cost repeats for every outer tuple.

Next examine a skewed input. One region contains 20% of all orders despite having 5% of customers. Estimated and actual join cardinalities now differ by a factor of four. Do not treat this as an inherent failure of SQL; the planner may lack statistics capturing the correlation. Compare an analyzed execution plan's actual row counts with estimated counts at each operator and investigate extended statistics or a query rewrite as supported by the engine.

**Correctness check.** Create a stable checksum of the set of `(order_id,amount)` included in the report. After an optimization, recompute both that checksum and the aggregate total. Faster execution is not an improvement if the query silently drops refunded orders, incorrectly double-counts customers, or changes the date-boundary semantics. Also test an empty region, an order without an allowed customer reference and timestamps at the start and end of the requested week.

### Extended executable laboratory

**Extended laboratory: a plan comparison workbook.**

Define three relations: Customers with 2,000 rows, Orders with 40,000 rows, and Regions with 20 rows. Assume, solely for an exercise, that each customer belongs to exactly one region and each order to exactly one customer. A query asks for total orders in a selected region over a date interval. First establish the logical result. If the query returns one total per region, the grain is region, even though its plan touches many order rows. Build a correctness oracle on a small deterministic sample: one customer with zero orders, one with several orders and one with orders just outside the date range.

Now compare two physical estimates. Plan A scans all 40,000 orders, joins customers and checks the filters. Plan B first selects the region's customers and probes an index on Orders by customer and date. If the selected region has 100 customers and each yields on average 20 relevant order records, Plan B expects 2,000 qualifying order rows, but that says nothing about the number of index pages or heap pages fetched. Make a cost table for sequential page reads, repeated index probes and CPU work. Vary the region's actual share from 5 percent to 30 percent and observe how a previously appealing probe plan can lose its advantage.

Introduce skew deliberately. Put half the orders under a handful of large corporate customers, even though most customers have only a few orders. An estimate based on the average customer can badly predict a query focused on those large accounts. Save estimated and actual rows at each EXPLAIN node and identify the first divergent node. The query planner may react to fresh histograms or extended statistics; this is a specific diagnosis, not a universal recommendation to disable nested loops or force hashes.

Finally inject a correctness bug: add a CustomerPhone relation with two phone numbers for one customer and join it before aggregation. The result now double-counts that customer's order amounts. Try to “fix” it with DISTINCT and explain why DISTINCT over `(order_id,amount)` could be wrong when separate orders legitimately share an amount or identifier scopes differ. The correct solution is to avoid irrelevant one-to-many joins or to aggregate child relations at their intended grain. A tuning report must include these logical checks alongside timing data.

### Connections and deeper pitfalls

**Further investigation: when equivalent syntax is not equivalent semantics.** A filter on the nullable side of an outer join is a classic optimization trap. Suppose the objective is to list every customer and any unpaid orders. Filtering order_status='unpaid' in the ON clause retains customers with no unpaid orders, while filtering that column in WHERE removes those customers because their joined status is NULL. An optimizer cannot freely swap those expressions without changing answers. Similarly, replacing NOT EXISTS with NOT IN can be unsafe when the inner expression contains NULL; SQL's three-valued logic changes the truth of membership tests.

Cardinality analysis should inspect data grain. A join that produces five million rows where only five thousand are expected may reflect one-to-many relationships rather than a bad index. If the aggregation is applied after accidental row multiplication, indexing simply computes the wrong total faster. Before tuning, write the intended uniqueness assumptions in the query review: one row per order, per customer, per invoice or per event. Verify those assumptions with constraints and sample counts.

Performance experiments can be confounded by caching and warm-up. First execution may read many pages from storage; later executions may serve them from memory. Also a production database runs concurrent writes and background maintenance. Repeat tests, record distributions instead of one lucky timing and compare under equivalent load. Distinguish planning time from execution time where possible. The goal is a consistently correct and maintainable query with adequate latency, not the smallest isolated benchmark number.

## Three worked questions

### Problem 1: Query Plans: worked verification
Two tables have 100 and 200 rows. Find naive nested-loop pair comparisons.

**Set up the model and conditions**
For each of 100 outer rows compare against 200 inner rows.

**Carry out the calculation or proof**
Multiply 100×200=20,000.

**State the result and its scope**
The simple nested loop performs 20,000 pair tests absent early termination.

**Detailed reasoning and validation.** For each of 100 outer rows, a basic nested loop examines 200 inner rows, giving 100×200=20,000 pairwise predicate evaluations. This is comparison work, not the number of output rows. If no key values match, output cardinality could be zero while all 20,000 comparisons are still made. If every pair matches, output cardinality can be 20,000. An index on the inner join key changes the physical algorithm by allowing probes instead of full inner scans. To compare the alternatives fairly, count index probes, page accesses, predicate evaluations and materialized output rows separately; raw comparison count alone cannot predict end-to-end time.

**Answer:** The simple nested loop performs 20,000 pair tests absent early termination.

### Problem 2: Cost Estimates: worked verification
An optimizer estimates two independent filters each retaining 10%. What combined selectivity results?

**Set up the model and conditions**
Under independence multiply the individual probabilities.

**Carry out the calculation or proof**
0.10×0.10=0.01.

**State the result and its scope**
Estimated combined selectivity is 1%; correlated filters can differ.

**Detailed reasoning and validation.** If two independent predicates each retain one tenth of input rows, their joint selectivity is 0.1×0.1=0.01, or one percent. For a 100,000-row input the model expects approximately 1,000 rows. Independence is an explicit assumption: “campus=North” and “program=Physics” may be correlated, so an actual data set could retain 3,000 or 100 rows. When a join planner relies on the 1,000-row estimate and real cardinality differs, it may choose the wrong build side or join algorithm. Validate using COUNT(*) for each predicate and for their conjunction, then compare the observed conditional proportions with the independence approximation.

**Answer:** Estimated combined selectivity is 1%; correlated filters can differ.

### Problem 3: Join Algorithms: worked verification
Why can pushing a selection before a join reduce intermediate size?

**Set up the model and conditions**
A filter on one input discards rows not needed downstream when semantics allow pushdown.

**Carry out the calculation or proof**
The join processes fewer candidate rows and may fit memory better.

**State the result and its scope**
Savings depend on selectivity and physical algorithms; outer-join transformations need proof.

**Detailed reasoning and validation.** Let a large Orders table have 1,000,000 rows but a date predicate retain 2,000. Joining the filtered rows to Customer can be cheaper than joining all one million rows and discarding almost everything afterward, assuming the transformation preserves query meaning. The optimizer may also exploit a date index. But moving conditions across LEFT JOIN can change which unmatched rows survive, and predicates involving aggregates cannot generally be applied before aggregation. State the operator algebra and null semantics before rewriting. Measure intermediate row counts and actual I/O, not only SQL query length; a rewrite can look cleaner yet yield an unchanged execution plan after optimizer normalization.

**Answer:** Savings depend on selectivity and physical algorithms; outer-join transformations need proof.
