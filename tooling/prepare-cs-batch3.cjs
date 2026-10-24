const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require(process.env.OPENSTEM_JSDOM_PATH || 'jsdom');

const root = path.resolve(__dirname, '..');
const groupedRoot = path.join(root, 'src', 'subjects');

const bookConfigs = [
  {
    slug: 'theory-of-computation',
    title: 'Theory of Computation',
    subtitle: 'Automata Theory, Formal Grammars, Computability, Turing Machines & Computational Complexity',
    seoTitle: 'Theory of Computation: Automata, Turing Machines, Decidability & NP-Completeness | OpenSTEM Library',
    badgeCredits: 'Theory of computation core',
    courseCodes: ['CS 301', 'CS 310'],
    searchPlaceholder: 'Search regular languages, DFA state transitions, NFA epsilon closures, pumping lemma for regular languages, context-free grammars, Chomsky normal form, pushdown automata, Turing machine transitions, Church-Turing thesis, halting problem undecidability, Rice theorem, polynomial-time reductions, NP-completeness, 3-SAT…',
    probSecTitle: 'Step-by-Step Theory of Computation Solutions',
    description: 'Comprehensive university textbook covering deterministic and nondeterministic finite automata, regular languages, pumping lemma, context-free grammars, pushdown automata, Turing machines, undecidability (Halting problem, Rice\'s theorem), reductions, and computational complexity (P, NP, NP-completeness, Cook-Levin theorem) with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university theory of computation courses. Eight units with exactly three solved questions per unit and 8 interactive simulations illustrating finite automata transitions, pumping lemma bounds, Turing machine deciders, and complexity class reductions. Numerical checks and an editorial review support this edition.',
    keywords: ['Theory of Computation', 'Automata Theory', 'Regular Languages and DFAs', 'Context-Free Grammars', 'Pushdown Automata', 'Turing Machines', 'Undecidability and Halting Problem', 'NP-Completeness and Reductions'],
    refPath: 'publishing/drafts/computer-science-theory-of-computation/references.json'
  },
  {
    slug: 'artificial-intelligence',
    title: 'Artificial Intelligence',
    subtitle: 'Heuristic Search, Adversarial Games, Knowledge Representation, Probabilistic Reasoning & Reinforcement Learning',
    seoTitle: 'Artificial Intelligence: Search, Logic, Bayesian Networks & Reinforcement Learning | OpenSTEM Library',
    badgeCredits: 'Artificial intelligence core',
    courseCodes: ['CS 360', 'CS 460'],
    searchPlaceholder: 'Search intelligent agents, state-space search, admissible heuristics, A* optimality, alpha-beta minimax pruning, constraint satisfaction AC-3, forward checking, resolution theorem proving, Bayesian network d-separation, variable elimination, Markov decision processes, Bellman optimality equations, Q-learning, policy gradients…',
    probSecTitle: 'Step-by-Step Artificial Intelligence Solutions',
    description: 'Comprehensive university textbook covering intelligent agents, uninformed and heuristic search (A*, IDA*), adversarial game playing (alpha-beta pruning, expectimax), constraint satisfaction problems, propositional and first-order logic, probabilistic reasoning and Bayesian networks, Markov decision processes, and reinforcement learning with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university artificial intelligence courses. Eight units with exactly three solved questions per unit and 8 interactive simulations illustrating search heuristics, minimax pruning, constraint propagation, and MDP value iteration. Numerical checks and an editorial review support this edition.',
    keywords: ['Artificial Intelligence', 'Heuristic Search and A*', 'Adversarial Game Search', 'Constraint Satisfaction', 'Knowledge Representation', 'Probabilistic Reasoning', 'Markov Decision Processes', 'Reinforcement Learning'],
    refPath: 'publishing/drafts/computer-science-artificial-intelligence/references.json'
  },
  {
    slug: 'machine-learning',
    title: 'Machine Learning',
    subtitle: 'Statistical Learning Theory, Linear Models, Kernel Methods, Neural Networks, Unsupervised Learning & Generalization',
    seoTitle: 'Machine Learning: Statistical Learning, Convex Optimization, Deep Networks & Kernel Methods | OpenSTEM Library',
    badgeCredits: 'Machine learning core',
    courseCodes: ['CS 361', 'CS 461'],
    searchPlaceholder: 'Search empirical risk minimization, PAC learnability, VC dimension, bias-variance tradeoff, gradient descent convergence, Ridge and Lasso L1/L2 regularization, maximum margin hyperplane, dual SVM, Mercer kernel conditions, multi-layer perceptron backpropagation, activation functions, PCA eigenvalue decomposition, k-means convergence…',
    probSecTitle: 'Step-by-Step Machine Learning Solutions',
    description: 'Comprehensive university textbook covering statistical learning theory, empirical risk minimization, bias-variance tradeoff, linear and logistic regression, regularized models (Lasso, Ridge), support vector machines and reproducing kernel Hilbert spaces, multi-layer perceptrons, backpropagation, dimensionality reduction (PCA, t-SNE), clustering, and generative modeling with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university machine learning courses. Eight units with exactly three solved questions per unit and 8 interactive simulations illustrating regression loss landscapes, decision boundary margins, gradient descent trajectories, and principal component projections. Numerical checks and an editorial review support this edition.',
    keywords: ['Machine Learning', 'Statistical Learning Theory', 'Empirical Risk Minimization', 'Support Vector Machines', 'Kernel Methods', 'Neural Networks and Backpropagation', 'Convex Optimization', 'Dimensionality Reduction'],
    refPath: 'publishing/drafts/computer-science-machine-learning/references.json'
  },
  {
    slug: 'computer-graphics',
    title: 'Computer Graphics',
    subtitle: 'Coordinate Transformations, Rasterization, Shading Models, Ray Tracing, GPU Pipelines & Physically Based Rendering',
    seoTitle: 'Computer Graphics: Transformations, Shading, Ray Tracing, GPU Pipelines & PBR | OpenSTEM Library',
    badgeCredits: 'Computer graphics core',
    courseCodes: ['CS 350', 'CS 450'],
    searchPlaceholder: 'Search affine transformations, homogeneous coordinates, perspective projection frustum, Bresenham line algorithm, Barycentric coordinates, rasterization, Z-buffer hidden surface removal, Blinn-Phong shading, texture coordinates mipmapping, ray-sphere intersection, BVH tree traversal, rendering equation, Monte Carlo path tracing…',
    probSecTitle: 'Step-by-Step Computer Graphics Solutions',
    description: 'Comprehensive university textbook covering 2D and 3D affine transformations, homogeneous coordinates, viewing and perspective projection matrices, line and polygon rasterization (Bresenham), depth buffering (Z-buffer), Blinn-Phong illumination, texture mapping, programmable shader pipelines, recursive ray tracing, acceleration hierarchies (BVH), and physically based rendering with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university computer graphics courses. Eight units with exactly three solved questions per unit and 8 interactive simulations illustrating affine transform matrices, pinhole camera projections, rasterization interpolation, and specular lighting calculations. Numerical checks and an editorial review support this edition.',
    keywords: ['Computer Graphics', 'Coordinate Transformations', 'Homogeneous Coordinates', 'Perspective Projection', 'Rasterization Pipelines', 'Blinn-Phong Illumination', 'Ray Tracing and BVH', 'Physically Based Rendering'],
    refPath: 'publishing/drafts/computer-science-computer-graphics/references.json'
  },
  {
    slug: 'human-computer-interaction',
    title: 'Human-Computer Interaction',
    subtitle: 'Human Cognition, Interaction Models, Usability Principles, Prototyping, Accessibility & Empirical Evaluation',
    seoTitle: 'Human-Computer Interaction: Cognitive Models, Usability Heuristics, Interaction Design & Evaluation | OpenSTEM Library',
    badgeCredits: 'Human-computer interaction core',
    courseCodes: ['CS 370', 'CS 470'],
    searchPlaceholder: 'Search human perception limits, mental models, Gulf of Execution and Evaluation, Norman action cycle, Fitts law index of difficulty, Hick-Hyman choice reaction time, Nielsen usability heuristics, low-fidelity paper prototyping, cognitive walkthrough, WCAG accessibility standards, screen reader compatibility, usability study power analysis…',
    probSecTitle: 'Step-by-Step Human-Computer Interaction Solutions',
    description: 'Comprehensive university textbook covering cognitive psychology of interaction, human sensory limits, mental models, Norman\'s action cycle, Fitts\'s law, Hick-Hyman law, Nielsen\'s usability heuristics, low and high fidelity prototyping, universal design, WCAG accessibility standards, empirical usability testing, qualitative think-aloud protocols, and statistical user study analysis with 24 solved questions and 8 interactive simulations.',
    editorialNote: '<strong>About this textbook.</strong> Original English teaching material for university human-computer interaction courses. Eight units with exactly three solved questions per unit and 8 interactive simulations illustrating Fitts pointing latency, Hick choice time, Nielsen heuristic sample sizes, and error occurrence distributions. Numerical checks and an editorial review support this edition.',
    keywords: ['Human-Computer Interaction', 'Cognitive Psychology in Computing', 'Fitts Law and Hick Law', 'Norman Action Cycle', 'Usability Heuristics', 'Interaction Design Prototyping', 'Accessibility and WCAG', 'Empirical User Testing'],
    refPath: 'publishing/drafts/computer-science-human-computer-interaction/references.json'
  }
];

const templateHtml = fs.readFileSync(
  path.join(groupedRoot, 'computer-science', 'programming-fundamentals', 'programming-fundamentals.html'),
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

  const appCss = d.querySelector('link[href*="programming-fundamentals.css"]');
  if (appCss) appCss.href = `${cfg.slug}.css?v=20261024_academic`;

  const dataScript = d.querySelector('script[src*="programming-fundamentals-data.js"]');
  if (dataScript) dataScript.src = `${cfg.slug}-data.js`;

  const simsScript = d.querySelector('script[src*="programming-fundamentals-sims.js"]');
  if (simsScript) simsScript.src = `${cfg.slug}-sims.js`;

  const bookTitleEl = d.getElementById('book-title');
  if (bookTitleEl) bookTitleEl.textContent = cfg.title;

  const badgeEl = d.querySelector('.badge');
  if (badgeEl) badgeEl.textContent = 'Free Interactive Textbook';

  const creditsEl = d.querySelector('.credits');
  if (creditsEl) creditsEl.textContent = cfg.badgeCredits;

  const searchInput = d.getElementById('search-input');
  if (searchInput) searchInput.placeholder = cfg.searchPlaceholder;

  const probSec = d.getElementById('problems-sec-title');
  if (probSec) probSec.textContent = cfg.probSecTitle;

  const edNote = d.getElementById('editorial-note');
  if (edNote) edNote.innerHTML = cfg.editorialNote;

  const curLink = d.getElementById('curriculum-source-link');
  if (curLink) {
    curLink.href = 'https://openstemlibrary.com/curriculum/computer-science';
    curLink.textContent = 'OpenSTEM University Computer Science Curriculum Framework';
  }

  // Update Breadcrumb and Book schemas
  const schemas = d.querySelectorAll('script[type="application/ld+json"]');
  schemas.forEach(s => {
    try {
      const data = JSON.parse(s.textContent);
      if (data['@type'] === 'BreadcrumbList') {
        data.itemListElement = [
          {
            '@type': 'ListItem',
            'position': 1,
            'name': 'OpenSTEM Library',
            'item': 'https://openstemlibrary.com/'
          },
          {
            '@type': 'ListItem',
            'position': 2,
            'name': 'Computer Science',
            'item': 'https://openstemlibrary.com/#computer-science'
          },
          {
            '@type': 'ListItem',
            'position': 3,
            'name': cfg.title,
            'item': 'https://openstemlibrary.com/' + cfg.slug
          }
        ];
        s.textContent = JSON.stringify(data, null, 2);
      } else if (data['@type'] === 'Book' || (Array.isArray(data['@graph']) && data['@graph'].some(x => x['@type'] === 'Book'))) {
        const bookObj = data['@type'] === 'Book' ? data : data['@graph'].find(x => x['@type'] === 'Book');
        bookObj.name = cfg.title;
        bookObj.description = cfg.description;
        bookObj.url = 'https://openstemlibrary.com/' + cfg.slug;
        bookObj.keywords = cfg.keywords.join(', ');
        s.textContent = JSON.stringify(data, null, 2);
      }
    } catch (e) {}
  });

  // Inject Course schema
  const courseSchema = d.createElement('script');
  courseSchema.type = 'application/ld+json';
  courseSchema.textContent = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'Course',
    'name': cfg.title,
    'description': cfg.description,
    'provider': {
      '@type': 'EducationalOrganization',
      'name': 'OpenSTEM Library',
      'url': 'https://openstemlibrary.com'
    },
    'courseCode': cfg.courseCodes.join(', '),
    'educationalLevel': 'Undergraduate',
    'hasCourseInstance': {
      '@type': 'CourseInstance',
      'courseMode': 'online',
      'courseWorkload': 'PT80H'
    }
  }, null, 2);
  d.head.appendChild(courseSchema);

  // Update references in footer
  const refList = d.getElementById('reference-sources-list');
  if (refList) {
    refList.replaceChildren();
    const refData = JSON.parse(fs.readFileSync(path.join(root, cfg.refPath), 'utf8'));
    for (const src of refData.sources) {
      const li = d.createElement('li');
      li.className = 'reference-source-item';
      const a = d.createElement('a');
      a.className = 'reference-institution';
      a.href = src.url;
      a.textContent = src.institution;
      const span = d.createElement('span');
      span.className = 'reference-role';
      span.textContent = ' — ' + src.role;
      li.appendChild(a);
      li.appendChild(span);
      refList.appendChild(li);
    }
  }

  // Update prerequisite links
  const prereqEl = d.getElementById('prerequisite-courses-list');
  if (prereqEl) {
    prereqEl.replaceChildren();
    const prereqs = [
      { name: 'Programming Fundamentals', url: 'https://openstemlibrary.com/programming-fundamentals' },
      { name: 'Data Structures', url: 'https://openstemlibrary.com/data-structures' },
      { name: 'Algorithms', url: 'https://openstemlibrary.com/algorithms' },
      { name: 'Discrete Structures for Computer Science', url: 'https://openstemlibrary.com/discrete-structures-for-computer-science' }
    ];
    for (const p of prereqs) {
      const a = d.createElement('a');
      a.className = 'prerequisite-chip';
      a.href = p.url;
      a.textContent = p.name;
      prereqEl.appendChild(a);
    }
  }

  // Update syllabus units in syllabus section
  const syllabusList = d.getElementById('course-syllabus-list');
  if (syllabusList) {
    syllabusList.replaceChildren();
  }

  // Evaluate book data and startApp
  const bookDataJs = fs.readFileSync(path.join(groupedRoot, 'computer-science', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
  w.eval(bookDataJs);
  const appJs = fs.readFileSync(path.join(root, 'app.js'), 'utf8').split('\nif (document.readyState === "loading")')[0];
  w.eval(appJs);
  w.startApp();

  d.getElementById('unit-title').textContent = w.COURSE_DATA.units[0].title;
  d.getElementById('unit-desc').textContent = w.COURSE_DATA.units[0].leadSummary || '';
  d.querySelectorAll('.mobile-chapters-button,.chapter-menu-close,.chapter-menu-backdrop').forEach(el => el.remove());
  d.querySelector('.sidebar').removeAttribute('id');

  const targetDir = path.join(groupedRoot, 'computer-science', cfg.slug);
  fs.mkdirSync(targetDir, { recursive: true });
  const targetHtmlPath = path.join(targetDir, cfg.slug + '.html');
  fs.writeFileSync(targetHtmlPath, dom.serialize(), 'utf8');
  w.close();
  console.log(`Generated landing page: ${targetHtmlPath}`);
}

// Update departments-data.js
const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root, 'departments-data.js'), 'utf8'), ctx);
const catalog = ctx.window.LIBRARY_CATALOG;
const dept = catalog.departments.find(d => d.id === 'computer-science');

for (const cfg of bookConfigs) {
  dept.courses = dept.courses.filter(b => b.id !== cfg.slug);
  const dataJsText = fs.readFileSync(path.join(groupedRoot, 'computer-science', cfg.slug, `${cfg.slug}-data.js`), 'utf8');
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
console.log(`Updated departments-data.js. Total Computer Science courses: ${dept.courses.length}`);

// Update publishing/book-queue.json
const queue = JSON.parse(fs.readFileSync(path.join(root, 'publishing/book-queue.json'), 'utf8'));
const queueDept = queue.departments.find(d => d.id === 'computer-science');
const now = new Date().toISOString();

for (const cfg of bookConfigs) {
  const qBook = queueDept.books.find(b => b.id === 'computer-science-' + cfg.slug);
  if (qBook) {
    qBook.status = 'published';
    qBook.published_at = now;
    qBook.content_file = cfg.slug + '-data.js';
    qBook.url = cfg.slug + '.html';
    qBook.qa_report = `publishing/qa/computer-science-${cfg.slug}.json`;
    console.log(`Updated book-queue.json: ${qBook.id} -> published`);
  }
}

fs.writeFileSync(
  path.join(root, 'publishing/book-queue.json'),
  JSON.stringify(queue, null, 2) + '\n',
  'utf8'
);
console.log('Updated publishing/book-queue.json successfully.');
