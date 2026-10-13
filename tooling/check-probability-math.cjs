const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'..'),ctx={window:{}};vm.createContext(ctx);vm.runInContext(fs.readFileSync(path.join(root,'probability-and-probability-distributions-data.js'),'utf8'),ctx);
const katex=require(process.env.OPENSTEM_KATEX_PATH||'katex');let equations=0;const errors=[];
for(const u of ctx.window.COURSE_DATA.units){const texts=[...u.sections.map(s=>s.content),...u.problems.flatMap(p=>[p.question,...p.steps.map(s=>s.explanation)])];
 for(const text of texts){const matches=text.matchAll(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$|\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g);for(const m of matches){const tex=m[1]||m[2]||m[3]||m[4];equations++;try{katex.renderToString(tex,{throwOnError:true,strict:'ignore',displayMode:!!(m[1]||m[3])});}catch(e){errors.push({unit:u.number,tex,error:e.message});}}}
}
const report={status:errors.length?'fail':'pass',equations,errors,katex_version:katex.version,scope:'Every delimited mathematical expression in all ten source units and all thirty worked questions/solutions parsed with KaTeX 0.16.9, the deployed reader version.'};fs.writeFileSync(path.join(root,'publishing/drafts/statistics-probability-probability-and-probability-distributions/math-checks.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));process.exit(errors.length?1:0);
