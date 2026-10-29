const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'power-electronics-i',
    title: 'Power Electronics I',
    subtitle: 'Power Semiconductors, Gate Drives, Non-Isolated DC-DC Converters (Buck, Boost, Buck-Boost), Rectifiers & Thermal Design',
    seoTitle: 'Power Electronics I: Semiconductors, DC-DC Converters & Rectifiers | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 401', 'ECE 401', 'EE 401'],
    searchPlaceholder: 'Search power diodes, MOSFETs, IGBTs, safe operating area (SOA), switching and conduction losses, gate driver circuits, non-isolated DC-DC converters, buck converter, boost converter, buck-boost converter, inductor volt-second balance, capacitor charge balance, continuous and discontinuous conduction modes (CCM, DCM), single-phase and three-phase diode rectifiers, phase-controlled thyristor converters, firing angle alpha, thermal management, heat sinks, junction temperature…',
    probSecTitle: 'Step-by-Step Power Electronics I Solutions',
    description: 'Comprehensive university textbook covering power semiconductor devices (diodes, MOSFETs, IGBTs), thermal modeling, gate drives, non-isolated DC-DC converters (buck, boost, buck-boost), CCM/DCM operating boundaries, uncontrolled and controlled rectifiers, and passive magnetic components with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university introductory power electronics courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating converter efficiency curves, inductor ripple current envelopes, buck-boost gain ratios, rectifier conduction angles, thyristor firing delay dynamics, thermal heat sink margins, and gate charge profiles. Numerical checks and an editorial review support this edition.',
    keywords: ['Power Electronics', 'Semiconductors', 'MOSFET', 'IGBT', 'DC-DC Converters', 'Buck Converter', 'Boost Converter', 'Rectifiers', 'Gate Drives'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-power-electronics-i/references.json'
  },
  {
    slug: 'power-electronics-ii',
    title: 'Power Electronics II',
    subtitle: 'Isolated Converters, Resonant Power Supplies, Inverters, Sinusoidal PWM, Space Vector Modulation (SVPWM) & Grid Ties',
    seoTitle: 'Power Electronics II: Isolated Converters, Resonant Supplies & Inverters | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 402', 'ECE 402', 'EE 402'],
    searchPlaceholder: 'Search flyback converters, forward converters, push-pull, half-bridge and full-bridge topologies, high-frequency transformer isolation, resonant LLC converters, zero-voltage switching (ZVS), zero-current switching (ZCS), single-phase and three-phase voltage-source inverters (VSI), sinusoidal PWM (SPWM), space vector pulse width modulation (SVPWM), third-harmonic injection, total harmonic distortion (THD), active filters, grid-connected inverters, phase-locked loop (PLL), multi-level inverters…',
    probSecTitle: 'Step-by-Step Power Electronics II Solutions',
    description: 'Comprehensive university textbook covering galvanically isolated DC-DC converters (flyback, forward, full-bridge), resonant LLC converters with ZVS/ZCS soft switching, single-phase and three-phase voltage source inverters, sinusoidal and space-vector PWM (SVPWM), multilevel inverters, and grid-connected renewable power converters with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced power electronics and conversion courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating flyback magnetizing reset, LLC resonant tank impedance curves, SPWM harmonic spectra, SVPWM rotating reference vector sectors, inverter dead-time distortion, multilevel voltage synthesis, active power factor correction, and grid-tie phase-locked loop synchronization. Numerical checks and an editorial review support this edition.',
    keywords: ['Power Electronics II', 'Isolated Converters', 'Flyback', 'Forward', 'Resonant LLC', 'Inverters', 'SPWM', 'SVPWM', 'Grid-Tie'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-power-electronics-ii/references.json'
  },
  {
    slug: 'electrical-measurements-and-instrumentation-i',
    title: 'Electrical Measurements & Instrumentation I',
    subtitle: 'Measurement Errors, Traceability, Analog Meters (PMMC, MI), DC/AC Bridges, Potentiometers & Instrument Transformers',
    seoTitle: 'Electrical Measurements & Instrumentation I: Errors, Meters & Bridges | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 403', 'ECE 403', 'EE 403'],
    searchPlaceholder: 'Search systematic and random errors, uncertainty propagation, GUM guide, SI traceability, PMMC galvanometer, dynamometer wattmeter, moving iron meters, shunts and multipliers, DC potentiometers, Wheatstone bridge, Kelvin double bridge for low resistance, AC impedance bridges, Maxwell-Wien bridge, Hay bridge, Schering bridge for capacitance and dielectric loss, Wien bridge for frequency, current transformers (CT), potential transformers (PT), instrument burden and phase angle error…',
    probSecTitle: 'Step-by-Step Electrical Measurements & Instrumentation I Solutions',
    description: 'Comprehensive university textbook covering measurement metrology, uncertainty propagation, SI traceability, PMMC, moving-iron and dynamometer movements, ammeter shunts, voltmeter multipliers, DC potentiometers, Kelvin double bridges, AC impedance bridges (Maxwell, Hay, Schering, Wien), and instrument transformers (CT/PT) with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university classical electrical measurements and instrumentation courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating Gaussian error distribution propagation, PMMC damping ratios, meter loading sensitivity, Kelvin double bridge lead resistance cancellation, Maxwell-Wien bridge balance convergence, Schering bridge dissipation factor curves, CT burden ratio errors, and fluxmeter magnetic induction trajectories. Numerical checks and an editorial review support this edition.',
    keywords: ['Electrical Measurements', 'Instrumentation', 'Error Analysis', 'PMMC', 'Moving Iron', 'DC Potentiometers', 'AC Bridges', 'Instrument Transformers'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-electrical-measurements-and-instrumentation-i/references.json'
  },
  {
    slug: 'electrical-measurements-and-instrumentation-ii',
    title: 'Electrical Measurements & Instrumentation II',
    subtitle: 'Digital Instrumentation, Transducers (RTD, Thermocouples, LVDT, Strain Gauges), DAQ, Oscilloscopes & Virtual Instruments',
    seoTitle: 'Electrical Measurements & Instrumentation II: Digital DAQ, Transducers & Sensors | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 404', 'ECE 404', 'EE 404'],
    searchPlaceholder: 'Search digital voltmeters (DVM), dual-slope ADC, successive approximation register (SAR), sigma-delta conversion, digital storage oscilloscopes (DSO), real-time sampling, equivalent-time sampling, trigger modes, resistive strain gauges, Wheatstone bridge conditioning, RTDs, Callendar-Van Dusen equation, thermocouples, Seebeck effect, cold-junction compensation, LVDT, capacitive transducers, piezoelectric sensors, data acquisition (DAQ) architectures, anti-aliasing filters, sample-and-hold, LabVIEW virtual instrumentation…',
    probSecTitle: 'Step-by-Step Electrical Measurements & Instrumentation II Solutions',
    description: 'Comprehensive university textbook covering primary transducers (strain gauges, RTDs, thermocouples, LVDTs, piezoelectric crystals), signal conditioning, high-resolution ADCs (dual-slope, SAR, sigma-delta), digital storage oscilloscopes, FFT spectrum analyzers, multichannel DAQ architectures, and virtual instrumentation with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university modern sensor technology and electronic instrumentation courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating strain gauge bridge non-linearity, thermocouple cold-junction voltage tracking, LVDT core displacement demodulation, dual-slope integrating ADC charge cycles, DSO equivalent-time sampling grids, DAQ multichannel multiplexer crosstalk, and lock-in amplifier noise rejection. Numerical checks and an editorial review support this edition.',
    keywords: ['Instrumentation II', 'Transducers', 'Sensors', 'RTD', 'Thermocouples', 'LVDT', 'Digital Storage Oscilloscope', 'DAQ', 'ADC'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-electrical-measurements-and-instrumentation-ii/references.json'
  },
  {
    slug: 'high-voltage-engineering-i',
    title: 'High Voltage Engineering I',
    subtitle: 'Electric Field Computation, Dielectric Breakdown in Gases, Liquids & Solids, Impulse Generation & Marx Circuits',
    seoTitle: 'High Voltage Engineering I: Electric Fields, Dielectric Breakdown & Impulse Marx | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 405', 'ECE 405', 'EE 405'],
    searchPlaceholder: 'Search electrostatic fields, Laplace equation, numerical field computation, finite element method (FEM), charge simulation method (CSM), dielectric breakdown in gases, Townsend ionization mechanism, streamer discharge, Paschen law, vacuum insulation, liquid dielectrics breakdown, streamer propagation, cavity breakdown, solid dielectrics, intrinsic breakdown, electromechanical breakdown, thermal breakdown, treeing and tracking, generation of high AC voltages, cascaded transformers, resonant transformers, generation of high DC voltages, Cockcroft-Walton multiplier, impulse voltage generation, Marx generator circuits, standard 1.2/50 impulse wave…',
    probSecTitle: 'Step-by-Step High Voltage Engineering I Solutions',
    description: 'Comprehensive university textbook covering electrostatic field modeling, numerical methods (FEM, CSM), dielectric breakdown in gases (Townsend, streamer, Paschen law), liquids, and solid dielectrics (thermal, treeing), generation of high AC voltages (cascaded, series-resonant), high DC (Cockcroft-Walton), and impulse lightning/switching waveforms via Marx generators with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university introductory high voltage and insulation physics courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating coaxial cable field stress profiles, Paschen curve minima in gases, oil bubble breakdown thresholds, solid dielectric thermal runaway, Cockcroft-Walton ripple and voltage drop, series resonant transformer tuning, standard 1.2/50 µs impulse waveform shaping, and multi-stage Marx generator discharge dynamics. Numerical checks and an editorial review support this edition.',
    keywords: ['High Voltage Engineering', 'Dielectric Breakdown', 'Paschen Law', 'Townsend Mechanism', 'Marx Generator', 'Cockcroft-Walton', 'Impulse Waveforms', 'Insulation Stress'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-high-voltage-engineering-i/references.json'
  },
  {
    slug: 'high-voltage-engineering-ii',
    title: 'High Voltage Engineering II',
    subtitle: 'Overvoltages, Insulation Coordination, Lightning Protection, High-Voltage Testing, Corona & Partial Discharges',
    seoTitle: 'High Voltage Engineering II: Overvoltages, Insulation Coordination & HV Testing | OpenSTEM Library',
    badgeCredits: 'Electrical engineering core',
    courseCodes: ['EEE 406', 'ECE 406', 'EE 406'],
    searchPlaceholder: 'Search traveling waves on transmission lines, Bewley lattice diagram, lightning overvoltages, switching surges, temporary overvoltages, ferroresonance, insulation coordination, IEC 60071 standard, statistical withstand voltage, basic impulse insulation level (BIL), surge arresters, metal-oxide varistors (MOV), high-voltage measurement techniques, sphere gaps, electrostatic voltmeters, resistive and capacitive potential dividers, corona discharge, radio interference, partial discharge (PD) detection and measurement, non-destructive insulation testing, loss angle tan delta…',
    probSecTitle: 'Step-by-Step High Voltage Engineering II Solutions',
    description: 'Comprehensive university textbook covering transmission line traveling waves, Bewley lattice diagrams, lightning and switching surges, insulation coordination (IEC 60071, BIL), metal-oxide surge arresters, high-voltage measurement (sphere gaps, dividers), corona phenomena, and partial discharge / tan-delta non-destructive testing with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced power apparatus insulation and high-voltage transmission courses. Eight units with five solved questions per unit and 8 interactive simulations illustrating Bewley lattice traveling wave reflections, lightning stroke back-flashover voltage spikes, surge arrester V-I non-linear clamping, statistical insulation coordination margins, resistive-capacitive divider frequency responses, corona inception electric field gradients, partial discharge apparent charge pulses, and dielectric dissipation factor tan delta phase angles. Numerical checks and an editorial review support this edition.',
    keywords: ['High Voltage Engineering II', 'Traveling Waves', 'Bewley Lattice', 'Lightning Overvoltages', 'Insulation Coordination', 'BIL', 'Surge Arresters', 'Corona', 'Partial Discharge'],
    refPath: 'publishing/drafts/electrical-and-electronics-engineering-high-voltage-engineering-ii/references.json'
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
  const ogTitle = d.querySelector('meta[property="og:title"]');
  if (ogTitle) ogTitle.content = cfg.seoTitle;
  const ogDesc = d.querySelector('meta[property="og:description"]');
  if (ogDesc) ogDesc.content = cfg.description;
  const ogUrl = d.querySelector('meta[property="og:url"]');
  if (ogUrl) ogUrl.content = 'https://openstemlibrary.com/' + cfg.slug;
  const twTitle = d.querySelector('meta[name="twitter:title"]');
  if (twTitle) twTitle.content = cfg.seoTitle;
  const twDesc = d.querySelector('meta[name="twitter:description"]');
  if (twDesc) twDesc.content = cfg.description;

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

// Update departments-data.js
console.log('Updating departments-data.js...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(deptCode, ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
const eeeDept = catalog.departments.find(d => d.id === 'electrical-and-electronics-engineering');

if (eeeDept) {
  for (const cfg of bookConfigs) {
    if (!eeeDept.courses.some(c => c.id === cfg.slug)) {
      const dataJs = fs.readFileSync(path.join(groupedRoot, 'electrical-and-electronics-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
      const bCtx = { window: {} };
      vm.createContext(bCtx);
      vm.runInContext(dataJs, bCtx);
      const units = bCtx.window.COURSE_DATA.units.map(u => u.title);

      eeeDept.courses.push({
        id: cfg.slug,
        title: cfg.title,
        subtitle: cfg.subtitle,
        status: "AVAILABLE",
        url: `${cfg.slug}.html`,
        badge: "Free Interactive Textbook",
        description: cfg.description,
        topics: units
      });
      console.log(`Added ${cfg.slug} to departments-data.js`);
    }
  }
  fs.writeFileSync(deptDataPath, 'window.LIBRARY_CATALOG = ' + JSON.stringify(catalog, null, 2) + ';\n', 'utf8');
  console.log('Saved departments-data.js');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json...');
const bqPath = path.join(root, 'publishing', 'book-queue.json');
const bq = JSON.parse(fs.readFileSync(bqPath, 'utf8'));

let eeeQueue = bq.departments.find(d => d.id === 'electrical-electronics-engineering' || d.id === 'electrical-and-electronics-engineering');
if (eeeQueue) {
  const now = new Date().toISOString();
  for (const cfg of bookConfigs) {
    let qb = eeeQueue.books.find(b => b.id === `electrical-and-electronics-engineering-${cfg.slug}` || b.id === `electrical-electronics-engineering-${cfg.slug}` || b.id === cfg.slug);
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
}

console.log('Batch 4 preparation complete!');
