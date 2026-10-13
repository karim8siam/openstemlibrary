const fs = require('node:fs');
const path = require('node:path');
const katex = require('katex');

const file = process.argv[2];
if (!file) {
  console.error("Usage: node tooling/check-math-file.cjs <file.md>");
  process.exit(1);
}

const text = fs.readFileSync(file, 'utf8');
const matches = text.matchAll(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$|\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g);

let count = 0;
const errors = [];

for (const m of matches) {
  const tex = m[1] || m[2] || m[3] || m[4];
  count++;
  try {
    katex.renderToString(tex, {
      throwOnError: true,
      strict: 'ignore',
      displayMode: !!(m[1] || m[3])
    });
  } catch (err) {
    errors.push({ tex, error: err.message });
  }
}

console.log(JSON.stringify({ file, count, errorCount: errors.length, errors }, null, 2));
process.exit(errors.length ? 1 : 0);
