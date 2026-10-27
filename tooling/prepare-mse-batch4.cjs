const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'materials-characterization',
    title: 'Materials Characterization',
    subtitle: 'XRD, SEM, TEM, AFM, Spectroscopy, Thermal Analysis & Surface Diagnostics',
    seoTitle: 'Materials Characterization: XRD, Electron Microscopy & Spectroscopy | OpenSTEM Library',
    badgeCredits: 'Characterization core',
    courseCodes: ['MSE 365', 'PHY 365'],
    searchPlaceholder: 'Search X-ray diffraction (XRD) peak indexing, Bragg law and Scherrer crystallite size, scanning electron microscopy (SEM) secondary vs backscattered electrons, transmission electron microscopy (TEM) bright field and selected area electron diffraction (SAED), atomic force microscopy (AFM) contact vs tapping mode, energy-dispersive X-ray spectroscopy (EDS), differential scanning calorimetry (DSC)…',
    probSecTitle: 'Step-by-Step Characterization Solutions',
    description: 'Comprehensive university textbook covering diffraction phenomena, electron beam optics, scanning and transmission electron microscopy, scanned probe microscopy, vibrational and core-level spectroscopies, thermal analysis, and surface chemical diagnostics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university materials characterization courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Bragg peak positions, electron beam penetration depths, Scherrer line broadening, EDS characteristic emission spectra, and DSC heat flow endotherms. Numerical checks and an editorial review support this edition.',
    keywords: ['Materials Characterization', 'XRD', 'SEM', 'TEM', 'AFM', 'EDS', 'Spectroscopy', 'Thermal Analysis'],
    refPath: 'publishing/drafts/materials-science-and-engineering-materials-characterization/references.json'
  },
  {
    slug: 'corrosion-and-degradation',
    title: 'Corrosion and Degradation',
    subtitle: 'Thermodynamics, Kinetics, Pourbaix Diagrams, Passivity & Environmental Failure',
    seoTitle: 'Corrosion & Degradation: Electrochemistry, Pourbaix & Passivity | OpenSTEM Library',
    badgeCredits: 'Corrosion core',
    courseCodes: ['MSE 370', 'CHE 370'],
    searchPlaceholder: 'Search electrochemical cell thermodynamics, Nernst equation, Pourbaix potential-pH diagrams, Butler-Volmer kinetics and Tafel slopes, mixed potential theory, active-passive transitions, pitting and crevice corrosion, stress corrosion cracking (SCC), galvanic coupling, cathodic protection design…',
    probSecTitle: 'Step-by-Step Corrosion & Degradation Solutions',
    description: 'Comprehensive university textbook covering electrochemical thermodynamics, Butler-Volmer electrode kinetics, Evans and Pourbaix diagrams, passivation mechanisms, localized corrosion phenomena, environmentally assisted cracking, polymer degradation, and industrial cathodic/anodic protection with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university corrosion engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Pourbaix immunity/passivity domains, mixed potential polarization intersections, Tafel slope extrapolations, pitting potential boundaries, and sacrificial anode galvanics. Numerical checks and an editorial review support this edition.',
    keywords: ['Corrosion', 'Electrochemistry', 'Pourbaix Diagrams', 'Passivity', 'Pitting', 'Stress Corrosion Cracking', 'Cathodic Protection', 'Degradation'],
    refPath: 'publishing/drafts/materials-science-and-engineering-corrosion-and-degradation/references.json'
  },
  {
    slug: 'sustainable-materials-and-circularity',
    title: 'Sustainable Materials and Circularity',
    subtitle: 'Life Cycle Assessment, Embodied Energy, Recycling, Biodegradation & Circular Economy',
    seoTitle: 'Sustainable Materials & Circularity: LCA, Recycling & Embodied Energy | OpenSTEM Library',
    badgeCredits: 'Sustainability core',
    courseCodes: ['MSE 375', 'ENV 375'],
    searchPlaceholder: 'Search life cycle assessment (LCA) ISO 14040 methodology, embodied energy and carbon footprint calculations, material circularity indicators (MCI), recycling thermodynamic limits and entropy of mixing, downcycling vs upcycling, biodegradable polymers, bio-based feedstocks, criticality matrices and supply risk…',
    probSecTitle: 'Step-by-Step Sustainable Materials Solutions',
    description: 'Comprehensive university textbook covering life cycle assessment (LCA), embodied carbon and energy metrics, thermodynamic limits of sorting and recycling, circular material flow indices, bio-derived and biodegradable polymers, critical raw materials scarcity, and closed-loop eco-design with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university sustainable materials courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating life cycle greenhouse gas trade-offs, embodied energy vs service life, recycling entropy degradation, bio-polymer breakdown kinetics, and material criticality risk grids. Numerical checks and an editorial review support this edition.',
    keywords: ['Sustainable Materials', 'Circularity', 'Life Cycle Assessment', 'Embodied Energy', 'Carbon Footprint', 'Recycling', 'Biodegradable Polymers', 'Eco-Design'],
    refPath: 'publishing/drafts/materials-science-and-engineering-sustainable-materials-and-circularity/references.json'
  },
  {
    slug: 'materials-processing-and-manufacturing',
    title: 'Materials Processing and Manufacturing',
    subtitle: 'Solidification, Casting, Powder Metallurgy, Deformation, Joining & Additive Manufacturing',
    seoTitle: 'Materials Processing & Manufacturing: Casting, Forming & Additive | OpenSTEM Library',
    badgeCredits: 'Processing core',
    courseCodes: ['MSE 380', 'ME 380'],
    searchPlaceholder: 'Search solidification front dynamics, Chvorinov rule for casting, dendritic growth and microsegregation, powder compaction and sintering kinetics, metal forming mechanics (rolling, forging, extrusion), yield criteria (Tresca, von Mises), welding metallurgy and heat affected zone (HAZ), additive manufacturing selective laser melting (SLM)…',
    probSecTitle: 'Step-by-Step Processing & Manufacturing Solutions',
    description: 'Comprehensive university textbook covering solidification thermodynamics, mold filling and casting design, powder synthesis and solid-state sintering, bulk deformation plastic flow, welding and brazing thermal cycles, polymer molding operations, and laser powder bed fusion additive manufacturing with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university materials processing courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Chvorinov freezing times, sintering densification curves, rolling force roll-bite mechanics, welding thermal profiles, and additive energy density thresholds. Numerical checks and an editorial review support this edition.',
    keywords: ['Materials Processing', 'Manufacturing', 'Solidification', 'Casting', 'Powder Metallurgy', 'Metal Forming', 'Welding', 'Additive Manufacturing'],
    refPath: 'publishing/drafts/materials-science-and-engineering-materials-processing-and-manufacturing/references.json'
  },
  {
    slug: 'computational-materials-science-design-and-selection',
    title: 'Computational Materials Science, Design and Selection',
    subtitle: 'Density Functional Theory, Molecular Dynamics, Phase-Field, CALPHAD & Ashby Charts',
    seoTitle: 'Computational Materials Science & Selection: DFT, MD & Ashby Charts | OpenSTEM Library',
    badgeCredits: 'Computational core',
    courseCodes: ['MSE 385', 'CMP 385'],
    searchPlaceholder: 'Search density functional theory (DFT) Hohenberg-Kohn theorems, Kohn-Sham equations and exchange-correlation functionals (LDA, GGA), molecular dynamics (MD) Verlet integration and interatomic potentials, Monte Carlo phase space sampling, CALPHAD Gibbs energy minimization, phase-field Allen-Cahn and Cahn-Hilliard equations, Ashby selection charts and performance indices…',
    probSecTitle: 'Step-by-Step Computational Materials Solutions',
    description: 'Comprehensive university textbook covering electronic structure methods (DFT), classical molecular dynamics, statistical mechanics simulations, thermodynamic CALPHAD modeling, meso-scale phase-field microstructural evolution, machine learning for materials property prediction, and multi-objective Ashby materials selection with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university computational materials science courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating electronic density convergence, Lennard-Jones trajectory steps, phase-field domain coarsening, CALPHAD phase equilibria, and Ashby chart material performance optimization. Numerical checks and an editorial review support this edition.',
    keywords: ['Computational Materials Science', 'DFT', 'Molecular Dynamics', 'Phase-Field', 'CALPHAD', 'Ashby Charts', 'Materials Selection', 'Machine Learning'],
    refPath: 'publishing/drafts/materials-science-and-engineering-computational-materials-science-design-and-selection/references.json'
  }
];

const templateHtml = fs.readFileSync(path.join(groupedRoot, 'materials-science-and-engineering/fundamentals-of-materials-science/fundamentals-of-materials-science.html'), 'utf8');

for (const cfg of bookConfigs) {
  const dom = new JSDOM(templateHtml);
  const w = dom.window;
  const d = w.document;

  d.title = cfg.seoTitle;

  const canon = d.querySelector('link[rel="canonical"]');
  if (canon) canon.href = `https://openstemlibrary.com/${cfg.slug}`;

  const descMeta = d.querySelector('meta[name="description"]');
  if (descMeta) descMeta.content = cfg.description;

  const kwMeta = d.querySelector('meta[name="keywords"]');
  if (kwMeta) kwMeta.content = cfg.keywords.join(', ');

  const ogTitle = d.querySelector('meta[property="og:title"]');
  if (ogTitle) ogTitle.content = cfg.title;

  const ogDesc = d.querySelector('meta[property="og:description"]');
  if (ogDesc) ogDesc.content = cfg.description;

  const ogUrl = d.querySelector('meta[property="og:url"]');
  if (ogUrl) ogUrl.content = `https://openstemlibrary.com/${cfg.slug}`;

  const twTitle = d.querySelector('meta[name="twitter:title"]');
  if (twTitle) twTitle.content = cfg.title;

  const twDesc = d.querySelector('meta[name="twitter:description"]');
  if (twDesc) twDesc.content = cfg.description;

  d.querySelectorAll('script[type="application/ld+json"]').forEach(s => {
    try {
      const data = JSON.parse(s.textContent);
      if (data['@type'] === 'Course' || data['@type'] === 'Book') {
        data.name = cfg.title;
        data.description = cfg.description;
        data.url = `https://openstemlibrary.com/${cfg.slug}`;
        s.textContent = JSON.stringify(data, null, 2);
      } else if (data['@type'] === 'BreadcrumbList') {
        if (data.itemListElement && data.itemListElement.length > 2) {
          data.itemListElement[2].name = cfg.title;
          data.itemListElement[2].item = `https://openstemlibrary.com/${cfg.slug}`;
        }
        s.textContent = JSON.stringify(data, null, 2);
      }
    } catch (e) {}
  });

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

  const noteEl = d.querySelector('#editorial-note') || d.querySelector('.editorial-note') || d.querySelector('#course-editorial-note');
  if (noteEl) noteEl.innerHTML = cfg.editorialNote;

  const codeContainer = d.querySelector('.course-codes');
  if (codeContainer) {
    codeContainer.innerHTML = '';
    cfg.courseCodes.forEach(code => {
      const span = d.createElement('span');
      span.className = 'course-code-tag';
      span.textContent = code;
      codeContainer.appendChild(span);
    });
  }

  let refData = [];
  try {
    refData = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
  } catch (e) {}
  const refList = d.querySelector('#references-list') || d.querySelector('.references-list');
  if (refList && refData.length > 0) {
    refList.innerHTML = '';
    refData.forEach(r => {
      const li = d.createElement('li');
      li.innerHTML = `<strong>${r.institution}</strong> — <span>${r.role}</span> (<a href="${r.url}" target="_blank" rel="noopener noreferrer">${r.url}</a>)`;
      refList.appendChild(li);
    });
  }

  const scripts = d.querySelectorAll('script[src]');
  scripts.forEach(s => {
    const src = s.getAttribute('src');
    if (src.endsWith('-data.js')) {
      s.setAttribute('src', `${cfg.slug}-data.js`);
    } else if (src.endsWith('-sims.js')) {
      s.setAttribute('src', `${cfg.slug}-sims.js`);
    } else if (src.startsWith('../../') || src.startsWith('../')) {
      s.setAttribute('src', src.replace(/^\.\.\/\.\.\//, '').replace(/^\.\.\//, ''));
    }
  });

  const bcCurrent = d.querySelector('.breadcrumb-item.current') || d.querySelector('.breadcrumb-item:last-child');
  if (bcCurrent) bcCurrent.textContent = cfg.title;

  const navLinks = d.querySelectorAll('.unit-nav-link');
  navLinks.forEach((link, idx) => {
    if (idx === 0) {
      link.setAttribute('href', `${cfg.slug}.html`);
    } else {
      link.setAttribute('href', `${cfg.slug}-chapter-${idx + 1}.html`);
    }
  });

  const nextBtn = d.querySelector('#next-unit-btn') || d.querySelector('.next-chapter-link');
  if (nextBtn) {
    nextBtn.setAttribute('href', `${cfg.slug}-chapter-2.html`);
  }

  const targetDir = path.join(groupedRoot, 'materials-science-and-engineering', cfg.slug);
  fs.mkdirSync(targetDir, { recursive: true });
  const targetHtmlPath = path.join(targetDir, cfg.slug + '.html');
  fs.writeFileSync(targetHtmlPath, dom.serialize(), 'utf8');
  w.close();
  console.log(`Generated landing page: ${targetHtmlPath}`);
}

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root, 'departments-data.js'), 'utf8'), ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
let dept = catalog.departments.find(d => d.id === 'materials-science-and-engineering');
if (!dept) {
  dept = {
    id: 'materials-science-and-engineering',
    name: 'Materials Science & Engineering',
    code: 'MSE',
    icon: '🔬',
    description: 'Crystallography, thermodynamics of materials, phase transformations, mechanical behavior, polymers, ceramics, semiconductors, and biomaterials.',
    courses: []
  };
  catalog.departments.push(dept);
}

for (const cfg of bookConfigs) {
  dept.courses = dept.courses.filter(b => b.id !== cfg.slug);
  const dataJsText = fs.readFileSync(path.join(groupedRoot, 'materials-science-and-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
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
console.log(`Updated departments-data.js. Total Materials Science & Engineering courses: ${dept.courses.length}`);

const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
let queueDept = queue.departments.find(d => d.id === 'materials-science-and-engineering');
if (!queueDept) {
  queueDept = {
    id: 'materials-science-and-engineering',
    name: 'Materials Science & Engineering',
    books: []
  };
  queue.departments.push(queueDept);
}
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  let qBook = queueDept.books.find(b => b.id === 'materials-science-and-engineering-' + cfg.slug);
  if (!qBook) {
    qBook = {
      id: 'materials-science-and-engineering-' + cfg.slug,
      title: cfg.title,
      status: 'published',
      published_at: now,
      content_file: cfg.slug + '-data.js',
      url: cfg.slug + '.html',
      qa_report: `publishing/qa/materials-science-and-engineering-${cfg.slug}.json`
    };
    queueDept.books.push(qBook);
  } else {
    qBook.status = 'published';
    qBook.published_at = now;
    qBook.content_file = cfg.slug + '-data.js';
    qBook.url = cfg.slug + '.html';
    qBook.qa_report = `publishing/qa/materials-science-and-engineering-${cfg.slug}.json`;
  }
  console.log(`Updated book-queue.json: ${qBook.id} -> published`);
}

fs.writeFileSync(
  path.join(root, 'publishing/book-queue.json'),
  JSON.stringify(queue, null, 2) + '\n',
  'utf8'
);
console.log('Updated publishing/book-queue.json successfully.');
