const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'information-security',
    title: 'Information Security',
    subtitle: 'Symmetric & Asymmetric Cryptography, Key Exchange, Access Control Models, Memory Exploits & Threat Analysis',
    seoTitle: 'Information Security: Cryptography, Key Exchange, Access Control & Exploit Mitigation | OpenSTEM Library',
    badgeCredits: 'Information security core',
    courseCodes: ['CS 355', 'CS 455'],
    searchPlaceholder: 'Search symmetric ciphers AES Galois counter mode, RSA modular exponentiation, elliptic curve cryptography, SHA-256 collision resistance, HMAC authentication, Diffie-Hellman key exchange, Bell-LaPadula confidentiality, Biba integrity, RBAC role hierarchy, stack buffer overflow, ASLR, DEP/NX, return-oriented programming, TLS 1.3 handshake…',
    probSecTitle: 'Step-by-Step Information Security Solutions',
    description: 'Comprehensive university textbook covering classical and modern cryptography (AES, RSA, ECC), cryptographic hash functions, digital signatures, Diffie-Hellman key exchange, access control models (DAC, MAC, RBAC, Bell-LaPadula), memory safety vulnerabilities (buffer overflows, ROP chains), web security (XSS, CSRF, SQLi), network security, and security engineering with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university information security courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating cryptographic key entropy, nonce collisions, memory layout bounds, and access control matrices. Numerical checks and an editorial review support this edition.',
    keywords: ['Information Security', 'Cryptography', 'Public Key Infrastructure', 'Access Control Models', 'Memory Safety and Exploits', 'Return-Oriented Programming', 'Network Security', 'Security Engineering'],
    refPath: 'publishing/drafts/computer-science-information-security/references.json'
  },
  {
    slug: 'distributed-systems',
    title: 'Distributed Systems',
    subtitle: 'Logical Clocks, Consensus Protocols, Paxos, Raft, Fault Tolerance, Partitioning & Eventual Consistency',
    seoTitle: 'Distributed Systems: Logical Clocks, Paxos, Raft Consensus & Fault Tolerance | OpenSTEM Library',
    badgeCredits: 'Distributed systems core',
    courseCodes: ['CS 417', 'CS 451'],
    searchPlaceholder: 'Search RPC semantics, network partitions, Byzantine generals, Lamport logical clocks, vector clock concurrency, snapshot isolation, Paxos consensus invariants, Raft leader election, log replication, quorum consensus read/write quorums, CAP theorem trade-offs, two-phase commit 2PC, gossip protocols, distributed stream watermarks…',
    probSecTitle: 'Step-by-Step Distributed Systems Solutions',
    description: 'Comprehensive university textbook covering distributed system architectures, RPC semantics, Lamport logical clocks, vector clocks, distributed mutual exclusion, consensus algorithms (Paxos, Raft), quorum consensus, CAP theorem, PACELC, distributed transactions (Two-Phase Commit), replication models, partition handling, and stream processing with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university distributed systems courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating RPC timeouts, quorum intersections, Lamport clock ordering, Raft leader election, and replication lag. Numerical checks and an editorial review support this edition.',
    keywords: ['Distributed Systems', 'Logical Clocks and Causality', 'Paxos and Raft Consensus', 'Fault Tolerance', 'Quorum Systems', 'CAP Theorem', 'Replication and Consistency', 'Distributed Transactions'],
    refPath: 'publishing/drafts/computer-science-distributed-systems/references.json'
  },
  {
    slug: 'parallel-computing',
    title: 'Parallel Computing',
    subtitle: 'Shared-Memory Threads, Message Passing (MPI), GPU Architecture (CUDA), Amdahl\'s Law & Synchronization',
    seoTitle: 'Parallel Computing: Shared Memory, MPI, GPU CUDA Architecture & Amdahl\'s Law | OpenSTEM Library',
    badgeCredits: 'Parallel computing core',
    courseCodes: ['CS 420', 'CS 452'],
    searchPlaceholder: 'Search Flynn taxonomy, SMP vs NUMA, Amdahl law speedup, Gustafson law, Roofline operational intensity, MESI cache coherence, false sharing, OpenMP work-sharing pragmas, MPI point-to-point and collective communication, GPU streaming multiprocessors, CUDA warp divergence, shared memory bank conflicts, lock-free queues…',
    probSecTitle: 'Step-by-Step Parallel Computing Solutions',
    description: 'Comprehensive university textbook covering parallel hardware architectures (SMP, NUMA, clusters, GPUs), shared-memory multi-threading (OpenMP, pthreads), message passing interfaces (MPI), GPU compute programming (CUDA, OpenCL), scalability analysis (Amdahl\'s law, Gustafson\'s law, Roofline model), cache coherence protocols (MESI), and lock-free synchronization with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university parallel and high-performance computing courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating Roofline bandwidth bounds, Amdahl speedup curves, cache line false sharing, and thread scheduling efficiency. Numerical checks and an editorial review support this edition.',
    keywords: ['Parallel Computing', 'Amdahl and Gustafson Laws', 'Roofline Model', 'Shared-Memory Threading', 'Message Passing Interface (MPI)', 'GPU Architecture and CUDA', 'Cache Coherence Protocols', 'Lock-Free Synchronization'],
    refPath: 'publishing/drafts/computer-science-parallel-computing/references.json'
  },
  {
    slug: 'web-systems',
    title: 'Web Systems',
    subtitle: 'HTTP Protocols, Client-Server Architectures, REST APIs, Browser Internals, Caching & Scalability',
    seoTitle: 'Web Systems: HTTP Protocols, RESTful APIs, Browser Rendering & Distributed Web Architecture | OpenSTEM Library',
    badgeCredits: 'Web systems core',
    courseCodes: ['CS 330', 'CS 430'],
    searchPlaceholder: 'Search HTTP evolution, HTTP/2 stream multiplexing, HTTP/3 QUIC connection migration, REST architectural constraints, idempotency and safety, browser rendering pipeline, critical rendering path, DOM and CSSOM construction, CDN caching hierarchies, Cache-Control headers, CORS preflight, Content Security Policy, WebSockets…',
    probSecTitle: 'Step-by-Step Web Systems Solutions',
    description: 'Comprehensive university textbook covering the architectural evolution of the World Wide Web, HTTP/1.1, HTTP/2 multiplexing, HTTP/3 (QUIC), RESTful API design, browser rendering engines (DOM tree, CSSOM, layout, paint), client-side state management, CDN edge caching, web security (CORS, CSP, same-origin policy), and high-concurrency server architectures with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university web systems and internet computing courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating HTTP conditional requests, viewport responsive layout, cookie security flags, and pagination cursor models. Numerical checks and an editorial review support this edition.',
    keywords: ['Web Systems', 'HTTP/2 and HTTP/3 Protocols', 'RESTful API Architecture', 'Browser Rendering Engine', 'Critical Rendering Path', 'CDN and Edge Caching', 'Web Security Standards', 'High-Concurrency Servers'],
    refPath: 'publishing/drafts/computer-science-web-systems/references.json'
  },
  {
    slug: 'software-testing-and-verification',
    title: 'Software Testing and Verification',
    subtitle: 'Unit Testing, Mutation Analysis, Fuzzing, Symbolic Execution, Model Checking & Formal Verification',
    seoTitle: 'Software Testing and Verification: Coverage Criteria, Mutation Testing, Fuzzing & Model Checking | OpenSTEM Library',
    badgeCredits: 'Software testing and verification core',
    courseCodes: ['CS 440', 'CS 480'],
    searchPlaceholder: 'Search test coverage criteria, equivalence partitioning, boundary value analysis, modified condition/decision coverage MC/DC, mutation adequacy score, test flakiness mitigation, coverage-guided fuzzing, symbolic execution concolic testing, Hoare triples loop invariants, SAT and SMT solving, model checking LTL and CTL, Kripke structures…',
    probSecTitle: 'Step-by-Step Software Testing and Verification Solutions',
    description: 'Comprehensive university textbook covering test engineering fundamentals, black-box partition testing, white-box graph coverage (statement, branch, prime path, MC/DC), mutation analysis, regression testing, property-based testing, automated fuzzing (AFL, coverage-guided), symbolic execution, Hoare logic, SAT/SMT solvers, and model checking (LTL, CTL) with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university software testing, verification, and formal methods courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating requirement traceability, test flakiness probability, boundary value partitions, and mutation adequacy scores. Numerical checks and an editorial review support this edition.',
    keywords: ['Software Testing', 'Verification and Validation', 'Coverage Criteria and MC/DC', 'Mutation Testing', 'Fuzzing and Concolic Execution', 'Hoare Logic and Formal Invariants', 'SAT and SMT Solvers', 'Model Checking'],
    refPath: 'publishing/drafts/computer-science-software-testing-and-verification/references.json'
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

  const appCss = d.querySelector('link[href*="programming-fundamentals.css"]');
  if (appCss) appCss.href = `${cfg.slug}.css?v=20261024_academic`;

  const dataScript = d.querySelector('script[src*="programming-fundamentals-data.js"]');
  if (dataScript) dataScript.src = `${cfg.slug}-data.js`;

  const simsScript = d.querySelector('script[src*="programming-fundamentals-sims.js"]');
  if (simsScript) simsScript.src = `${cfg.slug}-sims.js`;

  const bookTitleEl = d.getElementById('book-title');
  if (bookTitleEl) bookTitleEl.textContent = cfg.title;

  const badgeEl = d.querySelector('.badge');
  if (badgeEl) badgeEl.textContent = 'Free Interactive Textbook';

  const creditsEl = d.querySelector('.credits');
  if (creditsEl) creditsEl.textContent = cfg.badgeCredits;

  const searchInput = d.getElementById('search-input');
  if (searchInput) searchInput.placeholder = cfg.searchPlaceholder;

  const probSec = d.getElementById('problems-sec-title');
  if (probSec) probSec.textContent = cfg.probSecTitle;

  const edNote = d.getElementById('editorial-note');
  if (edNote) edNote.innerHTML = cfg.editorialNote;

  const curLink = d.getElementById('curriculum-source-link');
  if (curLink) {
    curLink.href = 'https://openstemlibrary.com/curriculum/computer-science';
    curLink.textContent = 'OpenSTEM University Computer Science Curriculum Framework';
  }

  // Update Breadcrumb and Book schemas
  const schemas = d.querySelectorAll('script[type="application/ld+json"]');
  schemas.forEach(s => {
    try {
      const data = JSON.parse(s.textContent);
      if (data['@type'] === 'BreadcrumbList') {
        data.itemListElement = [
          {
            '@type': 'ListItem',
            'position': 1,
            'name': 'OpenSTEM Library',
            'item': 'https://openstemlibrary.com/'
          },
          {
            '@type': 'ListItem',
            'position': 2,
            'name': 'Computer Science',
            'item': 'https://openstemlibrary.com/#computer-science'
          },
          {
            '@type': 'ListItem',
            'position': 3,
            'name': cfg.title,
            'item': 'https://openstemlibrary.com/' + cfg.slug
          }
        ];
        s.textContent = JSON.stringify(data, null, 2);
      } else if (data['@type'] === 'Book' || (Array.isArray(data['@graph']) && data['@graph'].some(x => x['@type'] === 'Book'))) {
        const bookObj = data['@type'] === 'Book' ? data : data['@graph'].find(x => x['@type'] === 'Book');
        bookObj.name = cfg.title;
        bookObj.description = cfg.description;
        bookObj.url = 'https://openstemlibrary.com/' + cfg.slug;
        bookObj.keywords = cfg.keywords.join(', ');
        s.textContent = JSON.stringify(data, null, 2);
      }
    } catch (e) {}
  });

  // Inject Course schema
  const courseSchema = d.createElement('script');
  courseSchema.type = 'application/ld+json';
  courseSchema.textContent = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'Course',
    'name': cfg.title,
    'description': cfg.description,
    'provider': {
      '@type': 'EducationalOrganization',
      'name': 'OpenSTEM Library',
      'url': 'https://openstemlibrary.com'
    },
    'courseCode': cfg.courseCodes.join(', '),
    'educationalLevel': 'Undergraduate',
    'hasCourseInstance': {
      '@type': 'CourseInstance',
      'courseMode': 'online',
      'courseWorkload': 'PT80H'
    }
  }, null, 2);
  d.head.appendChild(courseSchema);

  // Update references in footer
  const refList = d.getElementById('reference-sources-list');
  if (refList) {
    refList.replaceChildren();
    const refData = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
    for (const src of refData.sources) {
      const li = d.createElement('li');
      li.className = 'reference-source-item';
      const a = d.createElement('a');
      a.className = 'reference-institution';
      a.href = src.url;
      a.textContent = src.institution;
      const span = d.createElement('span');
      span.className = 'reference-role';
      span.textContent = ' — ' + src.role;
      li.appendChild(a);
      li.appendChild(span);
      refList.appendChild(li);
    }
  }

  // Update prerequisite links
  const prereqEl = d.getElementById('prerequisite-courses-list');
  if (prereqEl) {
    prereqEl.replaceChildren();
    const prereqs = [
      { name: 'Programming Fundamentals', url: 'https://openstemlibrary.com/programming-fundamentals' },
      { name: 'Data Structures', url: 'https://openstemlibrary.com/data-structures' },
      { name: 'Algorithms', url: 'https://openstemlibrary.com/algorithms' },
      { name: 'Operating Systems', url: 'https://openstemlibrary.com/operating-systems' },
      { name: 'Computer Networks', url: 'https://openstemlibrary.com/computer-networks' }
    ];
    for (const p of prereqs) {
      const a = d.createElement('a');
      a.className = 'prerequisite-chip';
      a.href = p.url;
      a.textContent = p.name;
      prereqEl.appendChild(a);
    }
  }

  // Update syllabus units in syllabus section
  const syllabusList = d.getElementById('course-syllabus-list');
  if (syllabusList) {
    syllabusList.replaceChildren();
  }

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
