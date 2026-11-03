# SAT Math Practice

A practice app for the math section of the digital SAT. It's built around hard questions, the built-in Desmos graphing calculator, a timed adaptive test, and a student model that steers practice toward weak skills.

## What's in it

**Full Math Section (adaptive).** Two 22-question modules at 35 minutes each, like the real test. Module 1 mixes difficulty levels. A student who gets 14 or more of its 22 questions right is routed to the *harder* Module 2; everyone else gets the standard Module 2. At the end you get an estimated 200–800 score with a likely range, a breakdown by domain, Desmos versus by-hand accuracy, time per question, and a full worked solution for every question.

**Adaptive Practice.** Questions are picked one at a time. The app favors skills where the student is weakest and aims for a difficulty just above her current level in that skill. Every answer updates a per-skill rating. Options:

- 10, 15, or 22 questions
- focus on one domain, or all four
- style: a mix, Desmos-only, or by-hand only
- feedback after each question, or only at the end
- SAT pace (1:35 per question) or untimed

**Retry Missed Questions.** Brings back every question she got wrong last time, with explanations.

**Test-like interface.** The layout follows the general style of the digital testing app: a header with a countdown timer (with Hide), Calculator, Reference sheet, and Directions; Mark for Review; answer-choice cross-out (ABC); student-produced-response directions and an answer preview; a question navigator; and a Check Your Work page before each module is submitted. The clock can't be hidden in the last 5 minutes, and the module auto-submits at 0:00.

**Desmos.** The Desmos graphing calculator opens in a side panel that can be expanded, as on test day. Every question is tagged either **Desmos** (graphing is the fastest or smartest route) or **By hand** (reasoning or algebra is the intended route). Every Desmos question comes with a "Desmos strategy" note in its solution.

**Parent area.** Linked at the bottom of the home page, optionally behind a PIN. It holds:

- the full answer key with explanations
- a "Remove from practice" switch for each question
- the calculator setting: always available (real SAT), or only on Desmos questions (to build by-hand skill)
- progress export, import, and reset

## The question bank

There are 130 original questions:

| Domain | Count | Medium / Hard / Very hard |
|---|---|---|
| Algebra | 28 | 8 / 14 / 6 |
| Advanced Math | 40 | 4 / 16 / 20 |
| Problem-Solving & Data Analysis | 33 | 9 / 16 / 8 |
| Geometry & Trigonometry | 29 | 4 / 15 / 10 |

About 35% are Desmos-route questions and 65% are by-hand. Most are multiple choice, with student-produced (grid-in) responses mixed in as on the real test. The bank covers all 19 official SAT math skills. It is large enough for two full sections with no repeated questions. After that, the app re-serves questions she missed, and spaces out the ones she already got right.

Every answer key went through several review rounds before it could reach the app. See [review/REVIEW.md](review/REVIEW.md) for the details and [review/answer-key.md](review/answer-key.md) for a readable answer key.

## Running it

It is a static web page with no server and no install.

- **On one computer:** open `app/index.html` in Chrome, Edge, or Safari. The math renders offline. The Desmos calculator needs an internet connection.
- **As a website (recommended):** the included GitHub workflow publishes `app/` to GitHub Pages. One-time setup: in the repo, go to **Settings → Pages → Source** and choose **GitHub Actions**. After the next push to `main`, the site is at `https://<your-user>.github.io/<repo>/`.

Progress is saved in the browser, so use the same computer and browser each time. To move to another computer, use Export/Import in the Parent area.

### Desmos API key

The app loads Desmos with the public demo API key from Desmos's documentation (in `app/js/app.js`, `DESMOS_URL`). If Desmos ever rejects that key, request a free key at <https://www.desmos.com/api> and paste it in. If the calculator can't load, the panel shows a link to open desmos.com/calculator in a new tab.

## Adding or editing questions

Questions are written in Python under `bank/`. Each one has a `verify` function that re-derives the answer from scratch with SymPy. The build refuses to export a question if its key doesn't match the computed answer.

```bash
pip install sympy
cd tools && npm ci && cd ..
python3 tools/build_bank.py     # verify every question and regenerate app/js/questions.js
node tools/check_render.js      # compile every math snippet with KaTeX
node tools/test_engine.js       # grading, adaptivity, and scoring tests
node tools/e2e.js               # drives the real app in a browser (needs Playwright)
```

Math goes inside `\( ... \)` or `\[ ... \]`. A plain `$` is just a dollar sign.

## Notes and limits

- The score estimate comes from a statistical model of question difficulty (a Rasch model). It's a useful guide, not an official College Board conversion.
- Questions are text-only (tables, but no drawn figures), so geometry questions describe their figures in words.
- This is an independent practice tool and isn't affiliated with or endorsed by College Board. SAT is a trademark of College Board.
