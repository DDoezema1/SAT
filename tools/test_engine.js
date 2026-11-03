// Unit tests for app/js/engine.js.  Run: node tools/test_engine.js
const assert = require("assert");
global.window = {};
require("../app/js/questions.js");
const E = require("../app/js/engine.js");
const Q = window.SAT_QUESTIONS;
let passed = 0;
function test(name, fn) { fn(); passed++; console.log("  ok  " + name); }

// Seeded RNG so failures are reproducible.
function rng(seed) { return () => ((seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296); }

test("SPR exact equivalents are accepted", () => {
  assert(E.gradeSPR("41/3", "41/3"));
  assert(E.gradeSPR("82/6", "41/3"));
  assert(E.gradeSPR("6.5", "13/2"));
  assert(E.gradeSPR("13/2", "13/2"));
  assert(E.gradeSPR("6.50", "13/2"));
  assert(E.gradeSPR("-.4", "-2/5"));
  assert(E.gradeSPR("-0.4", "-2/5"));
  assert(E.gradeSPR("-2/5", "-2/5"));
  assert(E.gradeSPR("1682", "1682"));
  assert(E.gradeSPR("0", "0"));
});

test("SPR repeating decimals: must fill the box, truncated or rounded", () => {
  assert(E.gradeSPR("13.66", "41/3"));
  assert(E.gradeSPR("13.67", "41/3"));
  assert(!E.gradeSPR("13.6", "41/3"));
  assert(!E.gradeSPR("13.7", "41/3"));
  assert(E.gradeSPR(".4166", "5/12"));
  assert(E.gradeSPR(".4167", "5/12"));
  assert(E.gradeSPR("0.416", "5/12"));
  assert(E.gradeSPR("0.417", "5/12"));
  assert(!E.gradeSPR(".42", "5/12"));
  assert(!E.gradeSPR(".4168", "5/12"));
  assert(E.gradeSPR("7.714", "54/7"));
  assert(!E.gradeSPR("7.715", "54/7"));
  assert(E.gradeSPR("3.428", "24/7"));
  assert(E.gradeSPR("3.429", "24/7"));
  assert(!E.gradeSPR("3.43", "24/7"));
  assert(E.gradeSPR("-.3333", "-1/3"));
  assert(E.gradeSPR("-0.333", "-1/3"));
  assert(!E.gradeSPR("-.33", "-1/3"));
  assert(!E.gradeSPR(".3333", "-1/3"));
});

test("SPR rejects wrong values and invalid input", () => {
  assert(!E.gradeSPR("41/4", "41/3"));
  assert(!E.gradeSPR("", "5"));
  assert(!E.gradeSPR("5%", "5"));
  assert(!E.gradeSPR("$56", "56"));
  assert(!E.gradeSPR("1,682", "1682"));
  assert(!E.gradeSPR("123456", "123456"));
  assert(!E.gradeSPR("1/0", "5"));
  assert(!E.gradeSPR("5/", "5"));
  assert(!E.gradeSPR("2", "-2"));
});

test("every SPR key in the bank is gradable as entered", () => {
  for (const q of Q.filter((q) => q.type === "spr")) {
    const key = q.answer;
    const fits = E.sprInputAllowed(key);
    if (fits) assert(E.gradeSPR(key, key), q.id);
    else {
      // the key is too long to type: the truncated decimal must be accepted instead
      const v = E.parseRational(key);
      const s = (v.n / v.d).toFixed(6);
      const max = s.startsWith("-") ? 6 : 5;
      const trunc = s.slice(0, max);
      assert(E.gradeSPR(trunc, key), `${q.id} ${trunc}`);
    }
  }
});

test("MC grading", () => {
  const q = Q.find((q) => q.type === "mc");
  assert(E.isCorrect(q, q.answer));
  assert(!E.isCorrect(q, "ABCD".replace(q.answer, "")[0]));
  assert(!E.isCorrect(q, null));
});

test("module 1 follows the blueprint: 22 unique questions, domain counts, mixed difficulty", () => {
  const st = E.defaultState();
  const used = new Set();
  const m = E.buildModule(st, Q, "m1", used, rng(1));
  assert.strictEqual(m.length, 22);
  assert.strictEqual(new Set(m.map((q) => q.id)).size, 22);
  const dom = {}; for (const q of m) dom[q.domain] = (dom[q.domain] || 0) + 1;
  assert.deepStrictEqual(dom, { ALG: 8, ADV: 8, PSD: 3, GEO: 3 });
  const diffs = new Set(m.map((q) => q.diff));
  assert(diffs.size === 3);
  for (let i = 1; i < m.length; i++) assert(m[i].diff >= m[i - 1].diff, "ordered by difficulty");
});

test("harder module 2 is harder than the standard one, and never repeats module 1", () => {
  const st = E.defaultState();
  const used1 = new Set(); E.buildModule(st, Q, "m1", used1, rng(2));
  const hard = E.buildModule(st, Q, "m2hard", new Set(used1), rng(3));
  const std = E.buildModule(st, Q, "m2std", new Set(used1), rng(3));
  const avg = (m) => m.reduce((a, q) => a + q.diff, 0) / m.length;
  assert(avg(hard) > avg(std) + 0.5 && avg(hard) >= 2.2 && avg(std) <= 2.0, `${avg(hard)} vs ${avg(std)}`);
  for (let seed = 10; seed < 30; seed++) {           // holds across many random draws, not just one
    const u = new Set(); E.buildModule(st, Q, "m1", u, rng(seed));
    const h = E.buildModule(st, Q, "m2hard", new Set(u), rng(seed)), d = E.buildModule(st, Q, "m2std", new Set(u), rng(seed));
    assert(avg(h) > avg(d) + 0.5, `seed ${seed}: ${avg(h)} vs ${avg(d)}`);
  }
  for (const q of hard.concat(std)) assert(!used1.has(q.id));
  assert.strictEqual(hard.length, 22);
  assert.strictEqual(std.length, 22);
});

test("bank supports two full sections without repeats", () => {
  const st = E.defaultState();
  const used = new Set();
  for (const key of ["m1", "m2hard", "m1", "m2std"]) assert.strictEqual(E.buildModule(st, Q, key, used, rng(4)).length, 22);
  assert.strictEqual(used.size, 88);
});

test("routing threshold", () => {
  const mk = (n) => Array.from({ length: 22 }, (_, i) => ({ correct: i < n }));
  assert.strictEqual(E.route(mk(E.ROUTE_THRESHOLD)), "m2hard");
  assert.strictEqual(E.route(mk(E.ROUTE_THRESHOLD - 1)), "m2std");
});

test("removed (disabled) questions are never served", () => {
  const st = E.defaultState();
  for (const q of Q.filter((q) => q.domain === "GEO").slice(0, 10)) st.disabled[q.id] = true;
  const used = new Set();
  const m = E.buildModule(st, Q, "m1", used, rng(5));
  for (const q of m) assert(!st.disabled[q.id]);
  for (let i = 0; i < 50; i++) { const q = E.nextPractice(st, Q, { domain: "GEO" }, used, rng(i)); if (!q) break; assert(!st.disabled[q.id]); used.add(q.id); }
});

test("adaptive practice targets the weak skill", () => {
  // Simulated student: perfect except at circles.
  const st = E.defaultState();
  const R = rng(9);
  const picks = {};
  const used = new Set();
  for (let i = 0; i < 60; i++) {
    const q = E.nextPractice(st, Q, { domain: "GEO" }, used, R);
    if (!q) { used.clear(); continue; }
    used.add(q.id);
    picks[q.skill] = (picks[q.skill] || 0) + 1;
    E.recordAnswer(st, q, q.skill !== "Circles", Date.now());
  }
  const circles = picks["Circles"] || 0;
  const others = Object.entries(picks).filter(([k]) => k !== "Circles").map(([, v]) => v);
  assert(circles > Math.max(...others), JSON.stringify(picks));
  assert(E.mastery(st, "Circles") < 0.3);
  assert(E.mastery(st, "Area and volume") > 0.7);
});

test("adaptive practice raises difficulty for a strong student", () => {
  const st = E.defaultState();
  const used = new Set();
  const diffs = [];
  for (let i = 0; i < 20; i++) {
    const q = E.nextPractice(st, Q, { domain: "ALL" }, used, rng(100 + i));
    used.add(q.id); diffs.push(q.diff);
    E.recordAnswer(st, q, true, Date.now());
  }
  const late = diffs.slice(10).reduce((a, b) => a + b, 0) / 10;
  assert(late >= 2.3, diffs.join(","));
  assert(!diffs.slice(3).includes(1), "no medium questions once the student is clearly strong: " + diffs.join(","));
});

test("adaptive practice eases off for a struggling student", () => {
  const st = E.defaultState();
  E.setBaseline(st, 600);
  const used = new Set();
  const diffs = [];
  for (let i = 0; i < 20; i++) {
    const q = E.nextPractice(st, Q, { domain: "ALL" }, used, rng(200 + i));
    used.add(q.id); diffs.push(q.diff);
    E.recordAnswer(st, q, false, Date.now());
  }
  const late = diffs.slice(10).reduce((a, b) => a + b, 0) / 10;
  assert(late <= 1.6, diffs.join(","));
});

test("practice filters: Desmos-only and by-hand-only", () => {
  const st = E.defaultState();
  for (let i = 0; i < 20; i++) {
    assert(E.nextPractice(st, Q, { calc: "desmos" }, new Set(), rng(i)).desmos);
    assert(!E.nextPractice(st, Q, { calc: "hand" }, new Set(), rng(i)).desmos);
  }
});

test("score estimate: monotonic, bounded, sensible anchors", () => {
  const mk = (n, diff) => Array.from({ length: 44 }, (_, i) => ({ diff, correct: i < n }));
  let prev = 0;
  for (let n = 0; n <= 44; n++) {
    const s = E.estimateScore(mk(n, 2)).score;
    assert(s >= prev && s >= 200 && s <= 800);
    prev = s;
  }
  assert(E.estimateScore(mk(44, 3)).score >= 760);
  assert(E.estimateScore(mk(0, 1)).score <= 350);
  assert(E.estimateScore(mk(22, 2)).score > 600 && E.estimateScore(mk(22, 2)).score < 700);
});

test("default starting level is the 740 baseline", () => {
  const st = E.defaultState();
  assert.strictEqual(E.thetaToScore(st.theta), 740);
  assert.strictEqual(st.settings.baseline, 740);
  E.setBaseline(st, 680);
  assert.strictEqual(E.thetaToScore(st.theta), 680);
});

test("slow correct answers count as partial mastery and become trouble spots", () => {
  const q = Q.find((q) => q.diff === 3);
  const fast = E.defaultState(), slow = E.defaultState();
  const rf = E.recordAnswer(fast, q, true, Date.now(), { secs: 60 });
  const rs = E.recordAnswer(slow, q, true, Date.now(), { secs: 400 });
  assert(!rf.slow && rs.slow);
  assert(slow.skills[q.skill].theta < fast.skills[q.skill].theta);
  assert(!E.isTrouble(fast.items[q.id]));
  assert(E.isTrouble(slow.items[q.id]));
  assert.deepStrictEqual(E.troubleIds(slow, Q), [q.id]);
});

test("using the Desmos hint caps credit and marks a trouble spot", () => {
  const q = Q.find((q) => q.desmos);
  const st = E.defaultState();
  const r = E.recordAnswer(st, q, true, Date.now(), { secs: 30, hint: true });
  assert.strictEqual(r.credit, 0.5);
  assert(E.isTrouble(st.items[q.id]));
});

test("trouble spots are re-served ahead of mastered questions after a few days", () => {
  const st = E.defaultState();
  const old = Date.now() - 5 * 86400000;
  const geo = Q.filter((q) => q.domain === "GEO");
  for (const q of geo) E.recordAnswer(st, q, true, old, { secs: 30 });          // all fast and correct...
  const slowQ = geo[3];
  E.recordAnswer(st, slowQ, true, old, { secs: 500 });                         // ...except one slow one
  const picked = E.nextPractice(st, Q, { domain: "GEO" }, new Set(), rng(3));
  assert.strictEqual(picked.id, slowQ.id);
});

test("timed sets: 11 and 22 questions, scaled blueprint, top-band mix at 740", () => {
  assert.deepStrictEqual(E.scaleBlueprint(11), { ALG: 4, ADV: 4, PSD: 2, GEO: 1 });
  assert.deepStrictEqual(E.scaleBlueprint(22), { ALG: 8, ADV: 8, PSD: 3, GEO: 3 });
  const st = E.defaultState();
  assert.strictEqual(E.levelMix(st), "top");
  for (const n of [11, 22]) {
    const set = E.buildModule(st, Q, E.levelMix(st), new Set(), rng(n), null, n);
    assert.strictEqual(set.length, n);
    assert(!set.some((q) => q.diff === 1), "no medium questions for a 740 student");
    assert(set.filter((q) => q.diff === 3).length >= n / 2, "mostly very hard");
  }
  const dset = E.buildModule(st, Q, "top", new Set(), rng(1), null, 11, { filter: (q) => q.desmos });
  assert.strictEqual(dset.length, 11);
  assert(dset.every((q) => q.desmos));
  const alg = E.buildModule(st, Q, "top", new Set(), rng(1), null, 11, { domain: "ALG" });
  assert(alg.length === 11 && alg.every((q) => q.domain === "ALG"));
});

test("modules are about 25% student-produced response, like the real test", () => {
  for (let seed = 1; seed <= 20; seed++) {
    const st = E.defaultState();
    for (const key of ["m1", "m2hard", "m2std", "top"]) {
      const m = E.buildModule(st, Q, key, new Set(), rng(seed), null, 22);
      const spr = m.filter((q) => q.type === "spr").length;
      assert(spr >= 5 && spr <= 6, `${key} seed ${seed}: ${spr} SPR`);
    }
    const half = E.buildModule(st, Q, "top", new Set(), rng(seed), null, 11).filter((q) => q.type === "spr").length;
    assert(half >= 2 && half <= 3, `11-question set: ${half} SPR`);
  }
});

console.log(`\n${passed} tests passed`);
