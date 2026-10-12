/* Structural publication gate. Academic correctness still needs documented review.
   Usage: node tooling/check-new-book.cjs <queue-book-id> */
const fs = require('node:fs'), path = require('node:path'), vm = require('node:vm'), crypto = require('node:crypto');
const root = path.resolve(__dirname, '..');
const read = p => fs.readFileSync(path.join(root,p), 'utf8');
const q = JSON.parse(read('publishing/book-queue.json'));
const id = process.argv[2];
const dept = q.departments.find(d => d.books.some(b => b.id === id));
const book = dept?.books.find(b => b.id === id);
if (!book) { console.error('Supply a valid queue book ID'); process.exit(1); }
const failures = [], units = [];
function localFile(p) {
  if (!p || path.isAbsolute(p) || !path.resolve(root,p).startsWith(root+path.sep)) throw Error('Invalid repository path: '+p);
  return read(p);
}
// Count authored English prose, excluding markup, formulas and code; no navigation or metadata.
function prose(text) {
  return String(text || '').replace(/```[\s\S]*?```/g,' ').replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi,' ').replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi,' ')
    .replace(/\$\$[\s\S]*?\$\$/g,' ').replace(/\$[^$\n]+\$/g,' ').replace(/\\\[[\s\S]*?\\\]/g,' ').replace(/\\\([\s\S]*?\\\)/g,' ')
    .replace(/<[^>]*>/g,' ').replace(/&[a-z0-9#]+;/gi,' ').replace(/\[[^\]]*\]\([^)]*\)/g,m=>m.slice(1,m.indexOf(']')));
}
const normalized = text => prose(text).toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
const count = text => (prose(text).match(/\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b/g) || []).length;
try {
  const state=JSON.parse(read('publishing/run-state.json'));
  const today=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Dhaka',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
  const consumesSlot=p=>!(p.mode==='manual_first_book' && p.book_id==='statistics-probability-introduction-to-statistics');
  const history=state.publications || [];
  const hasScheduledToday=history.some(p=>p.local_date===today && consumesSlot(p));
  const lastIsExempt=history.some(p=>p.book_id===state.last_published_book_id && p.local_date===today && !consumesSlot(p));
  if(hasScheduledToday || (state.last_successful_publication_date===today && !lastIsExempt))failures.push('A scheduled book has already been published on this Bangladesh calendar date');
  if(state.current_stage==='publication_pending')failures.push('Resolve the pending deployment before preparing another publication');
  if(book.status==='published')failures.push('This queue book is already published');
  if (dept.curriculum_status !== 'selected' || !dept.sources.length || book.curriculum_status !== 'mapped') failures.push('Official curriculum mapping incomplete');
  const source = localFile(book.content_file);
  const context = {window:{}}; vm.createContext(context); vm.runInContext(source,context,{timeout:1500});
  const data = context.window.COURSE_DATA;
  if (!data || !Array.isArray(data.units)) throw Error('Missing COURSE_DATA.units');
  if (data.units.length < 7 || data.units.length > 10) failures.push('Book must have 7–10 units');
  const seen = new Set(); let total = 0;
  data.units.forEach((u,i) => {
    const sections = u.sections || [], problems = u.problems || [];
    if (sections.length < 3) failures.push(`Unit ${i+1}: fewer than three sections`);
    const questionRule=q.book_requirements?.worked_questions_per_unit || {minimum:3,maximum:3};
    if (problems.length < questionRule.minimum || problems.length > questionRule.maximum) failures.push(`Unit ${i+1}: expected ${questionRule.minimum === questionRule.maximum ? questionRule.minimum : questionRule.minimum+'–'+questionRule.maximum} fully worked questions`);
    let words = 0;
    for (const s of sections) {
      const n=normalized(s.content);
      if (!n) failures.push(`Unit ${i+1}: empty section`);
      if (n && seen.has(n)) failures.push(`Unit ${i+1}: duplicate section`);
      if(n)seen.add(n); words += count(s.content);
      if (/\b(TODO|TBD|lorem ipsum)\b/i.test(s.content || '')) failures.push(`Unit ${i+1}: unfinished placeholder`);
    }
    for (const p of problems) {
      if (!p.question || !Array.isArray(p.steps) || p.steps.length < 2 || p.steps.some(s => !s.explanation)) failures.push(`Unit ${i+1}: incomplete worked problem ${p.id || ''}`);
      const n=normalized(p.question); if(n && seen.has(n))failures.push(`Unit ${i+1}: duplicate problem`); if(n)seen.add(n);
      words += count(p.question) + (p.steps || []).reduce((sum,s)=>sum+count(s.explanation),0);
    }
    total += words; units.push({unit:i+1,title:u.title,words,worked_problems:problems.length});
  });
  if (total < book.minimum_words) failures.push(`Substantive prose ${total} < ${book.minimum_words}`);
  const qa = JSON.parse(localFile(book.qa_report));
  const hash = crypto.createHash('sha256').update(source).digest('hex');
  if (qa.content_sha256 !== hash) failures.push('QA does not match current content hash');
  for (const key of ['academic_review','curriculum_coverage','worked_solutions','originality','simulation_behavior','mobile_reader','static_pages','seo_metadata']) {
    const check=qa.checks?.[key];
    if(check?.status !== 'pass' || typeof check.evidence !== 'string' || check.evidence.trim().length < 30) failures.push('Missing documented check: '+key);
    for(const p of check?.artifacts || []) { if(!localFile(p).trim()) failures.push('Empty check evidence: '+p); }
  }
  if(!Array.isArray(qa.units) || qa.units.length !== data.units.length || qa.units.some(u=>!u.coverage_complete || !u.question_set_checked))failures.push('Unit coverage/question review incomplete');
  const quantitative = dept.id === 'statistics-probability';
  if(quantitative && !qa.checks?.worked_solutions?.artifacts?.length)failures.push('Statistics needs executable answer-check evidence');
  console.log(JSON.stringify({book:id,words:total,units,failures},null,2));
} catch(e) { failures.push(e.message); console.log(JSON.stringify({book:id,failures},null,2)); }
process.exit(failures.length ? 1 : 0);
