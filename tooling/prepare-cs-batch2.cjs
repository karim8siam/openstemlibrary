const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'operating-systems',
    title: 'Operating Systems',
    subtitle: 'Kernel Abstractions, Process Scheduling, Synchronization, Memory Virtualization & File Systems',
    seoTitle: 'Operating Systems: Kernel Abstractions, Virtual Memory, Concurrency & File Systems | OpenSTEM Library',
    badgeCredits: 'Operating systems core',
    courseCodes: ['CS 205', 'CS 304'],
    searchPlaceholder: 'Search system calls, user/kernel mode, process state transitions, context switching, scheduling policies, mutexes, semaphores, deadlock conditions, page replacement, TLB misses, virtual memory, inode file system…',
    probSecTitle: 'Step-by-Step Operating Systems Solutions',
    description: 'Comprehensive university textbook covering operating system kernel architecture, dual-mode execution, preemptive scheduling, process control blocks, synchronization primitives, deadlock avoidance (Banker\'s algorithm), two-level paging, translation lookaside buffers, demand paging, inode allocation, and journaling file systems with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university operating systems courses. Eight units with exactly three solved questions per unit and interactive simulations illustrating scheduling algorithms, page replacement policies, and semaphore mutual exclusion. Numerical checks and an editorial review support this edition.',
    keywords: ['Operating Systems', 'Kernel Architecture', 'Process Scheduling', 'Concurrency and Deadlocks', 'Virtual Memory and Paging', 'File Systems and Inodes', 'I/O Subsystems', 'Protection and Security'],
    refPath: 'publishing/drafts/computer-science-operating-systems/references.json'
  },
  {
    slug: 'database-systems',
    title: 'Database Systems',
    subtitle: 'Relational Algebra, SQL Semantics, Storage Structures, B+ Trees, Query Optimization & ACID Transactions',
    seoTitle: 'Database Systems: Relational Algebra, B+ Trees, Query Optimization & ACID Transactions | OpenSTEM Library',
    badgeCredits: 'Database systems core',
    courseCodes: ['CS 305'],
    searchPlaceholder: 'Search relational algebra, tuple relational calculus, B+ tree leaf split, buffer pool management, external merge sort, cost-based query optimization, two-phase locking, serializability, write-ahead logging, ARIES recovery…',
    probSecTitle: 'Step-by-Step Database Systems Solutions',
    description: 'Comprehensive university textbook covering relational model mathematics, relational algebra, SQL declarative semantics, heap files, slotted pages, B+ tree indexing, buffer pool replacement (LRU-K), cost-based join optimization (nested loops, hash join, sort-merge), concurrency control (2PL, snapshot isolation), and ARIES write-ahead logging recovery with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university database systems courses. Eight units with exactly three solved questions per unit and interactive simulations illustrating B+ tree splits, join selectivity, two-phase locking schedules, and write-ahead log recovery. Numerical checks and an editorial review support this edition.',
    keywords: ['Database Systems', 'Relational Algebra', 'SQL Semantics', 'B+ Tree Indexing', 'Query Optimization', 'ACID Transactions', 'Concurrency Control', 'ARIES Recovery'],
    refPath: 'publishing/drafts/computer-science-database-systems/references.json'
  },
  {
    slug: 'computer-networks',
    title: 'Computer Networks',
    subtitle: 'Layered Architectures, Link Framing, IP Routing, BGP, Reliable Transport, Congestion Control & Security',
    seoTitle: 'Computer Networks: Layered Architecture, IP Routing, TCP Congestion Control & Sockets | OpenSTEM Library',
    badgeCredits: 'Computer networks core',
    courseCodes: ['CS 306', 'CS 308'],
    searchPlaceholder: 'Search OSI and TCP/IP models, CSMA/CD, link serialization, IPv4/IPv6 addressing, subnet masking, Dijkstra link-state, Bellman-Ford distance vector, BGP peering, TCP three-way handshake, sliding window, Tahoe/Reno congestion control, TLS handshake…',
    probSecTitle: 'Step-by-Step Computer Networks Solutions',
    description: 'Comprehensive university textbook covering the layered Internet architecture, framing, error detection (CRC), link-layer switching, IPv4 and IPv6 routing, distance-vector and link-state protocols (OSPF, BGP), TCP reliable transport, flow control, sliding windows, AIMD congestion control, DNS, HTTP/3, and cryptographic network security (TLS 1.3) with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university computer networking courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating packet serialization, propagation delay, sliding window dynamics, and queueing models. Numerical checks and an editorial review support this edition.',
    keywords: ['Computer Networks', 'Layered Architectures', 'Link Layer Framing', 'IPv4 and IPv6 Routing', 'TCP Flow and Congestion Control', 'BGP Peering', 'DNS and HTTP/3', 'Transport Layer Security'],
    refPath: 'publishing/drafts/computer-science-computer-networks/references.json'
  },
  {
    slug: 'software-engineering',
    title: 'Software Engineering',
    subtitle: 'Requirements Engineering, Architectural Styles, Design Patterns, Agile Methods, CI/CD & Verification',
    seoTitle: 'Software Engineering: Architecture, Design Patterns, Agile Methods, Testing & DevOps | OpenSTEM Library',
    badgeCredits: 'Software engineering core',
    courseCodes: ['CS 307'],
    searchPlaceholder: 'Search requirements specification, user stories, architectural styles, microservices, SOLID principles, Gang of Four design patterns, test-driven development, continuous integration, static analysis, refactoring, technical debt, release management…',
    probSecTitle: 'Step-by-Step Software Engineering Solutions',
    description: 'Comprehensive university textbook covering software lifecycle models, requirements engineering, architectural styles (layered, event-driven, microservices), object-oriented design principles (SOLID), design patterns, refactoring patterns, automated testing pyramids, continuous integration and delivery (CI/CD), version control branching models, and technical debt management with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for undergraduate software engineering courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating requirement traceability, design pattern decoupling, and test coverage metrics. Numerical checks and an editorial review support this edition.',
    keywords: ['Software Engineering', 'Requirements Specification', 'Software Architecture', 'SOLID Principles', 'Design Patterns', 'Test-Driven Development', 'CI/CD Pipelines', 'Refactoring and Code Quality'],
    refPath: 'publishing/drafts/computer-science-software-engineering/references.json'
  },
  {
    slug: 'programming-languages-and-compilers',
    title: 'Programming Languages and Compilers',
    subtitle: 'Lexical Analysis, Context-Free Grammars, LR Parsing, Type Systems, Static Single Assignment & Code Generation',
    seoTitle: 'Programming Languages and Compilers: Lexing, Parsing, Type Systems, SSA & Code Generation | OpenSTEM Library',
    badgeCredits: 'Programming languages and compilers major',
    courseCodes: ['CS 308', 'CS 401'],
    searchPlaceholder: 'Search regular expressions, deterministic finite automata, context-free grammars, LL(1) parsing, LR(1) and LALR parser tables, abstract syntax trees, Hindley-Milner type inference, Static Single Assignment form, register allocation, garbage collection…',
    probSecTitle: 'Step-by-Step Programming Languages and Compilers Solutions',
    description: 'Comprehensive university textbook covering programming language paradigms, formal grammars, deterministic finite automata for lexing, LL(k) and LR(k) shift-reduce parsing, abstract syntax tree representations, static type systems, unification and Hindley-Milner type inference, Static Single Assignment (SSA) intermediate representation, control-flow graphs, loop optimizations, graph-coloring register allocation, and code generation with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university compilers and programming language theory courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating grammar parsing, type checking, and optimization lowering. Numerical checks and an editorial review support this edition.',
    keywords: ['Compilers', 'Programming Language Theory', 'Lexical Analysis', 'Context-Free Grammars', 'LR Parsing', 'Static Type Systems', 'SSA Intermediate Representation', 'Register Allocation'],
    refPath: 'publishing/drafts/computer-science-programming-languages-and-compilers/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'computer-science', 'programming-fundamentals', 'programming-fundamentals.html'),
  'utf8'
);

for (const cfg of bookConfigs) {
  const dom = new JSDOM(templateHtml, {
    url: 'https://openstemlibrary.com/' + cfg.slug,
    runScripts: 'outside-only'
  });
  const w = dom.window, d = w.document;
  w.setTimeout = () => 0;
  w.scrollTo = () => {};

  d.title = cfg.seoTitle;
  d.querySelector('meta[name="description"]').content = cfg.description;
  d.querySelector('link[rel="canonical"]').href = 'https://openstemlibrary.com/' + cfg.slug;

  for (const selector of ['meta[property="og:title"]', 'meta[name="twitter:title"]']) {
    const el = d.querySelector(selector);
    if (el) el.content = cfg.seoTitle;
  }
  for (const selector of ['meta[property="og:description"]', 'meta[name="twitter:description"]']) {
    const el = d.querySelector(selector);
    if (el) el.content = cfg.description;
  }
  const ogUrl = d.querySelector('meta[property="og:url"]');
  if (ogUrl) ogUrl.content = 'https://openstemlibrary.com/' + cfg.slug;

  d.body.dataset.bookPath = cfg.slug + '.html';
  d.body.dataset.chapterIndex = '0';
  d.querySelector('.brand-title').textContent = cfg.title;
  d.querySelector('.badge-credits').textContent = cfg.badgeCredits;
  d.getElementById('topic-search-input').placeholder = cfg.searchPlaceholder;

  d.querySelectorAll('.textbook-section-card,.problem-card,.chapter-pagination,.stat-editorial-note,.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.getElementById('textbook-sections').innerHTML = '';
  (d.getElementById('problems-mount') || d.getElementById('problems-container') || d.getElementById('problem-cards-list')).innerHTML = '';
  d.querySelector('.sidebar').removeAttribute('id');

  const probSec = d.querySelector('.prob-sec-title');
  if (probSec) probSec.textContent = cfg.probSecTitle;

  // Replace script and css links
  for (const el of d.querySelectorAll('script[src],link[rel="stylesheet"]')) {
    const attr = el.tagName === 'SCRIPT' ? 'src' : 'href';
    const src = el.getAttribute(attr);
    if (src && src.includes('programming-fundamentals')) {
      el.setAttribute(attr, src.replace(/programming-fundamentals/g, cfg.slug));
    }
  }

  // Editorial note
  const note = d.createElement('aside');
  note.className = 'stat-editorial-note';
  note.setAttribute('aria-label', 'About this textbook');
  note.innerHTML = cfg.editorialNote;
  d.querySelector('.unit-hero').after(note);

  // References and trust footer
  const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
  const trustNav = '<nav class="reader-trust-links" aria-label="Related reading">' +
    '<a href="index#dept-computer-science">Computer Science Department</a>' +
    '<a href="programming-fundamentals">Programming Fundamentals</a>' +
    '<a href="data-structures">Data Structures</a>' +
    '<a href="algorithms">Algorithms</a>' +
    '<a href="discrete-structures-for-computer-science">Discrete Structures</a>' +
    '<a href="computer-architecture">Computer Architecture</a>' +
    '<a href="operating-systems">Operating Systems</a>' +
    '<a href="database-systems">Database Systems</a>' +
    '<a href="computer-networks">Computer Networks</a>' +
    '<a href="software-engineering">Software Engineering</a>' +
    '<a href="programming-languages-and-compilers">Programming Languages and Compilers</a>' +
    '<a href="discrete-mathematics">Discrete Mathematics prerequisite</a>' +
    '<a href="linear-algebra">Linear Algebra prerequisite</a>' +
    '<a href="calculus-1">Calculus prerequisite</a>' +
    '<a href="about">About & editorial</a>' +
    '<a href="privacy">Privacy</a>' +
    '<a href="terms">Terms</a>' +
    '<a href="mailto:shahriyarkarimsiam@gmail.com">Report a correction</a>' +
    '</nav>';
  const trustRefs = '<details><summary>Curriculum and academic references</summary><ul>' +
    refs.sources.map(s => `<li><a href="${s.url}" target="_blank" rel="noopener noreferrer">${s.institution}: ${s.role}</a></li>`).join('') +
    '</ul></details>';
  const trustCopy = '<p class="reader-trust-copy">© 2026 OpenSTEM Library • Free original educational textbook</p>';
  d.querySelector('.reader-trust-footer').innerHTML = trustNav + trustRefs + trustCopy;

  // Schema.org tags
  d.querySelectorAll('script[type="application/ld+json"]').forEach(el => el.remove());
  function addSchema(data) {
    const s = d.createElement('script');
    s.type = 'application/ld+json';
    s.textContent = JSON.stringify(data);
    d.head.append(s);
  }

  addSchema({
    '@context': 'https://schema.org',
    '@type': 'Book',
    name: cfg.title,
    description: cfg.description,
    url: 'https://openstemlibrary.com/' + cfg.slug,
    inLanguage: 'en',
    isAccessibleForFree: true,
    educationalLevel: 'Undergraduate',
    author: { '@type': 'Organization', name: 'OpenSTEM Library' },
    publisher: { '@type': 'Organization', name: 'OpenSTEM Library', url: 'https://openstemlibrary.com/' },
    learningResourceType: 'Textbook',
    about: cfg.keywords
  });

  addSchema({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'OpenSTEM Library', item: 'https://openstemlibrary.com/' },
      { '@type': 'ListItem', position: 2, name: 'Computer Science', item: 'https://openstemlibrary.com/#dept-computer-science' },
      { '@type': 'ListItem', position: 3, name: cfg.title, item: 'https://openstemlibrary.com/' + cfg.slug }
    ]
  });

  // Evaluate book data and startApp
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'computer-science', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'computer-science', cfg.slug);
  fs.mkdirSync(targetDir, { recursive: true });
  const targetHtmlPath = path.join(targetDir, cfg.slug + '.html');
  fs.writeFileSync(targetHtmlPath, dom.serialize(), 'utf8');
  w.close();
  console.log(`Generated landing page: ${targetHtmlPath}`);
}

// Update departments-data.js
const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root, 'departments-data.js'), 'utf8'), ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
const dept = catalog.departments.find(d => d.id === 'computer-science');

for (const cfg of bookConfigs) {
  dept.courses = dept.courses.filter(b => b.id !== cfg.slug);
  const dataJsText = fs.readFileSync(path.join(groupedRoot, 'computer-science', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  const courseData = JSON.parse(dataJsText.replace(/^[\s\S]*?window\.COURSE_DATA\s*=\s*/, '').replace(/;\s*$/, ''));
  dept.courses.push({
    id: cfg.slug,
    title: cfg.title,
    subtitle: cfg.subtitle,
    status: 'AVAILABLE',
    url: cfg.slug + '.html',
    badge: 'Free Interactive Textbook',
    description: cfg.description,
    topics: courseData.units.map(u => u.title)
  });
}

fs.writeFileSync(
  path.join(root, 'departments-data.js'),
  '// OpenSTEM academic catalog: only completed books appear as available.\nwindow.LIBRARY_CATALOG = ' + JSON.stringify(catalog, null, 2) + ';\n',
  'utf8'
);
console.log(`Updated departments-data.js. Total Computer Science courses: ${dept.courses.length}`);

// Update publishing/book-queue.json
const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
const queueDept = queue.departments.find(d => d.id === 'computer-science');
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  const qBook = queueDept.books.find(b => b.id === 'computer-science-' + cfg.slug);
  if (qBook) {
    qBook.status = 'published';
    qBook.published_at = now;
    qBook.content_file = cfg.slug + '-data.js';
    qBook.url = cfg.slug + '.html';
    qBook.qa_report = `publishing/qa/computer-science-${cfg.slug}.json`;
    console.log(`Updated book-queue.json: ${qBook.id} -> published`);
  }
}

fs.writeFileSync(
  path.join(root, 'publishing/book-queue.json'),
  JSON.stringify(queue, null, 2) + '\n',
  'utf8'
);
console.log('Updated publishing/book-queue.json successfully.');
