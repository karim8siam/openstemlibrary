const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'programming-fundamentals',
    title: 'Programming Fundamentals',
    subtitle: 'Problem Decomposition, Types, Control Flow, Functions, Scope, Testing & Numerical Practice',
    seoTitle: 'Programming Fundamentals: Decomposition, Types, Control Flow & Testing | OpenSTEM Library',
    badgeCredits: 'Programming fundamentals core',
    courseCodes: ['CS 101'],
    searchPlaceholder: 'Search problem decomposition, linear search, floating point precision, two\'s complement overflow, loop invariants, recursion, stack frames, hash tables, unit test boundaries, binary search, trapezoidal rule…',
    probSecTitle: 'Step-by-Step Programming Fundamentals Solutions',
    description: 'Comprehensive university textbook covering problem decomposition, numeric representation, control flow invariants, functions and scope, basic collections, exception handling, boundary unit testing, and numerical integration with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for introductory computer science and software construction. Eight units with exactly three solved questions per unit and 16 interactive numerical simulations illustrating problem decomposition, overflow boundaries, hash collisions, and test coverage. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Programming Fundamentals', 'Problem Decomposition', 'Control Flow Invariants', 'Two\'s Complement Representation', 'Modular Architecture', 'Unit Testing', 'Binary Search', 'Numerical Integration'],
    refPath: 'publishing/drafts/computer-science-programming-fundamentals/references.json'
  },
  {
    slug: 'data-structures',
    title: 'Data Structures',
    subtitle: 'Linear Collections, Binary Search Trees, Balanced Trees, Hash Tables, Heaps & Graph Traversals',
    seoTitle: 'Data Structures: Linear Collections, Binary Search Trees, Hash Tables & Heaps | OpenSTEM Library',
    badgeCredits: 'Data structures core',
    courseCodes: ['CS 102', 'CS 201'],
    searchPlaceholder: 'Search dynamic array growth, amortized doubling, linked lists, circular queue, BST height, separate chaining, linear probing, binary heaps, sift-up, BFS frontiers, connected components, trie prefixes, Fenwick tree…',
    probSecTitle: 'Step-by-Step Data Structures Solutions',
    description: 'Comprehensive university textbook covering dynamic arrays, singly and doubly linked lists, stacks, queues, circular buffers, binary search trees, separate chaining and open addressing hash tables, binary heaps, priority queues, breadth-first and depth-first search, Fenwick trees, and disjoint-set unions with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university data structures courses. Eight units with exactly three solved questions per unit and 16 interactive numerical simulations illustrating geometric array resizing, hash table probing, heap reorganization, and Fenwick tree queries. Numerical checks and an editorial review support this edition; it has not received independent academic peer review.',
    keywords: ['Data Structures', 'Dynamic Arrays', 'Linked Lists', 'Binary Search Trees', 'Hash Tables', 'Binary Heaps', 'Breadth-First Search', 'Fenwick Trees'],
    refPath: 'publishing/drafts/computer-science-data-structures/references.json'
  },
  {
    slug: 'algorithms',
    title: 'Algorithms',
    subtitle: 'Asymptotic Complexity, Divide-and-Conquer, Greedy Optimization, Dynamic Programming & Network Flow',
    seoTitle: 'Algorithms: Asymptotic Bounds, Divide-and-Conquer, Dynamic Programming & Graph Theory | OpenSTEM Library',
    badgeCredits: 'Algorithms core',
    courseCodes: ['CS 202', 'CS 301'],
    searchPlaceholder: 'Search big-O notation, master theorem, recurrence relations, mergesort, quicksort pivot degeneration, greedy interval scheduling, 0/1 knapsack dynamic program, Dijkstra shortest path, vertex cover approximation, Monte Carlo disk estimator…',
    probSecTitle: 'Step-by-Step Algorithms Solutions',
    description: 'Comprehensive university textbook covering asymptotic notation, recurrence relations, Master theorem, divide-and-conquer recurrences, greedy interval scheduling, dynamic programming memoization, shortest path algorithms (Dijkstra, Bellman-Ford), minimum spanning trees, NP-completeness, and approximation algorithms with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for undergraduate analysis and design of algorithms. Eight units with exactly three solved questions per unit and interactive simulations illustrating asymptotic comparisons, recursive branching, dynamic programming tables, and greedy exchange properties. Numerical checks and an editorial review support this edition.',
    keywords: ['Algorithms', 'Asymptotic Analysis', 'Divide-and-Conquer', 'Greedy Scheduling', 'Dynamic Programming', 'Dijkstra Algorithm', 'NP-Completeness', 'Approximation Algorithms'],
    refPath: 'publishing/drafts/computer-science-algorithms/references.json'
  },
  {
    slug: 'discrete-structures-for-computer-science',
    title: 'Discrete Structures for Computer Science',
    subtitle: 'Propositional Logic, Proof Systems, Set Theory, Combinatorics, Recurrences, Number Theory & Graph Theory',
    seoTitle: 'Discrete Structures for Computer Science: Logic, Proofs, Combinatorics & Graph Theory | OpenSTEM Library',
    badgeCredits: 'Discrete structures core',
    courseCodes: ['CS 103', 'Math 205'],
    searchPlaceholder: 'Search truth assignments, residue classes, binomial coefficients, coin toss probability, path trees, Fibonacci recurrence, modular inverse, parity DFA, formal proofs, induction, Pigeonhole principle, Euler totient…',
    probSecTitle: 'Step-by-Step Discrete Structures Solutions',
    description: 'Comprehensive university textbook covering propositional logic, predicate calculus, formal proof techniques, induction, set theory and relations, combinatorics, generating functions, modular arithmetic, RSA cryptography foundations, and finite automata with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university discrete mathematics and structures. Eight units with exactly three solved questions per unit and interactive simulations illustrating modular arithmetic, congruence classes, combinatorics, and automata state transitions. Numerical checks and an editorial review support this edition.',
    keywords: ['Discrete Mathematics', 'Propositional Logic', 'Formal Proofs', 'Combinatorics', 'Recurrence Relations', 'Modular Arithmetic', 'Graph Theory', 'Finite Automata'],
    refPath: 'publishing/drafts/computer-science-discrete-structures-for-computer-science/references.json'
  },
  {
    slug: 'computer-architecture',
    title: 'Computer Architecture',
    subtitle: 'Instruction Set Architecture, Digital Logic, Pipelining, Memory Hierarchy & Parallel Interconnects',
    seoTitle: 'Computer Architecture: Instruction Sets, Digital Logic, Pipelining & Cache Hierarchy | OpenSTEM Library',
    badgeCredits: 'Computer architecture core',
    courseCodes: ['CS 204', 'EE 204'],
    searchPlaceholder: 'Search CPU execution time, CPI, clock cycles, signed two\'s complement, 8-bit ALU carry out, five-stage pipeline speedup, branch hazards, direct-mapped cache hits, multi-level cache AMAT, page tables, TLB…',
    probSecTitle: 'Step-by-Step Computer Architecture Solutions',
    description: 'Comprehensive university textbook covering CPU performance metrics, digital logic gates, ALU design, arithmetic circuits, RISC instruction set architecture, 5-stage classic RISC pipeline, branch hazards, cache memory organizations, virtual memory, and multicore cache coherence with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university computer systems architecture and organization. Eight units with exactly three solved questions per unit and interactive simulations illustrating CPU performance equations, signed arithmetic overflow, ideal pipelining speedup, and cache hit latencies. Numerical checks and an editorial review support this edition.',
    keywords: ['Computer Architecture', 'Instruction Set Architecture', 'Digital Logic', 'ALU Design', 'Pipelining and Hazards', 'Cache Hierarchy', 'Virtual Memory', 'Multicore Coherence'],
    refPath: 'publishing/drafts/computer-science-computer-architecture/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'statistics-probability', 'statistical-simulation-and-monte-carlo-methods', 'statistical-simulation-and-monte-carlo-methods.html'),
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

  // Replace script and css links from old slug to this book's slug
  for (const el of d.querySelectorAll('script[src],link[rel="stylesheet"]')) {
    const attr = el.tagName === 'SCRIPT' ? 'src' : 'href';
    const src = el.getAttribute(attr);
    if (src && src.includes('statistical-simulation-and-monte-carlo-methods')) {
      el.setAttribute(attr, src.replace(/statistical-simulation-and-monte-carlo-methods/g, cfg.slug));
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
    '<a href="discrete-mathematics">Discrete Mathematics prerequisite</a>' +
    '<a href="linear-algebra">Linear Algebra prerequisite</a>' +
    '<a href="calculus-1">Calculus prerequisite</a>' +
    '<a href="probability-and-probability-distributions">Probability prerequisite</a>' +
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
let dept = catalog.departments.find(d => d.id === 'computer-science');
if (!dept) {
  dept = {
    id: 'computer-science',
    name: 'Computer Science',
    code: 'CS',
    icon: '💻',
    description: 'Foundational computing theory, algorithms, computer architecture, systems software, networks, artificial intelligence, and software engineering.',
    courses: []
  };
  catalog.departments.push(dept);
}

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
