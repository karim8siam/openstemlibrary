const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'engineering-mechanics',
    title: 'Engineering Mechanics',
    subtitle: 'Statics, Particle & Rigid Body Dynamics, Trusses, Friction, Moments of Inertia & Work-Energy Principles',
    seoTitle: 'Engineering Mechanics: Statics, Dynamics & Work-Energy Principles | OpenSTEM Library',
    badgeCredits: 'Mechanical engineering core',
    courseCodes: ['ME 201', 'ENGR 201', 'CE 201'],
    searchPlaceholder: 'Search vector resolution, resultant forces, rigid body equilibrium, Method of Joints, Method of Sections, friction capstan, kinematics, work-energy, impulse-momentum, planar kinetics…',
    probSecTitle: 'Step-by-Step Engineering Mechanics Solutions',
    description: 'Comprehensive university textbook covering Newtonian vector statics, equilibrium, trusses, dry friction, particle kinematics, rigid body planar dynamics, and work-energy methods with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university engineering mechanics and statics/dynamics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating force vectors, beam reactions, trusses, capstan friction, and rigid body kinematics. Numerical checks and an editorial review support this edition.',
    keywords: ['Engineering Mechanics', 'Statics', 'Dynamics', 'Equilibrium', 'Trusses', 'Friction', 'Work-Energy', 'Moments of Inertia'],
    refPath: 'publishing/drafts/mechanical-engineering-engineering-mechanics/references.json'
  },
  {
    slug: 'mechanics-of-solids',
    title: 'Mechanics of Solids',
    subtitle: 'Stress-Strain Analysis, Axial Deformation, Torsion, Beam Bending, Deflections & Failure Criteria',
    seoTitle: 'Mechanics of Solids: Stress, Strain, Torsion, Bending & Deflection | OpenSTEM Library',
    badgeCredits: 'Mechanical engineering core',
    courseCodes: ['ME 202', 'ENGR 202', 'CE 202'],
    searchPlaceholder: 'Search axial stress-strain, thermal strain, St. Venant principle, torque angle of twist, shear center, beam deflection, Macaulay method, Mohr circle, Von Mises criterion, Euler column buckling…',
    probSecTitle: 'Step-by-Step Mechanics of Solids Solutions',
    description: 'Comprehensive university textbook covering stress and strain tensors, Hooke\'s law, axial members, circular shaft torsion, flexural and shear stresses in beams, beam deflection equations, Mohr\'s circle, and column buckling with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university mechanics of solids and strength of materials courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating axial deformation, torsion, beam curvature, principal stresses, and Euler buckling. Numerical checks and an editorial review support this edition.',
    keywords: ['Mechanics of Solids', 'Strength of Materials', 'Stress and Strain', 'Torsion', 'Beam Bending', 'Mohr Circle', 'Euler Buckling', 'Failure Criteria'],
    refPath: 'publishing/drafts/mechanical-engineering-mechanics-of-solids/references.json'
  },
  {
    slug: 'engineering-thermodynamics',
    title: 'Engineering Thermodynamics',
    subtitle: 'First & Second Laws, Pure Substance Properties, Control Volumes, Gas Cycles & Vapor Power Systems',
    seoTitle: 'Engineering Thermodynamics: First & Second Laws, Gas Cycles & Exergy | OpenSTEM Library',
    badgeCredits: 'Mechanical engineering core',
    courseCodes: ['ME 203', 'ENGR 203', 'CHE 203'],
    searchPlaceholder: 'Search ideal gas laws, steam tables, quality of vapor, First Law control volume, nozzle flow, turbine work, Carnot efficiency, entropy generation, exergy destruction, Rankine cycle, Brayton cycle…',
    probSecTitle: 'Step-by-Step Engineering Thermodynamics Solutions',
    description: 'Comprehensive university textbook covering thermodynamic properties, ideal and real gases, closed and open system energy conservation, entropy, second-law analysis, exergy, Carnot limits, Rankine and Brayton cycles, and psychrometrics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university engineering thermodynamics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating ideal gas equations of state, nozzle expansion, Carnot limits, Rankine cycles, and psychrometric properties. Numerical checks and an editorial review support this edition.',
    keywords: ['Engineering Thermodynamics', 'First Law', 'Second Law', 'Entropy', 'Exergy', 'Rankine Cycle', 'Brayton Cycle', 'Steam Tables'],
    refPath: 'publishing/drafts/mechanical-engineering-engineering-thermodynamics/references.json'
  },
  {
    slug: 'fluid-mechanics',
    title: 'Fluid Mechanics',
    subtitle: 'Fluid Statics, Control Volume Conservation, Navier-Stokes, Dimensional Analysis, Pipe Flow & Boundary Layers',
    seoTitle: 'Fluid Mechanics: Statics, Bernoulli, Navier-Stokes & Pipe Flow | OpenSTEM Library',
    badgeCredits: 'Mechanical engineering core',
    courseCodes: ['ME 204', 'CE 204', 'CHE 204'],
    searchPlaceholder: 'Search fluid statics, hydrostatic pressure, buoyant force, Reynolds transport theorem, Bernoulli equation, Pitot tube, Navier-Stokes equations, Buckingham Pi theorem, Moody chart, Darcy friction factor, boundary layer thickness…',
    probSecTitle: 'Step-by-Step Fluid Mechanics Solutions',
    description: 'Comprehensive university textbook covering fluid statics, manometry, Reynolds transport theorem, Bernoulli and energy equations, differential Navier-Stokes formulations, Buckingham Pi dimensional analysis, laminar and turbulent internal pipe flows, and external aerodynamics with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university fluid mechanics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Reynolds numbers, hydrostatic forces, Bernoulli velocities, Moody friction factors, and vortex shedding. Numerical checks and an editorial review support this edition.',
    keywords: ['Fluid Mechanics', 'Fluid Statics', 'Bernoulli Equation', 'Navier-Stokes', 'Dimensional Analysis', 'Pipe Flow', 'Boundary Layers', 'Turbulence'],
    refPath: 'publishing/drafts/mechanical-engineering-fluid-mechanics/references.json'
  },
  {
    slug: 'manufacturing-processes',
    title: 'Manufacturing Processes',
    subtitle: 'Metal Casting, Bulk Deformation, Machining & Metal Cutting, Additive Manufacturing, Joining & Metrology',
    seoTitle: 'Manufacturing Processes: Casting, Forming, Machining & Additive Manufacturing | OpenSTEM Library',
    badgeCredits: 'Mechanical engineering core',
    courseCodes: ['ME 205', 'IE 205', 'MSE 205'],
    searchPlaceholder: 'Search casting solidification, Chvorinov rule, riser design, rolling force, extrusion ratio, Merchant circle, Taylor tool life equation, additive laser sintering, fusion welding heat input, surface roughness, GD&T, Cpk process capability…',
    probSecTitle: 'Step-by-Step Manufacturing Processes Solutions',
    description: 'Comprehensive university textbook covering sand and investment casting, Chvorinov solidification, rolling, forging, extrusion, orthogonal metal cutting, tool wear models, additive manufacturing, fusion welding, dimensional metrology, and statistical quality control with 40 solved questions and 16 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university manufacturing processes courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating solidification time, forging loads, Taylor tool life, cutting mechanics, and metrology uncertainty. Numerical checks and an editorial review support this edition.',
    keywords: ['Manufacturing Processes', 'Metal Casting', 'Bulk Deformation', 'Machining', 'Taylor Tool Life', 'Additive Manufacturing', 'Welding', 'Metrology'],
    refPath: 'publishing/drafts/mechanical-engineering-manufacturing-processes/references.json'
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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Mechanical Engineering Division</div>
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
      <p>This textbook synthesizes canonical university curricula and established mechanical engineering references:</p>
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
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'mechanical-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'mechanical-engineering', cfg.slug);
  const landingFile = path.join(targetDir, `${cfg.slug}.html`);
  fs.writeFileSync(landingFile, dom.serialize().replace(/^[ \t]+$/gm, ''), 'utf8');
  console.log(`Saved ${landingFile}`);
}

// Register department and courses in departments-data.js
console.log('Updating departments-data.js...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

// Check if mechanical-engineering department exists
if (!deptCode.includes('"id": "mechanical-engineering"')) {
  const meDeptObj = {
    id: "mechanical-engineering",
    name: "Mechanical Engineering",
    code: "ME",
    icon: "⚙️",
    description: "Classical statics, dynamics, solid mechanics, thermodynamics, fluid dynamics, manufacturing processes, heat transfer, machine design, vibrations, turbomachinery, robotics, and computational FEA.",
    courses: []
  };

  for (const cfg of bookConfigs) {
    const dataJs = fs.readFileSync(path.join(groupedRoot, 'mechanical-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
    const ctx = { window: {} };
    vm.createContext(ctx);
    vm.runInContext(dataJs, ctx);
    const units = ctx.window.COURSE_DATA.units.map(u => u.title);

    meDeptObj.courses.push({
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

  // Insert before the closing bracket of departments array
  const lastDeptIdx = deptCode.lastIndexOf('    }');
  if (lastDeptIdx !== -1) {
    const insertPos = deptCode.indexOf('  ]', lastDeptIdx);
    const formattedDept = ',\n    ' + JSON.stringify(meDeptObj, null, 2).replace(/\n/g, '\n    ') + '\n';
    deptCode = deptCode.slice(0, insertPos) + formattedDept + deptCode.slice(insertPos);
    fs.writeFileSync(deptDataPath, deptCode, 'utf8');
    console.log('Added Mechanical Engineering department to departments-data.js');
  }
} else {
  console.log('Mechanical Engineering department already in departments-data.js');
}

// Update publishing/book-queue.json
console.log('Updating publishing/book-queue.json...');
const bqPath = path.join(root, 'publishing', 'book-queue.json');
const bq = JSON.parse(fs.readFileSync(bqPath, 'utf8'));

const meQueue = bq.departments.find(d => d.id === 'mechanical-engineering');
if (meQueue) {
  const now = new Date().toISOString();
  for (const cfg of bookConfigs) {
    let qb = meQueue.books.find(b => b.id === `mechanical-engineering-${cfg.slug}` || b.id === cfg.slug);
    if (!qb) {
      // Find matching by sequence or title
      qb = meQueue.books.find(b => b.title.toLowerCase() === cfg.title.toLowerCase());
    }
    if (qb) {
      qb.id = `mechanical-engineering-${cfg.slug}`;
      qb.title = cfg.title;
      qb.status = 'published';
      qb.content_file = `${cfg.slug}-data.js`;
      qb.url = `${cfg.slug}.html`;
      qb.qa_report = `publishing/qa/mechanical-engineering-${cfg.slug}.json`;
      qb.published_at = now;
      console.log(`Marked published: ${cfg.slug}`);
    } else {
      console.log(`Could not find book ${cfg.slug} in queue, adding...`);
      meQueue.books.push({
        id: `mechanical-engineering-${cfg.slug}`,
        title: cfg.title,
        sequence: meQueue.books.length + 1,
        status: 'published',
        minimum_words: 25000,
        content_file: `${cfg.slug}-data.js`,
        url: `${cfg.slug}.html`,
        qa_report: `publishing/qa/mechanical-engineering-${cfg.slug}.json`,
        published_at: now
      });
    }
  }
  fs.writeFileSync(bqPath, JSON.stringify(bq, null, 2), 'utf8');
  console.log('Saved publishing/book-queue.json');
}

console.log('Batch 1 preparation complete!');
