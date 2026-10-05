// Generate pre-rendered electrodynamics.html
var units = window.COURSE_DATA.units;

function formatText(text) {
  if (!text) return '';
  let res = text
    .replace(/^####\s+(.*)$/gm, '<h4>$1</h4>')
    .replace(/^###\s+(.*)$/gm, '<h3>$1</h3>')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>');

  let chunks = res.split(/\n\s*\n/);
  return chunks.map(function(chunk) {
    let t = chunk.trim();
    if (!t) return '';
    if (t.startsWith('<h3>') || t.startsWith('<h4>') || t.startsWith('$$') || t.startsWith('<div') || t.startsWith('<ul') || t.startsWith('<ol') || t.startsWith('|')) {
      return t;
    }
    return '<p>' + t + '</p>';
  }).join('\n\n');
}

// 1. Sidebar TOC
var sidebarHtml = '';
units.forEach(function(u, idx) {
  sidebarHtml += '<li class="unit-nav-item ' + (idx === 0 ? 'active' : '') + '" data-unit-index="' + idx + '">';
  sidebarHtml += '<span class="unit-nav-num">Ch.' + u.number + '</span>';
  sidebarHtml += '<span class="unit-nav-text">' + u.title + '</span></li>';
});

// 2. Unit 0 sections
var u0 = units[0];
var sectionsHtml = '';
u0.sections.forEach(function(sec) {
  sectionsHtml += '<section class="textbook-section-card" id="sec-' + sec.secNumber.replace('.', '-') + '">';
  sectionsHtml += '<header class="sec-header"><h3 class="sec-title"><span class="sec-num">§' + sec.secNumber + '</span><span>' + sec.heading + '</span></h3></header>';
  sectionsHtml += '<div class="sec-content">' + formatText(sec.content) + '</div></section>';
});

// 3. Unit 0 problems
var problemsHtml = '';
u0.problems.forEach(function(prob, idx) {
  var diffClass = prob.difficulty === 'Easy' ? 'diff-easy' : (prob.difficulty === 'Medium' ? 'diff-medium' : 'diff-hard');
  problemsHtml += '<div class="problem-card">';
  problemsHtml += '<div class="problem-header"><div class="problem-title-box"><span class="diff-badge ' + diffClass + '">' + prob.difficulty + '</span><strong>Example 1.' + (idx+1) + ': ' + prob.title + '</strong></div></div>';
  problemsHtml += '<div class="problem-question-box">' + prob.question.split('\n').join('<br>') + '</div>';
  problemsHtml += '<button class="solution-toggle-btn" id="btn-sol-' + prob.id + '">👁️ Reveal Complete Derivation & Solution</button>';
  problemsHtml += '<div class="solution-content" id="sol-content-' + prob.id + '">';
  prob.steps.forEach(function(step) {
    problemsHtml += '<div class="solution-step"><div class="step-title">' + step.stepName + '</div><div class="step-math">$$' + step.math + '$$</div><div class="step-explanation">' + formatText(step.explanation) + '</div></div>';
  });
  problemsHtml += '</div></div>';
});

print('---SPLIT_SIDEBAR---');
print(sidebarHtml);
print('---SPLIT_SECTIONS---');
print(sectionsHtml);
print('---SPLIT_PROBLEMS---');
print(problemsHtml);
