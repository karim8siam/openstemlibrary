const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'plant-biology',
    title: 'Plant Biology',
    subtitle: 'Plant Architecture, Photosynthesis, Water Transport, Mineral Nutrition, Growth & Development',
    seoTitle: 'Plant Biology: Structure, Photosynthesis, Water Transport & Physiology | OpenSTEM Library',
    badgeCredits: 'Plant biology core',
    courseCodes: ['BIO 210', 'PLB 201'],
    searchPlaceholder: 'Search plant-cell architecture, meristems, xylem and phloem, water potential, C3 vs C4 photosynthesis, stomatal aperture, Rubisco carboxylation, phototropism, auxin gradients, phytochrome signaling…',
    probSecTitle: 'Step-by-Step Plant Biology Solutions',
    description: 'Comprehensive university textbook covering plant cell architecture, meristems and tissue differentiation, xylem and phloem transport, water potential mechanics, C3/C4/CAM photosynthesis, mineral nutrition, plant hormones (auxin, cytokinin, gibberellin), photomorphogenesis, and reproductive development with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university plant biology courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating osmotic turgor, meristem cell division, stomatal conductance, light saturation curves, and xylem water potential. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Plant Biology', 'Plant Anatomy', 'Water Potential', 'Xylem and Phloem', 'Photosynthesis', 'Plant Hormones', 'Photomorphogenesis', 'Plant Reproduction'],
    refPath: 'publishing/drafts/biological-sciences-plant-biology/references.json'
  },
  {
    slug: 'animal-biology',
    title: 'Animal Biology',
    subtitle: 'Animal Diversity, Body Plans, Phylogenetics, Invertebrates, Vertebrates & Comparative Anatomy',
    seoTitle: 'Animal Biology: Diversity, Body Plans, Phylogenetics & Comparative Anatomy | OpenSTEM Library',
    badgeCredits: 'Animal biology core',
    courseCodes: ['BIO 220', 'ZOOL 201'],
    searchPlaceholder: 'Search animal origins, phylogenetic tree inference, radial vs bilateral symmetry, coelom development, protostomes vs deuterostomes, cnidaria, arthropod segmentation, chordate characteristics, vertebrate skull evolution…',
    probSecTitle: 'Step-by-Step Animal Biology Solutions',
    description: 'Comprehensive university textbook covering animal origins, symmetry and tissue layers, phylogenetic reconstruction, major invertebrate phyla (Porifera, Cnidaria, Platyhelminthes, Annelida, Mollusca, Arthropoda, Echinodermata), chordate evolution, vertebrate comparative anatomy, and physiological adaptations with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university animal biology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating character state parsimony, population occupancy, metabolic scaling, and allometric limb ratios. Numerical checks and an editorial review support this edition.',
    keywords: ['Animal Biology', 'Zoology', 'Body Plans and Symmetry', 'Invertebrate Phyla', 'Chordates and Vertebrates', 'Comparative Anatomy', 'Phylogenetic Systematics', 'Metabolic Scaling'],
    refPath: 'publishing/drafts/biological-sciences-animal-biology/references.json'
  },
  {
    slug: 'evolutionary-biology',
    title: 'Evolutionary Biology',
    subtitle: 'Natural Selection, Speciation, Phylogenetics, Coevolution, Molecular Evolution & Macroevolution',
    seoTitle: 'Evolutionary Biology: Natural Selection, Speciation, Phylogenetics & Macroevolution | OpenSTEM Library',
    badgeCredits: 'Evolutionary biology core',
    courseCodes: ['BIO 301', 'EVO 301'],
    searchPlaceholder: 'Search fossil horizon duration, homologous character sampling, pairwise DNA mismatch, island survey vicariance, natural selection fitness differentials, genetic drift in small populations, allopatric speciation, phylogenetic reconstruction…',
    probSecTitle: 'Step-by-Step Evolutionary Biology Solutions',
    description: 'Comprehensive university textbook covering historical evidence for evolution, mechanisms of natural and sexual selection, genetic variation and drift, phylogenetic tree inference, speciation models (allopatric, sympatric), molecular evolution and molecular clocks, coevolution, evolutionary developmental biology (evo-devo), and macroevolutionary trends with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university evolutionary biology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating fossil preservation probabilities, pairwise sequence mismatch, selection coefficients, genetic drift decay, and allopatric reproductive isolation. Numerical checks and an editorial review support this edition.',
    keywords: ['Evolutionary Biology', 'Natural Selection', 'Genetic Drift', 'Phylogenetic Inference', 'Speciation', 'Molecular Clocks', 'Coevolution', 'Macroevolution'],
    refPath: 'publishing/drafts/biological-sciences-evolutionary-biology/references.json'
  },
  {
    slug: 'ecology',
    title: 'Ecology',
    subtitle: 'Population Dynamics, Community Structure, Trophic Interactions, Ecosystem Energetics & Biomes',
    seoTitle: 'Ecology: Population Dynamics, Community Interactions, Biomes & Ecosystem Energetics | OpenSTEM Library',
    badgeCredits: 'Ecology core',
    courseCodes: ['BIO 305', 'ECOL 301'],
    searchPlaceholder: 'Search sampling frame and density, thermal gradient magnitude, fundamental vs realized niche, terrestrial biomes, logistic population growth, Lotka-Volterra competition, predator-prey cycles, trophic efficiency, nutrient cycling…',
    probSecTitle: 'Step-by-Step Ecology Solutions',
    description: 'Comprehensive university textbook covering environmental gradients and biomes, behavioral ecology and foraging, population growth models (exponential and logistic), life history strategies, interspecific competition (Lotka-Volterra), predation and herbivory, community succession, trophic cascades and food webs, and biogeochemical cycles with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university ecology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating logistic growth equilibria, carrying capacity perturbations, thermal performance curves, predator-prey phase spaces, and biogeochemical residence times. Numerical checks and an editorial review support this edition.',
    keywords: ['Ecology', 'Population Dynamics', 'Logistic Growth', 'Lotka-Volterra Competition', 'Predator-Prey Cycles', 'Community Ecology', 'Trophic Cascades', 'Biogeochemical Cycles'],
    refPath: 'publishing/drafts/biological-sciences-ecology/references.json'
  },
  {
    slug: 'developmental-biology',
    title: 'Developmental Biology',
    subtitle: 'Embryogenesis, Morphogen Gradients, Pattern Formation, Cell Fate Specification & Organogenesis',
    seoTitle: 'Developmental Biology: Embryogenesis, Morphogen Gradients & Organogenesis | OpenSTEM Library',
    badgeCredits: 'Developmental biology core',
    courseCodes: ['BIO 310', 'DEV 301'],
    searchPlaceholder: 'Search potency and competence, reciprocal induction, morphogen threshold response, cleavage patterns, gastrulation cell movements, neural crest migration, limb bud patterning, Hox gene colinearity, stem cell differentiation…',
    probSecTitle: 'Step-by-Step Developmental Biology Solutions',
    description: 'Comprehensive university textbook covering developmental mechanisms and cell fate, fertilization and cleavage, gastrulation and primary germ layers, neurulation and neural crest specification, morphogen gradient French Flag models, axis specification, limb bud development, organogenesis, and stem cell biology with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university developmental biology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating sigmoidal cell fate response thresholds, cellular memory hysteresis, morphogen exponential decay, and somite boundary segmentation. Numerical checks and an editorial review support this edition.',
    keywords: ['Developmental Biology', 'Embryogenesis', 'Cell Fate Specification', 'Morphogen Gradients', 'Gastrulation', 'Neural Crest', 'Pattern Formation', 'Organogenesis'],
    refPath: 'publishing/drafts/biological-sciences-developmental-biology/references.json'
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
    '<a href="index#dept-biological-sciences">Biological Sciences Department</a>' +
    '<a href="cell-biology">Cell Biology</a>' +
    '<a href="molecular-biology">Molecular Biology</a>' +
    '<a href="genetics">Genetics</a>' +
    '<a href="biochemistry-for-biology">Biochemistry for Biology</a>' +
    '<a href="microbiology">Microbiology</a>' +
    '<a href="plant-biology">Plant Biology</a>' +
    '<a href="animal-biology">Animal Biology</a>' +
    '<a href="evolutionary-biology">Evolutionary Biology</a>' +
    '<a href="ecology">Ecology</a>' +
    '<a href="developmental-biology">Developmental Biology</a>' +
    '<a href="physical-chemistry-1">Physical Chemistry prerequisite</a>' +
    '<a href="organic-chemistry-1">Organic Chemistry prerequisite</a>' +
    '<a href="introduction-to-statistics">Statistics prerequisite</a>' +
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
      { '@type': 'ListItem', position: 2, name: 'Biological Sciences', item: 'https://openstemlibrary.com/#dept-biological-sciences' },
      { '@type': 'ListItem', position: 3, name: cfg.title, item: 'https://openstemlibrary.com/' + cfg.slug }
    ]
  });

  // Evaluate book data and startApp
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'biological-sciences', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'biological-sciences', cfg.slug);
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
let dept = catalog.departments.find(d => d.id === 'biological-sciences');
if (!dept) {
  dept = {
    id: 'biological-sciences',
    name: 'Biological Sciences',
    code: 'BIO',
    icon: '🧬',
    description: 'Foundational cellular and molecular biology, genetics, biochemistry, microbiology, physiology, ecology, genomics, and systems biology.',
    courses: []
  };
  catalog.departments.push(dept);
}

for (const cfg of bookConfigs) {
  dept.courses = dept.courses.filter(b => b.id !== cfg.slug);
  const dataJsText = fs.readFileSync(path.join(groupedRoot, 'biological-sciences', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
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
console.log(`Updated departments-data.js. Total Biological Sciences courses: ${dept.courses.length}`);

// Update publishing/book-queue.json
const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
let queueDept = queue.departments.find(d => d.id === 'biological-sciences');
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  const qBook = queueDept.books.find(b => b.id === 'biological-sciences-' + cfg.slug);
  if (qBook) {
    qBook.status = 'published';
    qBook.published_at = now;
    qBook.content_file = cfg.slug + '-data.js';
    qBook.url = cfg.slug + '.html';
    qBook.qa_report = `publishing/qa/biological-sciences-${cfg.slug}.json`;
    console.log(`Updated book-queue.json: ${qBook.id} -> published`);
  }
}

fs.writeFileSync(
  path.join(root, 'publishing/book-queue.json'),
  JSON.stringify(queue, null, 2) + '\n',
  'utf8'
);
console.log('Updated publishing/book-queue.json successfully.');
