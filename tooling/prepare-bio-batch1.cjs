const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'cell-biology',
    title: 'Cell Biology',
    subtitle: 'Cell Architecture, Membrane Transport, Bioenergetics, Cell Signaling, Organelles & Cell Division',
    seoTitle: 'Cell Biology: Structure, Organelles, Membrane Transport & Signaling | OpenSTEM Library',
    badgeCredits: 'Cell biology core',
    courseCodes: ['BIO 101', 'MCB 101'],
    searchPlaceholder: 'Search cellular organization, prokaryotes vs eukaryotes, lipid bilayer fluidity, active transport, ATPase pump, mitochondrial electron transport, signal transduction pathways, microtubules, actin filaments, mitosis checkpoints, apoptosis cascades…',
    probSecTitle: 'Step-by-Step Cell Biology Solutions',
    description: 'Comprehensive university textbook covering eukaryotic and prokaryotic cellular organization, membrane structure and transport, bioenergetics and respiration, intracellular trafficking, signal transduction, cytoskeleton dynamics, cell cycle regulation, and programmed cell death with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university cell biology courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating population doubling, optical resolution, enzyme kinetics, and membrane permeability. Numerical checks and an editorial review support this edition; it has not received independent academic peer review. Curriculum mapping does not imply university endorsement.',
    keywords: ['Cell Biology', 'Prokaryotes and Eukaryotes', 'Membrane Transport', 'Bioenergetics', 'Signal Transduction', 'Cytoskeleton', 'Cell Cycle', 'Apoptosis'],
    refPath: 'publishing/drafts/biological-sciences-cell-biology/references.json'
  },
  {
    slug: 'molecular-biology',
    title: 'Molecular Biology',
    subtitle: 'DNA Structure & Replication, Transcription, Translation, Gene Regulation & Recombinant DNA',
    seoTitle: 'Molecular Biology: DNA Replication, Transcription, Translation & Regulation | OpenSTEM Library',
    badgeCredits: 'Molecular biology core',
    courseCodes: ['BIO 201', 'MCB 201'],
    searchPlaceholder: 'Search DNA double helix geometry, Okazaki fragments, DNA polymerase proofreading, homologous recombination, promoter recognition, RNA polymerase, splicing mechanisms, tRNA charging, ribosome decoding, lac operon, CRISPR-Cas9…',
    probSecTitle: 'Step-by-Step Molecular Biology Solutions',
    description: 'Comprehensive university textbook covering nucleic acid chemistry, DNA replication mechanisms, DNA repair and recombination, prokaryotic and eukaryotic transcription, RNA processing, translation and the genetic code, gene expression regulation (operons and chromatin), and molecular biology techniques with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university molecular biology courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating DNA melting curves, transcription kinetics, translation decoding, and promoter affinities. Numerical checks and an editorial review support this edition.',
    keywords: ['Molecular Biology', 'DNA Structure and Replication', 'Transcription Mechanics', 'RNA Splicing', 'Translation and Ribosomes', 'Gene Expression Regulation', 'Recombinant DNA', 'CRISPR Cas9'],
    refPath: 'publishing/drafts/biological-sciences-molecular-biology/references.json'
  },
  {
    slug: 'genetics',
    title: 'Genetics',
    subtitle: 'Mendelian Inheritance, Chromosomal Linkage, Pedigree Analysis, Quantitative & Population Genetics',
    seoTitle: 'Genetics: Mendelian Inheritance, Linkage, Population Genetics & Epigenetics | OpenSTEM Library',
    badgeCredits: 'Genetics core',
    courseCodes: ['BIO 202', 'GEN 201'],
    searchPlaceholder: 'Search monohybrid crosses, test crosses, chi-square goodness of fit, chromosomal linkage mapping, centimorgans, sex-linked inheritance, pedigree charts, polygenic traits, narrow-sense heritability, Hardy-Weinberg equilibrium, genetic drift…',
    probSecTitle: 'Step-by-Step Genetics Solutions',
    description: 'Comprehensive university textbook covering Mendelian principles of segregation and independent assortment, chromosomal basis of inheritance, sex linkage, gene mapping and genetic recombination, quantitative traits and heritability, population genetics (Hardy-Weinberg equilibrium), mutations, and developmental genetics with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university genetics courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating Mendelian punnett matrices, recombination frequency mapping, and Hardy-Weinberg equilibrium shifts. Numerical checks and an editorial review support this edition.',
    keywords: ['Genetics', 'Mendelian Inheritance', 'Linkage and Crossing Over', 'Pedigree Analysis', 'Quantitative Genetics', 'Heritability', 'Hardy-Weinberg Equilibrium', 'Population Genetics'],
    refPath: 'publishing/drafts/biological-sciences-genetics/references.json'
  },
  {
    slug: 'biochemistry-for-biology',
    title: 'Biochemistry for Biology',
    subtitle: 'Biomolecules, Enzyme Kinetics, Glycolysis, Citric Acid Cycle, Oxidative Phosphorylation & Biosynthesis',
    seoTitle: 'Biochemistry for Biology: Biomolecules, Enzyme Kinetics & Cellular Metabolism | OpenSTEM Library',
    badgeCredits: 'Biochemistry core',
    courseCodes: ['BIO 203', 'BCH 201'],
    searchPlaceholder: 'Search Henderson-Hasselbalch equation, peptide bond geometry, protein alpha-helix, Michaelis-Menten Km and Vmax, Lineweaver-Burk plots, competitive inhibition, glycolysis enzymes, ATP yield, pyruvate dehydrogenase, Krebs cycle, chemiosmosis…',
    probSecTitle: 'Step-by-Step Biochemistry Solutions',
    description: 'Comprehensive university textbook covering water and buffer chemistry, amino acids and protein structure, enzyme kinetics (Michaelis-Menten, allosteric regulation), carbohydrate and lipid biochemistry, glycolysis, the citric acid cycle, oxidative phosphorylation and ATP synthesis, and metabolic integration with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university biochemistry for life sciences courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating weak acid ionization, enzyme saturation, substrate inhibition, and proton gradient energetics. Numerical checks and an editorial review support this edition.',
    keywords: ['Biochemistry', 'Protein Structure', 'Enzyme Kinetics', 'Michaelis-Menten', 'Glycolysis', 'Citric Acid Cycle', 'Oxidative Phosphorylation', 'Metabolic Pathways'],
    refPath: 'publishing/drafts/biological-sciences-biochemistry-for-biology/references.json'
  },
  {
    slug: 'microbiology',
    title: 'Microbiology',
    subtitle: 'Microbial Diversity, Bacterial Cell Structure, Microbial Metabolism, Pathogenesis & Antimicrobial Action',
    seoTitle: 'Microbiology: Microbial Diversity, Bacterial Physiology, Virology & Antimicrobial Therapy | OpenSTEM Library',
    badgeCredits: 'Microbiology core',
    courseCodes: ['BIO 204', 'MIC 201'],
    searchPlaceholder: 'Search Gram-positive vs Gram-negative peptidoglycan, endospore formation, batch culture growth phases, generation time equation, viral lysogeny, bacterial transformation and conjugation, endotoxins vs exotoxins, beta-lactam resistance, biofilm formation…',
    probSecTitle: 'Step-by-Step Microbiology Solutions',
    description: 'Comprehensive university textbook covering microbial diversity, bacterial and archaeal cell wall structures, microbial growth kinetics and environmental influences, viral structure and replication, microbial genetics, host-pathogen interactions, mechanisms of antibiotic resistance, and environmental and industrial microbiology with 24 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university microbiology courses. Eight units with exactly three solved questions per unit and 16 interactive simulations illustrating exponential bacterial growth, chemostat dilution rates, antibiotic dose response, and viral plaque assays. Numerical checks and an editorial review support this edition.',
    keywords: ['Microbiology', 'Bacterial Morphology', 'Gram Stain', 'Microbial Growth Kinetics', 'Bacteriophages', 'Pathogenesis and Toxins', 'Antimicrobial Resistance', 'Biofilms'],
    refPath: 'publishing/drafts/biological-sciences-microbiology/references.json'
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
