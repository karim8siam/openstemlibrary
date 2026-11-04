const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require('jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'process-design',
    title: 'Process Design',
    subtitle: 'Conceptual Synthesis, Flowsheet Hierarchy, Equipment Sizing, Guthrie Cost Estimation, Pinch Analysis & Plant Economics',
    seoTitle: 'Process Design: Flowsheet Synthesis, Pinch Analysis, Sizing & Plant Economics | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 408', 'CPE 408', 'PDE 408'],
    searchPlaceholder: 'Search conceptual design hierarchy, Douglas onion model, flowsheet synthesis, heuristics for separators and recycles, heat exchanger network synthesis, pinch point analysis, composite curves, grand composite curve, minimum utility target, Guthrie bare module equipment costing, CEPCI inflation index, fixed capital investment FCI, net present value NPV, discounted cash flow, internal rate of return IRR, payback period, design margin factor, utility pinch integration…',
    probSecTitle: 'Step-by-Step Process Design Solutions',
    description: 'Comprehensive university textbook covering conceptual flowsheet synthesis, Douglas hierarchy, heat exchanger network pinch analysis, composite curves, Guthrie bare module equipment sizing and costing, and discounted cash flow plant profitability with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university chemical plant design and process economics courses. Eight units with five solved questions per unit and eight interactive simulations illustrating Douglas hierarchy decision matrices, gross economic margin sensitivity, composite curve pinch analysis, heat exchanger utility targeting, Guthrie bare module cost estimation, discounted cash flow NPV/IRR profiles, column sequencing heuristics, and P&ID control loop resilience. Numerical checks and an editorial review support this edition.',
    keywords: ['Process Design', 'Flowsheet Synthesis', 'Pinch Analysis', 'Composite Curves', 'Guthrie Equipment Costing', 'Net Present Value', 'Plant Economics'],
    refPath: 'publishing/drafts/chemical-process-engineering-process-design/references.json'
  },
  {
    slug: 'process-safety',
    title: 'Process Safety',
    subtitle: 'Hazard Identification, Toxicity & Dispersion Models, Flammability, Relief Sizing, LOPA & SIL Verification',
    seoTitle: 'Process Safety: HAZOP, Dispersion Modeling, Relief Sizing, LOPA & SIL | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 412', 'CPE 412', 'SAF 412'],
    searchPlaceholder: 'Search process safety management PSM, OSHA standards, hazard and operability HAZOP, guide words and deviations, toxicity probit models, LC50 and ERPG thresholds, Gaussian puff and plume atmospheric dispersion, Pasquill-Gifford atmospheric stability classes, lower and upper flammability limits LFL and UFL, flash point, explosive TNT equivalence, BLEVE overpressure, emergency relief system sizing, DIERS runaway two-phase venting, layer of protection analysis LOPA, safety integrity levels SIL, target risk reduction…',
    probSecTitle: 'Step-by-Step Process Safety Solutions',
    description: 'Comprehensive university textbook covering process safety management, HAZOP methodology, probit toxicity models, atmospheric Gaussian dispersion, flammability limits and BLEVEs, DIERS emergency relief sizing, and LOPA risk reduction with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university process safety and loss prevention courses. Eight units with five solved questions per unit and eight interactive simulations illustrating HAZOP risk matrix ranking, Gaussian plume concentration contours, Le Chatelier flammability limits, TNT equivalence blast overpressure waves, Leung two-phase runaway relief sizing, LOPA independent protection layer mitigation, quantitative risk assessment QRA F-N curves, and SIS SIL verification PFDavg calculation. Numerical checks and an editorial review support this edition.',
    keywords: ['Process Safety', 'HAZOP', 'Gaussian Dispersion', 'Flammability Limits', 'BLEVE', 'Relief Sizing', 'LOPA', 'SIL Verification'],
    refPath: 'publishing/drafts/chemical-process-engineering-process-safety/references.json'
  },
  {
    slug: 'biochemical-engineering',
    title: 'Biochemical Engineering',
    subtitle: 'Microbial Growth Kinetics, Enzyme Biocatalysis, Bioreactor Design, Oxygen Mass Transfer, Sterilization & Downstream Processing',
    seoTitle: 'Biochemical Engineering: Fermentation, Enzyme Kinetics, Bioreactors & Downstream Processing | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 415', 'CPE 415', 'BIO 415'],
    searchPlaceholder: 'Search microbial cell composition, stoichiometry of cell growth, Michaelis-Menten enzyme kinetics, competitive and noncompetitive inhibition, Lineweaver-Burk plots, Monod growth model, substrate inhibition Haldane model, chemostat and continuous stirred bioreactors, wash-out dilution rate, fed-batch feeding strategies, volumetric oxygen transfer coefficient kLa, dynamic gassing-out method, power input in agitated vessels, thermal media sterilization, Del factor calculation, downstream cell disruption, chromatography resolution…',
    probSecTitle: 'Step-by-Step Biochemical Engineering Solutions',
    description: 'Comprehensive university textbook covering cellular stoichiometry, Michaelis-Menten biocatalysis, Monod microbial growth kinetics, continuous chemostats and fed-batch bioreactors, volumetric oxygen transfer kLa, thermal batch sterilization, and downstream purification with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university biochemical engineering and bioprocess technology courses. Eight units with five solved questions per unit and eight interactive simulations illustrating Michaelis-Menten and Lineweaver-Burk enzyme kinetics, Monod batch cell growth curves, chemostat steady-state wash-out profiles, fed-batch quasi-steady biomass accumulation, dynamic gassing-out oxygen transfer kLa, batch thermal media sterilization Del factor kinetics, cross-flow ultrafiltration membrane flux decline, and chromatographic peak resolution. Numerical checks and an editorial review support this edition.',
    keywords: ['Biochemical Engineering', 'Monod Growth', 'Michaelis Menten', 'Chemostat Sizing', 'kLa Oxygen Transfer', 'Downstream Processing', 'Bioreactors'],
    refPath: 'publishing/drafts/chemical-process-engineering-biochemical-engineering/references.json'
  },
  {
    slug: 'polymer-process-engineering',
    title: 'Polymer Process Engineering',
    subtitle: 'Polymerization Kinetics, Melt Rheology, Non-Newtonian Flow, Extrusion, Injection Molding & Sustainable Recycling',
    seoTitle: 'Polymer Process Engineering: Kinetics, Melt Rheology, Extrusion & Injection Molding | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 418', 'CPE 418', 'POL 418'],
    searchPlaceholder: 'Search step-growth and Carothers equation, free-radical addition chain polymerization, Trommsdorff gel effect, molecular weight distributions, number and weight average molecular weight Mn and Mw, polydispersity index PDI, polymer melt rheology, power-law and Carreau-Yasuda fluids, shear thinning viscosity, normal stress differences, single-screw extruder metering channel drag and pressure flow, die swell, twin-screw compounding, injection molding cavity filling and cooling time, polymer crystallization Avrami kinetics, mechanical and chemical plastics recycling…',
    probSecTitle: 'Step-by-Step Polymer Process Engineering Solutions',
    description: 'Comprehensive university textbook covering Carothers step-growth, free-radical polymerization kinetics, molecular weight distributions, non-Newtonian melt rheology, single-screw extruder pressure flow mechanics, injection molding filling and cooling dynamics, and plastics circularity with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university polymer engineering and plastics processing courses. Eight units with five solved questions per unit and eight interactive simulations illustrating Carothers step-growth degree of polymerization, free-radical Trommsdorff autoacceleration kinetics, Carreau-Yasuda shear thinning viscosity, single-screw extruder operating point intersection, injection molding gate filling pressure drop, part cooling thermal conduction time, Avrami crystallization kinetics, and mechanical recycling blend tensile performance. Numerical checks and an editorial review support this edition.',
    keywords: ['Polymer Engineering', 'Melt Rheology', 'Extrusion Modeling', 'Injection Molding', 'Carothers Equation', 'Power Law Fluid', 'Plastics Recycling'],
    refPath: 'publishing/drafts/chemical-process-engineering-polymer-process-engineering/references.json'
  },
  {
    slug: 'petroleum-and-petrochemical-processes',
    title: 'Petroleum and Petrochemical Processes',
    subtitle: 'Crude Characterization, Atmospheric Distillation, Fluid Catalytic Cracking, Hydrotreating, Steam Cracking & Petrochemical Building Blocks',
    seoTitle: 'Petroleum & Petrochemical Processes: Refining, Distillation, FCC, Hydroprocessing & Olefins | OpenSTEM Library',
    badgeCredits: 'Chemical engineering core',
    courseCodes: ['CHE 422', 'CPE 422', 'PET 422'],
    searchPlaceholder: 'Search crude oil assay characterization, API gravity, Watson characterization factor KW, True Boiling Point TBP curve, atmospheric distillation column side strippers, vacuum distillation deep cut, fluid catalytic cracking FCC riser-regenerator heat balance, catalyst circulation rate, hydrodesulfurization HDS trickle-bed reactor, catalytic reforming octane enhancement, thermal steam cracking of naphtha, coil outlet temperature, ethylene and propylene olefins yield, aromatics extraction BTX, refinery decarbonization and carbon intensity…',
    probSecTitle: 'Step-by-Step Petroleum & Petrochemical Solutions',
    description: 'Comprehensive university textbook covering crude oil assay characterization, atmospheric and vacuum distillation, fluid catalytic cracking FCC heat balances, hydrodesulfurization, naphtha steam cracking for olefins, BTX aromatics, and refinery decarbonization with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university petroleum refining and petrochemical technology courses. Eight units with five solved questions per unit and eight interactive simulations illustrating crude oil TBP assay cut sizing, atmospheric pipestill side-stripper heat duties, FCC riser-regenerator thermal balance and coke burning, hydrotreating trickle-bed HDS kinetics, naphtha steam cracking ethylene/propylene cracking severity, BTX aromatics liquid-liquid extraction ternary phase equilibrium, delayed coker cycle time optimization, and refinery carbon intensity abatement pathways. Numerical checks and an editorial review support this edition.',
    keywords: ['Petroleum Refining', 'Crude Assay', 'FCC Unit', 'Hydrotreating', 'Steam Cracking', 'Petrochemical Processes', 'Refinery Decarbonization'],
    refPath: 'publishing/drafts/chemical-process-engineering-petroleum-and-petrochemical-processes/references.json'
  }
];

// Reference template: chemical-engineering-fundamentals.html
const templatePath = path.join(groupedRoot, 'chemical-process-engineering', 'chemical-engineering-fundamentals', 'chemical-engineering-fundamentals.html');
const templateHtml = fs.readFileSync(templatePath, 'utf8');

for (const cfg of bookConfigs) {
  console.log(`Processing ${cfg.slug}...`);
  const dom = new JSDOM(templateHtml, {
    url: 'https://openstemlibrary.com/' + cfg.slug,
    runScripts: 'outside-only'
  });
  const d = dom.window.document;
  const w = dom.window;
  w.setTimeout = () => 0;
  w.scrollTo = () => {};

  // Title & Metadata
  d.title = cfg.seoTitle;
  const metaDesc = d.querySelector('meta[name="description"]');
  if (metaDesc) metaDesc.setAttribute('content', cfg.description);

  const canonical = d.querySelector('link[rel="canonical"]');
  if (canonical) canonical.setAttribute('href', `https://openstemlibrary.com/${cfg.slug}`);

  const ogTitle = d.querySelector('meta[property="og:title"]');
  if (ogTitle) ogTitle.setAttribute('content', cfg.seoTitle);

  const ogDesc = d.querySelector('meta[property="og:description"]');
  if (ogDesc) ogDesc.setAttribute('content', cfg.description);

  const ogUrl = d.querySelector('meta[property="og:url"]');
  if (ogUrl) ogUrl.setAttribute('content', `https://openstemlibrary.com/${cfg.slug}`);

  // Header Titles
  const h1 = d.querySelector('h1.book-title') || d.querySelector('h1');
  if (h1) h1.textContent = cfg.title;

  const subtitle = d.querySelector('p.lead-subtitle') || d.querySelector('.book-subtitle');
  if (subtitle) subtitle.textContent = cfg.subtitle;

  // Editorial note
  const edNote = d.querySelector('.editorial-callout-text') || d.querySelector('.editorial-note');
  if (edNote) edNote.innerHTML = cfg.editorialNote;

  // Search input placeholder
  const searchInput = d.querySelector('input[type="search"]') || d.querySelector('#search-input');
  if (searchInput) searchInput.setAttribute('placeholder', cfg.searchPlaceholder);

  // Solved problems section title
  const probTitle = d.querySelector('#solved-problems-title') || d.querySelector('.solved-problems h2');
  if (probTitle) probTitle.textContent = cfg.probSecTitle;

  // Fix assets / script links
  d.querySelectorAll('link[rel="stylesheet"]').forEach(l => {
    let href = l.getAttribute('href');
    if (href) {
      if (href.includes('chemical-engineering-fundamentals.css')) {
        l.setAttribute('href', `${cfg.slug}.css`);
      } else if (href.startsWith('../../') || href.startsWith('../')) {
        l.setAttribute('href', href.replace(/^\.\.\/\.\.\//, '').replace(/^\.\.\//, ''));
      }
    }
  });

  d.querySelectorAll('script').forEach(s => {
    let src = s.getAttribute('src');
    if (src) {
      if (src.includes('chemical-engineering-fundamentals-data.js')) {
        s.setAttribute('src', `${cfg.slug}-data.js`);
      } else if (src.includes('chemical-engineering-fundamentals-sims.js')) {
        s.setAttribute('src', `${cfg.slug}-sims.js`);
      } else if (src.startsWith('../../') || src.startsWith('../')) {
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
  console.log('Updated departments-data.js with Batch 4 courses.');
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

console.log('Batch 4 preparation complete!\n');
