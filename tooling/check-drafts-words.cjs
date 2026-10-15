const fs = require('fs');
const path = require('path');

const bookDir = process.argv[2] || 'publishing/drafts/statistics-probability-statistical-computing-with-python-and-r';

function prose(text) {
  return String(text || '').replace(/```[\s\S]*?```/g, ' ')
    .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi, ' ')
    .replace(/\$\$[\s\S]*?\$\$/g, ' ')
    .replace(/\$[^$\n]+\$/g, ' ')
    .replace(/\\\[[\s\S]*?\\\]/g, ' ')
    .replace(/\\\([\s\S]*?\\\)/g, ' ')
    .replace(/<[^>]*>/g, ' ')
    .replace(/&[a-z0-9#]+;/gi, ' ')
    .replace(/\[[^\]]*\]\([^)]*\)/g, m => m.slice(1, m.indexOf(']')));
}

const count = text => (prose(text).match(/\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b/g) || []).length;

let grandTotal = 0;
for (let i = 1; i <= 8; i++) {
  const p = path.join(bookDir, `unit-${i}.md`);
  if (fs.existsSync(p)) {
    const raw = fs.readFileSync(p, 'utf8');
    const c = count(raw);
    console.log(`Unit ${i}: ${c} words`);
    grandTotal += c;
  } else {
    console.log(`Unit ${i}: [MISSING]`);
  }
}
console.log(`-----------------------------------`);
console.log(`GRAND TOTAL WORDS: ${grandTotal}`);
console.log(`TARGET (>= 50,000): ${grandTotal >= 50000 ? 'PASS ✅' : 'FAIL ❌ (needs ' + (50000 - grandTotal) + ' more)'}`);
