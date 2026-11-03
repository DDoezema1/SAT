/* Core logic: answer grading, the student model, adaptive question selection, and
 * score estimation. No DOM access here, so it can be unit-tested in Node. */
(function (root) {
  "use strict";

  // Item difficulty on a logit scale. The scale is anchored so that a student whose
  // ability theta equals b has a 50% chance on that item, and the SAT-like score is
  // roughly 500 + 100*theta. Medium is about a 550 item, hard 650, very hard 730.
  const B = { 1: 0.5, 2: 1.5, 3: 2.3 };
  const DIFF_NAME = { 1: "Medium", 2: "Hard", 3: "Very hard" };
  const PACE_SEC = 95;            // 35 min / 22 questions, about the real pace
  const MODULE_SEC = 35 * 60;
  const MODULE_LEN = 22;
  const BLUEPRINT = { ALG: 7, ADV: 7, PSD: 4, GEO: 4 };   // per module, ~SAT domain weights
  const DIFF_MIX = {
    m1: { 1: 6, 2: 10, 3: 6 },
    m2hard: { 1: 2, 2: 9, 3: 11 },
    m2std: { 1: 9, 2: 10, 3: 3 },
  };
  const ROUTE_THRESHOLD = 14;     // correct answers in module 1 (of 22) to reach the harder module 2
  const DAY = 86400000;

  const sigmoid = (z) => 1 / (1 + Math.exp(-z));

  // ---------------------------------------------------------------- grading
  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a; }

  /** Parse "41/3", "-2.5", ".75" into {n, d} (exact rational), or null. */
  function parseRational(str) {
    const s = String(str).trim();
    let m;
    if ((m = s.match(/^(-?)(\d+)\/(\d+)$/))) {
      const n = parseInt(m[2], 10) * (m[1] ? -1 : 1), d = parseInt(m[3], 10);
      if (d === 0) return null;
      const g = gcd(n, d) || 1;
      return { n: n / g, d: d / g };
    }
    if ((m = s.match(/^(-?)(\d*)\.?(\d*)$/)) && (m[2] + m[3]).length > 0) {
      const decs = m[3].length;
      const d = Math.pow(10, decs);
      const n = parseInt((m[2] || "0") + m[3], 10) * (m[1] ? -1 : 1);
      const g = gcd(n, d) || 1;
      return { n: n / g, d: d / g };
    }
    return null;
  }

  /** Validate characters/length the way the SAT answer box does. */
  function sprInputAllowed(str) {
    if (!/^-?[0-9./]*$/.test(str)) return false;
    const max = str.startsWith("-") ? 6 : 5;
    if (str.length > max) return false;
    if ((str.match(/\./g) || []).length > 1 || (str.match(/\//g) || []).length > 1) return false;
    if (str.includes(".") && str.includes("/")) return false;
    return true;
  }

  /**
   * SAT rules for student-produced responses: any exact equivalent is correct
   * (fraction or decimal). For a non-terminating value, a decimal is correct if it
   * fills the whole answer box and equals the value either truncated or rounded.
   */
  function gradeSPR(input, answer) {
    const s = String(input || "").trim();
    if (!s || !sprInputAllowed(s)) return false;
    const key = parseRational(answer), v = parseRational(s);
    if (!key || !v) return false;
    if (v.n * key.d === key.n * v.d) return true;
    if (!s.includes(".")) return false;
    const max = s.startsWith("-") ? 6 : 5;
    if (s.length < max) return false;                 // must use all available space
    const decs = s.split(".")[1].length;
    const exact = key.n / key.d;
    const scaled = Math.abs(exact) * Math.pow(10, decs);
    if ((v.n < 0) !== (exact < 0)) return false;
    const entered = Math.round(Math.abs(v.n / v.d) * Math.pow(10, decs));
    return entered === Math.floor(scaled + 1e-9) || entered === Math.round(scaled);
  }

  function isCorrect(q, response) {
    if (response == null || response === "") return false;
    return q.type === "mc" ? response === q.answer : gradeSPR(response, q.answer);
  }

  // ---------------------------------------------------------------- student model
  function defaultState() {
    return {
      version: 1,
      name: "",
      settings: { calc: "always", pin: "" },
      theta: 1.0,           // overall ability, starts near a 600 level
      skills: {},           // skill -> {theta, n, correct}
      items: {},            // question id -> {n, correct, last, lastCorrect, wrongStreak}
      sessions: [],
      disabled: {},         // question id -> true (parent removed it)
      active: null,         // in-progress session snapshot
    };
  }

  function skillRec(state, skill) {
    return state.skills[skill] || (state.skills[skill] = { theta: state.theta, n: 0, correct: 0 });
  }

  /** Elo-style update after one answer. Unanswered counts as wrong. */
  function recordAnswer(state, q, correct, now) {
    const b = B[q.diff];
    const sk = skillRec(state, q.skill);
    const kSkill = Math.max(0.25, 0.9 / Math.sqrt(1 + sk.n / 4));
    sk.theta += kSkill * ((correct ? 1 : 0) - sigmoid(sk.theta - b));
    sk.n += 1; sk.correct += correct ? 1 : 0;
    state.n = (state.n || 0) + 1;
    const kGlobal = Math.max(0.2, 0.6 / Math.sqrt(1 + state.n / 6));
    state.theta += kGlobal * ((correct ? 1 : 0) - sigmoid(state.theta - b));
    const it = state.items[q.id] || (state.items[q.id] = { n: 0, correct: 0, last: 0, lastCorrect: false });
    it.n += 1; it.correct += correct ? 1 : 0; it.last = now || Date.now(); it.lastCorrect = !!correct;
  }

  /** Probability of answering a typical Hard question in this skill correctly. */
  function mastery(state, skill) {
    const sk = state.skills[skill];
    return sigmoid((sk ? sk.theta : state.theta) - B[2]);
  }

  // ---------------------------------------------------------------- selection
  function rand(rng) { return rng ? rng() : Math.random(); }

  /** Desirability of serving question q now (higher is better). */
  function priority(state, q, now, rng) {
    const it = state.items[q.id];
    let p = 2.0 * (1 - mastery(state, q.skill));     // weak skills first
    if (!it) p += 3;                                  // brand new
    else if (!it.lastCorrect && now - it.last > 2 * DAY) p += 1.5;   // missed before: spaced retry
    else if (!it.lastCorrect) p -= 1;                 // missed very recently: wait a bit
    else p -= 3 + Math.min(it.correct, 3);            // already mastered: rarely repeat
    if (it) p -= Math.max(0, 1.5 - (now - it.last) / (7 * DAY));     // seen in the past week
    return p + 0.6 * rand(rng);
  }

  function available(state, questions, exclude) {
    return questions.filter((q) => !state.disabled[q.id] && !exclude.has(q.id));
  }

  function pickBest(cands, state, now, rng) {
    let best = null, bestP = -Infinity;
    for (const q of cands) {
      const p = priority(state, q, now, rng);
      if (p > bestP) { bestP = p; best = q; }
    }
    return best;
  }

  /** Split n slots across difficulties in proportion to mix. */
  function allocate(n, mix) {
    const total = mix[1] + mix[2] + mix[3];
    const raw = [1, 2, 3].map((d) => (n * mix[d]) / total);
    const out = raw.map(Math.floor);
    let left = n - out.reduce((a, b) => a + b, 0);
    const order = [0, 1, 2].sort((i, j) => (raw[j] - out[j]) - (raw[i] - out[i]));
    for (let i = 0; left > 0; i = (i + 1) % 3, left--) out[order[i]]++;
    return { 1: out[0], 2: out[1], 3: out[2] };
  }

  /** Assemble a 22-question module following the domain blueprint and a difficulty mix. */
  function buildModule(state, questions, mixKey, used, rng, now) {
    now = now || Date.now();
    const mix = DIFF_MIX[mixKey];
    const picked = [];
    for (const dom of Object.keys(BLUEPRINT)) {
      const want = allocate(BLUEPRINT[dom], mix);
      for (const d of [3, 2, 1]) {
        for (let i = 0; i < want[d]; i++) {
          const pool = available(state, questions, used).filter((q) => q.domain === dom);
          // exact difficulty first, then the nearest difficulty
          const order = d === 2 ? [2, 3, 1] : d === 3 ? [3, 2, 1] : [1, 2, 3];
          let q = null;
          for (const dd of order) {
            q = pickBest(pool.filter((x) => x.diff === dd), state, now, rng);
            if (q) break;
          }
          if (!q) q = pickBest(available(state, questions, used), state, now, rng);
          if (!q) break;
          picked.push(q); used.add(q.id);
        }
      }
    }
    // Real modules get harder toward the end: order by difficulty, shuffling within each level.
    const shuffled = picked.map((q) => [q.diff + rand(rng), q]).sort((a, b) => a[0] - b[0]).map((p) => p[1]);
    return shuffled;
  }

  function route(module1Responses) {
    const correct = module1Responses.filter((r) => r.correct).length;
    return correct >= ROUTE_THRESHOLD ? "m2hard" : "m2std";
  }

  /**
   * Adaptive practice: choose the next question one at a time, favoring weak skills at a
   * difficulty slightly above the student's current level in that skill.
   */
  function nextPractice(state, questions, opts, used, rng, now) {
    now = now || Date.now();
    let pool = available(state, questions, used);
    if (opts.domain && opts.domain !== "ALL") pool = pool.filter((q) => q.domain === opts.domain);
    if (opts.calc === "desmos") pool = pool.filter((q) => q.desmos);
    if (opts.calc === "hand") pool = pool.filter((q) => !q.desmos);
    if (opts.onlyIds) pool = pool.filter((q) => opts.onlyIds.includes(q.id));
    if (!pool.length) return null;

    // Score every candidate: weak skills first (inside priority), difficulty close to
    // slightly above the student's level in that skill, and avoid repeating the skill
    // that was just practiced.
    const ids = [...used];
    const last = ids.length ? questions.find((q) => q.id === ids[ids.length - 1]) : null;
    let best = null, bestP = -Infinity;
    for (const q of pool) {
      const sk = state.skills[q.skill];
      const target = (sk ? sk.theta : state.theta) + 0.4;
      let p = priority(state, q, now, rng) - 1.5 * Math.abs(B[q.diff] - target);
      if (last && last.skill === q.skill) p -= 0.8;
      if (p > bestP) { bestP = p; best = q; }
    }
    return best;
  }

  // ---------------------------------------------------------------- scoring
  /**
   * Estimate an SAT-style math score (200-800) from responses [{diff, correct}] using a
   * one-parameter (Rasch) model with a mild prior, so all-correct or all-wrong still
   * gives a finite estimate. This is an approximation, not an official conversion.
   */
  function estimateScore(responses) {
    if (!responses.length) return null;
    const mu = 1.0, sd = 1.5;
    let th = mu;
    for (let iter = 0; iter < 50; iter++) {
      let g = -(th - mu) / (sd * sd), h = -1 / (sd * sd);
      for (const r of responses) {
        const p = sigmoid(th - B[r.diff]);
        g += (r.correct ? 1 : 0) - p;
        h -= p * (1 - p);
      }
      const step = g / h;
      th -= step;
      if (Math.abs(step) < 1e-6) break;
    }
    let info = 1 / (sd * sd);
    for (const r of responses) { const p = sigmoid(th - B[r.diff]); info += p * (1 - p); }
    const se = 1 / Math.sqrt(info);
    const clamp = (v) => Math.max(200, Math.min(800, Math.round(v / 10) * 10));
    return { score: clamp(500 + 100 * th), low: clamp(500 + 100 * (th - se)), high: clamp(500 + 100 * (th + se)), theta: th };
  }

  const api = {
    B, DIFF_NAME, PACE_SEC, MODULE_SEC, MODULE_LEN, BLUEPRINT, ROUTE_THRESHOLD,
    parseRational, sprInputAllowed, gradeSPR, isCorrect,
    defaultState, recordAnswer, mastery, buildModule, route, nextPractice, estimateScore,
  };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.Engine = api;
})(typeof window !== "undefined" ? window : globalThis);
