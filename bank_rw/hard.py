"""Harder Reading & Writing questions, calibrated against the College Board Question Bank.

A sample of the official bank's hardest questions (Hard, score band 7) showed that hard
reading questions use dense passages of about 100-150 words (median 120), usually
summarizing real research, and that hard grammar questions bury the blank inside long,
complex sentences. The original bank's reading passages were much shorter (median 46),
so these questions were written to match the official style. All passages are original;
the research they describe is real and well documented.
"""
from .questions import Q, B, CONV, WORD, INFER, QUESTIONS

SUPPORT = "Which finding, if true, would most directly support the {}?"
WEAKEN = "Which finding, if true, would most directly weaken the {}?"
MAIN = "Which choice best states the main idea of the text?"

# ------------------------------------------------------------------ Command of Evidence
Q(id="RW-HARD-01", domain="INFO", skill="Command of Evidence", diff=3, rule="evidence",
  passage="<p>The giraffe's extraordinarily long neck is usually explained as an adaptation for feeding: by reaching leaves that shorter herbivores cannot, giraffes would face less competition for food. Field observations complicate this account, however. During the dry season, when food is scarcest and height should matter most, giraffes often feed at about shoulder height rather than stretching upward. Some zoologists have therefore proposed the &ldquo;necks-for-sex&rdquo; hypothesis, which holds that long necks evolved mainly because males use their necks as weapons, swinging them to strike rivals in contests over access to mates.</p>",
  stem=SUPPORT.format("necks-for-sex hypothesis"),
  choices=["Among adult male giraffes, those with longer and heavier necks win more contests against rivals and mate more often than those with shorter necks.",
           "Giraffes spend more of their feeding time browsing on tall trees during the wet season than during the dry season.",
           "Female giraffes, which do not engage in neck contests, have necks that are just as long relative to their body size as males' necks are.",
           "Young giraffes grow taller more quickly in their first year than the young of most other large herbivores do."],
  answer="A",
  explain="The hypothesis says long necks evolved because males with longer necks do better in fights for mates. Evidence that males with longer, heavier necks win more contests and mate more often directly supports that link. "
          "The feeding-season finding is about the competing feeding explanation, not about mating. Equally long necks in females, who don't fight, would actually weaken the hypothesis. Growth rates of young giraffes are irrelevant.")

Q(id="RW-HARD-02", domain="INFO", skill="Command of Evidence", diff=3, rule="evidence",
  passage="<p>Low-frequency noise from traffic dominates the soundscape of most cities. Many songbirds rely on song both to attract mates and to defend territories, so being heard is essential. Ecologists studying great tits, small songbirds common in both European cities and forests, have found that urban great tits tend to sing songs with higher minimum pitches than their forest-dwelling counterparts. The researchers hypothesize that the difference is a response to noise itself: because traffic noise is concentrated at low frequencies, songs with higher pitches are less likely to be drowned out, so birds that shift their songs upward in noisy places are more likely to be heard by mates and rivals.</p>",
  stem=WEAKEN.format("researchers' hypothesis"),
  choices=["Great tits living beside loud highways in otherwise rural areas sing at the same pitches as great tits living in quiet forests.",
           "Urban great tits sing more often in the early morning, before traffic noise peaks, than later in the day.",
           "Several other songbird species in European cities also sing at higher pitches than their forest-dwelling relatives do.",
           "Female great tits respond more strongly to loud songs than to quiet songs."],
  answer="A",
  explain="The hypothesis is that noise causes the higher pitch. Birds exposed to loud traffic noise outside cities that do <i>not</i> sing higher would show that noise doesn't produce the shift, which weakens the hypothesis. "
          "The early-morning finding concerns when birds sing, not their pitch. Other urban species singing higher would support the hypothesis. A preference for loud songs is unrelated to pitch.")

Q(id="RW-HARD-03", domain="INFO", skill="Command of Evidence", diff=3, rule="quant",
  passage="<p>Many students prepare for exams by rereading or highlighting their notes, but cognitive psychologists have found that retrieval practice (testing oneself on material) often produces more durable learning. In one experiment, three groups of students studied the same passage using different methods and were tested either one day or one week later. A student analyzing the results claims that the benefit of self-testing was not apparent at first but emerged over time.</p>"
          "<table class='data'><tr><th>Study method</th><th>Recalled after 1 day (%)</th><th>Recalled after 1 week (%)</th></tr>"
          "<tr><td>Rereading</td><td>62</td><td>34</td></tr><tr><td>Highlighting</td><td>60</td><td>31</td></tr><tr><td>Self-testing</td><td>64</td><td>56</td></tr></table>",
  stem="Which choice most effectively uses data from the table to support the student's claim?",
  choices=["After one day, recall differed by only a few percentage points across the three methods, but after one week, students who self-tested recalled 56 percent compared with 34 and 31 percent for the other methods.",
           "Students who self-tested recalled 64 percent of the material after one day, more than students in either of the other groups.",
           "Recall declined from one day to one week for all three study methods.",
           "Students who highlighted their notes recalled the least after both one day and one week."],
  answer="A",
  explain="The claim has two parts: little difference at first, then a clear benefit later. Only the first choice shows both: after one day the methods were within 4 points of each other, and after one week self-testing (56%) far outpaced rereading (34%) and highlighting (31%). "
          "The 64% figure alone suggests an early advantage, the opposite of &ldquo;not apparent at first.&rdquo; The other two choices are true but don't address the claim.")

Q(id="RW-HARD-04", domain="INFO", skill="Command of Evidence", diff=2, rule="evidence",
  passage="<p>&ldquo;Because I could not stop for Death&rdquo; is a poem by Emily Dickinson, written around 1863. In the poem, the speaker portrays Death not as a frightening figure but as a courteous companion who is in no hurry.</p>",
  stem="Which quotation from the poem most effectively illustrates the claim?",
  choices=["&ldquo;We slowly drove &ndash; He knew no haste / And I had put away / My labor and my leisure too, / For His Civility &ndash;&rdquo;",
           "&ldquo;We passed the School, where Children strove / At Recess &ndash; in the Ring &ndash;&rdquo;",
           "&ldquo;We paused before a House that seemed / A Swelling of the Ground &ndash;&rdquo;",
           "&ldquo;Since then &ndash; &rsquo;tis Centuries &ndash; and yet / Feels shorter than the Day&rdquo;"],
  answer="A",
  explain="The claim has two parts: Death is courteous, and Death is in no hurry. The quotation with &ldquo;He knew no haste&rdquo; and &ldquo;His Civility&rdquo; shows both. "
          "The school and the house describe scenes along the way, and the last quotation is about time passing since the ride, not about Death's character.")

# ------------------------------------------------------------------ Inferences
Q(id="RW-HARD-05", domain="INFO", skill="Inferences", diff=3, rule="inference",
  passage=f"<p>Young sunflower plants track the sun across the sky during the day and reorient toward the east overnight, but once the plants mature, their flower heads stop moving and face east permanently. Both behaviors are governed by the plants' internal circadian clock. To learn why, plant biologists compared mature sunflowers whose heads had been turned to face west with plants left facing east. The east-facing flower heads warmed up more quickly in the morning, and they received roughly five times as many visits from pollinating insects as the west-facing heads did. Because many pollinators prefer warmer flowers, these results suggest that {B}</p>",
  stem=INFER,
  choices=["the eastward orientation of mature sunflowers increases pollinator visits by helping the flowers warm up early in the day.",
           "young sunflowers track the sun mainly in order to attract more pollinators.",
           "west-facing sunflowers are unable to produce any seeds.",
           "pollinating insects cannot detect flowers that face west."],
  answer="A",
  explain="East-facing heads warm faster, warm flowers attract pollinators, and east-facing heads got far more visits. The logical conclusion: facing east increases pollinator visits by helping the flowers warm early. "
          "The study was about mature plants, not why young plants track the sun. &ldquo;Unable to produce any seeds&rdquo; and &ldquo;cannot detect&rdquo; overreach: west-facing heads still got some visits.")

Q(id="RW-HARD-06", domain="INFO", skill="Inferences", diff=3, rule="inference",
  passage=f"<p>Many of the first planets discovered orbiting other stars were &ldquo;hot Jupiters,&rdquo; giant planets that circle their stars in just a few days. The first planet found orbiting a sunlike star, 51 Pegasi b, announced in 1995, completes an orbit in about four days. Some astronomers argued that this abundance reflected the detection method more than the true population of planets. The radial-velocity method detects a planet by the slight wobble it induces in its star, and that wobble is largest for massive planets on tight orbits, exactly the kind of planet that would be found first. Consistent with this view, later surveys using methods better suited to detecting smaller planets and wider orbits have found that {B}</p>",
  stem=INFER,
  choices=["hot Jupiters are relatively rare compared with smaller planets.",
           "the radial-velocity method cannot detect planets of any kind.",
           "most stars have no planets at all.",
           "hot Jupiters are more common than astronomers originally believed."],
  answer="A",
  explain="If hot Jupiters were overrepresented only because they're the easiest to detect, then methods that can find other kinds of planets should show hot Jupiters to be uncommon: &ldquo;hot Jupiters are relatively rare compared with smaller planets.&rdquo; "
          "The radial-velocity method obviously detects some planets, nothing is said about stars without planets, and &ldquo;more common&rdquo; contradicts the argument.")

Q(id="RW-HARD-07", domain="INFO", skill="Inferences", diff=3, rule="inference",
  passage=f"<p>Many retailers sell furniture that customers must put together themselves, a chore that might be expected to make the products less appealing. In a series of experiments, behavioral economists found that people valued storage boxes they had assembled themselves more highly than identical boxes that came already assembled: participants were willing to pay more for the boxes they had built. The researchers called this the &ldquo;IKEA effect.&rdquo; In a follow-up experiment, however, some participants built a box and then took it apart, while others were stopped before they could finish. Neither group showed the increase in valuation. These results suggest that {B}</p>",
  stem=INFER,
  choices=["the extra value people place on things they build depends on completing the task.",
           "people value all products more highly after spending time with them.",
           "pre-assembled furniture is generally of higher quality than furniture that buyers assemble themselves.",
           "taking a product apart increases how much people are willing to pay for it."],
  answer="A",
  explain="Effort alone wasn't enough: people who built and then dismantled their boxes, or didn't finish, showed no boost. So the effect depends on successfully completing the task. "
          "The second choice contradicts the follow-up, the quality of furniture is never discussed, and taking a box apart removed the effect rather than increasing value.")

# ------------------------------------------------------------------ Central ideas
Q(id="RW-HARD-08", domain="INFO", skill="Central Ideas and Details", diff=3, rule="mainidea",
  passage="<p>The ability to delay gratification, giving up a smaller reward now for a better one later, has been studied mostly in humans, apes, and birds, which are social animals with long lives. Researchers therefore tested common cuttlefish, which are solitary and short-lived. Cuttlefish learned that a less preferred food was available immediately while a preferred food, live shrimp, would appear only after a delay, and many waited for the shrimp. Moreover, the individuals that waited longest also learned a separate task most quickly. The findings suggest that self-control may be linked to learning ability even in animals whose lifestyles differ sharply from those of the species usually studied.</p>",
  stem=MAIN,
  choices=["Cuttlefish can delay gratification, and their self-control appears to be related to learning ability, which suggests that such abilities are not limited to long-lived social animals.",
           "Cuttlefish prefer live shrimp to other kinds of food.",
           "Delayed gratification has been studied more often in apes than in any other animal.",
           "Cuttlefish learn new tasks more quickly than humans and birds do."],
  answer="A",
  explain="The text describes the cuttlefish experiment and ends with its significance: self-control and learning may be linked even in solitary, short-lived animals. The first choice captures both the result and why it matters. "
          "The shrimp preference is a detail, the apes claim isn't stated, and no comparison of learning speed with humans or birds is made.")

Q(id="RW-HARD-09", domain="INFO", skill="Central Ideas and Details", diff=2, rule="mainidea",
  passage="<p>The following text is from Charles Dickens's 1859 novel <i>A Tale of Two Cities</i>. The novel is set in London and Paris in the years before and during the French Revolution.</p><p>It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us.</p>",
  stem=MAIN,
  choices=["The narrator characterizes the period as one of sharp contradictions.",
           "The narrator argues that the period was mostly a time of hope.",
           "The narrator suggests that people of the period were unaware of events around them.",
           "The narrator explains the causes of the French Revolution."],
  answer="A",
  explain="Every phrase pairs opposites: best and worst, wisdom and foolishness, belief and incredulity, Light and Darkness. The main idea is that the narrator characterizes the period as one of sharp contradictions. "
          "Choosing &ldquo;mostly a time of hope&rdquo; ignores half of each pair. Nothing is said about awareness of events or about causes.")

# ------------------------------------------------------------------ Text structure and purpose
Q(id="RW-HARD-10", domain="CRAFT", skill="Text Structure and Purpose", diff=3, rule="structure",
  passage="<p>Several studies published in the 2000s reported that bilingual children outperform monolingual children on tasks requiring executive control, such as ignoring distracting information or switching between rules. <u>Later, however, several large studies failed to find this advantage, and some researchers have suggested that the earlier positive results partly reflected publication bias, the tendency for striking findings to be published more readily than null results.</u> Other researchers respond that the advantage may appear only under specific conditions, such as when tasks are especially demanding. Settling the question will likely require large studies whose methods are fixed before any data are collected.</p>",
  stem="Which choice best describes the function of the underlined sentence in the text as a whole?",
  choices=["It presents evidence and an argument that cast doubt on the claim described in the previous sentence.",
           "It explains the method that the earlier studies used to measure executive control.",
           "It offers additional examples of tasks on which bilingual children perform well.",
           "It summarizes the conclusion that all researchers now accept."],
  answer="A",
  explain="The first sentence reports a claimed bilingual advantage. The underlined sentence reports failures to replicate it and a possible reason (publication bias), so it casts doubt on that claim. "
          "It doesn't explain methods or add examples, and the final sentence shows researchers still disagree, so there's no conclusion that &ldquo;all researchers now accept.&rdquo;")

Q(id="RW-HARD-11", domain="CRAFT", skill="Text Structure and Purpose", diff=3, rule="structure",
  passage="<p>In 1901, sponge divers recovered corroded lumps of bronze from a shipwreck off the Greek island of Antikythera. For decades the fragments, now known as the Antikythera mechanism, puzzled scholars, who could see only traces of gears. Beginning in the early 2000s, high-resolution X-ray imaging revealed dozens of interlocking gears and thousands of tiny inscriptions, showing that the more than 2,000-year-old device modeled the movements of the Sun and Moon and predicted eclipses. In 2021, researchers drew on this evidence to propose a reconstruction of the device's missing front display, which they believe also showed the positions of the planets.</p>",
  stem="Which choice best states the main purpose of the text?",
  choices=["To describe how modern imaging has revealed the sophistication of an ancient device",
           "To argue that ancient Greek astronomy was more accurate than modern astronomy",
           "To explain how sponge divers located ancient shipwrecks",
           "To compare the Antikythera mechanism with other ancient calendars"],
  answer="A",
  explain="The text moves from a puzzling discovery to what X-ray imaging revealed and the reconstruction it made possible, so its purpose is to describe how modern imaging has revealed the sophistication of an ancient device. "
          "It makes no comparison with modern astronomy or other calendars, and the divers are only part of the background.")

# ------------------------------------------------------------------ Cross-text
Q(id="RW-HARD-12", domain="CRAFT", skill="Cross-Text Connections", diff=3, rule="crosstext",
  passage="<p class='txtlabel'>Text 1</p><p>Historians often credit the printing press with the rapid spread of the Protestant Reformation. Printed pamphlets could be produced cheaply and in large numbers, carrying reformers' arguments across Europe far faster than handwritten copies ever could. Martin Luther's writings in particular were reprinted again and again within a few years of their first appearance.</p>"
          "<p class='txtlabel'>Text 2</p><p>In the early sixteenth century, most Europeans could not read. Printed pamphlets mattered, but chiefly because literate people read them aloud in taverns and marketplaces, and because printers paired the text with woodcut images. Sermons and songs carried the same messages to many more people than print alone could reach.</p>",
  stem="Based on the texts, how would the author of Text 2 most likely respond to the view described in Text 1?",
  choices=["By agreeing that printing contributed to the Reformation's spread while arguing that its reach depended heavily on spoken and visual forms of communication",
           "By arguing that the printing press had no effect on the spread of the Reformation",
           "By claiming that handwritten copies spread reformers' arguments faster than printed pamphlets did",
           "By suggesting that most Europeans learned to read because of the Reformation"],
  answer="A",
  explain="Text 2 concedes that &ldquo;printed pamphlets mattered&rdquo; but stresses reading aloud, images, sermons, and songs. So its author would agree that printing contributed while arguing that its reach depended on spoken and visual communication. "
          "&ldquo;No effect&rdquo; contradicts &ldquo;mattered,&rdquo; and neither text says handwritten copies were faster or that literacy rose.")

Q(id="RW-HARD-13", domain="CRAFT", skill="Cross-Text Connections", diff=3, rule="crosstext",
  passage="<p class='txtlabel'>Text 1</p><p>In a widely publicized 1993 study, college students who listened to ten minutes of a Mozart sonata scored higher on a spatial reasoning task than students who sat in silence. The finding, quickly dubbed the &ldquo;Mozart effect,&rdquo; inspired products promising to make children smarter, and many parents began playing classical recordings for their infants.</p>"
          "<p class='txtlabel'>Text 2</p><p>Later researchers found that the improvement was small and lasted only minutes. Moreover, listeners showed similar gains after hearing other upbeat music, but not after slow, sad music, suggesting that the gains came from improved mood and arousal rather than from anything special about Mozart.</p>",
  stem="Based on the texts, how would the researchers in Text 2 most likely describe the finding reported in Text 1?",
  choices=["As a real but short-lived improvement that is better explained by listeners' mood and arousal than by Mozart's music in particular",
           "As evidence that listening to Mozart permanently increases intelligence",
           "As the result of an error in how spatial reasoning was measured",
           "As a finding that applies to sad music as well as to upbeat music"],
  answer="A",
  explain="Text 2 accepts that there was an improvement but says it was small, brief, and produced by any upbeat music through mood and arousal. So they'd call it a real but short-lived improvement better explained by mood and arousal. "
          "They reject a permanent effect, never claim a measurement error, and specifically say sad music did not produce gains.")

# ------------------------------------------------------------------ Words in context
Q(id="RW-HARD-14", domain="CRAFT", skill="Words in Context", diff=3, rule="wordsincontext",
  passage=f"<p>The expedition crossed thousands of miles of territory that Indigenous peoples had known and named for centuries. Earlier histories of the expedition portrayed its leaders as flawless heroes. The historian's new account is notably {B} rather than simply celebrating the explorers, she weighs their genuine achievements against the hardships their journey imposed on the communities they encountered along the way.</p>",
  stem=WORD, choices=["hagiographic;", "even-handed;", "cursory;", "sensational;"], answer="B",
  explain="The new account weighs achievements against costs instead of simply celebrating, which is a balanced approach: &ldquo;even-handed;&rdquo;. "
          "&ldquo;Hagiographic&rdquo; (treating a subject as a saint) describes the <i>earlier</i> histories, which is the trap. &ldquo;Cursory&rdquo; (hasty) and &ldquo;sensational&rdquo; don't fit careful weighing.")

# ------------------------------------------------------------------ Hard grammar: long, complex sentences
Q(id="RW-HARD-15", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="agreement",
  passage=f"<p>The collection of essays that the poet published late in her career, together with several letters discovered among her papers after her death, {B} scholars a much fuller picture of how her views on the natural world changed over five decades.</p>",
  stem=CONV, choices=["give", "gives", "have given", "are giving"], answer="B",
  explain="The subject is &ldquo;The collection,&rdquo; which is singular. &ldquo;Of essays&rdquo; is a prepositional phrase, and &ldquo;together with several letters&rdquo; adds extra information without creating a plural subject (only &ldquo;and&rdquo; does that). So the verb is &ldquo;gives&rdquo;.")

Q(id="RW-HARD-16", domain="SEC", skill="Boundaries", diff=3, rule="nonessential",
  passage=f"<p>Italian-born Brazilian architect Lina Bo Bardi's {B} admired in Brazil during her lifetime but little known abroad, have attracted growing international attention in recent decades, particularly the S&atilde;o Paulo Museum of Art, whose main gallery is suspended above a public plaza.</p>",
  stem=CONV, choices=["buildings,", "buildings", "building's,", "buildings'"], answer="A",
  explain="&ldquo;Admired in Brazil &hellip; but little known abroad&rdquo; is extra information about the buildings, and it closes with the comma before &ldquo;have attracted.&rdquo; So it must open with a comma: &ldquo;buildings,&rdquo;. "
          "The plural verb &ldquo;have&rdquo; confirms the plural, non-possessive &ldquo;buildings.&rdquo;")

Q(id="RW-HARD-17", domain="SEC", skill="Boundaries", diff=3, rule="clauses",
  passage=f"<p>In 2011, researchers analyzing DNA preserved in 30,000-year-old permafrost from the Yukon reported finding genes that make bacteria resistant to several modern {B} the discovery showed that antibiotic resistance is an ancient natural phenomenon, far older than the medical use of antibiotics.</p>",
  stem=CONV, choices=["antibiotics,", "antibiotics;", "antibiotics", "antibiotics, which"], answer="B",
  explain="Both parts are complete sentences: &ldquo;researchers &hellip; reported finding genes &hellip;&rdquo; and &ldquo;the discovery showed &hellip;&rdquo;. They need a semicolon: &ldquo;antibiotics;&rdquo;. "
          "A comma alone is a comma splice, no punctuation is a run-on, and &ldquo;which the discovery showed&rdquo; is ungrammatical. The length of the first clause is the distraction.")

Q(id="RW-HARD-18", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="verbform",
  passage=f"<p>Completed in 1883 after fourteen years of construction, the Brooklyn Bridge, whose steel-wire cables were a technological novelty and whose Gothic stone towers rose higher than nearly every other structure in New York at the time, {B} the longest suspension bridge in the world when it opened.</p>",
  stem=CONV, choices=["was", "being", "having been", "to be"], answer="A",
  explain="After two long &ldquo;whose&rdquo; clauses, the subject &ldquo;the Brooklyn Bridge&rdquo; still needs a main verb. Only &ldquo;was&rdquo; is a finite verb; the others leave the sentence a fragment.")

# ------------------------------------------------------------------ recalibrate the original short reading items
# Official Hard reading passages run about 100-150 words; the original bank's are far
# shorter, so their difficulty labels are lowered one level to stay honest. Timed sets
# then use the dense passages above for the hardest slots.
for q in QUESTIONS:
    if q["domain"] in ("CRAFT", "INFO") and not q["id"].startswith("RW-HARD"):
        import html as _h, re as _re
        words = len(_re.sub(r"\s+", " ", _h.unescape(_re.sub(r"<[^>]+>", " ", q["passage"])))) / 6
        if words < 90:
            q["diff"] = max(1, q["diff"] - 1)
