const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { JSDOM } = require('jsdom');

const root = path.resolve(__dirname, '..');
const catalog = { window: {} };
vm.createContext(catalog);
vm.runInContext(fs.readFileSync(path.join(root, 'departments-data.js'), 'utf8'), catalog);
const books = catalog.window.LIBRARY_CATALOG.departments.flatMap(d =>
  d.courses.filter(c => c.status === 'AVAILABLE').map(c => ({ ...c, deptId: d.id, deptName: d.name }))
);

console.log(`Auditing simulations across all ${books.length} available books in 10 departments...`);

const results = {
  tested: 0,
  syntaxErrors: [],
  runtimeErrors: []
};

for (const book of books) {
  // Find book folder
  const deptDir = path.join(root, 'src', 'subjects', book.deptId);
  const bookDir = path.join(deptDir, book.id);
  if (!fs.existsSync(bookDir)) continue;

  const files = fs.readdirSync(bookDir);
  const simFiles = files.filter(f => f.endsWith('.js') && (f.includes('-sims') || f.includes('-sim.')));

  if (simFiles.length === 0) {
    // Check if there are other JS files like -bayes.js or if simulations are in HTML
    continue;
  }

  for (const sf of simFiles) {
    results.tested++;
    const fullPath = path.join(bookDir, sf);
    const code = fs.readFileSync(fullPath, 'utf8');

    // Syntax check
    try {
      new vm.Script(code);
    } catch (err) {
      results.syntaxErrors.push({ book: book.id, file: sf, error: err.message });
      continue;
    }

    // Test in JSDOM
    const dom = new JSDOM(`<!DOCTYPE html><html><body data-chapter-index="0"><div id="sim-container"></div><div id="sim-container-test"></div></body></html>`, {
      runScripts: 'dangerously',
      url: `https://openstemlibrary.com/${book.url.replace(/\.html$/, '')}`
    });

    try {
      dom.window.eval(code);
      if (dom.window.SimulationEngine && typeof dom.window.SimulationEngine.initSimulation === 'function') {
        // Try calling initSimulation for unit 1
        dom.window.SimulationEngine.initSimulation('sim-container');
      }
    } catch (err) {
      results.runtimeErrors.push({ book: book.id, file: sf, error: err.message });
    }
  }
}

console.log(`Test results: ${results.tested} simulation files tested.`);
console.log(`Syntax errors: ${results.syntaxErrors.length}`);
if (results.syntaxErrors.length > 0) {
  console.log(JSON.stringify(results.syntaxErrors, null, 2));
}
console.log(`Runtime errors: ${results.runtimeErrors.length}`);
if (results.runtimeErrors.length > 0) {
  console.log(JSON.stringify(results.runtimeErrors, null, 2));
}
