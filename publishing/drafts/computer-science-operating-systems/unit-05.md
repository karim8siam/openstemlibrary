# Operating Systems — Unit 5: File systems

naming; directories; allocation; crash consistency

## §5.1 Naming

**Core model — Naming**

A file-system namespace maps names to directory entries and underlying file objects. Names and data objects need not be in one-to-one correspondence.

**Original worked illustration**

Two hard links can name the same inode; removing one directory entry does not delete data if another hard link remains.

**Boundary conditions and checks**

Symbolic links refer to paths and can become dangling. Permissions and mount boundaries alter resolution semantics.

### Names, inode identity, and file lifetime

A pathname is a route through directory entries, not the file object itself. In a common inode-based model, each directory maps names to inode references. Two hard-link names can therefore identify the same inode and underlying bytes. Removing one directory entry decreases the name reference count; it need not immediately destroy the file. Open descriptors can also keep an object reachable under the file system's lifetime rules. A symbolic link is different: it stores a path-like target and can cross directory boundaries or become dangling if its target is removed. The distinctions matter for safe updates, cleanup code, backup tools, and access-control decisions.

Imagine an application writing a report into a temporary file and then replacing a published report name. Readers that already opened the old object may continue reading it, while later path lookups can reach the new object after a successful atomic rename in a filesystem and operation scope that supports that guarantee. 'Atomic' means observers do not see an intermediate namespace state; it does not mean the new contents are crash durable. File data and directory-entry persistence have separate ordering requirements. Applications that need a crash-safe protocol must consult their platform's sync and rename guarantees and test under controlled fault injection.

A directory traversal is also a security-sensitive operation. If an application receives a user-controlled path, components like '..', symbolic links, mount boundaries, and concurrent renames can defeat naive prefix checks. A string beginning with an approved directory prefix is not proof that its resolved file object is below the approved directory. Handle-relative traversal with explicit resolution restrictions can reduce ambiguity where supported. For a learning exercise, draw a tiny namespace with three inodes, four names, one symbolic link, and two open descriptors. Then perform unlink, rename, and descriptor close operations and update the reference graph. Students should compute which names remain valid and which objects remain open, separating namespace visibility from actual reclamation. This gives a more accurate model than saying deleting a name always deletes data.

## §5.2 Directories

**Core model — Directories**

Directories organize names into a hierarchy and require well-defined lookup, insertion and removal semantics. Race-free resolution matters for security.

**Original worked illustration**

A relative path ./data/report traverses the current directory's data entry and then report. The same path can resolve differently after a directory rename.

**Boundary conditions and checks**

A prior permission check followed by a separate open can suffer a time-of-check/time-of-use race if another process changes the path.

### Directories as indexed metadata and atomic namespaces

Directories are data structures maintained by the filesystem. Their purpose is to map component names into objects while enforcing permissions and consistency constraints. Small directories may use linear records; large implementations often adopt hashing or tree-like indices to reduce lookup cost. The choice is partly an engineering decision about update frequency, locality, sorting, and crash recovery. A directory entry is not a copy of the entire file's contents. Its recorded fields may include a name and object identifier, while size, blocks, timestamps, and link count belong to associated metadata. Exact structures differ by filesystem and should never be implied by a generic POSIX example.

An absolute path begins at a designated root of the process's namespace; a relative path begins at a working directory or an explicitly provided directory handle. Concurrent mutation matters because each component may be resolved at a different moment. Suppose a cleanup tool checks that '/allowed/project/output' lies under '/allowed' as a string, then follows a symbolic link whose target has changed to '/private'. The supposed authorization check does not bind the subsequent operation to the same object. Safe designs rely on handle ownership, resolve-time restrictions, or a namespace with enforced immutability when the threat model demands it. This is a correctness and security issue, not just a path-formatting detail.

Directory changes also interact with durability. Replacing a name may atomically switch visibility to other processes while leaving metadata in volatile caches until storage barriers occur. Crash testing should simulate interruption after file creation, after data writes, after rename, and after directory synchronization. The acceptable outcome is specified by the application, not by a vague claim that the filesystem is 'journaled.' Journal modes vary, and a journal protects some kinds of metadata consistency without necessarily promising complete application-level transaction semantics. In a lab, model a directory as a mapping and record a transactional rename from an old report to a new report. Show what a reader with a previously opened descriptor observes, what a new path lookup observes, and which steps a durable publication protocol requires. Distinguish process-level visibility from post-crash persistence throughout.

## §5.3 Allocation

**Core model — Allocation**

On-disk allocation structures assign data blocks to files. Extents, indirect pointers and bitmaps trade metadata cost, fragmentation and random access efficiency.

**Original worked illustration**

A 9000-byte file needs ceil(9000/4096)=3 blocks if block size is 4096 bytes, wasting 3288 bytes in the final allocated block.

**Boundary conditions and checks**

Real systems may store tiny files inline or use sparse holes; the ceiling formula models simple full-block allocation.

### Block allocation, free-space records, and locality

File contents are commonly stored in fixed-size logical blocks, even though applications read and write byte ranges. If block size is 4096 bytes, a 9000-byte file requires three full block allocations under a simple contiguous-block model: ceiling of 9000 divided by 4096 is three. The third block has 3288 bytes of unused capacity. This accounting describes allocated data capacity, not necessarily physical space consumed on a compressed, sparse, deduplicated, or copy-on-write filesystem. An engineer must choose which measure is relevant to capacity planning and document whether indirect metadata blocks, journaling, and replication count toward the total.

Block-mapping designs include extents, indexed pointers, linked allocation, and combinations. Extents encode a run of adjacent blocks compactly and can improve sequential I/O when sufficient contiguous free space exists. Indexed blocks allow flexible random access but can require additional metadata lookups. Sparse files represent unallocated ranges logically filled with zeros, enabling very large apparent lengths with relatively few physical blocks. Preallocation can reduce fragmentation but reserves capacity even if the application never writes all bytes. Copy-on-write can make sequential logical writes touch scattered physical locations until the allocator and maintenance tools reorganize them.

A concrete trace starts with six free extents of lengths 4, 3, 8, 2, 5, and 6 blocks. A request for seven contiguous blocks can be satisfied by the length-eight extent, although the total count of free blocks was far larger even before selection. After several requests, the remaining free extents can be too small for a new contiguous request despite large aggregate free space. Explain why an extent-based allocator might fall back to multiple extents, and why a requirement for *one* physically contiguous region is stronger than the ordinary promise to represent a file correctly. In a practical lab, track each allocation and free event as a block map, compute slack for files of different sizes, and differentiate block fragmentation from free-space fragmentation. Include a sparse file and compare logical length against allocated block count. Avoid calling any one allocation heuristic globally optimal: media behavior, write patterns, and background maintenance change the performance stakes.

## §5.4 Crash Consistency

**Core model — Crash Consistency**

Crash consistency governs which updates survive sudden failure. Journaling, copy-on-write and ordered writes enforce different consistency targets.

**Original worked illustration**

Writing new file data and then atomically replacing its directory pointer can avoid exposing half-updated content if flush and rename semantics are correctly respected.

**Boundary conditions and checks**

Atomic rename does not automatically guarantee durable user data: synchronization calls and underlying device guarantees still matter.

### Journaling, ordering barriers, and crash consistency

Crash consistency is the question of which application-visible states remain after power loss, process failure, or device reset. A program may issue write calls that succeed because data reached an operating-system cache rather than stable media. Metadata changes may be reordered for performance. Journaling can help a filesystem recover to a structurally consistent state after interruption, but it is not the same as guaranteeing that a particular application record survives. The application must establish the durability contract it needs: for example, whether a committed transaction must remain readable after the machine restarts, and what happens to a partially committed update.

A classic write-replace protocol uses a temporary file in the destination filesystem. The application writes the complete new contents, validates length and checksums, requests durable persistence of the file as appropriate, atomically replaces the destination name where supported, and then requests persistence of the containing directory metadata. This sequence is still subject to platform-specific rules; exact API calls and ordering are not universal. If a crash occurs immediately after the rename but before the relevant metadata reaches stable storage, some platforms may recover the previous name state. If the temporary data were not flushed, the new name could be visible before a crash but contain missing or stale bytes afterward. An effective lesson enumerates these cases rather than promising that rename alone solves everything.

Write-ahead logging is a related database technique: record intended changes durably before exposing a state that depends on them. During recovery, a log can guide redo or undo according to the system's transaction design. The log needs its own checksums, sequence numbers, and failure handling. For a lab, use a small simulated store with an old record A and intended replacement B. Inject a crash at six labeled points in the update protocol and record allowable states upon restart. Separate the property that the file system mounts successfully from the property that the application sees only valid complete records. Explain how checksums detect corruption but do not by themselves provide atomicity, and how ordering constraints help prevent mixed generations of metadata and data.

### Integrative case study — publishing a durable configuration file

A service periodically creates a configuration snapshot that other processes read by pathname. The desired property is that readers see either the previous complete snapshot or the new complete snapshot, never a partly written file. A second possible requirement is durability: after the service reports success, the new snapshot should survive a crash under documented storage guarantees. Those two properties are related but not identical. Atomic replacement controls the namespace transition; durable persistence controls which bytes and metadata survive abrupt failure. Many incorrect implementations achieve one but silently assume the other.

Write a candidate protocol. First open a unique temporary file in the destination directory or filesystem. Validate that the serialized content is well formed and stays under a maximum length. Write until all bytes are accepted, handling partial writes and errors. If the durability contract requires it, request a synchronization operation for the temporary file after writing. Next replace the destination name through a rename operation with the required atomicity guarantee for that filesystem and namespace relationship. Finally, synchronize relevant directory metadata as supported and required for crash persistence. Document platform assumptions rather than asserting that all filesystems implement identical durability guarantees.

Now inject failures. If the process crashes before writing the full temporary file, the stable destination should still refer to the old snapshot; cleanup may later remove a stray temporary object. If it crashes after writing but before rename, the stable destination also remains old, even if the temporary bytes reached disk. If it crashes after a successful rename but before metadata durability, the recovered state may depend on the filesystem and its guarantees; it is wrong to claim certainty without specifying them. If the new content failed validation, the program should never proceed to replace the destination. Application-level checksums can detect corrupted bytes, but do not themselves ensure atomic replacement or flush ordering.

Storage allocation is another concern. Suppose the snapshot is 9000 bytes and the filesystem allocates 4096-byte blocks with no compression. It needs three data blocks and has 3288 bytes of last-block slack. Rewriting the file by copy-on-write can temporarily require enough free space for both old and new block generations, plus metadata. A full disk may therefore prevent safe update even if the final visible file is no larger than the previous one. A production service must handle ENOSPC-like failures without destroying the last known good configuration. Creating a temporary file in an unrelated filesystem may also invalidate assumptions about atomic rename, so the target location matters.

Design an acceptance suite with fault injection at every labeled step, including short writes, permission denial, out-of-space, interrupted synchronization, rename failure, and power loss. Check all recovered snapshots using schema validation and generation identifiers, not simply file existence. Add two simultaneous writers and decide whether last-writer-wins behavior is acceptable or whether serialization or compare-and-swap semantics are needed. The resulting protocol has a proof obligation: one published generation is visible at a time under the chosen name, and success means exactly the durability property that was promised. This project ties together names, inodes, descriptors, allocation, crash consistency, and application-level correctness.

### Diagnostic exercise — durability is not visibility

Construct a crash-injection state table with columns for temporary file created, data write accepted, data synchronized, destination rename acknowledged, and directory metadata synchronized. Write down whether a live reader opening the stable name sees old or new bytes at each point. Separately state possible recovered outcomes after an immediate crash under the platform assumptions chosen for the exercise. A rename that is atomic for live path lookups may still require explicit directory synchronization for post-crash persistence. Next introduce two writers using the same target name. Decide whether one should win, whether version checks are needed, and whether an observer might see stale generations. Calculate the number of 4 KiB data blocks needed for lengths 0, 1, 4096, and 4097 bytes in the simplest non-sparse allocation model, then explain why copy-on-write and sparse files can invalidate a naive physical-capacity estimate.

### Boundary cases and falsifiable design claims

An empty file requires zero data blocks in a simple sparse-capable model but still consumes metadata and a directory entry; a file with one byte can require one allocated data block. A file exactly equal to the block size has zero slack, whereas adding one more byte creates a new block and nearly a full block of unused capacity. Compression and delayed allocation invalidate naive physical-space estimates, so a tool's displayed logical size and blocks-allocated field must be interpreted separately. An inode can outlive its last name if open references remain, while a renamed path may identify the same inode in another directory. These are distinct mechanisms and must not be conflated.

Crash persistence includes device behavior. A write sent to a device cache may be acknowledged before nonvolatile storage has committed it, depending on hardware configuration and protocol. Flush and barrier commands exist to establish ordering and persistence conditions, but their effectiveness depends on supported hardware guarantees. A journal may replay metadata after interruption without guaranteeing that an application's newly written file contents are complete. Consequently, a correct updater should use checksums or validation alongside the persistence protocol, and it should retain a recoverable previous generation when appropriate.

For a more advanced lab, create two simultaneous editors of the same configuration document. Each reads version seven and prepares a different version eight. If both rename over the stable name without coordinating, one update is lost even if each rename is individually atomic. Add generation numbers or conditional synchronization and define whether the application rejects conflicting writes or merges changes. Test that conflicts are detected across process crashes and retries, not merely within one runtime's memory. The exercise demonstrates that crash consistency, atomic namespace operations, and multi-writer concurrency control are three different problems requiring separate designs.

## Three worked questions

### Naming: worked application 1

A file of 9000 bytes uses 4096-byte blocks. Count allocated blocks and slack bytes.

**Set up the model and conditions**

Two blocks hold 8192 bytes and leave 808 bytes uncovered.

**Carry out the calculation or proof**

A third block is necessary; allocated space 3×4096=12288.

**State the result and its scope**

Slack is 12288−9000=3288 bytes.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Compute blocks using the ceiling function: ceil(9000/4096)=3. Multiplying yields 3×4096=12,288 allocated data bytes. Subtracting the logical file length gives 3,288 unused bytes in the last block under the simple non-sparse, noncompressed allocation model. Check that two blocks provide only 8192 bytes, insufficient for 9000; three provide enough. The result counts data-block capacity rather than inode metadata, journaling overhead, replicas, or device wear-leveling. A sparse file with the same logical size could use fewer data blocks, while a copy-on-write snapshot might require additional backing blocks. Boundary tests at 4096 and 4097 show the jump from one to two blocks. This teaches both ceiling arithmetic and the importance of specifying what 'disk usage' means.

### Directories: worked application 2

Two hard links point to one inode. One name is removed. Must the file data disappear?

**Set up the model and conditions**

Removing the name reduces the inode's link count by one.

**Carry out the calculation or proof**

The remaining hard link still reaches the object, and open handles may also retain references.

**State the result and its scope**

No; data remains until reference and filesystem lifetime rules permit reclamation.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

Two directory entries reference the same inode. Removing one name decrements the link count from two to one, so a second pathname still resolves to the file. The data are not destroyed solely because the first name disappeared. In many Unix-like models, even unlinking the last name need not immediately free blocks if an open descriptor still references the object. Reclamation depends on both namespace references and open-object lifetime. A symbolic link behaves differently: it stores a target path instead of incrementing the target inode's hard-link count. Removing the original name can therefore leave a symbolic link dangling. Demonstrate the result by drawing inode I with arrows from names A and B, then deleting arrow A. The remaining arrow B shows why identity is separate from naming. The conclusion depends on filesystem semantics and permissions, which should be stated rather than assumed globally.

### Allocation: worked application 3

Why is atomic rename alone not proof of durability after a crash?

**Set up the model and conditions**

Rename can provide atomic namespace replacement in a filesystem's supported scope.

**Carry out the calculation or proof**

Crash persistence also depends on flushing file content and directory metadata to stable storage.

**State the result and its scope**

Durability must be verified with sync semantics and fault tests.

**Independent verification and failure-mode analysis**

#### Extended verification and failure-mode analysis

A rename can atomically change which object a pathname designates without guaranteeing that the newly referenced file data or directory entry is durable after abrupt power loss. If an application writes bytes to a temporary file and immediately renames it, the writes may still be buffered. Under an intended crash-durable update protocol, it may need to synchronize the temporary file contents before renaming and synchronize relevant directory metadata afterward, subject to its filesystem's documented guarantees. Check two distinct properties: visibility atomicity during normal operation and persistence after restart. An observer seeing either old or new content before a crash establishes the first, not the second. A fault-injection test should interrupt after creation, write, file sync, rename, and directory sync, and report permitted recovered states. Never claim a particular platform's guarantees without qualifying them.
