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
    slug: 'statistical-simulation-and-monte-carlo-methods',
    title: 'Statistical Simulation and Monte Carlo Methods',
    subtitle: 'Pseudorandom Generation, Non-Uniform Sampling, Importance Sampling, MCMC & Particle Filtering',
    seoTitle: 'Statistical Simulation and Monte Carlo Methods: Pseudorandom Numbers, Rejection, MCMC & Particle Filtering | OpenSTEM Library',
    badgeCredits: 'Statistical simulation & Monte Carlo methods major',
    courseCodes: ['Stat H-307'],
    searchPlaceholder: 'Search PRNG, LCG, Mersenne Twister, inversion method, rejection sampling, Box-Muller, Monte Carlo integration, importance sampling, antithetic variates, Metropolis-Hastings, Gibbs sampler, Hamiltonian Monte Carlo, particle filter…',
    probSecTitle: 'Step-by-Step Statistical Simulation and Monte Carlo Solutions',
    description: 'Comprehensive university textbook covering pseudorandom number generators (LCG, Mersenne Twister, statistical test suites), non-uniform random variate generation (inversion, rejection sampling, Box-Muller, multivariate normal), Monte Carlo integration, variance reduction techniques (antithetic variates, control variates, importance sampling, stratified sampling), Markov Chain Monte Carlo foundations, the Metropolis-Hastings algorithm, Gibbs sampling, slice sampling, Hamiltonian Monte Carlo, convergence diagnostics (Gelman-Rubin R-hat, ESS), and Sequential Monte Carlo (particle filtering) with 24 solved questions and 4 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material mapped to University of Dhaka Statistics B.S. Honours 2023–24, Stat H-307 (Statistical Simulation and Monte Carlo Methods). Eight units and exactly three solved questions per unit. Interactive simulations illustrate linear congruential generators, rejection sampling envelopes, rare-event importance sampling, and Metropolis-Hastings random walks. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Statistical Simulation', 'Monte Carlo Methods', 'Pseudorandom Number Generators', 'Rejection Sampling and Inversion', 'Importance Sampling and Variance Reduction', 'Markov Chain Monte Carlo and Metropolis-Hastings', 'Gibbs Sampling and Hierarchical Bayes', 'Hamiltonian Monte Carlo and NUTS', 'Sequential Monte Carlo and Particle Filtering'],
    refPath: 'publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods/references.json'
  },
  {
    slug: 'big-data-methods-for-statistics',
    title: 'Big Data Methods for Statistics',
    subtitle: 'High-Dimensional Geometry, Spectral Learning, Regularization, Distributed Spark & Streaming Algorithms',
    seoTitle: 'Big Data Methods for Statistics: High-Dimensional Geometry, Lasso, Spark & Streaming Algorithms | OpenSTEM Library',
    badgeCredits: 'Big data methods for statistics major',
    courseCodes: ['Stat H-308'],
    searchPlaceholder: 'Search curse of dimensionality, Marchenko-Pastur, randomized SVD, Lasso, coordinate descent, Elastic Net, MapReduce, Spark RDD, stochastic gradient descent, Adam optimizer, Johnson-Lindenstrauss, Count-Min sketch, HyperLogLog, False Discovery Rate…',
    probSecTitle: 'Step-by-Step Big Data Methods for Statistics Solutions',
    description: 'Comprehensive university textbook covering high-dimensional statistical geometry (curse of dimensionality, volume collapse, concentration of measure, distance concentration), large-scale spectral dimension reduction (random matrix theory, Marchenko-Pastur law, BBP transition, randomized SVD), sparse statistical learning (Lasso coordinate descent, Ridge, Elastic Net, SCAD/MCP), distributed computing foundations (MapReduce, Hadoop, Apache Spark RDDs, MLlib), first-order stochastic optimization (SGD, mini-batch, Polyak momentum, Adam), randomized numerical linear algebra (Johnson-Lindenstrauss lemma, SRHT, leverage score sampling), streaming data algorithms (Welford algorithm, Reservoir Sampling, Count-Min sketch, HyperLogLog), and high-dimensional multiple testing (FWER, Benjamini-Hochberg FDR control, Storey q-values, local FDR) with 24 solved questions and 4 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material mapped to University of Dhaka Statistics B.S. Honours 2023–24, Stat H-308 (Big Data Methods for Statistics). Eight units and exactly three solved questions per unit. Interactive simulations illustrate high-dimensional distance concentration, Lasso regularization paths, stochastic optimization trajectories, and Benjamini-Hochberg FDR thresholding. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Big Data Statistics', 'Curse of Dimensionality', 'Random Matrix Theory and Marchenko-Pastur', 'Lasso and Regularized Regression', 'Distributed Computing and Apache Spark', 'Stochastic Gradient Descent and Adam', 'Randomized Numerical Linear Algebra and Sketching', 'Streaming Data Algorithms and HyperLogLog', 'False Discovery Rate and Multiple Testing'],
    refPath: 'publishing/drafts/statistics-probability-big-data-methods-for-statistics/references.json'
  },
  {
    slug: 'statistical-research-methods',
    title: 'Statistical Research Methods',
    subtitle: 'Epistemology, Research Design, Psychometrics, Survey Sampling, Power Analysis, Causal Inference & Reproducibility',
    seoTitle: 'Statistical Research Methods: Epistemology, Design, Psychometrics, Power Analysis & Causal Inference | OpenSTEM Library',
    badgeCredits: 'Statistical research methods major',
    courseCodes: ['Stat H-309', 'Stat H-413'],
    searchPlaceholder: 'Search epistemology, falsificationism, internal validity, regression to the mean, Classical Test Theory, Cronbach\'s alpha, McDonald\'s omega, Item Response Theory, Total Survey Error, nonresponse bias, statistical power, Cohen\'s d, causal DAGs, instrumental variables, RDD, Difference-in-Differences, publication bias, reproducible research…',
    probSecTitle: 'Step-by-Step Statistical Research Methods Solutions',
    description: 'Comprehensive university textbook covering epistemology of statistical inquiry (positivism, Popperian falsificationism, Kuhn, Lakatos, Box\'s maxim), research design architectures (Campbell-Stanley taxonomy, internal and external validity threats, regression to the mean, Heckman selection models), measurement theory and psychometrics (Stevens scales, Classical Test Theory, Cronbach\'s alpha, McDonald\'s omega, MTMM matrix, Item Response Theory), survey design and sampling strategies (Total Survey Error, Tourangeau cognitive model, nonresponse weighting, Kish design effect, Warner randomized response), statistical power analysis (non-central distributions, Cohen\'s d, Hedges\' g, sample size formulas, post-hoc power fallacy), modern causal inference (Neyman-Rubin potential outcomes, Judea Pearl\'s DAGs, d-separation, backdoor criterion, instrumental variables, RDD, Difference-in-Differences), research ethics and privacy (Belmont Report, differential privacy, publication bias, Egger\'s test), and reproducible scientific communication with 24 solved questions and 4 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material mapped to University of Dhaka Statistics B.S. Honours 2023–24, Stat H-309 (Research Methodology) and Stat H-413 (Research Project). Eight units and exactly three solved questions per unit. Interactive simulations illustrate statistical power curves, causal DAG backdoor adjustment, Difference-in-Differences trajectories, and publication bias funnel plots. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Research Methodology', 'Epistemology of Statistics', 'Experimental Design and Threats to Validity', 'Measurement Theory and Psychometrics', 'Survey Sampling and Total Survey Error', 'Statistical Power Analysis and Sample Size', 'Causal Inference and Directed Acyclic Graphs', 'Instrumental Variables and Difference-in-Differences', 'Research Ethics and Differential Privacy', 'Reproducible Research and Open Science'],
    refPath: 'publishing/drafts/statistics-probability-statistical-research-methods/references.json'
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
    '<a href="epidemiological-statistics">Epidemiological Statistics</a>' +
    '<a href="industrial-and-official-statistics">Industrial and Official Statistics</a>' +
    '<a href="actuarial-statistics-and-mathematical-demography">Actuarial Statistics</a>' +
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
