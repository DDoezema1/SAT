// Review round 2: compile every math snippet in the bank with KaTeX (strict, throw on error).
const katex = require("katex");
global.window = {};
require("../app/js/questions.js");
let n = 0, bad = 0;
const re = /\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g;
for (const q of window.SAT_QUESTIONS) {
  const fields = [q.stem, q.explain, q.tip, ...(q.choices || [])];
  for (const f of fields) {
    for (const m of (f || "").matchAll(re)) {
      n++;
      try { katex.renderToString(m[1] ?? m[2], { throwOnError: true, displayMode: !!m[2], strict: "error" }); }
      catch (e) { bad++; console.log(`${q.id}: ${e.message}`); }
    }
  }
}
console.log(`${n} math snippets checked, ${bad} errors`);
process.exit(bad ? 1 : 0);
