# Unit 3: Backend systems

## 3.1 Routing

Routing is the mapping from an incoming request to the application operation that will handle it. A framework can match a path pattern, extract parameters, dispatch middleware, and execute a controller. Order and precedence matter. If /users/:id appears before /users/new in a naïve router, the literal new path may be interpreted as an identifier. More serious mistakes occur when authorization middleware protects one route but misses an alternate route or method. Treat a route table as an externally visible API surface and review it with the same care as a schema.

The router should not contain every business rule. Its tasks include request parsing, method selection, basic validation, authentication context, response serialization, and error mapping. A service layer can enforce domain rules regardless of whether it was called through HTTP, a background job, or an administrative CLI. Consider /books/:bookId/borrow. The handler should establish who is requesting the book, invoke a domain operation, and translate a conflict into an appropriate response. It should not manually update five unrelated tables with unchecked queries, because that makes correctness dependent on one HTTP route.

Route parameters are untrusted input. An integer-looking identifier may overflow a parser; a path may contain percent-encoded delimiters; a query parameter can appear more than once. Declare whether a route accepts GET or POST, whether an omitted query value has a default, and whether an unsupported media type is rejected. A typed router or schema validator can reduce ambiguity, but developers must still decide what malformed input means. Returning 404 for an inaccessible object may be a deliberate anti-enumeration policy; returning 403 may provide more explicit client behavior. Either choice needs consistent enforcement and threat analysis.

Test a routing graph with both expected and unexpected requests. Include method mismatches, route collisions, suspicious encodings, missing authentication, and client requests from older versions. In a reverse-proxy deployment, verify path prefixes and host forwarding; a server that runs at '/' locally may run under '/api' in production. When generating absolute redirect URLs, use a configured trusted origin rather than blindly trusting forwarded Host headers. Routing is a boundary between the open network and domain behavior, so subtle assumptions here propagate through the entire system.

### Applied design, experiment, and interpretation

**Case analysis: unexpected route capture.** An application registers `/courses/:id` and `/courses/new`. A framework resolves the parameterized pattern first, so the New Course screen tries to fetch the resource with ID 'new'. Fix the order or use an explicit route constraint. Then inspect `/courses/4/export` to ensure its protected handler cannot be reached through a differently written path or HTTP method. If a reverse proxy strips a prefix, verify that redirects still include the correct public base. A route table should be tested as a graph of valid and invalid destinations.

**Research exercise.** Send GET, POST, PUT, and DELETE to both static and parameterized routes. Test URL encoded separators and malformed identifiers. Capture the router's resolved handler without exposing credentials. Confirm that authorization middleware executes for every sensitive variant. Different frameworks have different matching semantics, so tie the expected outcome to the actual implementation.

## 3.2 Apis

An API defines a contract between producers and consumers. That contract includes resource identity, request and response shapes, pagination, error semantics, authentication requirements, and compatibility guarantees. A JSON response is only one representation format; simply returning JSON does not make an endpoint well designed. A coherent API models resources and operations in terms that clients can reason about. A library service might provide GET /books?subject=physics, GET /books/:id, and POST /loans, with response fields documented precisely. The client should not need to inspect error-message prose to identify a machine-actionable conflict.

Pagination requires a stability strategy. Offset pagination can work for small relatively static lists, but a dataset changing between requests may cause duplicates or skipped items. Keyset pagination uses a stable ordering key and a cursor representing the next position; this is often more reliable for large feeds. Neither method is safe if the sort order is not deterministic. Filtering and sorting also need validation so that a user cannot inject arbitrary database expressions through a query parameter. Versioning should be based on actual compatibility needs: adding an optional field may be backward compatible, while reinterpreting an existing value often is not.

API errors should be legible and safe. An error response can carry a stable code, a concise explanation, and a correlation identifier. It should not expose raw SQL, stack traces, internal IP addresses, or other users' records. Rate limits, retry guidance, and cache policies are part of the contract. A client receiving 429 may reduce request frequency according to the service's guidance, but should avoid synchronized retries that increase the load. A server receiving the same idempotent request twice should not inadvertently create two conflicting effects.

Contract tests and integration tests serve different purposes. A contract test verifies structure and basic semantics; an integration test proves that the endpoint actually enforces domain logic against data stores and upstream dependencies. Maintain sample successful and failure responses, including boundary conditions. Use an OpenAPI description if suitable, but keep it synchronized with implementation. When a mobile client is deployed for months without an update, breaking its assumptions is not just a technical inconvenience; it can interrupt students' access to essential study materials. Design APIs for evolution as well as immediate convenience.

### Applied design, experiment, and interpretation

**Case analysis: paginating an expanding library.** A service returns the latest uploaded textbooks, sorted by created time. With offset pagination, a new book inserted before the second page can shift records so that the client sees one title twice and another not at all. A cursor containing the last seen sorting tuple, such as `(created_at,id)`, provides a more stable progression for a descending ordered feed. The identifier breaks ties when two books share a timestamp. The cursor must be validated and must not grant access to records outside the requester's authorization scope. A changing catalog may still yield snapshot inconsistency; document the guarantee instead of promising a perfect historical view.

**Research exercise.** Create test data with duplicate timestamps, insert new records between requests, and compare offset versus keyset page traversal. Verify no unauthorized books appear even when a cursor is guessed or modified. Document whether deleting a book during pagination can cause a legitimate item to disappear from the traversal. Expose a stable error code for invalid cursors rather than dumping parser internals.

## 3.3 Validation

Validation turns an untrusted representation into a well-defined domain input. It begins at parsing, continues through schema checks, and ends with business invariants. A request body may be syntactically valid JSON but still carry impossible or unauthorized meaning: an exam duration of minus fifteen minutes, a chapter title of ten million characters, or an attempt to change a field that only staff should control. Client-side validation helps users correct mistakes quickly, but it is always bypassable. The server must validate every externally supplied value, even when it originated from the application's official frontend.

Design validation by articulating invariants rather than by collecting arbitrary regular expressions. A quantity of books borrowed can be an integer within a defined range, and a due date must follow the checkout date under the relevant time zone policy. Unicode strings require thought about normalization, length, and storage representation. Email syntax and deliverability are distinct questions, and a permissive standards-aware parser is often preferable to an invented fragile regex. Reject unknown fields when clients should not be able to set them, or explicitly ignore them under a documented compatibility contract. Deserialization can change types in surprising ways, so validate after parsing and before domain operations.

Validation errors are part of user experience. If an enrollment form fails, return field-specific messages without exposing sensitive validation details. Do not report 'invalid credentials' in a way that needlessly reveals whether an account exists. Use server-side length limits and request size caps before expensive parsing to reduce resource exhaustion. Recheck cross-record constraints inside the same database transaction that makes a change, because an earlier read can become stale before the write. Duplicate usernames and limited-capacity course seats cannot be reliably protected by frontend checking alone.

A useful test suite contains three families: valid input representatives, boundary input representatives, and adversarial input representatives. If maximum file size is ten megabytes, test just below, exactly at, and above the boundary. If an integer field must be at least one, test zero, negative values, decimals, numeric strings, null, and very large values. Record which layer rejects the request. An application is not well validated simply because it refuses obviously malformed syntax; it must preserve meaningful business truth under races, encoding tricks, and direct API access.

### Applied design, experiment, and interpretation

**Case analysis: an assignment file upload.** A student may upload a PDF of at most 10 MB for one course. A client-side input limit gives immediate feedback, but a direct API request can bypass it. The server should enforce body-size limits before expensive buffering, validate the enrollment and due date, inspect the actual file type using appropriate parsing checks, and store the file under a generated key outside executable paths. An archive-like upload or malformed PDF may consume substantial resources during processing; extraction should run with bounded memory and privileges. Student-supplied filenames are display metadata, not storage paths.

**Research exercise.** Test 0 bytes, 9.99 MB, 10.00 MB, 10.01 MB, unsupported types, and a valid file renamed with a different extension. Attempt a late submission and a submission to another course. Verify that validation failures leave no orphaned database references or unbounded temporary files. Record what is checked synchronously and what security scanning occurs asynchronously.

## 3.4 Business Logic

Business logic represents the rules the application exists to enforce. In a course platform, it decides who can submit an assignment, when an attempt closes, and whether a certificate can be issued. These rules must not be scattered across HTML templates, route handlers, and background workers. A domain function should receive validated inputs, consult authoritative state, enforce invariants, and commit an outcome. The same function may be invoked by an HTTP request or a scheduled job without changing its meaning. Keeping this boundary clear makes the system testable independently of the web framework.

Consider a paid laboratory booking. Each session has a capacity of twenty seats. A naïve implementation reads the current number of bookings, sees nineteen, and allows the request. Two concurrent requests can both observe nineteen and create twenty-one bookings. The invariant is not 'show a warning at twenty' but 'never commit more active bookings than capacity'. Enforce that through a transaction with appropriate locking or a conditional update, or use a database constraint where the model permits. This is an example of domain correctness requiring infrastructure cooperation. A unit test that invokes requests sequentially will not reveal the race; a concurrent integration test may.

Separate commands from queries when it improves clarity. A command attempts to change state and may fail for business reasons; a query reads a projection that might be cached or eventually consistent. Do not pretend a read immediately after a write always observes the latest value if it is served from a delayed replica. Domain events can capture that 'a booking was confirmed' for email or analytics, but event publication must be coordinated with the database commit. Otherwise a message can be sent for a transaction that later rolled back, or a committed booking may never generate its message.

The most useful documentation is an invariant table: what must always be true, which operation can change it, which data store enforces it, and which tests prove it. Include cancellation, partial failure, retries, and administrative exceptions. A maintainable web service is one in which these business rules remain intelligible after the router, UI framework, and hosting provider have changed. That goal is more demanding than quickly assembling working screens, but it directly reduces financial and operational mistakes.

### Applied design, experiment, and interpretation

**Case analysis: reserving the last seat.** A course has capacity one remaining. Two students click Enroll within the same millisecond. Both requests can read the old count and decide that space exists. Domain logic needs one atomic reservation decision, possibly implemented with a conditional update or suitable row lock. When the second request fails, it should receive a meaningful conflict response rather than a generic outage message. Payment or email effects must not be started for a reservation that will not commit. The route handler delegates to the domain operation, keeping the invariant in one place.

**Research exercise.** Run the requests concurrently against a real transactional database. Assert that at most one seat was consumed and one registration committed. Crash the process after committing but before responding; retry the request using the same operation key and verify that a duplicate reservation is not created. Do not substitute sequential unit tests for this concurrency evidence.

### Integrated laboratory: a contract-driven enrollment API

Design three endpoints for an academic enrollment service: read a course offering, request a seat, and inspect one student's enrollment status. Define which operations are safe reads and which cause state changes. Sketch example HTTP requests and responses with realistic status codes. A successful reservation may return 201, a duplicate request with the same idempotency key should return a consistent existing result, and a full course may generate a domain conflict rather than 500. The contract must specify authentication, authorization, request validation, and a stable error shape. Do not rely on a browser's hidden button to prevent direct API calls.

Define the database invariants. The number of confirmed seats may not exceed capacity; a student may have at most one active enrollment for a particular course; an instructor may manage only assigned offerings. Build the simplest schema and unique constraints that support those rules. The first endpoint can use a prepared parameterized query and return a public subset of course metadata. The second must evaluate the capacity change and record creation in an appropriate transaction. The third must use identity-scoped access and avoid exposing another student's record by changing an identifier in the path.

Create a validation matrix. For courseId, test a valid identifier, missing value, malformed text, excessive length, and an identifier for a resource the user cannot access. For seat requests, test absent credentials, expired sessions, duplicate operations, and requests using a different student's identity. Record which error is expected and which layer detects it. If your framework validates JSON syntax automatically, still test domain constraints after parsing; syntactically valid input can contain an impossible semester or a forbidden assignment of staff-only fields.

Introduce a concurrency experiment with one available seat and two simultaneous clients. Both requests should not succeed. Use a real transactional database in the test if possible and run the requests with a synchronization barrier so that the race is likely to occur. A sequential test of two handler functions is inadequate evidence. Consider the crash window after commit and before client acknowledgement; show how a stable idempotency key allows the client to retry safely.

End with a review of failure and observability. Map each response into a client state, including loading, success, validation error, authorization failure, conflict, and temporary server failure. Add a correlation identifier to logs and error responses without logging passwords or entire sensitive request bodies. Trace a request from router through domain service to database transaction. Explain which contract fields may evolve compatibly and which would require client migration. The result is a modest API with a clear correctness argument, not an oversized architecture diagram.

### Synthesis: translating public requests into safe domain changes

Every request crosses layers with different responsibilities. A router decides which handler matches the path and method. A validator establishes usable types and bounds. An authentication layer associates a verified identity. An authorization check determines what this identity may do to this particular resource. The domain layer enforces business invariants, and persistence commits the consequence. Collapsing these into a single controller makes it difficult to see missing checks. Overseparating them into dozens of services can also obscure the business outcome. The appropriate boundary is the simplest one that makes correctness inspectable and testable.

Revisit a course-seat reservation. A request may have perfectly valid JSON, a recognized route, and a legitimate student session while still conflicting with capacity. A 409 conflict communicates a business outcome, not a programming failure. Concurrent reservations require a transaction or conditional write; the browser's disabled Submit button does not enforce that invariant. A retry after timeout must not create a second reservation, and response codes should guide the client accordingly. Build tests from these narratives: malformed IDs, forbidden courses, last-seat races, duplicate operation keys, and a crash after commit. A sound backend contract must survive clients you do not control and failures you did not schedule.

## Worked questions

### Resolve a route collision

A router registers /users/:id before /users/new. A request for /users/new reaches the generic handler. Identify the defect and design negative tests including unauthorized access.

**Explain the collision.** The parameterized route treats 'new' as an identifier under a router that resolves the pattern first. The handler may query a nonexistent user or leak an internal parsing error. Static paths and parameterized paths need an explicit precedence rule or constraints. Route order is framework dependent, so the fix must be chosen for the actual router rather than assumed from a generic example.

**Select a remedy.** Register the static path ahead of the parameterized one when order governs matching, or constrain the identifier route to a validated type or naming scheme. Keep authorization middleware bound to every sensitive method and variant. Do not treat guessing a numeric identifier as the user's authorization to see a profile.

**Test the boundary.** Send GET /users/new, GET /users/9, GET /users/garbage, and state-changing requests against both forms. Exercise encoded path segments and a missing login session. Assert the resolved handler and HTTP status as well as whether private records are returned. A correct router should reject unauthorized and malformed requests without falling through to a less protected alternate handler.

### Compare pagination designs

A library has 1000 books sorted by (created_at,id). A client loads 50 entries per page while a new book is inserted before page two. Explain the offset anomaly and a keyset alternative.

**Show the offset risk.** The first request returns positions 1–50 under the original ordering. A new book inserted at the top shifts the old positions by one. If the second request uses offset 50, it can include the old fiftieth book again and move another book to the next page. The exact affected records depend on ordering, but the duplicate or omission risk follows from mutable offsets.

**Specify a cursor.** Use a stable total ordering such as descending created_at with id as the tie-breaker. Return a cursor derived from the last seen tuple and request records after that tuple under the chosen order. This avoids the simple top-insertion duplication but does not automatically create a historical snapshot if records are edited or removed.

**Validate API behavior.** Protect the cursor against malformed values and apply the same authorization filter on every page. Create test data with identical timestamps to verify tie-breaking, insert and delete between requests, and document the guarantee that clients may rely on. An API contract should say how to detect the end of a collection, not merely expose an arbitrary page number.

### Validate a course upload

An assignment endpoint permits PDFs up to 10 MB from enrolled students. Describe boundary inputs and the order in which the service should reject invalid submissions.

**Order cheap checks.** Authenticate and authorize the student for the course; enforce request size at the earliest practical stage; and validate media and file properties in a bounded parser before committing metadata. Reject unsupported types and oversize bodies without reading unlimited content into memory. A user-controlled filename must not determine the server's storage path.

**Choose boundary cases.** Test an empty file, just below the maximum, exactly at the maximum under the service's defined byte units, and one byte above. Also test a non-PDF renamed with a .pdf extension, malformed input, a late assignment, and an unauthorized course. Document whether 10 MB means decimal ten million bytes or binary ten mebibytes so the test has a definite oracle.

**Verify cleanup and consistency.** A rejected upload should not leave a durable successful-submission record or unbounded temporary bytes. If scanning or conversion is asynchronous, the UI should distinguish Uploaded from Accepted or Processed. Test crashes after object storage succeeds but before metadata commits. The correct result includes recoverable state, not only a useful validation error message.

