const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'animal-physiology',
    title: 'Animal Physiology',
    subtitle: 'Homeostasis, Neurobiology, Muscle Mechanics, Circulation, Respiration, Osmoregulation & Endocrinology',
    seoTitle: 'Animal Physiology: Homeostasis, Neurobiology, Circulation & Respiration | OpenSTEM Library',
    badgeCredits: 'Animal physiology core',
    courseCodes: ['BIO 315', 'PHS 301'],
    searchPlaceholder: 'Search homeostatic set points, Nernst and Goldman membrane potentials, action potential propagation, sarcomere length-tension curves, cardiac output and Starling curve, countercurrent oxygen exchange, glomerular filtration rate, loop of Henle concentration gradient, endocrine feedback loops, thermoregulation…',
    probSecTitle: 'Step-by-Step Animal Physiology Solutions',
    description: 'Comprehensive university textbook covering homeostatic control systems, neurophysiology and action potentials, sensory and motor systems, cardiovascular dynamics, gas exchange and respiration, renal physiology and osmoregulation, gastrointestinal processing, and endocrine signaling with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university animal physiology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating homeostatic feedback decay, Nernst potentials, force-velocity relations, cardiac Starling curves, and countercurrent renal gradients. Numerical checks and an editorial review support this edition.',
    keywords: ['Animal Physiology', 'Homeostasis', 'Neurophysiology', 'Muscle Contraction', 'Cardiovascular System', 'Respiratory Gas Exchange', 'Renal Osmoregulation', 'Endocrine Signaling'],
    refPath: 'publishing/drafts/biological-sciences-animal-physiology/references.json'
  },
  {
    slug: 'plant-physiology',
    title: 'Plant Physiology',
    subtitle: 'Water Relations, Solute Transport, Photosynthetic Carbon Assimilation, Phloem Translocation & Hormonal Regulation',
    seoTitle: 'Plant Physiology: Water Relations, Photosynthesis, Phloem & Hormonal Control | OpenSTEM Library',
    badgeCredits: 'Plant physiology core',
    courseCodes: ['BIO 325', 'PLP 301'],
    searchPlaceholder: 'Search water potential components, van \'t Hoff osmotic potential, Hagen-Poiseuille xylem flow, stomatal conductance, Rubisco kinetics, photorespiration, Calvin-Benson cycle, phloem pressure-flow hypothesis, auxin polarization, phytochrome photoequilibria…',
    probSecTitle: 'Step-by-Step Plant Physiology Solutions',
    description: 'Comprehensive university textbook covering plant water relations and cavitation, mineral nutrient uptake and assimilation, photosynthetic light reactions and carbon fixation (C3, C4, CAM), phloem translocation mechanics, respiration and lipid metabolism, plant growth regulators (auxin, cytokinin, gibberellin, ABA, ethylene), photoperiodism, and abiotic stress physiology with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university plant physiology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating osmotic potentials, hydraulic conductance, light saturation kinetics, phloem pressure gradients, and stomatal ABA responsiveness. Numerical checks and an editorial review support this edition.',
    keywords: ['Plant Physiology', 'Water Potential', 'Xylem Cavitation', 'C3 C4 Photosynthesis', 'Phloem Translocation', 'Plant Hormones', 'Photoperiodism', 'Abiotic Stress Physiology'],
    refPath: 'publishing/drafts/biological-sciences-plant-physiology/references.json'
  },
  {
    slug: 'immunology',
    title: 'Immunology',
    subtitle: 'Innate Immunity, Antigen Processing, T & B Cell Development, Antibodies, Cytokines & Immunopathology',
    seoTitle: 'Immunology: Innate Defense, Antigen Processing, T & B Cells & Antibodies | OpenSTEM Library',
    badgeCredits: 'Immunology core',
    courseCodes: ['BIO 330', 'IMM 301'],
    searchPlaceholder: 'Search toll-like receptors, complement activation cascades, MHC Class I and II antigen presentation, V(D)J recombination, clonal selection, somatic hypermutation, affinity maturation, cytokine signaling pathways, hypersensitivity types, autoimmunity…',
    probSecTitle: 'Step-by-Step Immunology Solutions',
    description: 'Comprehensive university textbook covering anatomical and chemical innate defenses, pattern recognition receptors, complement pathways, MHC antigen presentation, T cell and B cell receptor gene rearrangement, lymphocyte activation and differentiation, antibody effector functions, immunological memory, tolerance, and clinical immunopathology with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university immunology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating mucosal barrier kinetics, receptor binding isotherms, clonal expansion doubling, cytotoxic killing ratios, and antibody waning kinetics. Numerical checks and an editorial review support this edition.',
    keywords: ['Immunology', 'Innate Immunity', 'Antigen Presentation', 'MHC Molecules', 'T Cell Receptors', 'B Cell Activation', 'Antibodies and Isotypes', 'Immunological Memory'],
    refPath: 'publishing/drafts/biological-sciences-immunology/references.json'
  },
  {
    slug: 'virology',
    title: 'Virology',
    subtitle: 'Viral Architecture, Genome Replication, Viral Entry & Assembly, Pathogenesis, Antivirals & Vaccines',
    seoTitle: 'Virology: Viral Structure, Genome Replication, Pathogenesis & Antivirals | OpenSTEM Library',
    badgeCredits: 'Virology core',
    courseCodes: ['BIO 335', 'VIR 301'],
    searchPlaceholder: 'Search icosahedral vs helical capsids, Baltimore classification scheme, positive vs negative-sense RNA replication, reverse transcriptase kinetics, viral attachment and fusion, one-step growth curves, plaque assays, antigenic drift and shift, antiviral resistance…',
    probSecTitle: 'Step-by-Step Virology Solutions',
    description: 'Comprehensive university textbook covering viral morphology and capsid geometry, Baltimore classification, replication cycles of DNA and RNA viruses, retroviral reverse transcription, host cell entry and membrane fusion, viral assembly and egress, cellular tropism, viral immune evasion, antiviral pharmacology, and vaccine design with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university virology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating viral plaque dilution counting, one-step replication kinetics, receptor saturation, clearance half-lives, and diagnostic predictive values. Numerical checks and an editorial review support this edition.',
    keywords: ['Virology', 'Baltimore Classification', 'Viral Capsids', 'RNA Virus Replication', 'Retroviruses', 'Viral Pathogenesis', 'Antiviral Therapeutics', 'Viral Vaccines'],
    refPath: 'publishing/drafts/biological-sciences-virology/references.json'
  },
  {
    slug: 'bioinformatics',
    title: 'Bioinformatics',
    subtitle: 'Sequence Alignment, Database Searching, Phylogenetics, RNA-Seq Analysis, Structural Modeling & Pipelines',
    seoTitle: 'Bioinformatics: Sequence Alignment, BLAST, RNA-Seq & Structural Modeling | OpenSTEM Library',
    badgeCredits: 'Bioinformatics core',
    courseCodes: ['BIO 340', 'BINF 301'],
    searchPlaceholder: 'Search Phred quality scores, FASTQ format, Needleman-Wunsch global alignment, Smith-Waterman local alignment, BLAST E-values and bit scores, PAM and BLOSUM substitution matrices, Jukes-Cantor distance, RNA-Seq CPM and TPM normalization, DESeq2 fold change, Benjamini-Hochberg FDR…',
    probSecTitle: 'Step-by-Step Bioinformatics Solutions',
    description: 'Comprehensive university textbook covering biological sequence file formats, dynamic programming alignment (Needleman-Wunsch, Smith-Waterman), heuristic search algorithms (BLAST), substitution models (Jukes-Cantor, Kimura), molecular phylogenetics, high-throughput RNA-Seq quantification (CPM, log2 fold change), multiple testing corrections (Benjamini-Hochberg FDR), and structural bioinformatics (RMSD) with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university bioinformatics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Phred error rates, pairwise alignment matrices, BLAST E-value scaling, Jukes-Cantor correction curves, and FDR ranking thresholds. Numerical checks and an editorial review support this edition.',
    keywords: ['Bioinformatics', 'Sequence Alignment', 'Needleman-Wunsch', 'BLAST Search', 'Phred Quality Scores', 'RNA-Seq Analysis', 'Multiple Testing Correction', 'Structural Bioinformatics'],
    refPath: 'publishing/drafts/biological-sciences-bioinformatics/references.json'
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
    '<a href="animal-physiology">Animal Physiology</a>' +
    '<a href="plant-physiology">Plant Physiology</a>' +
    '<a href="immunology">Immunology</a>' +
    '<a href="virology">Virology</a>' +
    '<a href="bioinformatics">Bioinformatics</a>' +
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
