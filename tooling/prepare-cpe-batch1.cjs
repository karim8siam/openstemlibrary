const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'chemical-engineering-fundamentals',
    title: 'Chemical Engineering Fundamentals',
    subtitle: 'Process Industries, Units & Dimensions, Flowsheets, Material & Energy Balances, PVT & Equipment Sizing',
    seoTitle: 'Chemical Engineering Fundamentals: Balances, PVT & Flowsheets | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 101', 'CPE 101', 'PROC 101'],
    searchPlaceholder: 'Search chemical manufacturing value chains, SI and engineering dimensions, unit conversion, flowsheets, degrees of freedom, material accounting, recycle and purge, energy foundations, enthalpy balances, PVT state equations, Van der Waals, heat exchangers, LMTD sizing, Dow Fire & Explosion Index, process safety…',
    probSecTitle: 'Step-by-Step Chemical Engineering Fundamentals Solutions',
    description: 'Comprehensive university textbook covering process industries, engineering dimensions, flowsheet representation, degrees of freedom, steady-state material conservation, recycle and purge loops, first-law enthalpy balances, PVT equation of state non-ideality, heat exchanger sizing, and process safety indices with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university chemical engineering fundamentals courses. Eight units with five solved questions per unit and eight interactive simulations illustrating economic mass balance, dimensional analysis Reynolds profiles, degrees of freedom solvers, recycle-purge stream conservation, continuous reactor enthalpy balance, Van der Waals PVT isotherms, countercurrent heat exchanger sizing, and Dow F&EI safety indices. Numerical checks and an editorial review support this edition.',
    keywords: ['Chemical Engineering Fundamentals', 'Material Balances', 'Energy Balances', 'Degrees of Freedom', 'Recycle Purge', 'PVT Behavior', 'Process Safety'],
    refPath: 'publishing/drafts/chemical-process-engineering-chemical-engineering-fundamentals/references.json'
  },
  {
    slug: 'material-and-energy-balances',
    title: 'Material and Energy Balances',
    subtitle: 'Conservation Laws, Multi-Unit Flowsheets, Combustion, Reactive Balances, Psychrometry & Unsteady-State Dynamics',
    seoTitle: 'Material and Energy Balances: Reactive Balances, Psychrometry & Dynamics | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 201', 'CPE 201', 'PROC 201'],
    searchPlaceholder: 'Search multi-component mass balances, tie components, atomic balances, extent of reaction, combustion excess air, flue gas Orsat, Hess law, flame temperature, steam tables, psychrometric humidity chart, adiabatic saturation, unsteady-state tank filling, flash drums, purge loops…',
    probSecTitle: 'Step-by-Step Material and Energy Balances Solutions',
    description: 'Comprehensive university textbook covering multi-component mass balances, bypass and purge calculations, reactive systems, atomic and extent-of-reaction formulations, combustion stoichiometry, energy balances, enthalpy changes with phase change, psychrometric chart drying, and unsteady-state conservation equations with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university material and energy balance courses. Eight units with five solved questions per unit and eight interactive simulations illustrating binary stream mixing, reactive conversion and extent of reaction, methane combustion flue gas Orsat, flash drum VLE mass split, heat exchanger sensible and latent balance, psychrometric wet-bulb cooling, transient liquid level dynamics, and integrated reactor-separator recycle loops. Numerical checks and an editorial review support this edition.',
    keywords: ['Material and Energy Balances', 'Reactive Balances', 'Combustion Stoichiometry', 'Extent of Reaction', 'Psychrometry', 'Flash Drums', 'Unsteady State Balances'],
    refPath: 'publishing/drafts/chemical-process-engineering-material-and-energy-balances/references.json'
  },
  {
    slug: 'chemical-engineering-thermodynamics',
    title: 'Chemical Engineering Thermodynamics',
    subtitle: 'First & Second Laws, Real Fluids, Residual Properties, VLE, Activity Models, Chemical Equilibrium & Power Cycles',
    seoTitle: 'Chemical Engineering Thermodynamics: VLE, Fugacity, Activity Models & Cycles | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 202', 'CPE 202', 'THERMO 202'],
    searchPlaceholder: 'Search Maxwell relations, cubic equations of state, fugacity coefficients, activity coefficient models, Margules, NRTL, UNIQUAC, Wilson, binary VLE phase diagrams, azeotrope formation, liquid-liquid equilibrium, chemical reaction equilibrium constant, Van t Hoff equation, Rankine vapor power cycle, refrigeration…',
    probSecTitle: 'Step-by-Step Chemical Engineering Thermodynamics Solutions',
    description: 'Comprehensive university textbook covering volumetric properties of pure fluids, Maxwell relations and residual enthalpy/entropy, vapor-liquid phase equilibria (VLE), fugacity in fluid mixtures, non-ideal liquid activity models (NRTL, UNIQUAC, Margules), reaction equilibrium constants, and process power/refrigeration thermodynamic cycles with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university chemical engineering thermodynamics courses. Eight units with five solved questions per unit and eight interactive simulations illustrating Peng-Robinson cubic equation of state, reversible Carnot and Rankine cycles, binary P-x-y / T-x-y VLE with Margules non-ideality, Van t Hoff chemical equilibrium temperature dependence, vapor compression refrigeration COP, excess Gibbs free energy mixing, adiabatic expansion Joule-Thomson inversion, and binary azeotrope pinch points. Numerical checks and an editorial review support this edition.',
    keywords: ['Chemical Engineering Thermodynamics', 'Phase Equilibria', 'VLE', 'Activity Coefficients', 'Peng Robinson', 'Fugacity', 'Reaction Equilibrium'],
    refPath: 'publishing/drafts/chemical-process-engineering-chemical-engineering-thermodynamics/references.json'
  },
  {
    slug: 'transport-phenomena',
    title: 'Transport Phenomena',
    subtitle: 'Unified Momentum, Thermal & Mass Transport: Shell Balances, Navier-Stokes, Boundary Layers & Analogies',
    seoTitle: 'Transport Phenomena: Momentum, Heat & Mass Transfer Analogies | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 301', 'CPE 301', 'TRAN 301'],
    searchPlaceholder: 'Search Newton law of viscosity, Fourier law of conduction, Fick law of diffusion, shell balances, Navier-Stokes differential equations, creeping flow, boundary layer theory, Blasius similarity, convective heat transfer, Nusselt number, Sherwood number, Chilton-Colburn analogy, interphase transport, two-film theory…',
    probSecTitle: 'Step-by-Step Transport Phenomena Solutions',
    description: 'Comprehensive university textbook covering unified momentum, energy, and mass transport mechanisms, microscopic differential shell balances, Navier-Stokes and energy equations, laminar and turbulent boundary layer velocity/temperature/concentration profiles, Chilton-Colburn and Reynolds analogies, and interphase flux coupling with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university transport phenomena courses. Eight units with five solved questions per unit and eight interactive simulations illustrating falling film velocity and shear stress profiles, radial thermal conduction in composite cylinders, steady-state equimolar counterdiffusion vs. unimolecular diffusion, Hagen-Poiseuille pipe flow, hydrodynamic and thermal boundary layer growth, Chilton-Colburn analogy j-factors, two-film mass transfer interface gradients, and unsteady transient diffusion penetration. Numerical checks and an editorial review support this edition.',
    keywords: ['Transport Phenomena', 'Momentum Transfer', 'Heat Transfer', 'Mass Transfer', 'Navier Stokes', 'Boundary Layer Theory', 'Chilton Colburn Analogy'],
    refPath: 'publishing/drafts/chemical-process-engineering-transport-phenomena/references.json'
  },
  {
    slug: 'fluid-flow-in-processes',
    title: 'Fluid Flow in Processes',
    subtitle: 'Fluid Statics, Incompressible & Compressible Flow, Piping Networks, Centrifugal Pumps, Packed Beds & Fluidization',
    seoTitle: 'Fluid Flow in Processes: Piping Networks, Pumps, Packed Beds & Fluidization | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 302', 'CPE 302', 'PROC 302'],
    searchPlaceholder: 'Search manometers, Bernoulli equation, Darcy-Weisbach friction factor, minor loss coefficients, equivalent length, parallel piping networks, centrifugal pump system curves, NPSH available and required, cavitation, compressible gas flow, convergent-divergent nozzles, choked flow, Ergun equation, packed columns, minimum fluidization velocity…',
    probSecTitle: 'Step-by-Step Fluid Flow in Processes Solutions',
    description: 'Comprehensive university textbook covering industrial fluid mechanics, manometer statics, mechanical energy balance with frictional dissipation, equivalent length minor losses, parallel pipe branching, centrifugal pump characteristic curves and NPSH cavitation limits, compressible gas expansion, Ergun packed bed pressure drop, and gas-solid fluidization dynamics with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university process fluid mechanics courses. Eight units with five solved questions per unit and eight interactive simulations illustrating differential manometer head, Moody diagram Colebrook friction factor, centrifugal pump system operating point match, NPSH available vs. cavitation margin, Ergun equation packed bed pressure drop, minimum fluidization bed expansion, compressible gas nozzle sonic choking, and parallel pipe flow splitting. Numerical checks and an editorial review support this edition.',
    keywords: ['Fluid Flow in Processes', 'Process Piping', 'Centrifugal Pumps', 'NPSH Cavitation', 'Packed Beds', 'Ergun Equation', 'Fluidization'],
    refPath: 'publishing/drafts/chemical-process-engineering-fluid-flow-in-processes/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'materials-science-and-engineering', 'fundamentals-of-materials-science', 'fundamentals-of-materials-science.html'),
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
    if (href && (href.includes('fundamentals-of-materials-science') || href.includes('materials-science'))) {
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

// Register department and courses in departments-data.js
console.log('Updating departments-data.js...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

if (!deptCode.includes('"id": "chemical-process-engineering"')) {
  const cpeDeptObj = {
    id: "chemical-process-engineering",
    name: "Chemical & Process Engineering",
    code: "CPE",
    icon: "⚗️",
    description: "Chemical engineering thermodynamics, material and energy balances, transport phenomena, fluid mechanics, heat and mass transfer, separation processes, chemical reaction engineering, process dynamics and control, process simulation and plant design, process safety, biochemical engineering, polymers, and petroleum and petrochemical processes.",
    courses: []
  };

  for (const cfg of bookConfigs) {
    const dataJs = fs.readFileSync(path.join(groupedRoot, 'chemical-process-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
    const ctx = { window: {} };
    vm.createContext(ctx);
    vm.runInContext(dataJs, ctx);
    const units = ctx.window.COURSE_DATA.units.map(u => u.title);

    cpeDeptObj.courses.push({
      id: cfg.slug,
      title: cfg.title,
      subtitle: cfg.subtitle,
      status: "AVAILABLE",
      url: `${cfg.slug}.html`,
      badge: "Free Interactive Textbook",
      description: cfg.description,
      topics: units
    });
  }

  const lastDeptIdx = deptCode.lastIndexOf('    }');
  if (lastDeptIdx !== -1) {
    const insertPos = deptCode.indexOf('  ]', lastDeptIdx);
    const formattedDept = ',\n    ' + JSON.stringify(cpeDeptObj, null, 2).replace(/\n/g, '\n    ') + '\n';
    deptCode = deptCode.slice(0, insertPos) + formattedDept + deptCode.slice(insertPos);
    fs.writeFileSync(deptDataPath, deptCode, 'utf8');
    console.log('Added Chemical & Process Engineering department to departments-data.js');
  }
} else {
  console.log('Chemical & Process Engineering department already in departments-data.js; checking courses...');
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
    console.log('Updated departments-data.js with new courses.');
  }
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json...');
const bqPath = path.join(root, 'publishing', 'book-queue.json');
const bq = JSON.parse(fs.readFileSync(bqPath, 'utf8'));

let cpeQueue = bq.departments.find(d => d.id === 'chemical-process-engineering');
if (!cpeQueue) {
  cpeQueue = {
    id: "chemical-process-engineering",
    name: "Chemical & Process Engineering",
    order: 13,
    curriculum_status: "research_required",
    sources: [],
    major_scope_note: "Comprehensive undergraduate chemical and process engineering curriculum covering fundamentals, mass/energy balances, thermodynamics, transport phenomena, fluid mechanics, heat/mass transfer, separations, reaction kinetics, dynamics/control, simulation, plant design, safety, biochemical, polymer, and petrochemical processes.",
    books: []
  };
  bq.departments.push(cpeQueue);
}

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

console.log('Batch 1 preparation complete!');
