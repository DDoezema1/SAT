# Calibration against the official SAT

This compares the app with College Board's published specifications for the digital SAT, then lists what was changed as a result.

**Scope and limits.** College Board's site (satsuite.collegeboard.org) was blocked by the network policy of the environment this was built in. The specifications below therefore come from College Board's own documents as returned by web search, not from reading the documents directly. The official practice tests and the Educator Question Bank could not be opened at all, so the questions have **not** yet been compared one by one with real test questions. See "Not yet verified" at the end.

## Math

| Official specification | App before | Status |
|---|---|---|
| 2 modules × 22 questions (20 scored + 2 unscored pretest), 35 minutes each | Same | ✅ matches |
| Domains (of 40 scored): Algebra 13–15, Advanced Math 13–15, Problem-Solving & Data Analysis 5–7, Geometry & Trigonometry 5–7 | 7 / 7 / 4 / 4 per module (14/14/8/8 per test): PSDA and Geometry slightly overweighted | **Fixed:** 8 / 8 / 3 / 3 per module = 16 / 16 / 6 / 6 per test (the official counts plus the 4 pretest slots) |
| ≈75% multiple choice, ≈25% student-produced response | Not controlled. The bank is 45% grid-in, so a module could have about 10 grid-ins | **Fixed:** 5–6 grid-ins per 22-question module (2–3 per 11), spread through the module. Tested across 20 random draws per module type |
| Within a module, questions run from easiest to hardest | Same | ✅ matches |
| Module 2 still mixes easy, medium, and hard questions, with average difficulty set by Module 1 performance | Same design | ✅ matches. Harder vs. standard Module 2 average difficulty differs by 0.57 on the app's 1–3 scale (minimum 0.55 over 200 draws) |
| Desmos graphing calculator available on every math question; College Board notes that some questions are better done without a calculator | Same; questions tagged "Desmos" or "By hand" | ✅ matches |
| Some (not all) math questions are set in real-world contexts | Mix of context and pure-math items | ✅ matches |
| Official difficulty labels: Easy / Medium / Hard | Medium / Hard / Very hard | ⚠️ Intentional: the app's scale is shifted up for a 700+ student. Its "Medium" ≈ official Medium; its "Hard" and "Very hard" split the official Hard band |

## Reading & Writing

| Official specification | App before | Status |
|---|---|---|
| 2 modules × 27 questions (25 scored + 2 pretest), 32 minutes each | Same | ✅ matches |
| Domains: Craft & Structure ≈28% (13–15), Information & Ideas ≈26% (12–14), Standard English Conventions ≈26%, Expression of Ideas ≈20% (8–12) | 7 / 7 / 7 / 6 per 27-question module | ✅ matches |
| All questions are discrete four-option multiple choice, one passage (or passage pair) each | Same | ✅ matches |
| Each passage (or pair) is 25–150 words, where a "word" is 6 characters | Linted with a looser rule; 8 grammar passages were 7–24 words | **Fixed:** context sentences added to the 8 short passages; the build now enforces 25–150 by College Board's definition. Current range: 25–98 |
| Module order: Craft & Structure, then Information & Ideas, then Conventions, then Expression of Ideas; similar skills grouped, easiest to hardest | Timed sets ordered only by difficulty | **Fixed:** timed sets follow the official domain order, with skills grouped and easiest to hardest within each. Conventions questions are ordered by difficulty regardless of rule; that last detail comes from prep-company sources, not College Board |
| Question wording ("Which choice completes the text so that it conforms to the conventions of Standard English?", "…with the most logical transition?", "…most effectively uses relevant information from the notes…") | Same wording | ✅ consistent with the wording seen in search results. The third phrase was not found in search results, so it is still unverified |

## Question-by-question comparison with official practice tests 4, 7 and 10

Once satsuite.collegeboard.org was allowed, the PDF editions of official practice tests 4, 7 and 10 and their answer explanations were downloaded and analyzed: 198 Reading & Writing and 162 math questions. They were used only as a yardstick. No official question was copied into the app.

| What was measured | Official tests | App before | Action |
|---|---|---|---|
| Math answer format | Exactly 20 multiple choice + 7 grid-in per 27-question module (26%), all six modules | Fixed to ~25% in the previous round | ✅ confirmed |
| Hardest math topics (Module 2, last third) | Parameter giving exactly one or no solution, discriminant, *g(c+7)=4c*-style linear functions, exponential forms showing a value, factor with a parameter, circle equations, data displays, multi-step area/volume, unit conversion | All present in the app's Hard/Very hard set except squared-unit conversion | Added a squared-unit conversion (FIG-12) and an absolute-value equation (FIG-13) |
| Math questions with a figure, graph, or table | About 15% (graphs, dot plots, histograms, parallel-line and triangle diagrams; this is a lower bound from text matching) | 4 of 156 (3%) | **Added 11 figure questions** (graphs of lines, a parabola, an exponential, and a circle; a dot plot, a histogram, scatterplots, and a bar graph; parallel lines; a right triangle with an altitude). Every figure is drawn by code from the same numbers the verifier solves |
| R&W question wording | Same wording for every type | Same | ✅ confirmed (including the notes-question wording that search couldn't confirm earlier) |
| Words in Context share | 31 of 198 (16%), the single most common type | 4 of 67 (6%) | **Added 10**, including 2 from public-domain novels |
| Transitions share | 20 of 198 (10%) | 7 of 67 (10%) | ✅ matches |
| Grammar topics tested | Tense and verb forms most often (12 of 48), then punctuation between clauses, supplements, agreement, modifiers, possessives, series | Tense and verb forms 6 of 36 | **Added 4** tense/verb-form/agreement items |
| Literary passages | 16 of 198 (8%) | 2 of 67 (3%) | Added 2 (Jack London, Herman Melville) |
| Purpose, inference, data questions | 10%, 7%, 6% | 3%, 4%, 3% | Added 2 purpose, 2 inference, 1 data-table item |

Grammar topics that appear in the official tests but are still not covered (each appeared once in 198 questions): end-of-sentence punctuation for statements that contain questions, and punctuation of integrated relative clauses.

All new items went through the same checks as the rest of the bank:
- Math is re-derived by computer. This caught two errors before they shipped: two answer choices that were the same function in different forms, and a key/verifier mismatch.
- Reading & Writing passes the automated checks and a separate re-solve, which led to replacing two arguably defensible distractors.
- Every figure was rendered and inspected; one unreadable axis was fixed.

## Still not verified

- **Exact difficulty labels.** The PDF practice tests don't label individual questions Easy/Medium/Hard; that lives in College Board's Educator Question Bank, which is served from a different site that is still blocked. The difficulty comparison above is by topic and by position in the module, not by official label.
- **The adaptive Bluebook versions** of these tests (22 and 27 questions per module) weren't available; the PDF editions use longer modules drawn from the same question pool.

## Sources

- [Assessment Framework for the Digital SAT Suite](https://satsuite.collegeboard.org/media/pdf/assessment-framework-for-digital-sat-suite.pdf)
- [Digital SAT Suite Specifications Overview](https://satsuite.collegeboard.org/media/pdf/digital-sat-test-spec-overview.pdf)
- [Math Specifications](https://satsuite.collegeboard.org/k12-educators/about/alignment/math)
- [Reading and Writing Specifications](https://satsuite.collegeboard.org/k12-educators/about/alignment/reading)
- [The SAT Math Section: Overview](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/overview)
- [The SAT Reading and Writing Section](https://satsuite.collegeboard.org/sat/whats-on-the-test/reading-writing)
- [How the SAT Is Structured](https://satsuite.collegeboard.org/sat/whats-on-the-test/structure)
- [Official SAT Practice Test 4](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-4-digital.pdf), [7](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-7-digital.pdf), and [10](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-10-digital.pdf), with their answer explanations
- [Digital SAT Suite Technical Manual](https://research.collegeboard.org/media/pdf/Digital%20SAT%20Suite%20of%20Assessments%20Technical%20Manual-FINAL.pdf)
- [SAT Suite Calculator Policy](https://satsuite.collegeboard.org/in-school-assessments/calculator-policy)
- [Texas alignment document (domain counts)](https://satsuite.collegeboard.org/media/pdf/tx-sat-suite-alignment-texas-standards.pdf) and [Kentucky alignment document](https://satsuite.collegeboard.org/media/pdf/ky-sat-suite-alignment-kentucky-standards.pdf)
- [SAT Suite Educator Question Bank help (difficulty levels)](https://satsuitequestionbank.collegeboard.org/help)
- Ordering of Conventions questions: [Acely SAT Reading & Writing guide](https://acely.com/sat-prep/sat-reading-and-writing-guide) and [Test Ninjas](https://test-ninjas.com/sat-reading-writing-question-types) (third-party)
