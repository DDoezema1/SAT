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

## Not yet verified (needs access to College Board's site)

1. **Question-by-question comparison with the official Bluebook / PDF practice tests:** topics, phrasing, and how hard the hardest Module 2 questions really are compared with the app's "Very hard" items.
2. **The share of literary passages** (fiction, poetry) in Reading & Writing. The app has only 2, which is probably low.
3. **Typical passage length for the reading questions.** The app's longest is 98 words, against an allowed maximum of 150. Real hard reading passages may run longer.

To finish this, allow `satsuite.collegeboard.org` in the environment's network settings. Then the official practice tests can be profiled question by question (without copying them) and compared with the bank.

## Sources

- [Assessment Framework for the Digital SAT Suite](https://satsuite.collegeboard.org/media/pdf/assessment-framework-for-digital-sat-suite.pdf)
- [Digital SAT Suite Specifications Overview](https://satsuite.collegeboard.org/media/pdf/digital-sat-test-spec-overview.pdf)
- [Math Specifications](https://satsuite.collegeboard.org/k12-educators/about/alignment/math)
- [Reading and Writing Specifications](https://satsuite.collegeboard.org/k12-educators/about/alignment/reading)
- [The SAT Math Section: Overview](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/overview)
- [The SAT Reading and Writing Section](https://satsuite.collegeboard.org/sat/whats-on-the-test/reading-writing)
- [How the SAT Is Structured](https://satsuite.collegeboard.org/sat/whats-on-the-test/structure)
- [Digital SAT Suite Technical Manual](https://research.collegeboard.org/media/pdf/Digital%20SAT%20Suite%20of%20Assessments%20Technical%20Manual-FINAL.pdf)
- [SAT Suite Calculator Policy](https://satsuite.collegeboard.org/in-school-assessments/calculator-policy)
- [Texas alignment document (domain counts)](https://satsuite.collegeboard.org/media/pdf/tx-sat-suite-alignment-texas-standards.pdf) and [Kentucky alignment document](https://satsuite.collegeboard.org/media/pdf/ky-sat-suite-alignment-kentucky-standards.pdf)
- [SAT Suite Educator Question Bank help (difficulty levels)](https://satsuitequestionbank.collegeboard.org/help)
- Ordering of Conventions questions: [Acely SAT Reading & Writing guide](https://acely.com/sat-prep/sat-reading-and-writing-guide) and [Test Ninjas](https://test-ninjas.com/sat-reading-writing-question-types) (third-party)
