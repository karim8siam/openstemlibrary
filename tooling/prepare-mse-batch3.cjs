const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'semiconductor-materials',
    title: 'Semiconductor Materials',
    subtitle: 'Band Structure, Carrier Transport, Doping, Junctions, Heterostructures & Device Physics',
    seoTitle: 'Semiconductor Materials: Band Theory, Carrier Transport & PN Junctions | OpenSTEM Library',
    badgeCredits: 'Semiconductor core',
    courseCodes: ['MSE 345', 'ECE 301'],
    searchPlaceholder: 'Search Kronig-Penney band structure, intrinsic vs extrinsic carrier densities (ni), Fermi-Dirac distribution and quasi-Fermi levels, drift and diffusion current equations, Einstein relation, p-n junction built-in potential and depletion width, Anderson heterojunction rule, quantum well subbands…',
    probSecTitle: 'Step-by-Step Semiconductor Solutions',
    description: 'Comprehensive university textbook covering electronic energy bands, effective mass tensor, shallow and deep dopants, recombination-generation mechanisms, minority carrier diffusion length, p-n and Schottky junctions, metal-oxide-semiconductor (MOS) electrostatics, and low-dimensional quantum heterostructures with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university semiconductor courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating intrinsic carrier concentrations, Fermi level shifts with doping, depletion region electric fields, junction capacitance curves, and quantum well energy levels. Numerical checks and an editorial review support this edition.',
    keywords: ['Semiconductors', 'Band Structure', 'Carrier Transport', 'Doping', 'PN Junction', 'MOSFET', 'Heterostructures', 'Fermi Level'],
    refPath: 'publishing/drafts/materials-science-and-engineering-semiconductor-materials/references.json'
  },
  {
    slug: 'electronic-and-magnetic-materials',
    title: 'Electronic and Magnetic Materials',
    subtitle: 'Dielectrics, Ferroelectrics, Piezoelectrics, Ferromagnetism, Spintronics & Superconductors',
    seoTitle: 'Electronic & Magnetic Materials: Dielectrics, Ferromagnetism & Spintronics | OpenSTEM Library',
    badgeCredits: 'Electronic & magnetic core',
    courseCodes: ['MSE 350', 'PHY 350'],
    searchPlaceholder: 'Search dielectric polarization mechanisms (electronic, ionic, dipolar), Clausius-Mossotti relation, ferroelectric Curie-Weiss law, piezoelectric d-coefficients, diamagnetism vs paramagnetism vs ferromagnetism, magnetic domain wall energy, magnetocrystalline anisotropy, giant magnetoresistance (GMR), BCS superconductivity…',
    probSecTitle: 'Step-by-Step Electronic & Magnetic Solutions',
    description: 'Comprehensive university textbook covering electric polarization dynamics, dielectric breakdown, ferroelectric polarization switching, piezoelectric transduction, magnetic exchange interactions, ferromagnetic hysteresis loops, soft vs hard magnetic materials, spintronic spin valves, and Type I/II superconductors with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university electronic and magnetic materials courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Clausius-Mossotti permittivity, Curie temperature susceptibilities, piezoelectric strain responses, ferromagnetic hysteresis curves, and superconducting Meissner screening. Numerical checks and an editorial review support this edition.',
    keywords: ['Electronic Materials', 'Magnetic Materials', 'Dielectrics', 'Ferroelectrics', 'Piezoelectricity', 'Ferromagnetism', 'Hysteresis Loops', 'Superconductivity'],
    refPath: 'publishing/drafts/materials-science-and-engineering-electronic-and-magnetic-materials/references.json'
  },
  {
    slug: 'optical-and-photonic-materials',
    title: 'Optical and Photonic Materials',
    subtitle: 'Kramers-Kronig Relations, Band Transitions, Lasers, Photodetectors, Optical Fibers & Photonic Crystals',
    seoTitle: 'Optical & Photonic Materials: Kramers-Kronig, Lasers & Photodetectors | OpenSTEM Library',
    badgeCredits: 'Photonics core',
    courseCodes: ['MSE 355', 'PHT 301'],
    searchPlaceholder: 'Search complex refractive index (n + ik), Kramers-Kronig dispersion integrals, direct vs indirect interband absorption, exciton absorption peaks, population inversion and Einstein A/B coefficients, stimulated emission in semiconductor lasers, photodiode responsivity and quantum efficiency, photonic band gaps…',
    probSecTitle: 'Step-by-Step Optical & Photonic Solutions',
    description: 'Comprehensive university textbook covering electromagnetic wave interaction with solids, dielectric permittivity dispersion, radiative and non-radiative transitions, light-emitting diodes (LEDs), laser diodes, photovoltaic solar cell absorption, fiber optic attenuation mechanisms, and periodic photonic crystals with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university optical materials courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating complex refractive indices, absorption coefficient band edge curves, Einstein stimulated gain coefficients, photodiode spectral responsivities, and photonic crystal band structures. Numerical checks and an editorial review support this edition.',
    keywords: ['Optical Materials', 'Photonics', 'Refractive Index', 'Kramers-Kronig', 'Lasers', 'Photodetectors', 'Photonic Crystals', 'Fiber Optics'],
    refPath: 'publishing/drafts/materials-science-and-engineering-optical-and-photonic-materials/references.json'
  },
  {
    slug: 'nanomaterials-and-surfaces',
    title: 'Nanomaterials and Surfaces',
    subtitle: 'Quantum Confinement, Surface Energy, Nanoparticle Synthesis, 2D Materials & Nanocomposites',
    seoTitle: 'Nanomaterials & Surfaces: Quantum Dots, 2D Materials & Surface Energy | OpenSTEM Library',
    badgeCredits: 'Nanotechnology core',
    courseCodes: ['MSE 360', 'NANO 301'],
    searchPlaceholder: 'Search quantum confinement in quantum dots/wires/wells, surface-to-volume ratio scaling, Young-Laplace and Kelvin equations for nano-droplets, localized surface plasmon resonance (LSPR), bottom-up sol-gel vs top-down ball milling synthesis, graphene and transition metal dichalcogenides (TMDs), carbon nanotubes…',
    probSecTitle: 'Step-by-Step Nanomaterials Solutions',
    description: 'Comprehensive university textbook covering size-dependent electronic and optical properties, surface thermodynamics and wetting, chemical vapor deposition (CVD) and colloidal nanocrystal growth, two-dimensional atomic crystals, carbon allotropes, plasmonic nanoparticles, and polymer-nanofiller composites with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university nanomaterials courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating quantum dot band gap shifts with particle diameter, surface area-to-volume scaling curves, Kelvin vapor pressure elevations, Mie plasmonic extinction spectra, and carbon nanotube chiral vector indices. Numerical checks and an editorial review support this edition.',
    keywords: ['Nanomaterials', 'Surfaces', 'Quantum Dots', 'Surface Energy', 'Plasmonics', 'Graphene', 'Carbon Nanotubes', 'Nanocomposites'],
    refPath: 'publishing/drafts/materials-science-and-engineering-nanomaterials-and-surfaces/references.json'
  },
  {
    slug: 'biomaterials',
    title: 'Biomaterials',
    subtitle: 'Biocompatibility, Host Response, Biodegradable Polymers, Bioactive Ceramics & Tissue Scaffolds',
    seoTitle: 'Biomaterials: Biocompatibility, Host Immune Response & Scaffolds | OpenSTEM Library',
    badgeCredits: 'Biomaterials core',
    courseCodes: ['MSE 365', 'BIOE 301'],
    searchPlaceholder: 'Search foreign body reaction and fibrous encapsulation, protein adsorption Vroman effect, titanium osseointegration, hydroxyapatite and Bioglass bioactivity, bioresorbable polymers (PLA, PGA, PLGA), hydrogels for drug delivery, mechanical matching for orthopedics, sterilization and cytotoxicity protocols…',
    probSecTitle: 'Step-by-Step Biomaterials Solutions',
    description: 'Comprehensive university textbook covering cell-material surface interactions, host immunological pathways, synthetic and natural biomedical polymers, structural metallic implants (Ti alloys, CoCr, 316L), calcium phosphate ceramics, tissue engineering scaffolds, controlled drug release kinetics, and regulatory ISO 10993 standards with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university biomaterials courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating protein adsorption kinetics, polymer hydrolytic degradation curves, scaffold pore size permeability, osseointegration shear strength, and drug elution diffusion profiles. Numerical checks and an editorial review support this edition.',
    keywords: ['Biomaterials', 'Biocompatibility', 'Tissue Engineering', 'Osseointegration', 'Biodegradable Polymers', 'Hydrogels', 'Drug Delivery', 'Implants'],
    refPath: 'publishing/drafts/materials-science-and-engineering-biomaterials/references.json'
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
