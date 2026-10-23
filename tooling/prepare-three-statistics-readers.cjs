const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const groupedFiles = new Map();
for (const dept of fs.readdirSync(groupedRoot, { withFileTypes: true })) {
  if (!dept.isDirectory()) continue;
  for (const book of fs.readdirSync(path.join(groupedRoot, dept.name), { withFileTypes: true })) {
    if (!book.isDirectory()) continue;
    const folder = path.join(groupedRoot, dept.name, book.name);
    for (const file of fs.readdirSync(folder, { withFileTypes: true })) {
      if (!file.isFile()) continue;
      groupedFiles.set(file.name, path.join(folder, file.name));
    }
  }
}

function sourcePath(file) {
  const rootFile = path.join(root, file);
  if (fs.existsSync(rootFile)) return rootFile;
  if (groupedFiles.has(file)) return groupedFiles.get(file);
  return rootFile;
}

const read = p => fs.readFileSync(sourcePath(p), 'utf8');

const bookConfigs = [
  {
    slug: 'epidemiological-statistics',
    title: 'Epidemiological Statistics',
    subtitle: 'Disease Frequency, Causal Inference, Bias, Confounding & Outbreak Modeling',
    seoTitle: 'Epidemiological Statistics: Disease Frequency, Causal Inference, Bias, Confounding & Outbreak Modeling | OpenSTEM Library',
    badgeCredits: 'Epidemiological statistics major',
    courseCodes: ['Stat H-304'],
    searchPlaceholder: 'Search incidence, prevalence, odds ratio, risk ratio, confounding, Mantel-Haenszel, DAGs, selection bias, ROC curve, SIR model…',
    probSecTitle: 'Step-by-Step Epidemiological Statistics Solutions',
    description: 'Comprehensive university textbook covering measures of disease frequency (incidence, prevalence), measures of association (risk ratio, odds ratio, rate ratio), confounding and effect modification, Mantel-Haenszel methods, study designs (cohort, case-control, cross-sectional), selection and information bias, causal inference and DAGs, diagnostic testing and ROC curves, and mathematical infectious disease modeling (SIR models, R_0, herd immunity) with 24 solved questions and 4 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material mapped to University of Dhaka Statistics B.S. Honours 2023–24, Stat H-304 (Epidemiological Statistics). Eight units and exactly three solved questions per unit. Interactive simulations illustrate epidemiological measures, confounding stratification, diagnostic ROC curves, and SIR transmission dynamics. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Epidemiology', 'Epidemiological statistics', 'Measures of disease frequency', 'Risk ratio and odds ratio', 'Confounding and effect modification', 'Mantel-Haenszel estimation', 'Study designs and case-control studies', 'Causal inference and directed acyclic graphs', 'Diagnostic testing and ROC curves', 'Mathematical epidemic modeling and SIR dynamics'],
    refPath: 'publishing/drafts/statistics-probability-epidemiological-statistics/references.json'
  },
  {
    slug: 'industrial-and-official-statistics',
    title: 'Industrial and Official Statistics',
    subtitle: 'Statistical Process Control, Process Capability, CUSUM/EWMA, Acceptance Sampling & National Statistical Systems',
    seoTitle: 'Industrial and Official Statistics: Statistical Process Control, Capability, Acceptance Sampling & Official Data Systems | OpenSTEM Library',
    badgeCredits: 'Industrial & official statistics major',
    courseCodes: ['Stat H-305'],
    searchPlaceholder: 'Search Shewhart charts, X-bar, R chart, process capability, Cpk, CUSUM, EWMA, acceptance sampling, OC curve, official statistics, census operations…',
    probSecTitle: 'Step-by-Step Industrial and Official Statistics Solutions',
    description: 'Comprehensive university textbook covering statistical process control (Shewhart X-bar, R, S, p, np, c, u charts), process capability analysis (Cp, Cpk, Cpm), advanced monitoring (CUSUM, EWMA), acceptance sampling plans (single, double, sequential, OC curves, AOQL, AQL), official statistical systems, national statistical architecture, census operations, administrative data registers, and statistical disclosure control with 24 solved questions and 4 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material mapped to University of Dhaka Statistics B.S. Honours 2023–24, Stat H-305 (Industrial and Official Statistics). Eight units and exactly three solved questions per unit. Interactive simulations illustrate Shewhart X-bar and R charts, process capability indices, CUSUM and EWMA tracking, and acceptance sampling OC curves. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Industrial Statistics', 'Official Statistics', 'Statistical Quality Control', 'Shewhart control charts', 'Process capability analysis and Cpk', 'CUSUM and EWMA charts', 'Acceptance sampling and OC curves', 'National statistical systems and BBS', 'Census methodology and demographic registers', 'Statistical disclosure control and data confidentiality'],
    refPath: 'publishing/drafts/statistics-probability-industrial-and-official-statistics/references.json'
  },
  {
    slug: 'actuarial-statistics-and-mathematical-demography',
    title: 'Actuarial Statistics and Mathematical Demography',
    subtitle: 'Financial Mathematics, Life Contingencies, Survival Models, Benefit Reserves & Mathematical Demography',
    seoTitle: 'Actuarial Statistics and Mathematical Demography: Financial Mathematics, Life Tables, Life Contingencies & Benefit Reserves | OpenSTEM Library',
    badgeCredits: 'Actuarial statistics & mathematical demography major',
    courseCodes: ['Stat H-306', 'Stat H-312'],
    searchPlaceholder: 'Search force of interest, annuities-certain, loan amortization, life table, Gompertz-Makeham, multi-state models, Lotka renewal, net level premiums, benefit reserves, Thiele equation, Panjer recursion…',
    probSecTitle: 'Step-by-Step Actuarial Statistics Solutions',
    description: 'Comprehensive university textbook covering interest theory, discount factors, annuities-certain, loan amortization schedules, survival models and life tables, Gompertz-Makeham parametric laws, multi-state models and Kolmogorov equations, mathematical demography (Lotka renewal, Leslie matrix, fertility and migration), life insurance benefit valuation, life annuities and equivalence principle, prospective policy benefit reserves (Thiele\'s equation, Hattendorff\'s theorem), and collective risk models with 24 solved questions and 4 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material mapped to University of Dhaka Statistics B.S. Honours 2023–24, Stat H-306 (Actuarial Statistics) and Stat H-312 (Actuarial Lab / Mathematical Demography). Eight units and exactly three solved questions per unit. Interactive simulations illustrate annuities-certain, life table survival curves, net level insurance premiums, and policy benefit reserves. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Actuarial Science', 'Actuarial Statistics', 'Mathematical Demography', 'Theory of interest and discount rates', 'Annuities certain and loan amortization', 'Survival models and life tables', 'Multi-state models and Markov contingencies', 'Lotka renewal equation and Leslie matrix', 'Life insurance and contingent claims valuation', 'Benefit reserves and Thiele differential equation', 'Collective risk models and ruin theory'],
    refPath: 'publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography/references.json'
  }
];

const templateHtml = read('introduction-to-statistics.html');

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

  // Replace script and css links from introduction-to-statistics to this book's slug
  for (const el of d.querySelectorAll('script[src],link[rel="stylesheet"]')) {
    const attr = el.tagName === 'SCRIPT' ? 'src' : 'href';
    const src = el.getAttribute(attr);
    if (src.includes('introduction-to-statistics')) {
      el.setAttribute(attr, src.replace(/introduction-to-statistics/g, cfg.slug));
    }
  }

  // Editorial note
  const note = d.createElement('aside');
  note.className = 'stat-editorial-note';
  note.setAttribute('aria-label', 'About this textbook');
  note.innerHTML = cfg.editorialNote;
  d.querySelector('.unit-hero').after(note);

  // References and trust footer
  const refs = JSON.parse(read(cfg.refPath));
  const trustNav = '<nav class="reader-trust-links" aria-label="Related reading">' +
    '<a href="index#dept-statistics-probability">Statistics department</a>' +
    '<a href="introduction-to-statistics">Introduction to Statistics</a>' +
    '<a href="probability-and-probability-distributions">Probability and Probability Distributions</a>' +
    '<a href="sample-surveys-and-sampling-theory">Sample Surveys and Sampling Theory</a>' +
    '<a href="statistical-computing-with-python-and-r">Statistical Computing</a>' +
    '<a href="mathematical-statistics">Mathematical Statistics</a>' +
    '<a href="statistical-estimation">Statistical Estimation</a>' +
    '<a href="demography-and-population-statistics">Demography and Population Statistics</a>' +
    '<a href="economic-statistics">Economic Statistics</a>' +
    '<a href="basic-algebra">Algebra prerequisite</a>' +
    '<a href="calculus-1">Calculus prerequisite</a>' +
    '<a href="about">About & editorial</a>' +
    '<a href="privacy">Privacy</a>' +
    '<a href="terms">Terms</a>' +
    '<a href="mailto:shahriyarkarimsiam@gmail.com">Report a correction</a>' +
    '</nav>';
  const trustRefs = '<details><summary>Curriculum and mathematical references</summary><ul>' +
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
      { '@type': 'ListItem', position: 2, name: 'Statistics & Probability', item: 'https://openstemlibrary.com/#dept-statistics-probability' },
      { '@type': 'ListItem', position: 3, name: cfg.title, item: 'https://openstemlibrary.com/' + cfg.slug }
    ]
  });

  // Evaluate book data and startApp
  w.eval(read(cfg.slug + '-data.js'));
  w.eval(read('app.js').split('\nif (document.readyState === "loading")')[0]);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary;
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'statistics-probability', cfg.slug);
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
const dept = catalog.departments.find(d => d.id === 'statistics-probability');

for (const cfg of bookConfigs) {
  dept.courses = dept.courses.filter(b => b.id !== cfg.slug);
  dept.courses.push({
    id: cfg.slug,
    title: cfg.title,
    subtitle: cfg.subtitle,
    status: 'AVAILABLE',
    url: cfg.slug + '.html',
    badge: 'Free Interactive Textbook',
    description: cfg.description,
    topics: JSON.parse(read(cfg.slug + '-data.js').replace(/^[\s\S]*?window\.COURSE_DATA\s*=\s*/, '').replace(/;\s*$/, '')).units.map(u => u.title)
  });
}

fs.writeFileSync(
  path.join(root, 'departments-data.js'),
  '// OpenSTEM academic catalog: only completed books appear as available.\nwindow.LIBRARY_CATALOG = ' + JSON.stringify(catalog, null, 2) + ';\n',
  'utf8'
);
console.log(`Updated departments-data.js. Total statistics courses: ${dept.courses.length}`);

// Update publishing/book-queue.json
const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
const queueDept = queue.departments.find(d => d.id === 'statistics-probability');
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  const qBook = queueDept.books.find(b => b.id === 'statistics-probability-' + cfg.slug);
  if (qBook) {
    qBook.status = 'published';
    qBook.published_at = now;
    qBook.content_file = cfg.slug + '-data.js';
    qBook.url = cfg.slug + '.html';
    qBook.qa_report = `publishing/qa/statistics-probability-${cfg.slug}.json`;
    console.log(`Updated book-queue.json: ${qBook.id} -> published`);
  }
}

fs.writeFileSync(
  path.join(root, 'publishing/book-queue.json'),
  JSON.stringify(queue, null, 2) + '\n',
  'utf8'
);
console.log('Updated publishing/book-queue.json successfully.');
