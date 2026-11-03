// End-to-end test for the Reading & Writing page.  Usage: node tools/e2e_rw.js [screenshotDir]
const { chromium } = require("playwright");
const http = require("http");
const fs = require("fs");
const path = require("path");
const assert = require("assert");

const ROOT = path.join(__dirname, "..", "app");
// Usage: node tools/e2e_rw.js [screenshotDir] [--url=https://site/]
const URL_ARG = (process.argv.find((a) => a.startsWith("--url=")) || "").slice(6);
const LIVE = !!URL_ARG;
const SHOTS = process.argv.slice(2).find((a) => !a.startsWith("--"));
const TYPES = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2" };
const server = http.createServer((req, res) => {
  const p = path.join(ROOT, decodeURIComponent(req.url.split("?")[0]).replace(/^\/$/, "/index.html"));
  if (!p.startsWith(ROOT) || !fs.existsSync(p)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "Content-Type": TYPES[path.extname(p)] || "application/octet-stream" });
  fs.createReadStream(p).pipe(res);
});

(async () => {
  if (!LIVE) await new Promise((r) => server.listen(0, r));
  const base = LIVE ? URL_ARG : `http://localhost:${server.address().port}/`;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1366, height: 860 } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
  page.on("dialog", (d) => d.accept());
  const shot = async (n) => { if (SHOTS) await page.screenshot({ path: path.join(SHOTS, n + ".png") }); };
  const step = (s) => console.log("  - " + s);
  const KEY = "satRWPractice.v1";
  const active = () => page.evaluate((k) => JSON.parse(localStorage.getItem(k)).active, KEY);
  async function answer(correct) {
    const s = await active();
    const q = await page.evaluate((id) => window.SAT_QUESTIONS.find((q) => q.id === id), s.items[s.idx].id);
    await page.click(`.choice[data-o="${correct ? q.answer : "ABCD".replace(q.answer, "")[0]}"]`);
    return q;
  }

  // math page links to R&W
  await page.goto(base);
  assert.strictEqual(await page.locator(".subjtabs a").count(), 2);
  await page.click(".subjtabs a[href='english.html']");
  await page.waitForSelector("#playbookBtn");
  step("R&W home loads from the Math tab");
  assert.match(await page.textContent(".hero"), /Reading & Writing[\s\S]*Starting point: 700/);
  const nRules = await page.evaluate(() => window.SAT_RULES.length);
  await shot("rw-01-home");

  // ------------------------------------------------ rules page and a rule drill
  step("must-know rules page and rule drill");
  await page.click("#playbookBtn");
  assert.strictEqual(await page.locator(".playbook .pb").count(), nRules);
  await shot("rw-02-rules");
  await page.click(".drillrule[data-rule='nonessential']");
  assert.match(await page.textContent("#secTitle"), /Rule Drill: Extra information/);
  assert.match(await page.textContent(".rulebox"), /Rule to apply/);
  assert(await page.locator(".qpane.passage .blank").count() === 1, "passage pane with a blank");
  assert(await page.locator("#calcBtn.hidden").count() === 1, "no calculator in R&W");
  await shot("rw-03-drill-question");
  await answer(false);
  await page.click("#nextBtn");
  await page.waitForSelector(".feedback.no");
  assert.match(await page.textContent(".feedback"), /Rule: Extra information[\s\S]*Trap:/);
  await shot("rw-04-drill-feedback");
  const nDrill = await page.evaluate(() => window.SAT_QUESTIONS.filter((q) => q.rule === "nonessential").length);
  await page.click("#nextBtn");
  for (let i = 1; i < nDrill; i++) {
    const q = await answer(true);
    assert.strictEqual(q.rule, "nonessential", "drill serves only its rule");
    await page.click("#nextBtn"); await page.waitForSelector(".feedback.ok"); await page.click("#nextBtn");
  }
  await page.waitForSelector(".bigscore");
  assert.strictEqual((await page.textContent(".bigscore")).trim(), `${nDrill - 1}/${nDrill}`);
  assert.match(await page.textContent(".cards"), /By rule[\s\S]*Drill next: Extra information/);

  // ------------------------------------------------ timed set: fast points
  step("timed set: 13 grammar/transition/notes questions with coach");
  await page.click("#homeBtn");
  await page.selectOption("#sLen", "13");
  await page.selectOption("#sDom", "QUICK");
  assert.match(await page.textContent("#setTime"), /15:23/);
  await page.click("#setBtn");
  assert.match(await page.textContent("#navBtn"), /Question 1 of 13/);
  assert(await page.locator("#refBtn.hidden").count() === 1, "no rules button during a timed set");
  const doms = await page.evaluate((k) => JSON.parse(localStorage.getItem(k)).active.items.map((i) => window.SAT_QUESTIONS.find((q) => q.id === i.id).domain), KEY);
  assert(doms.every((d) => d === "SEC" || d === "EXPR"), doms.join(","));
  const ORDER = ["CRAFT", "INFO", "SEC", "EXPR"];
  for (let i = 1; i < doms.length; i++) assert(ORDER.indexOf(doms[i]) >= ORDER.indexOf(doms[i - 1]), "official domain order: " + doms.join(","));
  await page.waitForTimeout(1100);
  assert.match(await page.textContent("#pace"), /on pace|ahead|behind/);
  await shot("rw-05-timed-set");
  for (let i = 0; i < 13; i++) { await answer(i % 4 !== 0); await page.click("#nextBtn"); }
  await page.click("#nextBtn");
  await page.waitForSelector(".bigscore");
  assert.strictEqual((await page.textContent(".bigscore")).trim(), "9/13");
  assert.match(await page.textContent(".cards"), /Timing[\s\S]*By rule/);
  await page.click(".qitem summary");
  assert(await page.locator(".qitem .passage-r").count() >= 1);
  await shot("rw-06-results");

  // ------------------------------------------------ progress, trouble spots, separate storage
  step("progress by rule, trouble spots, separate storage from math");
  await page.click("#homeBtn");
  assert.match(await page.textContent("body"), /Rules[\s\S]*Mastery/);
  assert(!(await page.isDisabled("#retryBtn")));
  const keys = await page.evaluate(() => Object.keys(localStorage));
  assert(keys.includes(KEY));
  assert(!keys.includes("satMathPractice.v1") || await page.evaluate(() => !JSON.parse(localStorage.getItem("satMathPractice.v1")).sessions.length));
  await shot("rw-07-home-progress");

  // ------------------------------------------------ parent area
  step("parent area renders every R&W question");
  await page.click("#parentBtn");
  const n = await page.locator(".bank-q").count();
  assert.strictEqual(n, await page.evaluate(() => window.SAT_QUESTIONS.length));
  assert.strictEqual(await page.locator(".bank-q .passage-r").count(), n);
  assert.strictEqual(await page.locator("#calcSet.hidden").count(), 1);

  // phone width
  await page.setViewportSize({ width: 390, height: 844 });
  await page.click("#homeBtn");
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  assert(!overflow, "no horizontal scroll at phone width");
  await shot("rw-08-mobile");

  assert.deepStrictEqual(errors, [], "browser errors");
  console.log(`\nR&W E2E passed (${n} questions, ${nRules} rules, 0 page errors)`);
  await browser.close();
  if (!LIVE) server.close();
})().catch((e) => { console.error(e); process.exit(1); });
