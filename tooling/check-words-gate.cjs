const fs = require('fs'), vm = require('vm');
const source = fs.readFileSync('sample-surveys-and-sampling-theory-data.js', 'utf8');
const context = { window: {} };
vm.createContext(context);
vm.runInContext(source, context);
const data = context.window.COURSE_DATA;

function prose(text) {
  return String(text || '').replace(/```[\s\S]*?```/g,' ').replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi,' ').replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi,' ')
    .replace(/\$\$[\s\S]*?\$\$/g,' ').replace(/\$[^$\n]+\$/g,' ').replace(/\\\[[\s\S]*?\\\]/g,' ').replace(/\\\([\s\S]*?\\\)/g,' ')
    .replace(/<[^>]*>/g,' ').replace(/&[a-z0-9#]+;/gi,' ').replace(/\[[^\]]*\]\([^)]*\)/g,m=>m.slice(1,m.indexOf(']')));
}
const count = text => (prose(text).match(/\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b/g) || []).length;
let total = 0;
data.units.forEach((u, i) => {
  let w = 0;
  for (const s of u.sections) w += count(s.content);
  for (const p of u.problems) w += count(p.question) + (p.steps || []).reduce((sum, s) => sum + count(s.explanation), 0);
  console.log(`Unit ${i+1}: ${w} words`);
  total += w;
});
console.log('TOTAL SUBSTANTIVE PROSE WORDS:', total);
