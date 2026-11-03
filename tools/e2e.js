// End-to-end test: drives the real app in Chromium.
// Usage: node tools/e2e.js [screenshotDir]   (serves ./app on a local port)
const { chromium } = require("playwright");
const http = require("http");
const fs = require("fs");
const path = require("path");
const assert = require("assert");

const ROOT = path.join(__dirname, "..", "app");
const SHOTS = process.argv[2];
const TYPES = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2" };

const server = http.createServer((req, res) => {
  const p = path.join(ROOT, decodeURIComponent(req.url.split("?")[0]).replace(/^\/$/, "/index.html"));
  if (!p.startsWith(ROOT) || !fs.existsSync(p)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "Content-Type": TYPES[path.extname(p)] || "application/octet-stream" });
  fs.createReadStream(p).pipe(res);
});

(async () => {
  await new Promise((r) => server.listen(0, r));
  const url = `http://localhost:${server.address().port}/`;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1366, height: 860 } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  page.on("console", (m) => { if (m.type() === "error" && !/desmos/i.test(m.text())) errors.push(m.text()); });
  page.on("dialog", (d) => d.accept());
  // The sandbox that runs this test can't reach desmos.com, so serve a stand-in that
  // implements the parts of the Desmos API the app uses. Pass --real-desmos to skip.
  const calls = [];
  if (!process.argv.includes("--real-desmos")) {
    await page.route(/desmos\.com\/api/, (route) => route.fulfill({ contentType: "text/javascript", body: `
      window.Desmos = { GraphingCalculator(el, opts) {
        window.__desmosCalls = (window.__desmosCalls || []).concat(["create:" + JSON.stringify(opts)]);
        el.innerHTML = '<div class="dcg-container" style="height:100%;background:#f7f9fc;display:grid;place-items:center;color:#666">[Desmos calculator stand-in]</div>';
        return { resize() { window.__desmosCalls.push("resize"); }, destroy() { window.__desmosCalls.push("destroy"); } };
      } };` }));
  }
  const shot = async (name) => { if (SHOTS) await page.screenshot({ path: path.join(SHOTS, name + ".png") }); };
  const step = (s) => console.log("  - " + s);

  await page.goto(url);
  await page.fill("#nameIn", "Test Student");
  await page.press("#nameIn", "Tab");
  await shot("01-home");

  // Answer the current question. correct=true picks the key; false picks a wrong answer.
  async function answer(correct) {
    const id = await page.evaluate(() => {
      const s = JSON.parse(localStorage.getItem("satMathPractice.v1")).active;
      return s.items[s.idx].id;
    });
    const q = await page.evaluate((id) => window.SAT_QUESTIONS.find((q) => q.id === id), id);
    if (q.type === "mc") {
      const pick = correct ? q.answer : "ABCD".replace(q.answer, "")[0];
      await page.click(`.choice[data-o="${pick}"]`);
    } else {
      let v = q.answer;
      if (v.length > (v.startsWith("-") ? 6 : 5)) v = String(eval(v)).slice(0, v.startsWith("-") ? 6 : 5);
      await page.fill("#sprIn", correct ? v : "99999");
    }
    return q;
  }

  // ---------------------------------------------------------------- full section
  step("full section: module 1");
  await page.click("#fullBtn");
  assert.strictEqual(await page.textContent("#secTitle"), "Section 1, Module 1: Math");
  assert.match(await page.textContent("#timer"), /^3[45]:\d\d$/);
  assert.match(await page.textContent("#navBtn"), /Question 1 of 22/);
  let sawSpr = false, sawMc = false;
  for (let i = 0; i < 22; i++) {
    const q = await answer(i < 16);
    if (q.type === "spr" && !sawSpr) { sawSpr = true; await shot("03-spr-question"); }
    if (q.type === "mc" && !sawMc) { sawMc = true; await shot("02-mc-question"); }
    if (i === 2) {
      await page.click("#markBtn");
      assert.match(await page.textContent("#markBtn"), /Marked/);
    }
    await page.click("#nextBtn");
  }
  assert.match(await page.textContent("#qscroll"), /Check Your Work/);
  assert.strictEqual(await page.locator(".grid .gbox.ans").count(), 22);
  assert.strictEqual(await page.locator(".grid .gbox.flag").count(), 1);
  await shot("04-check-your-work");
  await page.click("#nextBtn");               // submit (dialog auto-accepted)
  await page.waitForSelector("#beginM2");
  const route = await page.evaluate(() => JSON.parse(localStorage.getItem("satMathPractice.v1")).active.route);
  assert.strictEqual(route, "m2hard", "16/22 correct must route to the harder module");
  step("routed to harder module 2 after 16/22");
  await page.click("#beginM2");
  assert.strictEqual(await page.textContent("#secTitle"), "Section 1, Module 2: Math");

  // calculator
  await page.click("#calcBtn");
  await page.waitForTimeout(4000);
  const desmosOk = await page.evaluate(() => !!document.querySelector("#desmos .dcg-container, #desmos .dcg-calculator-api-container"));
  if (!process.argv.includes("--real-desmos")) {
    assert(desmosOk, "Desmos stand-in should mount");
    await page.click("#calcWide");
    assert(await page.evaluate(() => document.querySelector("#calcPanel").classList.contains("wide")));
    assert((await page.evaluate(() => window.__desmosCalls)).includes("resize"));
  }
  const desmosMsg = await page.textContent("#desmos");
  step(desmosOk ? "Desmos calculator loaded" : "Desmos unavailable here; fallback message shown: " + /couldn't load/.test(desmosMsg));
  assert(desmosOk || /couldn't load/.test(desmosMsg));
  await shot("05-calculator");
  await page.click("#calcClose");

  // reference + navigator
  await page.click("#refBtn");
  assert.match(await page.textContent(".pop"), /Pythagorean/);
  await shot("06-reference");
  await page.click(".pop .close");
  await page.click("#navBtn");
  assert.strictEqual(await page.locator("#overlay .grid .gbox").count(), 22);
  await shot("07-navigator");
  await page.click("#overlay .gbox[data-i='5']");
  assert.match(await page.textContent("#navBtn"), /Question 6 of 22/);

  // module 2: answer half, leave rest blank, then submit via review page
  for (let i = 0; i < 6; i++) { await answer(i % 2 === 0); await page.click("#nextBtn"); }
  await page.click("#navBtn");
  await page.click("#toReview");
  await page.click("#nextBtn");
  await page.waitForSelector(".bigscore");
  const score = +(await page.textContent(".bigscore"));
  step(`results page: estimated score ${score}`);
  assert(score >= 200 && score <= 800);
  assert.strictEqual(await page.locator(".qitem").count(), 44);
  await page.click(".qitem summary");
  await shot("08-results");

  // ---------------------------------------------------------------- practice with feedback
  step("adaptive practice with feedback");
  await page.click("#homeBtn");
  await page.selectOption("#pLen", "10");
  await page.click("#practiceBtn");
  assert.match(await page.textContent("#nextBtn"), /Check Answer/);
  await answer(false);
  await page.click("#nextBtn");
  await page.waitForSelector(".feedback.no");
  assert.match(await page.textContent(".feedback"), /Not quite/);
  await shot("09-practice-feedback");
  await page.click("#nextBtn");
  for (let i = 1; i < 10; i++) {
    await answer(true);
    await page.click("#nextBtn");
    await page.waitForSelector(".feedback.ok");
    await page.click("#nextBtn");
  }
  await page.waitForSelector(".bigscore");
  assert.strictEqual((await page.textContent(".bigscore")).trim(), "9/10");
  step("practice results 9/10");

  // ---------------------------------------------------------------- timed set (11 questions, speed pace, coach)
  step("timed set: 11 questions at speed pace with pacing coach");
  await page.click("#homeBtn");
  assert.match(await page.textContent(".hero p"), /Starting point: 740/);
  await page.selectOption("#sLen", "11");
  await page.selectOption("#sPace", "speed");
  assert.match(await page.textContent("#setTime"), /14:40/);
  await page.click("#setBtn");
  assert.match(await page.textContent("#navBtn"), /Question 1 of 11/);
  assert.match(await page.textContent("#timer"), /^14:[34]\d$/);
  await page.waitForTimeout(1200);
  assert.match(await page.textContent("#pace"), /on pace/);
  assert.match(await page.textContent("#watch"), /⏱ 0:0\d \/ 1:20/);
  const setDiffs = await page.evaluate(() => JSON.parse(localStorage.getItem("satMathPractice.v1")).active.items.map((i) => window.SAT_QUESTIONS.find((q) => q.id === i.id).diff));
  assert(!setDiffs.includes(1), "a 740 student gets no medium questions in a timed set");
  await shot("13-timed-set-coach");
  for (let i = 0; i < 11; i++) {
    await answer(i !== 4);
    if (i === 2) { await page.click("#calcBtn"); await page.click("#calcClose"); }   // Desmos use gets tracked
    await page.click("#nextBtn");
  }
  await page.click("#nextBtn");               // submit from Check Your Work
  await page.waitForSelector(".bigscore");
  assert.strictEqual((await page.textContent(".bigscore")).trim(), "10/11");
  assert.match(await page.textContent(".cards"), /Timing[\s\S]*of 14:40[\s\S]*Desmos use/);
  const calcFlag = await page.evaluate(() => JSON.parse(localStorage.getItem("satMathPractice.v1")).sessions.at(-1).modules[0].items[2].calc);
  assert.strictEqual(calcFlag, true, "opening Desmos on a question is recorded");
  await shot("14-timed-set-results");

  // ---------------------------------------------------------------- Desmos drill
  step("Desmos speed drill: calculator auto-opens, hint, feedback");
  await page.click("#homeBtn");
  await page.click("#drillBtn");
  assert(await page.evaluate(() => !document.querySelector("#calcPanel").classList.contains("hidden")), "calculator opens automatically");
  const drillQ = await page.evaluate(() => { const s = JSON.parse(localStorage.getItem("satMathPractice.v1")).active; return window.SAT_QUESTIONS.find((q) => q.id === s.items[0].id); });
  assert(drillQ.desmos, "drill serves Desmos questions");
  await page.click("#hintBtn");
  assert.match(await page.textContent(".qcol"), /Hint:/);
  await shot("15-drill-hint");
  await answer(true);
  await page.click("#nextBtn");
  await page.waitForSelector(".feedback");
  assert.match(await page.textContent(".feedback"), /Desmos strategy/);
  const drillItem = await page.evaluate(() => JSON.parse(localStorage.getItem("satMathPractice.v1")).active.items[0]);
  assert(drillItem.hint && drillItem.calc);
  await page.click("#moreBtn");
  await page.click("#endNow");
  await page.waitForSelector(".bigscore");

  // ---------------------------------------------------------------- trouble spots + playbook
  step("trouble spots and playbook");
  await page.click("#homeBtn");
  assert.match(await page.textContent("body"), /you missed, answered slowly, or needed a hint on/);
  assert(!(await page.isDisabled("#retryBtn")));
  await page.click("#retryBtn");
  const tIds = await page.evaluate(() => { const st = JSON.parse(localStorage.getItem("satMathPractice.v1")); return [st.active.items[0].id, Object.entries(st.items).filter(([, it]) => !it.lastCorrect || it.lastSlow || it.lastHint).map(([id]) => id)]; });
  assert(tIds[1].includes(tIds[0]), "trouble-spot session serves a trouble spot");
  await page.click("#moreBtn");
  await page.click("#saveExit");
  await page.click("#abandonBtn");
  await page.click("#playbookBtn");
  assert.match(await page.textContent(".playbook"), /Regression from a table/);
  await shot("16-playbook");
  await page.click("#homeBtn");

  // ---------------------------------------------------------------- resume
  step("save & resume");
  await page.click("#practiceBtn");
  await answer(true);
  await page.click("#moreBtn");
  await page.click("#saveExit");
  await page.reload();
  await page.click("#resumeBtn");
  assert(await page.locator("#test").count());
  await page.click("#moreBtn");
  await page.click("#endNow");
  await page.waitForSelector(".bigscore");

  // ---------------------------------------------------------------- parent area renders every question
  step("parent area: render every question");
  await page.click("#homeBtn");
  await shot("10-home-progress");
  await page.click("#parentBtn");
  const n = await page.locator(".bank-q").count();
  const katexErrors = await page.locator(".katex-error").count();
  const rawDelims = await page.evaluate(() => [...document.querySelectorAll(".bank-q")].filter((el) => /\\\(|\\\[/.test(el.innerText)).map((el) => el.querySelector("b").textContent));
  assert.strictEqual(n, await page.evaluate(() => window.SAT_QUESTIONS.length));
  assert.strictEqual(katexErrors, 0, "KaTeX errors in rendered bank");
  assert.deepStrictEqual(rawDelims, [], "unrendered math delimiters");
  await shot("11-parent");
  // remove a question
  const firstId = await page.textContent(".bank-q .head b");
  await page.check(`[data-dis="${firstId}"]`);
  const dis = await page.evaluate(() => JSON.parse(localStorage.getItem("satMathPractice.v1")).disabled);
  assert(dis[firstId]);
  // baseline setting
  await page.fill("#baseSet", "700");
  await page.click("#saveSet");
  assert.strictEqual(await page.evaluate(() => JSON.parse(localStorage.getItem("satMathPractice.v1")).settings.baseline), 700);

  // mobile layout sanity
  await page.setViewportSize({ width: 390, height: 844 });
  await page.click("#homeBtn");
  const overflow = await page.evaluate(() => [...document.querySelectorAll("body *")]
    .filter((e) => e.getBoundingClientRect().right > window.innerWidth + 1)
    .map((e) => e.tagName + "." + e.className));
  assert.deepStrictEqual(overflow, [], "no horizontal scroll on phone width");
  await shot("12-mobile-home");

  assert.deepStrictEqual(errors, [], "browser errors");
  console.log(`\nE2E passed (${n} questions rendered, 0 KaTeX errors, 0 page errors)`);
  await browser.close();
  server.close();
})().catch(async (e) => { console.error(e); process.exit(1); });
