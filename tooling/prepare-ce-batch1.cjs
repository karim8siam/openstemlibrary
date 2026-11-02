const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'civil-engineering-statics',
    title: 'Civil Engineering Statics',
    subtitle: 'Vector Forces, Moments, Equilibrium, Trusses, Frames, Cables, Friction & Virtual Work',
    seoTitle: 'Civil Engineering Statics: Equilibrium, Trusses, Frames & Cables | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 101', 'CIV 101', 'ENG 101'],
    searchPlaceholder: 'Search vector loads, moments, force-couple transformations, free-body diagrams, support reactions, distributed loads, method of joints, method of sections, frames, cables, arches, centroids, second moments of area, Coulomb friction, sliding stability, virtual work…',
    probSecTitle: 'Step-by-Step Civil Engineering Statics Solutions',
    description: 'Comprehensive university textbook covering Newtonian vector equilibrium, support reactions, determinate trusses, frames, multi-force members, cables, three-hinged arches, centroids, moment of inertia, friction, sliding and overturning stability, and virtual work with 40 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university civil engineering statics courses. Eight units with five solved questions per unit and eight interactive simulations illustrating distributed load resultants, simply supported beam reactions, roof truss apex forces, parabolic cable tension and sag, composite section centroids, retaining wall overturning stability, virtual work levers, and construction staging load balance. Numerical checks and an editorial review support this edition.',
    keywords: ['Civil Engineering Statics', 'Equilibrium', 'Trusses', 'Method of Joints', 'Cables', 'Friction', 'Virtual Work', 'Centroids'],
    refPath: 'publishing/drafts/civil-engineering-civil-engineering-statics/references.json'
  },
  {
    slug: 'strength-of-materials',
    title: 'Strength of Materials',
    subtitle: "Stress, Strain, Axial Loading, Torsion, Beam Bending & Shear, Deflections, Mohr's Circle & Column Buckling",
    seoTitle: 'Strength of Materials: Stress-Strain, Torsion, Beam Flexure & Buckling | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 102', 'CIV 102', 'MECH 102'],
    searchPlaceholder: "Search normal stress, shear stress, axial stiffness, thermal expansion, indeterminate axial bars, torque transmission, angle of twist, shear force and bending moment diagrams, flexure formula, transverse shear stress, beam deflection, Mohr circle, principal stresses, combined axial and bending, Euler column buckling, pressure vessels…",
    probSecTitle: 'Step-by-Step Strength of Materials Solutions',
    description: "Comprehensive university textbook covering stress and strain tensors, axially loaded bars, thermal stress, circular shaft torsion, beam shear and moment diagrams, elastic flexure, transverse shear flow, elastic deflections, plane stress transformation, Mohr's circle, combined loading, Euler buckling, and thin-walled cylinders with 45 solved questions and 13 interactive simulations.",
    editorialNote: "<strong>About this textbook.</strong> Original English teaching material for university mechanics of materials and strength of materials courses. Nine units with five solved questions per unit and 13 interactive simulations illustrating axial bar elongation, bilinear stress-strain unloading, strain-gauge bridge circuits, circular shaft torsion, beam shear-moment envelopes, elastic deflection profiles, section geometry, transverse shear parabolic distribution, Mohr's circle stress rotations, combined axial plus bending, Euler column stability, thin-walled pressure cylinders, and fatigue S-N curves. Numerical checks and an editorial review support this edition.",
    keywords: ['Strength of Materials', 'Stress and Strain', 'Mohr Circle', 'Beam Deflection', 'Torsion', 'Column Buckling', 'Combined Stresses'],
    refPath: 'publishing/drafts/civil-engineering-strength-of-materials/references.json'
  },
  {
    slug: 'structural-analysis-i',
    title: 'Structural Analysis I',
    subtitle: 'Determinate Beams, Trusses, Three-Hinged Arches, Energy Methods, Virtual Work & Influence Lines',
    seoTitle: 'Structural Analysis I: Determinate Beams, Trusses, Virtual Work & Influence Lines | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 201', 'CIV 201', 'STR 201'],
    searchPlaceholder: 'Search structural idealization, load paths, determinate beams, internal shear and moment, method of joints, method of sections, truss deflections, three-hinged arches, cable sag and tension, virtual work method, unit load method, Castigliano theorem, moving loads, influence lines, Müller-Breslau principle, envelope curves…',
    probSecTitle: 'Step-by-Step Structural Analysis I Solutions',
    description: 'Comprehensive university textbook covering structural modeling, static determinacy and stability, determinate beam and frame analysis, pin-jointed trusses, three-hinged arches, suspension cables, elastic deflections via virtual work and energy methods, moving vehicle loads, influence lines, and structural verification with 40 solved questions and 13 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university determinate structural analysis courses. Eight units with five solved questions per unit and 13 interactive simulations illustrating beam reaction equilibrium, shear and moment diagrams, elastic beam deflections, triangular truss force resolution, virtual work truss displacements, three-hinged arch thrust, cable sag profiles, cantilever virtual displacements, moment influence lines, moving axle trains, propped cantilevers, and moving load envelopes. Numerical checks and an editorial review support this edition.',
    keywords: ['Structural Analysis I', 'Determinate Structures', 'Truss Analysis', 'Influence Lines', 'Virtual Work Method', 'Deflection Analysis', 'Three-Hinged Arches'],
    refPath: 'publishing/drafts/civil-engineering-structural-analysis-i/references.json'
  },
  {
    slug: 'structural-analysis-ii',
    title: 'Structural Analysis II',
    subtitle: 'Indeterminate Structures, Force Method, Moment Distribution, Matrix Stiffness, Dynamics & Plastic Analysis',
    seoTitle: 'Structural Analysis II: Indeterminate Frames, Moment Distribution & Matrix Stiffness | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 202', 'CIV 202', 'STR 202'],
    searchPlaceholder: 'Search degree of static indeterminacy, force method, flexibility matrix, slope-deflection equations, moment distribution method, sway frames, matrix stiffness method, local and global coordinates, transformation matrices, support settlement, thermal strains, second-order P-Delta effects, structural dynamics, SDOF and MDOF vibration, plastic collapse analysis…',
    probSecTitle: 'Step-by-Step Structural Analysis II Solutions',
    description: 'Comprehensive university textbook covering statically indeterminate structures, flexibility and force methods, slope-deflection, Hardy Cross moment distribution, direct stiffness method for trusses and frames, support settlement, thermal actions, geometric non-linearity and P-Delta effects, structural dynamics, and plastic limit analysis with 40 solved questions and 15 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university advanced structural analysis courses. Eight units with five solved questions per unit and 15 interactive simulations illustrating indeterminate axial load sharing, propped cantilever compatibility, continuous beam finite elements, moment distribution joint rotations, planar truss stiffness matrices, rigid portal frame matrices, support settlement redistribution, restrained thermal stresses, Euler buckling amplification, moving two-axle influence lines, shear-building natural frequencies, damped SDOF harmonic vibrations, plastic collapse mechanisms, stiffness uncertainty propagation, and beam mesh convergence. Numerical checks and an editorial review support this edition.',
    keywords: ['Structural Analysis II', 'Indeterminate Structures', 'Force Method', 'Moment Distribution', 'Matrix Stiffness Method', 'Structural Dynamics', 'Plastic Collapse'],
    refPath: 'publishing/drafts/civil-engineering-structural-analysis-ii/references.json'
  },
  {
    slug: 'concrete-technology',
    title: 'Concrete Technology',
    subtitle: 'Cements, Aggregates, Admixtures, Hydration, Fresh Concrete Rheology, Mix Design, Durability & Quality Control',
    seoTitle: 'Concrete Technology: Cement Hydration, Mix Design, Durability & Quality Control | OpenSTEM Library',
    badgeCredits: 'Civil engineering core',
    courseCodes: ['CE 203', 'CIV 203', 'MAT 203'],
    searchPlaceholder: 'Search Portland cement composition, Bogue compounds, pozzolans, fly ash, slag, silica fume, aggregate grading, fineness modulus, packing density, superplasticizers, air entrainment, hydration kinetics, heat of hydration, fresh concrete workability, slump test, Bingham rheology, ACI mix design, absolute volume method, compressive strength testing, modulus of elasticity, creep and drying shrinkage, durability transport, chloride penetration, carbonation front, alkali-silica reaction, quality control statistics…',
    probSecTitle: 'Step-by-Step Concrete Technology Solutions',
    description: 'Comprehensive university textbook covering Portland cements, supplementary cementitious materials, aggregate particle packing, chemical admixtures, hydration kinetics, heat of hydration, fresh concrete rheology, mix proportioning by absolute volume, compressive and tensile strength development, viscoelastic creep and shrinkage, durability transport mechanisms, chloride diffusion, carbonation, and statistical quality assurance with 40 solved questions and 14 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university concrete technology and civil materials courses. Eight units with five solved questions per unit and 14 interactive simulations illustrating aggregate grading curves, hydration reaction kinetics, temperature-time maturity, lumped thermal heat release, Bingham flow curves, absolute-volume mix balances, SSD aggregate moisture corrections, water-cement ratio strength sensitivity, restrained shrinkage envelopes, capillary sorptivity, carbonation depth fronts, chloride diffusion profiles, concrete strength quality control dispersion, and binder embodied carbon scenarios. Numerical checks and an editorial review support this edition.',
    keywords: ['Concrete Technology', 'Cement Hydration', 'Aggregate Grading', 'Mix Proportioning', 'Durability', 'Chloride Diffusion', 'Concrete Strength'],
    refPath: 'publishing/drafts/civil-engineering-concrete-technology/references.json'
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
      <div class="editorial-signoff">OpenSTEM Editorial Board • Civil Engineering Division</div>
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
      <p>This textbook synthesizes canonical university curricula and established civil engineering references:</p>
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
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'civil-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'civil-engineering', cfg.slug);
  const landingFile = path.join(targetDir, `${cfg.slug}.html`);
  fs.writeFileSync(landingFile, dom.serialize().replace(/^[ \t]+$/gm, ''), 'utf8');
  console.log(`Saved ${landingFile}`);
}

// Register department and courses in departments-data.js
console.log('Updating departments-data.js...');
const deptDataPath = path.join(root, 'departments-data.js');
let deptCode = fs.readFileSync(deptDataPath, 'utf8');

if (!deptCode.includes('"id": "civil-engineering"')) {
  const ceDeptObj = {
    id: "civil-engineering",
    name: "Civil Engineering",
    code: "CE",
    icon: "🏗️",
    description: "Structural analysis and design, strength of materials, concrete technology, steel and timber structures, soil mechanics, foundation engineering, fluid mechanics and hydraulics, hydrology, water resources, environmental engineering, transportation, and surveying.",
    courses: []
  };

  for (const cfg of bookConfigs) {
    const dataJs = fs.readFileSync(path.join(groupedRoot, 'civil-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
    const ctx = { window: {} };
    vm.createContext(ctx);
    vm.runInContext(dataJs, ctx);
    const units = ctx.window.COURSE_DATA.units.map(u => u.title);

    ceDeptObj.courses.push({
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
    const formattedDept = ',\n    ' + JSON.stringify(ceDeptObj, null, 2).replace(/\n/g, '\n    ') + '\n';
    deptCode = deptCode.slice(0, insertPos) + formattedDept + deptCode.slice(insertPos);
    fs.writeFileSync(deptDataPath, deptCode, 'utf8');
    console.log('Added Civil Engineering department to departments-data.js');
  }
} else {
  console.log('Civil Engineering department already in departments-data.js; checking courses...');
  const ctx = { window: {} };
  vm.createContext(ctx);
  vm.runInContext(deptCode, ctx);
  const catalog = ctx.window.LIBRARY_CATALOG;
  const ceDept = catalog.departments.find(d => d.id === 'civil-engineering');
  if (ceDept) {
    for (const cfg of bookConfigs) {
      if (!ceDept.courses.some(c => c.id === cfg.slug)) {
        const dataJs = fs.readFileSync(path.join(groupedRoot, 'civil-engineering', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
        const bCtx = { window: {} };
        vm.createContext(bCtx);
        vm.runInContext(dataJs, bCtx);
        const units = bCtx.window.COURSE_DATA.units.map(u => u.title);

        ceDept.courses.push({
          id: cfg.slug,
          title: cfg.title,
          subtitle: cfg.subtitle,
          status: "AVAILABLE",
          url: `${cfg.slug}.html`,
          badge: "Free Interactive Textbook",
          description: cfg.description,
          topics: units
        });
        console.log(`Added course ${cfg.slug} to civil-engineering department`);
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

let ceQueue = bq.departments.find(d => d.id === 'civil-engineering');
if (!ceQueue) {
  ceQueue = {
    id: "civil-engineering",
    name: "Civil Engineering",
    order: 12,
    curriculum_status: "research_required",
    sources: [],
    major_scope_note: "Comprehensive undergraduate civil engineering curriculum covering statics, strength of materials, structural analysis, concrete, steel, geotechnical, water resources, environmental, transportation, and geomatics.",
    books: []
  };
  bq.departments.push(ceQueue);
}

const now = new Date().toISOString();
for (const cfg of bookConfigs) {
  let qb = ceQueue.books.find(b => b.id === `civil-engineering-${cfg.slug}` || b.id === cfg.slug);
  if (!qb) {
    qb = ceQueue.books.find(b => b.title.toLowerCase() === cfg.title.toLowerCase());
  }
  if (qb) {
    qb.id = `civil-engineering-${cfg.slug}`;
    qb.title = cfg.title;
    qb.status = 'published';
    qb.content_file = `${cfg.slug}-data.js`;
    qb.url = `${cfg.slug}.html`;
    qb.qa_report = `publishing/qa/civil-engineering-${cfg.slug}.json`;
    qb.published_at = now;
    console.log(`Marked published: ${cfg.slug}`);
  } else {
    console.log(`Adding book ${cfg.slug} to queue...`);
    ceQueue.books.push({
      id: `civil-engineering-${cfg.slug}`,
      title: cfg.title,
      sequence: ceQueue.books.length + 1,
      level_year: null,
      curriculum_status: "research_required",
      curriculum_course_codes: cfg.courseCodes,
      status: 'published',
      minimum_words: 25000,
      unit_range: [8, 9],
      content_file: `${cfg.slug}-data.js`,
      url: `${cfg.slug}.html`,
      qa_report: `publishing/qa/civil-engineering-${cfg.slug}.json`,
      published_at: now
    });
  }
}
fs.writeFileSync(bqPath, JSON.stringify(bq, null, 2), 'utf8');
console.log('Saved publishing/book-queue.json');

console.log('Batch 1 preparation complete!');
