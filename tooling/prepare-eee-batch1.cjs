const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'circuit-analysis-i',
    title: 'Circuit Analysis I',
    subtitle: "Ohm's Law, Kirchhoff's Laws, Nodal & Mesh Analysis, Network Theorems, First & Second Order RLC Transients",
    seoTitle: 'Circuit Analysis I: DC Circuits, Network Theorems & RLC Transients | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 101', 'ECE 101', 'EE 101'],
    searchPlaceholder: 'Search electric charge and current, Ohm law, Kirchhoff laws, nodal and mesh analysis, Thevenin and Norton equivalents, maximum power transfer, RL and RC transients, RLC second-order damping…',
    probSecTitle: 'Step-by-Step Circuit Analysis I Solutions',
    description: "Comprehensive university textbook covering electric charge, current, Ohm's law, Kirchhoff's laws, nodal and mesh analysis, Thevenin and Norton theorems, maximum power transfer, first-order RL and RC transients, second-order RLC circuits, and measurement loading with 40 solved questions and 16 interactive simulations.",
    editorialNote: "<strong>About this textbook.</strong> Original English teaching material for university circuit analysis courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Ohm's law dissipation, passive sign convention, loaded voltage dividers, equivalent resistances, nodal equations, mesh analysis, Thevenin matching, capacitive and inductive energy, RL/RC time constants, and RLC damping regimes. Numerical checks and an editorial review support this edition.",
    keywords: ['Circuit Analysis', 'Ohm Law', 'Kirchhoff Laws', 'Nodal Analysis', 'Mesh Analysis', 'Thevenin Equivalent', 'RLC Transients', 'Network Theorems'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-circuit-analysis-i/references.json'
  },
  {
    slug: 'circuit-analysis-ii',
    title: 'Circuit Analysis II',
    subtitle: 'Sinusoidal Steady-State, Phasor Analysis, AC Power, Three-Phase Networks, Resonance & Laplace Transform',
    seoTitle: 'Circuit Analysis II: AC Circuits, Phasors, Resonance, Three-Phase & Laplace Transforms | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 102', 'ECE 102', 'EE 102'],
    searchPlaceholder: 'Search sinusoidal waveforms, RMS values, phasor transformation, AC impedance and admittance, sinusoidal nodal and mesh analysis, complex power, power factor correction, series and parallel resonance, mutual inductance, three-phase networks, Laplace transforms…',
    probSecTitle: 'Step-by-Step Circuit Analysis II Solutions',
    description: 'Comprehensive university textbook covering sinusoidal steady-state analysis, phasors, impedance, AC power and power factor correction, series and parallel resonance, magnetically coupled circuits, balanced and unbalanced three-phase systems, Laplace transforms, and frequency response with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university AC circuit analysis courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating sinusoidal peak and RMS, phase shift, RL/RC/RLC AC impedance, parallel admittance, AC nodal voltages, phasor power triangles, power factor capacitors, RLC resonance Q-factor, mutual coupling, and three-phase line currents. Numerical checks and an editorial review support this edition.',
    keywords: ['Circuit Analysis II', 'Phasors', 'AC Power', 'Resonance', 'Three-Phase Systems', 'Coupled Inductors', 'Laplace Transform', 'Bode Plots'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-circuit-analysis-ii/references.json'
  },
  {
    slug: 'signals-and-systems',
    title: 'Signals and Systems',
    subtitle: 'Continuous & Discrete Signals, LTI Systems, Convolution, Fourier Series, Transforms, Sampling & Z-Transforms',
    seoTitle: 'Signals and Systems: LTI Systems, Convolution, Fourier, Laplace & Z-Transforms | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 201', 'ECE 201', 'EE 201'],
    searchPlaceholder: 'Search continuous and discrete signals, unit impulse and step, LTI systems, convolution integral and sum, Fourier series, Fourier transforms, sampling theorem, aliasing, Laplace transform ROC, Z-transforms…',
    probSecTitle: 'Step-by-Step Signals and Systems Solutions',
    description: 'Comprehensive university textbook covering continuous and discrete-time signals, linear time-invariant (LTI) systems, convolution, continuous-time Fourier series and transforms, discrete-time Fourier transforms (DTFT), sampling theory, Laplace transforms, and Z-transforms with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university signals and systems courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating continuous sampling and aliasing, system linearity, time-shifting and scaling, continuous and discrete convolution, Fourier synthesis, Gibbs phenomenon, frequency response filtering, and Z-plane stability. Numerical checks and an editorial review support this edition.',
    keywords: ['Signals and Systems', 'LTI Systems', 'Convolution', 'Fourier Transform', 'DTFT', 'Sampling Theorem', 'Laplace Transform', 'Z-Transform'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-signals-and-systems/references.json'
  },
  {
    slug: 'analog-electronics',
    title: 'Analog Electronics',
    subtitle: 'Semiconductor Diodes, BJT & MOSFET Bias, Small-Signal Amplifiers, Op-Amps, Feedback & Oscillators',
    seoTitle: 'Analog Electronics: Bipolar & MOS Amplifiers, Op-Amps, Feedback & Filters | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 202', 'ECE 202', 'EE 202'],
    searchPlaceholder: 'Search semiconductor physics, p-n junction diodes, half-wave and bridge rectifiers, Zener regulators, BJT load lines, four-resistor bias, hybrid-pi small-signal models, common-emitter amplifiers, MOSFET square-law, operational amplifiers, active filters, feedback stability…',
    probSecTitle: 'Step-by-Step Analog Electronics Solutions',
    description: 'Comprehensive university textbook covering semiconductor physics, p-n junction diodes, rectifiers, BJT and MOSFET bias design, small-signal hybrid-pi modeling, single-stage and differential amplifiers, op-amp circuits, frequency response, feedback stability, active filters, and oscillators with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university analog electronics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating diode exponential IV curves, rectifier smoothing, capacitor ripple, Zener regulation, BJT load lines, hybrid-pi transconductance, emitter degeneration, MOSFET square-law, op-amp saturation, active low-pass filtering, and negative feedback stability. Numerical checks and an editorial review support this edition.',
    keywords: ['Analog Electronics', 'Diodes', 'BJT Amplifiers', 'MOSFETs', 'Operational Amplifiers', 'Feedback', 'Frequency Response', 'Oscillators'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-analog-electronics/references.json'
  },
  {
    slug: 'digital-electronics-for-electrical-engineers',
    title: 'Digital Electronics for Electrical Engineers',
    subtitle: 'Boolean Algebra, Karnaugh Maps, Combinational Logic, Sequential Circuits, Counters, FSMs & Memory',
    seoTitle: 'Digital Electronics for Electrical Engineers: Logic Design, FSMs & Memory | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 203', 'ECE 203', 'EE 203'],
    searchPlaceholder: 'Search binary and hexadecimal arithmetic, two complement, Boolean algebra, Karnaugh maps, multiplexers, adders, SR, D, JK and T flip-flops, synchronous counters, shift registers, Mealy and Moore FSM synthesis, CMOS inverter characteristics, SRAM and ROM architectures…',
    probSecTitle: 'Step-by-Step Digital Electronics Solutions',
    description: 'Comprehensive university textbook covering number systems, Boolean algebra, logic minimization via Karnaugh maps, combinational MSI circuits, flip-flops, synchronous counters, registers, finite state machine (FSM) synthesis, logic families (TTL, CMOS), and semiconductor memory architectures with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university digital electronics and logic design courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating binary radix words, logic gate truth tables, 2-to-1 multiplexers, full adders, D latch transparent timing, edge-triggered flip-flops, 3-bit synchronous counters, and finite state machine transitions. Numerical checks and an editorial review support this edition.',
    keywords: ['Digital Electronics', 'Boolean Algebra', 'Karnaugh Maps', 'Combinational Logic', 'Flip-Flops', 'Counters', 'Finite State Machines', 'CMOS Logic'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-digital-electronics-for-electrical-engineers/references.json'
  },
  {
    slug: 'electromagnetic-field-theory-i',
    title: 'Electromagnetic Field Theory I',
    subtitle: 'Curvilinear Vector Calculus, Electrostatics, Gauss Law, Dielectrics, Magnetostatics, Ampère Law & Boundary Values',
    seoTitle: 'Electromagnetic Field Theory I: Electrostatics, Magnetostatics & Boundary Value Problems | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 204', 'ECE 204', 'PHYS 204'],
    searchPlaceholder: 'Search curvilinear vector calculus, gradient, divergence, curl, Laplacian, divergence theorem, Stokes theorem, Coulomb law, Gauss law, electrostatic potential, Poisson and Laplace equations, method of images, dielectrics, capacitance, steady currents, Biot-Savart law, Ampere circuital law, vector potential…',
    probSecTitle: 'Step-by-Step Electromagnetic Field Theory I Solutions',
    description: "Comprehensive university textbook covering curvilinear vector calculus, Coulomb's and Gauss's laws, electrostatic potential, Laplace and Poisson equations, boundary value problems, dielectrics and capacitance, Biot-Savart and Ampère circuital laws, magnetic vector potential, magnetic forces and boundary conditions with 40 solved questions and 8 interactive simulations.",
    editorialNote: "<strong>About this textbook.</strong> Original English teaching material for university electromagnetic fields and waves courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating two-charge Coulomb field vectors, Gauss spherical flux surfaces, 1D parallel plate potential profiles, coaxial dielectric fields, Biot-Savart wire fields, solenoid magnetic flux density, boundary refraction, and induction. Numerical checks and an editorial review support this edition.",
    keywords: ['Electromagnetic Field Theory', 'Vector Calculus', 'Electrostatics', 'Gauss Law', 'Laplace Equation', 'Magnetostatics', 'Ampere Law', 'Boundary Value Problems'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-electromagnetic-field-theory-i/references.json'
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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Electrical & Electronics Engineering Division</div>
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
      <p>This textbook synthesizes canonical university curricula and established electrical engineering references:</p>
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
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'electrical-and-electronics-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'electrical-and-electronics-engineering', cfg.slug);
  const landingFile = path.join(targetDir, `${cfg.slug}.html`);
  fs.writeFileSync(landingFile, dom.serialize().replace(/^[ \t]+$/gm, ''), 'utf8');
  console.log(`Saved ${landingFile}`);
}

// Register department and courses in departments-data.js
console.log('Updating departments-data.js...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

if (!deptCode.includes('"id": "electrical-and-electronics-engineering"')) {
  const eeeDeptObj = {
    id: "electrical-and-electronics-engineering",
    name: "Electrical & Electronics Engineering",
    code: "EEE",
    icon: "⚡",
    description: "Electric circuits, signals and systems, analog and digital electronics, electromagnetic fields, electrical machines, power systems, control engineering, telecommunications, digital signal processing, power electronics, and high voltage engineering.",
    courses: []
  };

  for (const cfg of bookConfigs) {
    const dataJs = fs.readFileSync(path.join(groupedRoot, 'electrical-and-electronics-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
    const ctx = { window: {} };
    vm.createContext(ctx);
    vm.runInContext(dataJs, ctx);
    const units = ctx.window.COURSE_DATA.units.map(u => u.title);

    eeeDeptObj.courses.push({
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
    const formattedDept = ',\n    ' + JSON.stringify(eeeDeptObj, null, 2).replace(/\n/g, '\n    ') + '\n';
    deptCode = deptCode.slice(0, insertPos) + formattedDept + deptCode.slice(insertPos);
    fs.writeFileSync(deptDataPath, deptCode, 'utf8');
    console.log('Added Electrical & Electronics Engineering department to departments-data.js');
  }
} else {
  console.log('Electrical & Electronics Engineering department already in departments-data.js');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json...');
const bqPath = path.join(root, 'publishing', 'book-queue.json');
const bq = JSON.parse(fs.readFileSync(bqPath, 'utf8'));

let eeeQueue = bq.departments.find(d => d.id === 'electrical-and-electronics-engineering');
if (!eeeQueue) {
  eeeQueue = {
    id: "electrical-and-electronics-engineering",
    name: "Electrical & Electronics Engineering",
    order: 10,
    curriculum_status: "research_required",
    sources: [],
    major_scope_note: "Comprehensive undergraduate curriculum covering circuit analysis, signals, analog and digital electronics, electromagnetics, machines, power, control, communications, DSP, and high voltage engineering.",
    books: []
  };
  bq.departments.push(eeeQueue);
}

const now = new Date().toISOString();
for (const cfg of bookConfigs) {
  let qb = eeeQueue.books.find(b => b.id === `electrical-and-electronics-engineering-${cfg.slug}` || b.id === cfg.slug);
  if (!qb) {
    qb = eeeQueue.books.find(b => b.title.toLowerCase() === cfg.title.toLowerCase());
  }
  if (qb) {
    qb.id = `electrical-and-electronics-engineering-${cfg.slug}`;
    qb.title = cfg.title;
    qb.status = 'published';
    qb.content_file = `${cfg.slug}-data.js`;
    qb.url = `${cfg.slug}.html`;
    qb.qa_report = `publishing/qa/electrical-and-electronics-engineering-${cfg.slug}.json`;
    qb.published_at = now;
    console.log(`Marked published: ${cfg.slug}`);
  } else {
    console.log(`Adding book ${cfg.slug} to queue...`);
    eeeQueue.books.push({
      id: `electrical-and-electronics-engineering-${cfg.slug}`,
      title: cfg.title,
      sequence: eeeQueue.books.length + 1,
      level_year: null,
      curriculum_status: "research_required",
      curriculum_course_codes: cfg.courseCodes,
      status: 'published',
      minimum_words: 25000,
      unit_range: [8, 8],
      content_file: `${cfg.slug}-data.js`,
      url: `${cfg.slug}.html`,
      qa_report: `publishing/qa/electrical-and-electronics-engineering-${cfg.slug}.json`,
      published_at: now
    });
  }
}
fs.writeFileSync(bqPath, JSON.stringify(bq, null, 2), 'utf8');
console.log('Saved publishing/book-queue.json');

console.log('Batch 1 preparation complete!');
