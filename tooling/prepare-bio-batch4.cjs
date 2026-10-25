const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'genomics',
    title: 'Genomics',
    subtitle: 'Genome Architecture, Next-Generation Sequencing, Variant Calling, Epigenomics & Comparative Genomics',
    seoTitle: 'Genomics: Genome Architecture, NGS, Variant Calling & Epigenomics | OpenSTEM Library',
    badgeCredits: 'Genomics core',
    courseCodes: ['BIO 401', 'GEN 401'],
    searchPlaceholder: 'Search C-value paradox, flow cytometry DNA content, short-read vs long-read sequencing, Illumina SBS chemistry, Phred quality and error rate, Lander-Waterman coverage, de novo k-mer assembly, N50 statistic, BWA alignment, VCF variant calling, GATK HaplotypeCaller, ENCODE ChIP-Seq, ATAC-Seq open chromatin, Hi-C topologically associating domains, single-cell RNA-Seq doublet rates…',
    probSecTitle: 'Step-by-Step Genomics Solutions',
    description: 'Comprehensive university textbook covering eukaryotic genome architecture and ploidy, high-throughput sequencing technologies (Illumina, PacBio, Oxford Nanopore), read quality assessment, genome assembly algorithms (de Bruijn graphs, overlap-layout-consensus), variant discovery (SNVs, indels, SVs), functional genomics (RNA-Seq, ChIP-Seq, ATAC-Seq), chromatin conformation, and population pangenomics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university genomics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating genome repeat fractions, sequencing depth coverage, k-mer spectrums, assembly N50 thresholds, and variant allele frequencies. Numerical checks and an editorial review support this edition.',
    keywords: ['Genomics', 'Next-Generation Sequencing', 'Genome Assembly', 'Variant Calling', 'Epigenomics', 'ChIP-Seq', 'ATAC-Seq', 'Pangenomics'],
    refPath: 'publishing/drafts/biological-sciences-genomics/references.json'
  },
  {
    slug: 'biotechnology',
    title: 'Biotechnology',
    subtitle: 'Recombinant DNA, Bioprocess Engineering, Fermentation, CRISPR Gene Editing & Synthetic Biology',
    seoTitle: 'Biotechnology: Recombinant DNA, Bioprocess, CRISPR & Synthetic Biology | OpenSTEM Library',
    badgeCredits: 'Biotechnology core',
    courseCodes: ['BIO 410', 'BIOT 401'],
    searchPlaceholder: 'Search plasmid cloning vectors, restriction digestion and ligation, Gibson assembly, golden gate assembly, host strain selection (E. coli, CHO, Pichia), microbial growth kinetics (Monod model), chemostat vs batch fermentation, dissolved oxygen mass transfer, downstream purification (affinity chromatography), CRISPR-Cas9 sgRNA design, off-target editing assays, metabolic pathway flux engineering…',
    probSecTitle: 'Step-by-Step Biotechnology Solutions',
    description: 'Comprehensive university textbook covering recombinant DNA technology, gene editing platforms (CRISPR-Cas9, base editors, prime editors), protein expression hosts, upstream bioprocess and fermentation kinetics, mass transfer in bioreactors, downstream protein purification, biopharmaceutical quality control, biosafety compliance, and synthetic biology circuits with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university biotechnology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating recovery yields, qPCR amplification cycles, Hill equation binding curves, microbial growth kinetics, and Michaelis-Menten enzyme rates. Numerical checks and an editorial review support this edition.',
    keywords: ['Biotechnology', 'Recombinant DNA', 'CRISPR Gene Editing', 'Bioprocess Engineering', 'Fermentation Kinetics', 'Downstream Purification', 'Synthetic Biology', 'Biopharmaceuticals'],
    refPath: 'publishing/drafts/biological-sciences-biotechnology/references.json'
  },
  {
    slug: 'conservation-biology',
    title: 'Conservation Biology',
    subtitle: 'Biodiversity Assessment, Population Viability, Habitat Fragmentation, Protected Areas & Restoration',
    seoTitle: 'Conservation Biology: Biodiversity, Extinction Risk, Habitat Loss & Restoration | OpenSTEM Library',
    badgeCredits: 'Conservation biology core',
    courseCodes: ['BIO 415', 'CONS 401'],
    searchPlaceholder: 'Search species richness (alpha, beta, gamma), species-area curves (Arrhenius model), minimum viable population (MVP), population viability analysis (PVA), effective population size (Ne), inbreeding depression, habitat fragmentation edge effects, wildlife corridors, IUCN Red List categories and criteria, protected area design (SLOSS debate), ecological restoration trajectories…',
    probSecTitle: 'Step-by-Step Conservation Biology Solutions',
    description: 'Comprehensive university textbook covering global biodiversity patterns, extinction drivers (habitat loss, overexploitation, invasive species, climate change), conservation genetics and effective population size, population viability analysis, island biogeography applied to nature reserves, landscape connectivity, endangered species recovery, and ecological restoration with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university conservation biology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating species-area scaling, exponential population decline, logistic recovery equilibria, genetic drift decay, and landscape connectivity percolation. Numerical checks and an editorial review support this edition.',
    keywords: ['Conservation Biology', 'Biodiversity Patterns', 'Species-Area Relationship', 'Population Viability Analysis', 'Habitat Fragmentation', 'Protected Areas', 'IUCN Red List', 'Ecological Restoration'],
    refPath: 'publishing/drafts/biological-sciences-conservation-biology/references.json'
  },
  {
    slug: 'biological-research-methods',
    title: 'Biological Research Methods',
    subtitle: 'Experimental Design, Hypothesis Testing, Bioimaging, Quantitative Measurements & Reproducibility',
    seoTitle: 'Biological Research Methods: Experimental Design, Microscopy & Data Analysis | OpenSTEM Library',
    badgeCredits: 'Research methods core',
    courseCodes: ['BIO 420', 'RES 401'],
    searchPlaceholder: 'Search factorial experimental designs, randomized complete block design, statistical power and sample size calculation, Type I and Type II error rates, fluorescence microscopy resolution (Abbe limit), confocal laser scanning, flow cytometry gating, qPCR standard curves and 2^-ddCt, immunoblot quantification, blinding and pre-registration, FAIR data principles…',
    probSecTitle: 'Step-by-Step Biological Research Methods Solutions',
    description: 'Comprehensive university textbook covering the scientific method in biology, hypothesis formulation, randomized experimental design, sample size determination, advanced light and electron microscopy, quantitative molecular assays (spectrophotometry, qPCR, Western blotting), flow cytometry, data normalization, error propagation, and scientific reproducibility with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university biological research methods courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating contrast sensitivity indices, search yield curves, effect size contrasts, confidence interval margins, and protocol reproducibility thresholds. Numerical checks and an editorial review support this edition.',
    keywords: ['Biological Research Methods', 'Experimental Design', 'Statistical Power', 'Fluorescence Microscopy', 'Quantitative Assays', 'Flow Cytometry', 'Scientific Reproducibility', 'Data Normalization'],
    refPath: 'publishing/drafts/biological-sciences-biological-research-methods/references.json'
  },
  {
    slug: 'systems-biology',
    title: 'Systems Biology',
    subtitle: 'Network Motifs, Dynamic Modeling, Feedback Loops, Metabolic Flux Analysis & Synthetic Gene Circuits',
    seoTitle: 'Systems Biology: Network Motifs, Dynamic Modeling, Feedback & Metabolic Flux | OpenSTEM Library',
    badgeCredits: 'Systems biology core',
    courseCodes: ['BIO 425', 'SYS 401'],
    searchPlaceholder: 'Search transcriptional regulation networks, network motifs (feed-forward loops, negative autoregulation), ordinary differential equation (ODE) modeling, steady-state response, bistability and hysteresis, limit cycle oscillations, metabolic flux analysis (FBA), stoichiometry matrices, stochastic gene expression and Gillespie algorithm, synthetic toggle switches and repressilators…',
    probSecTitle: 'Step-by-Step Systems Biology Solutions',
    description: 'Comprehensive university textbook covering biological networks, graph theory metrics, sensory transcription networks, dynamic modeling with differential equations, negative feedback accelerating response time, coherent and incoherent feed-forward loops, bistable switches and oscillations, genome-scale metabolic flux analysis, cellular noise and stochasticity, and design principles of synthetic biological circuits with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university systems biology courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating saturating response functions, reporter background correction, first-order decay clearance, Poisson molecule count noise, and synthetic circuit leakage. Numerical checks and an editorial review support this edition.',
    keywords: ['Systems Biology', 'Network Motifs', 'Feed-Forward Loops', 'Differential Equation Modeling', 'Bistability and Hysteresis', 'Metabolic Flux Analysis', 'Cellular Stochasticity', 'Synthetic Gene Circuits'],
    refPath: 'publishing/drafts/biological-sciences-systems-biology/references.json'
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
  const allBioBooks = [
    ['cell-biology', 'Cell Biology'],
    ['molecular-biology', 'Molecular Biology'],
    ['genetics', 'Genetics'],
    ['biochemistry-for-biology', 'Biochemistry for Biology'],
    ['microbiology', 'Microbiology'],
    ['plant-biology', 'Plant Biology'],
    ['animal-biology', 'Animal Biology'],
    ['evolutionary-biology', 'Evolutionary Biology'],
    ['ecology', 'Ecology'],
    ['developmental-biology', 'Developmental Biology'],
    ['animal-physiology', 'Animal Physiology'],
    ['plant-physiology', 'Plant Physiology'],
    ['immunology', 'Immunology'],
    ['virology', 'Virology'],
    ['bioinformatics', 'Bioinformatics'],
    ['genomics', 'Genomics'],
    ['biotechnology', 'Biotechnology'],
    ['conservation-biology', 'Conservation Biology'],
    ['biological-research-methods', 'Biological Research Methods'],
    ['systems-biology', 'Systems Biology']
  ];

  const trustNav = '<nav class="reader-trust-links" aria-label="Related reading">' +
    '<a href="index#dept-biological-sciences">Biological Sciences Department</a>' +
    allBioBooks.map(([s, t]) => `<a href="${s}">${t}</a>`).join('') +
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
