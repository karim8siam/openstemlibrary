const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'formal-logic',
    title: 'Formal Logic',
    subtitle: 'Propositional Calculus, Truth Tables, Natural Deduction, Semantics & First-Order Languages',
    seoTitle: 'Formal Logic: Propositional Calculus, Truth Tables & Natural Deduction | OpenSTEM Library',
    badgeCredits: 'Formal logic core',
    courseCodes: ['LSS 201', 'PHI 201', 'MTH 201'],
    searchPlaceholder: 'Search propositional calculus, truth tables, modus ponens, natural deduction rules, semantic tableaux, first-order quantifiers, Kleene 3-valued logic, modal Kripke frames, conjunctive normal form (CNF), automated SAT…',
    probSecTitle: 'Step-by-Step Formal Logic Solutions',
    description: 'Comprehensive university textbook covering propositional logic, truth tables, semantic tableaux, natural deduction, first-order languages, validity, soundness, and completeness with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university formal logic and deductive systems courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating propositional truth tables, validity tests, proof trees, semantic tableaux, quantifier scopes, Kleene tables, and modal accessibility frames. Numerical checks and an editorial review support this edition.',
    keywords: ['Formal Logic', 'Propositional Calculus', 'Truth Tables', 'Natural Deduction', 'Semantic Tableaux', 'Quantifiers', 'Modal Logic', 'SAT Solving'],
    refPath: 'publishing/drafts/logic-and-systems-science-formal-logic/references.json'
  },
  {
    slug: 'model-theory-and-mathematical-semantics',
    title: 'Model Theory and Mathematical Semantics',
    subtitle: 'Structures, Satisfaction, Homomorphisms, Elementary Equivalence, Compactness & Ultraproducts',
    seoTitle: 'Model Theory & Mathematical Semantics: Structures, Satisfaction & Compactness | OpenSTEM Library',
    badgeCredits: 'Model theory core',
    courseCodes: ['LSS 301', 'MTH 301', 'CS 301'],
    searchPlaceholder: 'Search first-order structures, Tarskian satisfaction, homomorphisms and embeddings, substructure closure, automorphism orbits, quantifier rank, elementary equivalence, Ehrenfeucht-Fraïssé games, compactness theorem, partial types…',
    probSecTitle: 'Step-by-Step Model Theory Solutions',
    description: 'Comprehensive university textbook covering mathematical semantics, first-order structures, Tarskian satisfaction, homomorphisms, elementary equivalence, compactness, type omission, and Ehrenfeucht-Fraïssé games with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university model theory and mathematical semantics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating finite structure satisfaction, term evaluations, relation transport, substructure closures, automorphism orbits, compactness prefixes, and Ehrenfeucht-Fraïssé game rounds. Numerical checks and an editorial review support this edition.',
    keywords: ['Model Theory', 'Mathematical Semantics', 'Structures', 'Satisfaction', 'Homomorphisms', 'Elementary Equivalence', 'Compactness Theorem', 'Ehrenfeucht-Fraïssé Games'],
    refPath: 'publishing/drafts/logic-and-systems-science-model-theory-and-mathematical-semantics/references.json'
  },
  {
    slug: 'proof-theory-and-deductive-systems',
    title: 'Proof Theory and Deductive Systems',
    subtitle: 'Natural Deduction, Sequent Calculus, Cut Elimination, Normalization & Curry-Howard Isomorphism',
    seoTitle: 'Proof Theory & Deductive Systems: Sequent Calculus, Cut Elimination & Normalization | OpenSTEM Library',
    badgeCredits: 'Proof theory core',
    courseCodes: ['LSS 305', 'MTH 305', 'CS 305'],
    searchPlaceholder: 'Search natural deduction trees, Gentzen sequent calculus LK/LJ, cut elimination theorem, proof normalization, subformula property, detour elimination, lambda calculus beta-reduction, Curry-Howard correspondence, resolution refutation, Kripke semantics…',
    probSecTitle: 'Step-by-Step Proof Theory Solutions',
    description: 'Comprehensive university textbook covering deductive systems, Gentzen sequent calculi, natural deduction, cut elimination, normalization theorems, structural proof theory, and the Curry-Howard isomorphism with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university proof theory courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating sequent derivations, natural deduction rule certificates, detour contractions, lambda reductions, resolution refutations, and type checking derivations. Numerical checks and an editorial review support this edition.',
    keywords: ['Proof Theory', 'Deductive Systems', 'Sequent Calculus', 'Cut Elimination', 'Normalization', 'Curry-Howard Isomorphism', 'Natural Deduction', 'Resolution'],
    refPath: 'publishing/drafts/logic-and-systems-science-proof-theory-and-deductive-systems/references.json'
  },
  {
    slug: 'set-theory-and-foundations',
    title: 'Set Theory and Foundations',
    subtitle: 'Zermelo-Fraenkel Axioms, Relations, Functions, Ordinals, Cardinals, Transfinite Induction & Choice',
    seoTitle: 'Set Theory and Foundations: ZFC Axioms, Ordinals, Cardinals & Transfinite Induction | OpenSTEM Library',
    badgeCredits: 'Set theory core',
    courseCodes: ['LSS 210', 'MTH 210', 'PHI 210'],
    searchPlaceholder: 'Search Zermelo-Fraenkel axioms (ZFC), extensionality, axiom of pairing, comprehension and separation, ordinals, von Neumann hierarchy, transfinite induction, cardinal arithmetic, Cantor diagonal argument, Schröder-Bernstein theorem, Axiom of Choice…',
    probSecTitle: 'Step-by-Step Set Theory Solutions',
    description: 'Comprehensive university textbook covering axiomatic set theory (ZFC), relations, orderings, von Neumann ordinals, transfinite induction, cardinalities, Cantor\'s theorem, and the Axiom of Choice with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university set theory and foundations courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating membership vs subset inclusion, set algebra, relation equivalence classes, injectivity/surjectivity, Cantor diagonal cuts, ordinal ranks, and separation filters. Numerical checks and an editorial review support this edition.',
    keywords: ['Set Theory', 'ZFC Axioms', 'Ordinals', 'Cardinals', 'Transfinite Induction', 'Axiom of Choice', 'Cantor Theorem', 'Mathematical Foundations'],
    refPath: 'publishing/drafts/logic-and-systems-science-set-theory-and-foundations/references.json'
  },
  {
    slug: 'symbolic-and-predicate-logic',
    title: 'Symbolic and Predicate Logic',
    subtitle: 'First-Order Languages, Quantifiers, Variable Binding, Semantic Domains, Prenex Normal Form & Skolemization',
    seoTitle: 'Symbolic & Predicate Logic: Quantifiers, Free Variables & Prenex Normal Form | OpenSTEM Library',
    badgeCredits: 'Predicate logic core',
    courseCodes: ['LSS 205', 'PHI 205', 'CS 205'],
    searchPlaceholder: 'Search first-order syntax, variable binding, quantifier scope, capture-avoiding substitution, free vs bound variables, relational domains, prenex normal form, Skolemization, first-order resolution, Datalog semantics, policy compliance…',
    probSecTitle: 'Step-by-Step Symbolic & Predicate Logic Solutions',
    description: 'Comprehensive university textbook covering first-order predicate logic, quantifier scope, variable capture, semantic valuation, prenex normal forms, Skolem functions, first-order resolution, and Datalog with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university predicate logic courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating quantifier scope shifts, capture-avoiding substitutions, restricted quantification, relation dependency tests, prenex transformations, and resolution derivations. Numerical checks and an editorial review support this edition.',
    keywords: ['Symbolic Logic', 'Predicate Logic', 'First-Order Logic', 'Quantifiers', 'Variable Binding', 'Prenex Normal Form', 'Skolemization', 'Resolution'],
    refPath: 'publishing/drafts/logic-and-systems-science-symbolic-and-predicate-logic/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'materials-science-and-engineering', 'fundamentals-of-materials-science', 'fundamentals-of-materials-science.html'),
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

  d.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (href.startsWith('../../') || href.startsWith('../'))) {
      link.setAttribute('href', href.replace(/^\.\.\/\.\.\//, '').replace(/^\.\.\//, ''));
    }
  });

  let bookCss = d.querySelector(`link[href="${cfg.slug}.css"]`);
  if (!bookCss) {
    bookCss = d.createElement('link');
    bookCss.rel = 'stylesheet';
    bookCss.href = `${cfg.slug}.css`;
    d.head.appendChild(bookCss);
  }

  const courseBadge = d.querySelector('.course-badge');
  if (courseBadge) courseBadge.textContent = 'Free Interactive Textbook';

  const titleEl = d.querySelector('h1#course-title') || d.querySelector('h1');
  if (titleEl) titleEl.textContent = cfg.title;

  const subtitleEl = d.querySelector('#course-subtitle') || d.querySelector('.course-subtitle');
  if (subtitleEl) subtitleEl.textContent = cfg.subtitle;

  const searchInput = d.querySelector('#problem-search');
  if (searchInput) searchInput.placeholder = cfg.searchPlaceholder;

  const probSec = d.querySelector('#worked-problems-section h2');
  if (probSec) probSec.textContent = cfg.probSecTitle;

  const editorialBox = d.querySelector('.editorial-review-box');
  if (editorialBox) {
    editorialBox.innerHTML = `
      <div class="editorial-review-badge">Peer Review & Editorial Standards</div>
      <p>${cfg.editorialNote}</p>
      <div class="editorial-signoff">OpenSTEM Editorial Board • Logic & Systems Science Division</div>
    `;
  }

  const refBlock = d.querySelector('.references-block');
  if (refBlock && fs.existsSync(path.join(root, cfg.refPath))) {
    const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
    const refItems = refs.sources.map(s => `<li><strong>${s.institution}</strong>: ${s.role}</li>`).join('\n');
    refBlock.innerHTML = `
      <h3>Authoritative Academic Benchmarks & Citations</h3>
      <p>This textbook synthesizes canonical university curricula and established formal logic references:</p>
      <ul>
        ${refItems}
      </ul>
    `;
  }

  const scripts = d.querySelectorAll('script');
  scripts.forEach(s => {
    const src = s.getAttribute('src');
    if (src) {
      if (src.includes('-data.js')) s.setAttribute('src', `${cfg.slug}-data.js`);
      if (src.includes('-sims.js')) s.setAttribute('src', `${cfg.slug}-sims.js`);
      if (src.startsWith('../../') || src.startsWith('../')) {
        s.setAttribute('src', src.replace(/^\.\.\/\.\.\//, '').replace(/^\.\.\//, ''));
      }
    }
  });

  const structuredDataScript = d.querySelector('script[type="application/ld+json"]');
  if (structuredDataScript) {
    try {
      const sd = JSON.parse(structuredDataScript.textContent);
      if (sd['@type'] === 'Course' || sd['@type'] === 'Book') {
        sd.name = cfg.title;
        sd.description = cfg.description;
        sd.url = 'https://openstemlibrary.com/' + cfg.slug;
        sd.keywords = cfg.keywords.join(', ');
      }
      structuredDataScript.textContent = JSON.stringify(sd, null, 2);
    } catch (e) {}
  }

  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'logic-and-systems-science', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'logic-and-systems-science', cfg.slug);
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
let dept = catalog.departments.find(d => d.id === 'logic-and-systems-science');
if (!dept) {
  dept = {
    id: 'logic-and-systems-science',
    name: 'Logic & Systems Science',
    code: 'LSS',
    icon: '📐',
    description: 'Formal logic, model theory, proof theory, set theory and mathematical foundations, and symbolic predicate calculus.',
    courses: []
  };
  catalog.departments.push(dept);
}

for (const cfg of bookConfigs) {
  dept.courses = dept.courses.filter(b => b.id !== cfg.slug);
  const dataJsText = fs.readFileSync(path.join(groupedRoot, 'logic-and-systems-science', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
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
console.log(`Updated departments-data.js. Total Logic & Systems Science courses: ${dept.courses.length}`);

// Update publishing/book-queue.json
const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
let queueDept = queue.departments.find(d => d.id === 'logic-systems-science' || d.id === 'logic-and-systems-science');
if (!queueDept) {
  queueDept = {
    id: 'logic-and-systems-science',
    name: 'Logic & Systems Science',
    books: []
  };
  queue.departments.push(queueDept);
}
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  // Find matching book in queue by slug or title
  let qBook = queueDept.books.find(b => 
    b.id === 'logic-systems-science-' + cfg.slug || 
    b.id === 'logic-and-systems-science-' + cfg.slug ||
    b.title.toLowerCase() === cfg.title.toLowerCase() ||
    (cfg.slug.includes('model-theory') && b.id.includes('model-theory')) ||
    (cfg.slug.includes('proof-theory') && b.id.includes('proof-theory'))
  );
  if (!qBook) {
    qBook = {
      id: 'logic-and-systems-science-' + cfg.slug,
      title: cfg.title,
      status: 'published',
      published_at: now,
      content_file: cfg.slug + '-data.js',
      url: cfg.slug + '.html',
      qa_report: `publishing/qa/logic-and-systems-science-${cfg.slug}.json`
    };
    queueDept.books.push(qBook);
  } else {
    qBook.id = 'logic-and-systems-science-' + cfg.slug;
    qBook.status = 'published';
    qBook.published_at = now;
    qBook.content_file = cfg.slug + '-data.js';
    qBook.url = cfg.slug + '.html';
    qBook.qa_report = `publishing/qa/logic-and-systems-science-${cfg.slug}.json`;
  }
  console.log(`Updated book-queue.json: ${qBook.id} -> published`);
}

fs.writeFileSync(
  path.join(root, 'publishing/book-queue.json'),
  JSON.stringify(queue, null, 2) + '\n',
  'utf8'
);
console.log('Updated publishing/book-queue.json successfully.');
