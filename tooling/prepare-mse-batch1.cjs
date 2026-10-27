const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'fundamentals-of-materials-science',
    title: 'Fundamentals of Materials Science and Engineering',
    subtitle: 'Bonding, Crystal Structures, Imperfections, Mechanical Properties, Phase Diagrams & Failure',
    seoTitle: 'Fundamentals of Materials Science: Bonding, Structure & Mechanical Properties | OpenSTEM Library',
    badgeCredits: 'Materials science core',
    courseCodes: ['MSE 201', 'MAT 201'],
    searchPlaceholder: 'Search materials tetrahedron, ionic vs covalent vs metallic bonding, FCC/BCC/HCP crystal packing, point defects and vacancies, linear elasticity and Young modulus, engineering stress-strain curves, binary isomorphous phase diagrams, Griffith fracture criterion…',
    probSecTitle: 'Step-by-Step Materials Science Solutions',
    description: 'Comprehensive university textbook covering atomic bonding, crystal structures, point and line imperfections, dislocation-mediated slip, diffusion kinetics, binary phase equilibria, mechanical testing, and fracture mechanics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university materials science and engineering courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating atomic bonding forces, cubic unit cell geometries, elastic deflection curves, phase rule equilibrium fractions, and stress-concentration profiles. Numerical checks and an editorial review support this edition.',
    keywords: ['Materials Science', 'Atomic Bonding', 'Crystal Structures', 'Defects', 'Dislocations', 'Phase Diagrams', 'Mechanical Properties', 'Failure Analysis'],
    refPath: 'publishing/drafts/materials-science-and-engineering-fundamentals-of-materials-science/references.json'
  },
  {
    slug: 'crystallography-and-diffraction',
    title: 'Crystallography and Diffraction',
    subtitle: 'Bravais Lattices, Space Groups, Reciprocal Space, X-Ray & Electron Diffraction',
    seoTitle: 'Crystallography & Diffraction: Lattices, Space Groups & Bragg Law | OpenSTEM Library',
    badgeCredits: 'Crystallography core',
    courseCodes: ['MSE 301', 'MAT 301'],
    searchPlaceholder: 'Search 14 Bravais lattices, 32 crystallographic point groups, 230 space groups, Miller indices (hkl), reciprocal lattice vectors, Ewald sphere construction, Bragg law diffraction geometry, structure factor calculations, Scherrer crystallite size equation…',
    probSecTitle: 'Step-by-Step Crystallography Solutions',
    description: 'Comprehensive university textbook covering direct and reciprocal space geometry, symmetry operations, space group classification, kinematic diffraction theory, X-ray powder diffraction (XRD), transmission electron microscopy (TEM) diffraction patterns, and structure refinement with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university crystallography courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating cubic cell volumes, interplanar d-spacings, structure factor peak intensities, Bragg diffraction angles, and reciprocal lattice Ewald cuts. Numerical checks and an editorial review support this edition.',
    keywords: ['Crystallography', 'Diffraction', 'Bravais Lattices', 'Space Groups', 'Miller Indices', 'Reciprocal Space', 'Bragg Law', 'X-Ray Diffraction'],
    refPath: 'publishing/drafts/materials-science-and-engineering-crystallography-and-diffraction/references.json'
  },
  {
    slug: 'thermodynamics-of-materials',
    title: 'Thermodynamics of Materials',
    subtitle: 'Laws of Thermodynamics, Chemical Potential, Free Energy Curves, Phase Equilibria & Solutions',
    seoTitle: 'Thermodynamics of Materials: Free Energy, Chemical Potential & Phase Equilibria | OpenSTEM Library',
    badgeCredits: 'Thermodynamics core',
    courseCodes: ['MSE 305', 'MAT 305'],
    searchPlaceholder: 'Search first and second laws of thermodynamics, Gibbs free energy minimization, chemical potential and activity, ideal vs regular solution models, common tangent construction, Ellingham diagrams for oxides, unary and binary phase diagrams, CALPHAD thermodynamic modeling…',
    probSecTitle: 'Step-by-Step Thermodynamics Solutions',
    description: 'Comprehensive university textbook covering classical and statistical thermodynamics of materials, enthalpy and entropy of phase transitions, partial molar properties, non-ideal solution thermodynamics, free energy-composition curves, electrochemical thermodynamics, and phase stability diagrams with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university thermodynamics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating heat capacity integrations, regular solution mixing energies, chemical potential curves, Ellingham oxygen partial pressures, and binodal-spinodal phase boundaries. Numerical checks and an editorial review support this edition.',
    keywords: ['Thermodynamics', 'Materials Science', 'Gibbs Free Energy', 'Chemical Potential', 'Phase Equilibria', 'Regular Solutions', 'Ellingham Diagrams', 'Activity Coefficients'],
    refPath: 'publishing/drafts/materials-science-and-engineering-thermodynamics-of-materials/references.json'
  },
  {
    slug: 'diffusion-and-kinetics',
    title: 'Diffusion and Kinetics',
    subtitle: 'Fick Laws, Atomistic Mechanisms, Interface Mobility, Nucleation Kinetics & Growth',
    seoTitle: 'Diffusion and Kinetics in Materials: Fick Laws & Phase Transformations | OpenSTEM Library',
    badgeCredits: 'Kinetics core',
    courseCodes: ['MSE 310', 'MAT 310'],
    searchPlaceholder: 'Search Fick first and second laws of diffusion, error function concentration profiles, vacancy vs interstitial diffusion mechanisms, Kirkendall effect and Darken equations, grain boundary and dislocation pipe diffusion, homogeneous vs heterogeneous nucleation rates, Johnson-Mehl-Avrami-Kolmogorov (JMAK) kinetics…',
    probSecTitle: 'Step-by-Step Diffusion & Kinetics Solutions',
    description: 'Comprehensive university textbook covering mass transport fundamentals, non-steady-state diffusion solutions, interdiffusion in binary alloys, short-circuit transport, interface migration mechanics, classical nucleation theory, spinodal decomposition, and isothermal transformation kinetics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university kinetics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating diffusion penetration depths, Arrhenius temperature dependencies, Darken interdiffusion coefficients, critical nucleation radii, and JMAK transformed volume fractions. Numerical checks and an editorial review support this edition.',
    keywords: ['Diffusion', 'Kinetics', 'Fick Laws', 'Kirkendall Effect', 'Nucleation Theory', 'JMAK Kinetics', 'Interface Mobility', 'Spinodal Decomposition'],
    refPath: 'publishing/drafts/materials-science-and-engineering-diffusion-and-kinetics/references.json'
  },
  {
    slug: 'mechanical-behavior-of-solids',
    title: 'Mechanical Behavior of Solids',
    subtitle: 'Elasticity, Dislocations, Plastic Deformation, Fracture Mechanics, Fatigue & Creep',
    seoTitle: 'Mechanical Behavior of Solids: Elasticity, Dislocations, Fracture & Fatigue | OpenSTEM Library',
    badgeCredits: 'Mechanics of materials core',
    courseCodes: ['MSE 315', 'MAT 315'],
    searchPlaceholder: 'Search generalized Hooke law and compliance tensor, dislocation stress fields and Peach-Koehler force, Schmid law resolved shear stress, Hall-Petch grain boundary strengthening, linear elastic fracture mechanics (K_IC stress intensity), Paris law fatigue crack growth, power-law creep deformation mechanisms…',
    probSecTitle: 'Step-by-Step Mechanical Behavior Solutions',
    description: 'Comprehensive university textbook covering anisotropic continuum elasticity, dislocation mechanics and interaction energetics, strengthening mechanisms (solid solution, precipitation, strain hardening), fracture mechanics (energy release rate G and stress intensity K), fatigue cycle life, and high-temperature creep with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university mechanical behavior courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating resolved shear stress projections, dislocation line energies, Hall-Petch yield strengths, Griffith fracture stresses, and steady-state creep strain rates. Numerical checks and an editorial review support this edition.',
    keywords: ['Mechanical Behavior', 'Elasticity', 'Dislocations', 'Strengthening Mechanisms', 'Fracture Mechanics', 'Stress Intensity Factor', 'Fatigue Life', 'Creep'],
    refPath: 'publishing/drafts/materials-science-and-engineering-mechanical-behavior-of-solids/references.json'
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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Materials Science & Engineering Division</div>
    `;
  }

  const refBlock = d.querySelector('.references-block');
  if (refBlock && fs.existsSync(path.join(root, cfg.refPath))) {
    const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
    const refItems = refs.sources.map(s => `<li><strong>${s.institution}</strong>: ${s.role}</li>`).join('\n');
    refBlock.innerHTML = `
      <h3>Authoritative Academic Benchmarks & Citations</h3>
      <p>This textbook synthesizes canonical university curricula and established materials science references:</p>
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

  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'materials-science-and-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

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
