# SAT Practice: Math and Reading & Writing

A practice app for the digital SAT. The **Math** page (`app/index.html`) and the **Reading & Writing** page (`app/english.html`) share one interface and switch with the tabs at the top.

The math section is tuned for a student who already scores in the 700s, so the goal is the last 50–60 points. In practice that means three things: more accuracy on the hardest questions, faster pacing, and reaching for Desmos whenever it's the fastest route.

## Math: what's in it

**Timed Set (the everyday mode).** A short, test-like block: 11 questions (half a module, 17:25) or 22 (one module, 35:00). It's built at her level, so a 740 student gets only Hard and Very hard questions. The questions are drawn from her trouble spots and weak skills. Pace is either SAT pace (1:35 per question) or **speed training** (1:20 per question, which builds a time buffer for test day). It can focus on one domain or on Desmos questions only.

**Pacing coach** (optional, in any timed mode):

- under the timer, a live **ahead / on pace / behind** indicator
- on each question, a **stopwatch** that turns amber at the target time and red when it's time to guess, mark the question, and move on

**Desmos Speed Drill.** 8 Desmos-route questions. The calculator opens automatically, each question has a target time, and a "Desmos hint" button is available if she's stuck (it counts as half credit). The Desmos solution appears after each answer.

**Trouble Spots.** Re-serves every question she **missed, answered slowly, or needed a hint on**. A correct answer that took too long counts as a trouble spot, because on test day time costs points.

**Adaptive Practice.** Questions are chosen one at a time based on accuracy *and speed*, with feedback after each question or only at the end.

**Full Math Section.** Both modules, 2 × 22 questions at 35 minutes each. A student who gets 14 or more right on Module 1 is routed to the harder Module 2. You can save and exit between modules. At the end you get an estimated score.

**Desmos Playbook.** One page of the Desmos techniques that matter on the SAT: sliders for unknown constants, counting solutions, max/min, regression from a table, lists for statistics, equivalent expressions, degree mode, and when *not* to use Desmos. It's also reachable from inside the calculator panel.

**Scores stay in the background.** The home screens don't show the student's official score or the app's estimate. An estimated score appears on the results page right after a full section. The Parent area has a **Scores** card with the latest official score, the current estimate, and recent full-section estimates.

**Seeing the answers.**
- Practice modes (Adaptive Practice, Desmos Drill, Trouble Spots, Rule Drill) show the correct answer, the explanation, and the Desmos strategy or rule right after each question.
- Timed Sets show answers on the results page.
- The Full Math Section has an optional **Review Module 1 answers first** button between the modules. It doesn't use any Module 2 time, but skip it for a test-day dress rehearsal.
- On every review, missed and skipped questions open automatically. Each shows a plain line ("You chose B (…), but the correct answer is A (…)"), the choices marked red and green, the full explanation, and the faster Desmos route or rule.
- Filters show Missed & skipped / Correct but slow / Marked for review / All.

**Getting pointers from Claude.**
- Every results page has a **Get pointers from Claude** button.
- The home page has one for overall progress.
- Each produces a plain-text summary: every question with its ID, result, time against target, and Desmos use; for misses, the question, the answer given, and the correct answer.
- The summary ends with a request for focused coaching. Copy it (or Share it on a phone) and paste it into a chat with Claude.
- Nothing is sent anywhere automatically.

**Results after every session** cover:

- **Timing:** time used vs. allowed, average per question, correct-but-slow count, time spent on missed questions, and the biggest time sinks
- **Desmos use:** how often she opened Desmos on Desmos questions; accuracy and time with vs. without it; "missed Desmos opportunities"
- a worked solution and Desmos strategy for every question

**Starting level.** The app starts at **740** (the latest official SAT Math score). It changes in the Parent area. After about 20 answers, the app's own estimate takes over.

**Test-like interface.** Timer with Hide, Calculator (Desmos) panel, Reference sheet, Directions, Mark for Review, answer cross-out, grid-in answer preview, question navigator, and a Check Your Work page.

**Parent area** (bottom of the home page, optional PIN):

- answer key with explanations
- "Remove from practice" switch for each question
- baseline score and calculator setting
- export, import, and reset of progress

## Math question bank

There are 182 original questions, 15 of them with a figure, graph, or table:

| Domain | Count | Medium / Hard / Very hard |
|---|---|---|
| Algebra | 36 | 8 / 19 / 9 |
| Advanced Math | 54 | 4 / 21 / 29 |
| Problem-Solving & Data Analysis | 43 | 10 / 23 / 10 |
| Geometry & Trigonometry | 36 | 4 / 18 / 14 |

- **65 are Desmos-route questions** (graphing is the intended fast route).
- **23 by-hand questions also show a "Desmos alternative"**, so 88 questions teach a Desmos method.
- A top-band set of 26 questions targets what separates 740 from 790: tangency and number-of-solutions conditions with parameters, regressions, cubic behavior, messy systems, and statistics from lists.
- All 19 official SAT math skills are covered.

Every answer key went through several review rounds before it could reach the app. See [review/REVIEW.md](review/REVIEW.md) for the details and [review/answer-key.md](review/answer-key.md) for a readable answer key.

## Reading & Writing

This page is built around **must-know rules** rather than a big question bank. Each of its 104 questions is tied to one of 21 high-impact rules. They include 18 dense, official-style hard questions (100–150-word research passages and long-sentence grammar), calibrated against College Board's Question Bank. They are weighted toward the question types that are pure rules: grammar/punctuation, transitions, and student-notes questions. Those make up about half of each module and can be answered in 20–40 seconds once the rules are automatic.

- **Must-Know Rules:** every rule on one page, ordered by points, each with an example, the trap the test sets, and a "Drill this rule" button. Covers:
  - punctuation: joining sentences, colons, nonessential elements, no punctuation in the core, *however*, possessives
  - grammar: agreement, pronouns, tense, modifiers, complete sentences and parallel forms
  - transitions and notes questions
  - reading strategies: words in context, purpose, cross-text, evidence, data, inferences, main idea
  - pacing
- **Rule Drill:** shows the rule, then questions that test only that rule, with the rule and its trap repeated after every answer. The home page preselects her weakest rule.
- **Timed Set:** 9, 13, or 27 questions at SAT pace (1:11 per question) or speed training (1:00 per question). One focus option is "Grammar, transitions & notes", the fast-points block. Results show **which rules cost points** and recommend what to drill next.
- **Trouble Spots**, **Adaptive Practice**, and the pacing coach work as they do in Math, with **700** as the starting level.
- Math and Reading & Writing keep **separate progress**.

The Reading & Writing bank is intentionally small and focused. It covers each rule several times, but it doesn't have enough reading questions for full-length R&W modules, so there is no full R&W section yet.

## Running it

It is a static web page with no server and no install.

- **On one computer:** open `app/index.html` (Math) or `app/english.html` (Reading & Writing) in Chrome, Edge, or Safari. The math renders offline. The Desmos calculator needs an internet connection.
- **As a website (recommended):** the included GitHub workflow publishes `app/` to GitHub Pages. One-time setup: in the repo, go to **Settings → Pages → Source** and choose **GitHub Actions**. After the next push to `main`, the site is at `https://<your-user>.github.io/<repo>/`.

Progress is saved in the browser, so use the same computer and browser each time. To move to another computer, use Export/Import in the Parent area.

### Desmos API key

The app loads Desmos with the public demo API key from Desmos's documentation (in `app/js/app.js`, `DESMOS_URL`). If Desmos ever rejects that key, request a free key at <https://www.desmos.com/api> and paste it in. If the calculator can't load, the panel shows a link to open desmos.com/calculator in a new tab.

## Adding or editing questions

Questions are written in Python under `bank/`. Each one has a `verify` function that re-derives the answer from scratch with SymPy. The build refuses to export a question if its key doesn't match the computed answer.

```bash
pip install sympy
cd tools && npm ci && cd ..
python3 tools/build_bank.py     # verify every math question and regenerate app/js/questions.js
python3 tools/build_rw.py       # check the Reading & Writing bank and regenerate app/js/rw_questions.js
node tools/check_render.js      # compile every math snippet with KaTeX
node tools/test_engine.js       # grading, adaptivity, pacing, and scoring tests
node tools/e2e.js               # drives the Math page in a browser (needs Playwright)
node tools/e2e_rw.js            # drives the Reading & Writing page
```

Math goes inside `\( ... \)` or `\[ ... \]`. A plain `$` is just a dollar sign.

## Notes and limits

- The score estimate comes from a statistical model of question difficulty (a Rasch model). It's a useful guide, not an official College Board conversion.
- Target times per question: 1:00 for Medium, 1:30 for Hard, 2:00 for Very hard. A correct answer more than 30% over its target is counted as "slow".
- Questions are text-only (tables, but no drawn figures), so geometry questions describe their figures in words.
- At the top difficulty mix, there are enough unseen Hard and Very hard questions for roughly 3–4 one-module sets per domain mix. After that, the app re-serves trouble spots first.
- This is an independent practice tool and isn't affiliated with or endorsed by College Board. SAT is a trademark of College Board.
