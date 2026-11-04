const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'heat-transfer-in-processes',
    title: 'Heat Transfer in Processes',
    subtitle: 'Conduction, Thermal Resistance Networks, Transient Response, Convection, Radiation, Heat Exchangers & Evaporation',
    seoTitle: 'Heat Transfer in Processes: Conduction, Convection & Exchanger Design | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 303', 'CPE 303', 'HEAT 303'],
    searchPlaceholder: 'Search Fourier conduction law, thermal contact resistance, cylindrical composite insulation, lumped capacitance Biot number, transient Heisler charts, Dittus-Boelter correlation, external boundary layers, natural convection Grashof number, Stefan-Boltzmann radiation, view factors, shell-and-tube LMTD, effectiveness-NTU method, pool and forced boiling curves, film condensation, falling film evaporators…',
    probSecTitle: 'Step-by-Step Heat Transfer in Processes Solutions',
    description: 'Comprehensive university textbook covering multidimensional conduction, extended surfaces, transient thermal response, forced and natural convection correlations, radiation exchange, heat exchanger design via LMTD and NTU methods, boiling, condensation, and industrial evaporation with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university heat transfer in chemical processes courses. Eight units with five solved questions per unit and eight interactive simulations illustrating composite wall conduction, transient lumped thermal cooling, pipe convection Nusselt correlations, radiation view factor geometry, shell-and-tube exchanger rating, pool boiling regime transitions, multiple-effect evaporator steam economy, and pinch point heat exchanger network analysis. Numerical checks and an editorial review support this edition.',
    keywords: ['Heat Transfer in Processes', 'Thermal Conduction', 'Convective Heat Transfer', 'Heat Exchangers', 'LMTD Method', 'Boiling and Condensation', 'Evaporators'],
    refPath: 'publishing/drafts/chemical-process-engineering-heat-transfer-in-processes/references.json'
  },
  {
    slug: 'mass-transfer',
    title: 'Mass Transfer',
    subtitle: 'Molecular Diffusion, Convective Mass Transport, Interphase Flux, Two-Film Theory, Absorption & Membrane Transport',
    seoTitle: 'Mass Transfer: Diffusion, Convection, Interphase Transfer & Absorption | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 304', 'CPE 304', 'MASS 304'],
    searchPlaceholder: 'Search Fick first and second laws, Maxwell-Stefan multicomponent diffusion, Knudsen diffusion in pores, Sherwood and Schmidt numbers, laminar and turbulent boundary layer mass transfer, Chilton-Colburn analogy, two-film resistance model, Henry law, gas absorption equilibrium, packed tower height of a transfer unit HTU and NTU, evaporative cooling, drying rate periods, solution-diffusion membrane permeation, solid dissolution leaching…',
    probSecTitle: 'Step-by-Step Mass Transfer Solutions',
    description: 'Comprehensive university textbook covering molecular diffusion in fluids and porous media, convective mass transfer coefficients, two-film interphase flux coupling, packed absorption column sizing via HTU/NTU, psychrometric drying curves, membrane permeation mechanics, and solid-liquid leaching with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university mass transfer courses. Eight units with five solved questions per unit and eight interactive simulations illustrating equimolar vs. unimolecular diffusion, mass transfer boundary layer Sherwood scaling, two-film interface concentration profiles, packed column absorption operating line and NTU, wet-bulb cooling and drying rate kinetics, membrane solute rejection and permeance, solid leaching dissolution, and packed tower hydrodynamic flooding. Numerical checks and an editorial review support this edition.',
    keywords: ['Mass Transfer', 'Molecular Diffusion', 'Fick Law', 'Two-Film Theory', 'Gas Absorption', 'HTU and NTU', 'Membrane Transport'],
    refPath: 'publishing/drafts/chemical-process-engineering-mass-transfer/references.json'
  },
  {
    slug: 'separation-processes-i',
    title: 'Separation Processes I',
    subtitle: 'Phase Equilibria, Flash Separation, Binary Distillation, McCabe-Thiele, Multicomponent Fractionation & Extraction',
    seoTitle: 'Separation Processes I: Distillation, McCabe-Thiele, Column Hydraulics & Extraction | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 305', 'CPE 305', 'SEP 305'],
    searchPlaceholder: 'Search vapor-liquid equilibria, Raoult and non-ideal activity coefficients, equilibrium flash drums, Rachford-Rice equation, binary distillation, McCabe-Thiele graphical construction, minimum reflux ratio, total reflux, Fenske-Underwood-Gilliland shortcut methods, tray column hydraulics, weeping, entrainment, flooding, sieve tray sizing, packed column mass transfer, liquid-liquid extraction, ternary liquid-liquid equilibrium diagrams, Hunter-Nash method…',
    probSecTitle: 'Step-by-Step Separation Processes I Solutions',
    description: 'Comprehensive university textbook covering phase equilibria, single-stage flash drum vapor-liquid separation, binary distillation column staging via McCabe-Thiele, column internals and hydraulic limits, multicomponent FUG shortcut design, absorption column stage calculations, and liquid-liquid extraction with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university equilibrium-staged separation processes courses. Eight units with five solved questions per unit and eight interactive simulations illustrating Rachford-Rice flash separation, McCabe-Thiele stepping with dynamic reflux, q-line thermal feed conditions, tray column flooding and weeping envelopes, Fenske minimum stages and Underwood minimum reflux, packed column absorption Kremser solver, ternary liquid-liquid extraction tie-lines, and energy-integrated distillation columns. Numerical checks and an editorial review support this edition.',
    keywords: ['Separation Processes', 'Binary Distillation', 'McCabe Thiele Method', 'Rachford Rice Flash', 'Column Hydraulics', 'Multicomponent Distillation', 'Liquid-Liquid Extraction'],
    refPath: 'publishing/drafts/chemical-process-engineering-separation-processes-i/references.json'
  },
  {
    slug: 'separation-processes-ii',
    title: 'Separation Processes II',
    subtitle: 'Membrane Separations, Reverse Osmosis, Gas Permeation, Adsorption, Chromatography & Industrial Crystallization',
    seoTitle: 'Separation Processes II: Membranes, Adsorption, Chromatography & Crystallization | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 401', 'CPE 401', 'SEP 401'],
    searchPlaceholder: 'Search reverse osmosis osmotic pressure and Van t Hoff equation, concentration polarization, ultrafiltration gel polarization, nanofiltration Donnan exclusion, gas separation cross-flow and countercurrent modules, Langmuir and Freundlich adsorption isotherms, breakthrough curves, fixed-bed adsorption, ion exchange capacity, preparative chromatography band broadening, Van Deemter equation, crystallization supersaturation, primary and secondary nucleation, crystal size distribution, solid-liquid cake filtration, centrifugal clarification…',
    probSecTitle: 'Step-by-Step Separation Processes II Solutions',
    description: 'Comprehensive university textbook covering advanced rate-based and modern separation technologies: reverse osmosis, ultrafiltration, gas permeation, fixed-bed adsorption breakthrough, preparative chromatography, solution crystallization kinetics, cake filtration, and solid-liquid processing with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced and non-thermal separation processes courses. Eight units with five solved questions per unit and eight interactive simulations illustrating reverse osmosis water flux and concentration polarization, gas permeation stage-cut selectivity, fixed-bed adsorption breakthrough fronts, Van Deemter chromatography plate height resolution, crystallization supersaturation and crystal size distribution, constant-pressure cake filtration resistance, rotary drum vacuum filter throughput, and hybrid membrane-distillation flowsheet energy optimization. Numerical checks and an editorial review support this edition.',
    keywords: ['Separation Processes II', 'Membrane Separations', 'Reverse Osmosis', 'Adsorption Breakthrough', 'Preparative Chromatography', 'Crystallization', 'Cake Filtration'],
    refPath: 'publishing/drafts/chemical-process-engineering-separation-processes-ii/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'chemical-process-engineering', 'chemical-engineering-fundamentals', 'chemical-engineering-fundamentals.html'),
  'utf8'
);

for (const cfg of bookConfigs) {
  console.log(`Preparing landing page for ${cfg.slug}...`);
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

  // Clean stylesheet links
  d.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (href.includes('chemical-engineering-fundamentals') || href.includes('chemical-process-engineering'))) {
      link.remove();
    } else if (href && (href.startsWith('../../') || href.startsWith('../'))) {
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

  const badgeCredits = d.querySelector('.badge-credits');
  if (badgeCredits) badgeCredits.textContent = cfg.badgeCredits;

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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Chemical & Process Engineering Division</div>
    `;
  }

  const editorialNoteAside = d.querySelector('.stat-editorial-note');
  if (editorialNoteAside) {
    editorialNoteAside.innerHTML = cfg.editorialNote;
  }

  const refBlock = d.querySelector('.references-block');
  if (refBlock && fs.existsSync(path.join(root, cfg.refPath))) {
    const refs = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
    const refItems = refs.sources.map(s => `<li><strong>${s.institution}</strong>: ${s.role}</li>`).join('\n');
    refBlock.innerHTML = `
      <h3>Authoritative Academic Benchmarks & Citations</h3>
      <p>This textbook synthesizes canonical university curricula and established chemical engineering references:</p>
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

  // Populate unit 1 content using COURSE_DATA
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'chemical-process-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'chemical-process-engineering', cfg.slug);
  const landingFile = path.join(targetDir, `${cfg.slug}.html`);
  fs.writeFileSync(landingFile, dom.serialize().replace(/^[ \t]+$/gm, ''), 'utf8');
  console.log(`Saved ${landingFile}`);
}

// Register courses in departments-data.js
console.log('Updating departments-data.js...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(deptCode, ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
const cpeDept = catalog.departments.find(d => d.id === 'chemical-process-engineering');

if (cpeDept) {
  for (const cfg of bookConfigs) {
    if (!cpeDept.courses.some(c => c.id === cfg.slug)) {
      const dataJs = fs.readFileSync(path.join(groupedRoot, 'chemical-process-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
      const bCtx = { window: {} };
      vm.createContext(bCtx);
      vm.runInContext(dataJs, bCtx);
      const units = bCtx.window.COURSE_DATA.units.map(u => u.title);

      cpeDept.courses.push({
        id: cfg.slug,
        title: cfg.title,
        subtitle: cfg.subtitle,
        status: "AVAILABLE",
        url: `${cfg.slug}.html`,
        badge: "Free Interactive Textbook",
        description: cfg.description,
        topics: units
      });
      console.log(`Added course ${cfg.slug} to chemical-process-engineering department`);
    }
  }
  const updatedCatalogCode = `window.LIBRARY_CATALOG = ${JSON.stringify(catalog, null, 2)};\n`;
  fs.writeFileSync(deptDataPath, updatedCatalogCode, 'utf8');
  console.log('Updated departments-data.js with Batch 2 courses.');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json...');
const bqPath = path.join(root, 'publishing', 'book-queue.json');
const bq = JSON.parse(fs.readFileSync(bqPath, 'utf8'));

let cpeQueue = bq.departments.find(d => d.id === 'chemical-process-engineering');
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  let qb = cpeQueue.books.find(b => b.id === `chemical-process-engineering-${cfg.slug}` || b.id === cfg.slug);
  if (!qb) {
    qb = cpeQueue.books.find(b => b.title.toLowerCase() === cfg.title.toLowerCase());
  }
  if (qb) {
    qb.id = `chemical-process-engineering-${cfg.slug}`;
    qb.title = cfg.title;
    qb.status = 'published';
    qb.content_file = `${cfg.slug}-data.js`;
    qb.url = `${cfg.slug}.html`;
    qb.qa_report = `publishing/qa/chemical-process-engineering-${cfg.slug}.json`;
    qb.published_at = now;
    console.log(`Marked published: ${cfg.slug}`);
  } else {
    console.log(`Adding book ${cfg.slug} to queue...`);
    cpeQueue.books.push({
      id: `chemical-process-engineering-${cfg.slug}`,
      title: cfg.title,
      sequence: cpeQueue.books.length + 1,
      level_year: null,
      curriculum_status: "research_required",
      curriculum_course_codes: cfg.courseCodes,
      status: 'published',
      minimum_words: 25000,
      unit_range: [8, 9],
      content_file: `${cfg.slug}-data.js`,
      url: `${cfg.slug}.html`,
      qa_report: `publishing/qa/chemical-process-engineering-${cfg.slug}.json`,
      published_at: now
    });
  }
}
fs.writeFileSync(bqPath, JSON.stringify(bq, null, 2), 'utf8');
console.log('Saved publishing/book-queue.json');

console.log('Batch 2 preparation complete!');
