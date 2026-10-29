const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const meDir = path.join(__dirname, '../src/subjects/mechanical-engineering');
const books = fs.readdirSync(meDir, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name);

console.log(`Found ${books.length} Mechanical Engineering books to test simulations for.`);

let totalTests = 0;
let errors = [];

for (const book of books) {
  const simFile = path.join(meDir, book, `${book}-sims.js`);
  if (!fs.existsSync(simFile)) {
    errors.push({ book, error: `Missing sims file: ${simFile}` });
    continue;
  }

  const simCode = fs.readFileSync(simFile, 'utf8');

  for (let unit = 1; unit <= 8; unit++) {
    totalTests++;
    const consoleLogs = [];

    const dom = new JSDOM(`<!DOCTYPE html><html><body data-chapter-index="${unit - 1}"><div id="sim-container"></div></body></html>`, {
      runScripts: 'dangerously',
      url: `https://openstemlibrary.com/${book}-chapter-${unit}.html`
    });

    const { window } = dom;

    // Attach custom logger to window.console
    const origWarn = window.console.warn;
    const origError = window.console.error;
    window.console.warn = (...args) => {
      const msg = args.join(' ');
      if (msg.includes('Sim init error') || msg.includes('error') || msg.includes('Error')) {
        consoleLogs.push(`WARN: ${msg}`);
      }
      origWarn.apply(window.console, args);
    };
    window.console.error = (...args) => {
      consoleLogs.push(`ERROR: ${args.join(' ')}`);
      origError.apply(window.console, args);
    };

    try {
      // Execute the sim code in this window
      window.eval(simCode);

      if (!window.SimulationEngine || typeof window.SimulationEngine.initSimulation !== 'function') {
        errors.push({ book, unit, error: 'window.SimulationEngine.initSimulation is not defined' });
        continue;
      }

      window.SimulationEngine.initSimulation('sim-container');

      const cards = window.document.querySelectorAll('.me-sim-card');
      if (cards.length === 0) {
        errors.push({ book, unit, error: 'No .me-sim-card elements rendered' });
      }

      // Check card contents and trigger inputs
      cards.forEach((card, idx) => {
        const inputs = card.querySelectorAll('input, select');
        inputs.forEach(input => {
          // Trigger input event
          const evt = new window.Event('input', { bubbles: true });
          input.dispatchEvent(evt);
        });

        // Check if outputs have NaN or undefined
        const outputs = card.querySelectorAll('output');
        outputs.forEach(out => {
          if (out.textContent.includes('NaN') || out.textContent.includes('undefined')) {
            errors.push({ book, unit, error: `Output in card ${idx + 1} has invalid value: "${out.textContent}"` });
          }
        });
      });

      if (consoleLogs.length > 0) {
        errors.push({ book, unit, error: `Console logs: ${consoleLogs.join('; ')}` });
      }
    } catch (err) {
      errors.push({ book, unit, error: `Execution exception: ${err.stack || err.message}` });
    }
  }
}

console.log(`Completed ${totalTests} simulation test runs across all 20 books.`);
if (errors.length > 0) {
  console.error(`Found ${errors.length} simulation errors:`);
  errors.forEach(e => console.error(JSON.stringify(e, null, 2)));
  process.exit(1);
} else {
  console.log('ALL Mechanical Engineering simulations passed 100% cleanly without errors!');
}
