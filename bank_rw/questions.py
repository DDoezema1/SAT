"""Reading & Writing practice questions, each tied to one must-know rule (rules.py).

Passages are original. Facts in the passages were chosen to be well established; the
questions themselves test the rule, not the fact.
"""
QUESTIONS = []

B = '<span class="blank">______</span>'
CONV = "Which choice completes the text so that it conforms to the conventions of Standard English?"
TRANS = "Which choice completes the text with the most logical transition?"
WORD = "Which choice completes the text with the most logical and precise word or phrase?"
SYN = "Which choice most effectively uses relevant information from the notes to accomplish this goal?"
INFER = "Which choice most logically completes the text?"


def Q(**kw):
    QUESTIONS.append(kw)


def notes(items):
    return "<p>While researching a topic, a student has taken the following notes:</p><ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ====================================================================== Boundaries
Q(id="RW-SEC-01", domain="SEC", skill="Boundaries", diff=2, rule="clauses",
  passage=f"<p>Monarch butterflies in eastern North America migrate up to 3,000 miles each fall to forests in central {B} no single butterfly completes the round trip, since the journey back north spans several generations.</p>",
  stem=CONV, choices=["Mexico,", "Mexico;", "Mexico", "Mexico, however,"], answer="B",
  explain="Both sides are complete sentences (&ldquo;Monarch butterflies &hellip; migrate &hellip;&rdquo; and &ldquo;no single butterfly completes the round trip&rdquo;), so they need a semicolon: &ldquo;Mexico;&rdquo;. A comma alone, or &ldquo;, however,&rdquo; is a comma splice; no punctuation is a run-on.")

Q(id="RW-SEC-02", domain="SEC", skill="Boundaries", diff=2, rule="clauses",
  passage=f"<p>Honeybees communicate the location of food through a &ldquo;waggle {B} the angle of the dance relative to vertical indicates the direction of the food source relative to the sun.</p>",
  stem=CONV, choices=["dance,&rdquo;", "dance&rdquo;:", "dance,&rdquo; and,", "dance&rdquo;"], answer="B",
  explain="The second clause explains <i>how</i> the dance communicates location, and both clauses are complete, so a colon fits: &ldquo;dance&rdquo;:&rdquo;. A comma alone is a comma splice, &ldquo;and,&rdquo; puts a comma in the wrong place, and no punctuation makes a run-on.")

Q(id="RW-SEC-03", domain="SEC", skill="Boundaries", diff=3, rule="clauses",
  passage=f"<p>Architect Zaha Hadid became the first woman to win the Pritzker Architecture Prize in {B} her designs, known for their sweeping curves, include the aquatics center built for the 2012 London Olympics.</p>",
  stem=CONV, choices=["2004,", "2004, and", "2004, which", "2004"], answer="B",
  explain="Two independent clauses need a comma plus a coordinating conjunction: &ldquo;2004, and&rdquo;. A comma alone is a splice, &ldquo;which her designs include&hellip;&rdquo; is ungrammatical here, and no punctuation is a run-on.")

Q(id="RW-SEC-04", domain="SEC", skill="Boundaries", diff=3, rule="however",
  passage=f"<p>Early critics dismissed the novel as too experimental to find an {B} within a decade, it had become required reading in many university literature courses.</p>",
  stem=CONV, choices=["audience, however,", "audience; however,", "audience, however;", "audience however,"], answer="B",
  explain="&ldquo;However&rdquo; can't join two complete sentences on its own. The semicolon must come <i>before</i> it, ending the first clause, and a comma follows it: &ldquo;audience; however,&rdquo;. &ldquo;audience, however;&rdquo; would attach &ldquo;however&rdquo; to the wrong clause and reverse the logic.")

Q(id="RW-SEC-05", domain="SEC", skill="Boundaries", diff=2, rule="clauses",
  passage=f"<p>The Great Pacific Garbage Patch is not a solid island of floating {B} consists mostly of tiny plastic particles suspended in the water, which makes it difficult to see even from a ship passing through it.</p>",
  stem=CONV, choices=["trash, it", "trash. It", "trash it", "trash, and it,"], answer="B",
  explain="&ldquo;The Great Pacific Garbage Patch is not a solid island of floating trash&rdquo; and &ldquo;It consists mostly of tiny plastic particles&hellip;&rdquo; are both complete sentences, so a period works: &ldquo;trash. It&rdquo;. The comma version is a splice, the version with no punctuation is a run-on, and &ldquo;and it,&rdquo; puts a comma between the subject and its verb.")

Q(id="RW-SEC-06", domain="SEC", skill="Boundaries", diff=2, rule="colon",
  passage=f"<p>The ecologists identified three factors that predicted how quickly a coral reef recovered after a bleaching {B} water temperature, the abundance of plant-eating fish, and the reef's distance from human settlements.</p>",
  stem=CONV, choices=["event:", "event,", "event;", "event, such as:"], answer="A",
  explain="A complete sentence introduces a list, so a colon is correct: &ldquo;event:&rdquo;. A semicolon must be followed by a complete sentence, and the list isn't one. A comma creates a confusing run-on list. A colon after &ldquo;such as&rdquo; is always wrong.")

Q(id="RW-SEC-07", domain="SEC", skill="Boundaries", diff=3, rule="colon",
  passage=f"<p>The museum's new exhibit on twentieth-century Mexican art focuses on painters who helped shape the country's cultural identity after the Mexican Revolution. It features works by {B} Frida Kahlo, Diego Rivera, and Rufino Tamayo.</p>",
  stem=CONV, choices=["artists such as:", "artists such as", "artists, such as:", "artists; such as"], answer="B",
  explain="&ldquo;Works by artists such as&rdquo; isn't a complete sentence, so no colon can follow it, and a semicolon can't either. The phrase flows straight into its list: &ldquo;artists such as&rdquo;.")

Q(id="RW-SEC-08", domain="SEC", skill="Boundaries", diff=3, rule="colon",
  passage=f"<p>Ornithologists who tracked Arctic terns with tiny geolocators were surprised by one feature of the birds' {B} the terns flew a winding, S-shaped route that was far longer than a direct path between their breeding and wintering grounds.</p>",
  stem=CONV, choices=["migration:", "migration,", "migration", "migration, that"], answer="A",
  explain="The first clause is complete and promises &ldquo;one feature&rdquo;; the second clause names it. That's exactly what a colon does: &ldquo;migration:&rdquo;. A comma would be a splice, and no punctuation is a run-on.")

Q(id="RW-SEC-09", domain="SEC", skill="Boundaries", diff=2, rule="nonessential",
  passage=f"<p>Katherine Johnson, a mathematician whose calculations of orbital trajectories were critical to early NASA {B} received the Presidential Medal of Freedom in 2015.</p>",
  stem=CONV, choices=["missions,", "missions;", "missions&mdash;", "missions"], answer="A",
  explain="The description of Johnson opens with a comma, so it must close with a comma: &ldquo;missions,&rdquo;. A dash would mismatch the pair, a semicolon would separate the subject from its verb, and no punctuation leaves the extra information unclosed.")

Q(id="RW-SEC-10", domain="SEC", skill="Boundaries", diff=3, rule="nonessential",
  passage=f"<p>The axolotl&mdash;a salamander native to the lakes and canals around Mexico {B} can regenerate entire limbs, parts of its heart, and even portions of its brain.</p>",
  stem=CONV, choices=["City,", "City&mdash;", "City;", "City"], answer="B",
  explain="The extra information opens with a dash after &ldquo;axolotl,&rdquo; so it must close with a dash: &ldquo;City&mdash;&rdquo;. Mixing a dash with a comma is always wrong.")

Q(id="RW-SEC-11", domain="SEC", skill="Boundaries", diff=3, rule="nonessential",
  passage=f"<p>Nigerian author Chinua Achebe wrote several novels, but he is best known for his first. Achebe's {B} was published in 1958 and has since been translated into more than fifty languages.</p>",
  stem=CONV, choices=["novel, <i>Things Fall Apart</i>,", "novel <i>Things Fall Apart</i>", "novel, <i>Things Fall Apart</i>", "novel: <i>Things Fall Apart</i>"], answer="B",
  explain="Achebe wrote several novels, so the title is <i>essential</i>: it tells us which novel. Essential information takes no commas: &ldquo;novel <i>Things Fall Apart</i>&rdquo;. A pair of commas would wrongly imply it was his only novel; a single comma or a colon separates the subject from its verb.")

Q(id="RW-SEC-12", domain="SEC", skill="Boundaries", diff=2, rule="nonessential",
  passage=f"<p>The James Webb Space Telescope (launched on December 25, {B} observes the universe primarily in infrared light, which allows it to see through clouds of dust that block visible light.</p>",
  stem=CONV, choices=["2021)", "2021),", "2021,", "2021)&mdash;"], answer="A",
  explain="The parenthesis opened after &ldquo;Telescope,&rdquo; so it must close: &ldquo;2021)&rdquo;. Nothing else goes there, because after the parenthesis the subject (&ldquo;The James Webb Space Telescope&rdquo;) runs straight into its verb (&ldquo;observes&rdquo;).")

Q(id="RW-SEC-13", domain="SEC", skill="Boundaries", diff=2, rule="nopunct",
  passage=f"<p>The forest ecologists had expected young, fast-growing trees to absorb the most carbon. The study's most surprising finding was {B} the oldest and largest trees in the forest absorbed more carbon each year than younger ones did.</p>",
  stem=CONV, choices=["that,", "that", "that:", "that;"], answer="B",
  explain="&ldquo;That the oldest and largest trees&hellip;&rdquo; is the complement of &ldquo;was.&rdquo; No punctuation belongs between a verb and its complement or right after &ldquo;that&rdquo;: &ldquo;that&rdquo;.")

Q(id="RW-SEC-14", domain="SEC", skill="Boundaries", diff=3, rule="nopunct",
  passage=f"<p>The thousands of handwritten letters that the poet exchanged with her editor over three {B} a detailed record of how her poems evolved from first draft to publication.</p>",
  stem=CONV, choices=["decades, provide", "decades provide", "decades, provides", "decades provides"], answer="B",
  explain="The long subject (&ldquo;The thousands of handwritten letters that&hellip;&rdquo;) must not be separated from its verb by a comma, and the subject is plural (&ldquo;thousands of letters&rdquo;), so: &ldquo;decades provide&rdquo;.")

Q(id="RW-SEC-15", domain="SEC", skill="Boundaries", diff=1, rule="nopunct",
  passage=f"<p>Because the canyon funnels strong spring winds through its narrowest point, the engineers designed the new suspension bridge's cables to {B} gusts of more than 100 miles per hour.</p>",
  stem=CONV, choices=["withstand:", "withstand,", "withstand", "withstand&mdash;"], answer="C",
  explain="A verb and its object (&ldquo;withstand gusts&rdquo;) are never separated by punctuation: &ldquo;withstand&rdquo;.")

Q(id="RW-SEC-16", domain="SEC", skill="Boundaries", diff=3, rule="however",
  passage=f"<p>The festival's opening night featured jazz pianist Hiromi Uehara, from {B} Senegalese singer Youssou N'Dour, a pioneer of mbalax; and Cuban percussionist Pedrito Mart&iacute;nez.</p>",
  stem=CONV, choices=["Japan;", "Japan,", "Japan:", "Japan"], answer="A",
  explain="The list items already contain commas (&ldquo;Hiromi Uehara, from Japan&rdquo;), and the later items are separated by a semicolon (&ldquo;mbalax; and&rdquo;), so the items must be separated by semicolons: &ldquo;Japan;&rdquo;.")

Q(id="RW-SEC-17", domain="SEC", skill="Boundaries", diff=2, rule="however",
  passage=f"<p>The bridge's original wooden supports had rotted after decades of exposure to salt {B} engineers replaced them with steel beams coated in a corrosion-resistant epoxy.</p>",
  stem=CONV, choices=["water, therefore,", "water; therefore,", "water therefore", "water, therefore"], answer="B",
  explain="&ldquo;Therefore&rdquo; can't join two complete sentences with commas alone; a semicolon must come before it: &ldquo;water; therefore,&rdquo;.")

Q(id="RW-SEC-18", domain="SEC", skill="Boundaries", diff=2, rule="possessive",
  passage=f"<p>Each spring, the city's community gardens open {B} gates to new volunteers, who are assigned plots in the order in which their applications were received.</p>",
  stem=CONV, choices=["its", "it's", "their", "they're"], answer="C",
  explain="The pronoun refers to &ldquo;gardens&rdquo; (plural) and shows possession: &ldquo;their&rdquo;. &ldquo;It's&rdquo; and &ldquo;they're&rdquo; are contractions (it is, they are).")

Q(id="RW-SEC-19", domain="SEC", skill="Boundaries", diff=3, rule="possessive",
  passage=f"<p>Two independent groups, one in Canada and one in Japan, studied how sleep affects memory. Both research {B} findings suggest that sleep helps consolidate memories formed during the day.</p>",
  stem=CONV, choices=["team's", "teams", "teams'", "teams's"], answer="C",
  explain="&ldquo;Both&rdquo; means more than one team, and the findings belong to them, so the plural possessive is needed: &ldquo;teams'&rdquo;. &ldquo;Teams&rdquo; with no apostrophe isn't possessive, and &ldquo;team's&rdquo; is singular.")

Q(id="RW-SEC-20", domain="SEC", skill="Boundaries", diff=2, rule="possessive",
  passage=f"<p>Andean condors are among the largest flying birds in the world. The Andean {B} wings, which can span ten feet, allow it to soar for hours over the mountains while barely flapping.</p>",
  stem=CONV, choices=["condors", "condors'", "condor's", "condors's"], answer="C",
  explain="&ldquo;Allow it&rdquo; tells you there is one condor, and the wings belong to it: singular possessive &ldquo;condor's&rdquo;.")

# ====================================================================== Form, Structure, and Sense
Q(id="RW-SEC-21", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="agreement",
  passage=f"<p>The collection of ancient manuscripts, many of which were rescued from flooded monastery libraries, {B} now housed in a climate-controlled archive at the university.</p>",
  stem=CONV, choices=["are", "were", "is", "have been"], answer="C",
  explain="Cross out &ldquo;of ancient manuscripts&rdquo; and the extra information between the commas: the subject is &ldquo;The collection,&rdquo; which is singular. &ldquo;Now&rdquo; signals present tense: &ldquo;is&rdquo;.")

Q(id="RW-SEC-22", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="agreement",
  passage=f"<p>Astronomers have long suspected that most large galaxies have enormous black holes at their centers, and our own galaxy is no exception. Near the center of the Milky Way {B} a supermassive black hole, Sagittarius A*, with a mass about four million times that of the Sun.</p>",
  stem=CONV, choices=["lie", "lies", "are lying", "have lain"], answer="B",
  explain="The sentence is inverted: the subject comes after the verb. What lies near the center? &ldquo;a supermassive black hole,&rdquo; which is singular: &ldquo;lies&rdquo;.")

Q(id="RW-SEC-23", domain="SEC", skill="Form, Structure, and Sense", diff=2, rule="agreement",
  passage=f"<p>Bird counts depend on volunteers who can identify species quickly and accurately, often without ever seeing the birds. Each of the volunteers who participated in last winter's bird count {B} trained in advance to identify local species by their songs and calls.</p>",
  stem=CONV, choices=["were", "are", "was", "have been"], answer="C",
  explain="The subject is &ldquo;Each,&rdquo; which is singular (&ldquo;of the volunteers&rdquo; is a prepositional phrase), and &ldquo;last winter&rdquo; signals past tense: &ldquo;was&rdquo;.")

Q(id="RW-SEC-24", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="agreement",
  passage=f"<p>The error went unnoticed through three printings: neither the author nor her editors {B} aware that one of the maps in the book placed a river on the wrong side of a mountain range.</p>",
  stem=CONV, choices=["was", "were", "is", "has been"], answer="B",
  explain="With &ldquo;neither &hellip; nor,&rdquo; the verb agrees with the nearer subject, &ldquo;her editors,&rdquo; which is plural. The story is in the past (&ldquo;went unnoticed&rdquo;): &ldquo;were&rdquo;.")

Q(id="RW-SEC-25", domain="SEC", skill="Form, Structure, and Sense", diff=2, rule="pronoun",
  passage=f"<p>When the company released {B} first electric delivery truck, critics doubted that the vehicle could travel far enough on a single charge to be practical for long routes.</p>",
  stem=CONV, choices=["their", "its", "it's", "they're"], answer="B",
  explain="&ldquo;The company&rdquo; is a single organization, so the possessive pronoun is &ldquo;its&rdquo;. &ldquo;It's&rdquo; means &ldquo;it is.&rdquo;")

Q(id="RW-SEC-26", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="pronoun",
  passage=f"<p>Sea otters use rocks as tools to crack open clams and sea urchins, and some otters keep a favorite rock tucked in a pouch of loose skin under {B} forelegs for repeated use.</p>",
  stem=CONV, choices=["its", "their", "it's", "they're"], answer="B",
  explain="The pronoun refers to &ldquo;some otters,&rdquo; which is plural, and shows possession: &ldquo;their&rdquo;.")

Q(id="RW-SEC-27", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="pronoun",
  passage=f"<p>Researchers compared the nests of house sparrows living in cities with the nests of house sparrows living on farms. They found that {B} contained far more synthetic materials, such as plastic and string.</p>",
  stem=CONV, choices=["they", "it", "the city nests", "this"], answer="C",
  explain="&ldquo;They&rdquo; could mean the city nests, the farm nests, or even the researchers, so the pronoun is unclear. &ldquo;It&rdquo; and &ldquo;this&rdquo; don't match a plural noun. Only &ldquo;the city nests&rdquo; is clear.")

Q(id="RW-SEC-28", domain="SEC", skill="Form, Structure, and Sense", diff=2, rule="tense",
  passage=f"<p>Returning to his laboratory in September 1928 after a vacation, Alexander Fleming noticed that a mold growing on one of his culture plates {B} the bacteria around it, an observation that led to the discovery of penicillin.</p>",
  stem=CONV, choices=["kills", "has killed", "had killed", "will kill"], answer="C",
  explain="The killing happened before Fleming noticed it (a past event), so the past perfect fits the timeline: &ldquo;had killed&rdquo;.")

Q(id="RW-SEC-29", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="tense",
  passage=f"<p>Since its launch in 1990, the Hubble Space Telescope {B} more than 1.5 million observations, and astronomers have used its data in tens of thousands of scientific papers.</p>",
  stem=CONV, choices=["made", "has made", "makes", "had made"], answer="B",
  explain="&ldquo;Since 1990&rdquo; describes something that started in the past and continues now, which calls for the present perfect: &ldquo;has made&rdquo;. The parallel verb &ldquo;have used&rdquo; confirms it.")

Q(id="RW-SEC-30", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="tense",
  passage=f"<p>Before the printing press arrived in Europe in the mid-1400s, scribes copied books by hand, a process that often {B} months of work for a single volume.</p>",
  stem=CONV, choices=["takes", "has taken", "took", "will take"], answer="C",
  explain="The passage describes the past (&ldquo;Before &hellip; the mid-1400s, scribes copied&rdquo;), so the simple past matches: &ldquo;took&rdquo;.")

Q(id="RW-SEC-31", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="modifier",
  passage=f"<p>Frida Kahlo is among the most celebrated painters of the twentieth century, and many of her best-known works are self-portraits. Born in 1907 in Coyoac&aacute;n, Mexico, {B}</p>",
  stem=CONV,
  choices=["Frida Kahlo's self-portraits explore themes of identity, pain, and Mexican culture.",
           "the self-portraits of Frida Kahlo explore themes of identity, pain, and Mexican culture.",
           "Frida Kahlo painted self-portraits exploring themes of identity, pain, and Mexican culture.",
           "identity, pain, and Mexican culture are themes explored in Frida Kahlo's self-portraits."],
  answer="C",
  explain="Who was born in 1907? Frida Kahlo, so her name must come right after the comma, as in &ldquo;Frida Kahlo painted self-portraits exploring themes of identity, pain, and Mexican culture.&rdquo; In the other choices, the self-portraits or the themes would be the ones &ldquo;born.&rdquo; Note that &ldquo;Frida Kahlo's self-portraits&rdquo; makes the self-portraits the subject, not Kahlo.")

Q(id="RW-SEC-32", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="modifier",
  passage=f"<p>Male humpback whales in a population sing a shared song, but the song does not stay the same from one season to the next. After analyzing thousands of hours of underwater recordings, {B}</p>",
  stem=CONV,
  choices=["the researchers concluded that humpback whale songs change gradually from year to year.",
           "humpback whale songs were found by the researchers to change gradually from year to year.",
           "the conclusion of the researchers was that humpback whale songs change gradually from year to year.",
           "gradual changes from year to year were found in humpback whale songs."],
  answer="A",
  explain="Who analyzed the recordings? The researchers, so they must come right after the comma: &ldquo;the researchers concluded that humpback whale songs change gradually from year to year.&rdquo; The songs, the conclusion, and the changes didn't analyze anything.")

Q(id="RW-SEC-33", domain="SEC", skill="Form, Structure, and Sense", diff=2, rule="modifier",
  passage=f"<p>The Great Wall is not a single continuous structure but a network of walls and fortifications built and connected by different dynasties. Stretching thousands of miles across northern China, {B}</p>",
  stem=CONV,
  choices=["the Great Wall's construction took place over many centuries.",
           "the Great Wall was built and rebuilt over many centuries.",
           "many centuries were needed to build the Great Wall.",
           "builders worked on the Great Wall for many centuries."],
  answer="B",
  explain="What stretches across northern China? The Great Wall itself, as in &ldquo;the Great Wall was built and rebuilt over many centuries.&rdquo; Its construction, the centuries, and the builders don't stretch across China.")

Q(id="RW-SEC-34", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="verbform",
  passage=f"<p>The coelacanth, a deep-sea fish that scientists once believed had gone extinct around the time of the dinosaurs, {B} rediscovered off the coast of South Africa in 1938.</p>",
  stem=CONV, choices=["being", "was", "having been", "to be"], answer="B",
  explain="The subject &ldquo;The coelacanth&rdquo; needs a main verb after the long interruption. Only &ldquo;was&rdquo; is a finite verb; the other choices leave the sentence a fragment.")

Q(id="RW-SEC-35", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="verbform",
  passage=f"<p>In her 1962 book <i>Silent Spring</i>, Rachel Carson documented the harmful effects of pesticides such as DDT on birds and other wildlife, {B} public concern that contributed to a United States ban on DDT's agricultural use in 1972.</p>",
  stem=CONV, choices=["sparked", "sparking", "she sparked", "it sparked"], answer="B",
  explain="The sentence already has a complete clause, so the result is attached as a modifying phrase: &ldquo;sparking&rdquo;. &ldquo;She sparked&rdquo; and &ldquo;it sparked&rdquo; create comma splices. &ldquo;Sparked&rdquo; would need &ldquo;and&rdquo; to form a compound verb.")

Q(id="RW-SEC-36", domain="SEC", skill="Form, Structure, and Sense", diff=2, rule="verbform",
  passage=f"<p>The park's volunteer program trains participants to monitor water quality in the streams, {B} invasive plants along the trails, and to educate visitors about local wildlife.</p>",
  stem=CONV, choices=["removing", "to remove", "remove", "the removal of"], answer="B",
  explain="The list items must match: &ldquo;to monitor &hellip;, to remove &hellip;, and to educate.&rdquo; Since the last item keeps &ldquo;to,&rdquo; the middle one must too: &ldquo;to remove&rdquo;.")

# ====================================================================== Transitions
Q(id="RW-EXP-01", domain="EXPR", skill="Transitions", diff=2, rule="transitions",
  passage=f"<p>Many desert plants survive long droughts by storing water in thick, fleshy stems. {B} the saguaro cactus can expand its pleated trunk like an accordion to hold as much as 200 gallons of water after a heavy rain.</p>",
  stem=TRANS, choices=["For example,", "However,", "Nevertheless,", "In contrast,"], answer="A",
  explain="The saguaro is a specific case of the general claim about desert plants storing water, so the relationship is example: &ldquo;For example,&rdquo;.")

Q(id="RW-EXP-02", domain="EXPR", skill="Transitions", diff=3, rule="transitions",
  passage=f"<p>Because octopuses are solitary animals that rarely interact, scientists long assumed that they had little capacity to learn from one another. {B} a 1992 study found that octopuses could learn to choose an object of a particular color simply by watching another octopus do so.</p>",
  stem=TRANS, choices=["Similarly,", "Therefore,", "However,", "Moreover,"], answer="C",
  explain="The study's finding contradicts the long-held assumption, so the relationship is contrast: &ldquo;However,&rdquo;.")

Q(id="RW-EXP-03", domain="EXPR", skill="Transitions", diff=3, rule="transitions",
  passage=f"<p>The city's new subway line opened two years late and cost nearly twice its original budget. {B} ridership in its first year exceeded projections by 40 percent, and city officials now describe the project as a success.</p>",
  stem=TRANS, choices=["Still,", "Consequently,", "For instance,", "Likewise,"], answer="A",
  explain="The second sentence acknowledges the problems but presents a positive outcome despite them. That's a concession: &ldquo;Still,&rdquo;. The delays didn't <i>cause</i> high ridership, so &ldquo;Consequently&rdquo; is wrong.")

Q(id="RW-EXP-04", domain="EXPR", skill="Transitions", diff=2, rule="transitions",
  passage=f"<p>Some species of bamboo can grow more than 30 inches in a single day. {B} these species can reach their full height in just a few months, far faster than any tree.</p>",
  stem=TRANS, choices=["As a result,", "In contrast,", "Nonetheless,", "Similarly,"], answer="A",
  explain="Reaching full height in a few months is a consequence of growing so fast each day, so the relationship is cause and effect: &ldquo;As a result,&rdquo;.")

Q(id="RW-EXP-05", domain="EXPR", skill="Transitions", diff=1, rule="transitions",
  passage=f"<p>To make paper, early Chinese craftspeople first soaked plant fibers, such as mulberry bark, in water and pounded them into a pulp. {B} they spread the pulp evenly over a screen and left it to dry into thin sheets.</p>",
  stem=TRANS, choices=["Next,", "For example,", "Instead,", "Conversely,"], answer="A",
  explain="The text describes steps in order (&ldquo;first &hellip;&rdquo;), so the next step needs a sequence transition: &ldquo;Next,&rdquo;.")

Q(id="RW-EXP-06", domain="EXPR", skill="Transitions", diff=3, rule="transitions",
  passage=f"<p>Honeybees perform a &ldquo;waggle dance&rdquo; that tells other bees in the hive where to find food. {B} many ant species lay down chemical trails that guide their nestmates to food sources.</p>",
  stem=TRANS, choices=["Similarly,", "As a result,", "In other words,", "For instance,"], answer="A",
  explain="Ants and honeybees are separate cases of the same behavior: insects guiding nestmates to food. That's a parallel, so &ldquo;Similarly,&rdquo;. The ants aren't an example of the bee dance, and they aren't caused by it.")

Q(id="RW-EXP-07", domain="EXPR", skill="Transitions", diff=3, rule="transitions",
  passage=f"<p>The theory of plate tectonics holds that Earth's outer shell is divided into large rigid plates that move slowly over the hotter, softer layer beneath them. {B} the continents are not fixed in place but drift, typically a few centimeters each year.</p>",
  stem=TRANS, choices=["In other words,", "Nevertheless,", "By contrast,", "Previously,"], answer="A",
  explain="The second sentence restates the theory's meaning in plainer terms, so &ldquo;In other words,&rdquo;.")

# ====================================================================== Rhetorical synthesis
Q(id="RW-EXP-08", domain="EXPR", skill="Rhetorical Synthesis", diff=2, rule="synthesis",
  passage=notes(["Mary Anning (1799&ndash;1847) was a fossil collector in Lyme Regis, England.",
                 "In 1811&ndash;1812, she and her brother found the first ichthyosaur skeleton to be correctly identified.",
                 "In 1823, she discovered the first complete plesiosaur skeleton.",
                 "Because she was a woman, she was not allowed to join the Geological Society of London."]),
  stem="The student wants to emphasize an obstacle Anning faced despite her achievements. " + SYN,
  choices=["Mary Anning, who lived from 1799 to 1847, collected fossils in Lyme Regis, England.",
           "Although Anning discovered the first complete plesiosaur skeleton, she was barred from the Geological Society of London because she was a woman.",
           "In 1811&ndash;1812, Anning and her brother found the first correctly identified ichthyosaur skeleton.",
           "Anning made important discoveries in 1811&ndash;1812 and in 1823."],
  answer="B",
  explain="The goal asks for an <i>obstacle</i> she faced <i>despite</i> her achievements. Only the second choice pairs an achievement with an obstacle (&ldquo;Although&hellip; she was barred&rdquo;). The others are accurate but list only facts or achievements.")

Q(id="RW-EXP-09", domain="EXPR", skill="Rhetorical Synthesis", diff=3, rule="synthesis",
  passage=notes(["The Svalbard Global Seed Vault is a secure facility built into a mountain on a Norwegian island in the Arctic.",
                 "It stores duplicate seed samples from gene banks around the world.",
                 "It opened in 2008.",
                 "It holds more than 1.2 million seed samples.",
                 "Its purpose is to protect the world's crop diversity in case of disasters."]),
  stem="The student wants to introduce the Svalbard Global Seed Vault to an audience unfamiliar with it. " + SYN,
  choices=["Since 2008, the Svalbard Global Seed Vault's collection has grown to more than 1.2 million samples.",
           "The vault's seeds are duplicates of samples held by gene banks around the world.",
           "The Svalbard Global Seed Vault, a secure facility on a Norwegian Arctic island, stores backup seed samples from around the world to protect crop diversity in case of disasters.",
           "Opened in 2008, the vault is located on an island in the Arctic."],
  answer="C",
  explain="An unfamiliar audience needs to know <i>what</i> the vault is and <i>why</i> it exists. Only the third choice gives both: a secure facility that stores backup seeds to protect crop diversity. The others assume the reader already knows what the vault is.")

Q(id="RW-EXP-10", domain="EXPR", skill="Rhetorical Synthesis", diff=2, rule="synthesis",
  passage=notes(["The Hubble Space Telescope was launched in 1990.",
                 "Hubble observes mainly visible and ultraviolet light.",
                 "Hubble orbits Earth about 540 kilometers above the surface.",
                 "The James Webb Space Telescope was launched in 2021.",
                 "Webb observes mainly infrared light.",
                 "Webb orbits the Sun about 1.5 million kilometers from Earth."]),
  stem="The student wants to emphasize a difference in where the two telescopes are located. " + SYN,
  choices=["Hubble was launched in 1990, and Webb was launched in 2021.",
           "Whereas Hubble orbits Earth about 540 kilometers above the surface, Webb orbits the Sun about 1.5 million kilometers from Earth.",
           "Hubble observes mainly visible and ultraviolet light, while Webb observes mainly infrared light.",
           "Both Hubble and Webb are space telescopes that orbit far above Earth's surface."],
  answer="B",
  explain="The goal is a difference in <i>location</i>. The second choice contrasts their positions (&ldquo;Whereas&rdquo;). The first choice gives a difference in launch dates, the third a difference in light, and the fourth a similarity.")

Q(id="RW-EXP-11", domain="EXPR", skill="Rhetorical Synthesis", diff=2, rule="synthesis",
  passage=notes(["The Rosetta Stone was found in 1799 near the town of Rashid (Rosetta) in Egypt.",
                 "It is inscribed with the same decree in three scripts: hieroglyphic, Demotic, and ancient Greek.",
                 "Scholars could already read ancient Greek.",
                 "In 1822, Jean-Fran&ccedil;ois Champollion announced that he had deciphered Egyptian hieroglyphs.",
                 "The stone has been displayed at the British Museum since 1802."]),
  stem="The student wants to explain why the Rosetta Stone helped scholars decipher hieroglyphs. " + SYN,
  choices=["The Rosetta Stone, found in 1799, has been displayed at the British Museum since 1802.",
           "In 1822, Champollion announced that he had deciphered Egyptian hieroglyphs.",
           "The Rosetta Stone is inscribed in hieroglyphic, Demotic, and ancient Greek scripts.",
           "Because the Rosetta Stone carries the same decree in hieroglyphs and in ancient Greek, a language scholars could already read, it gave them a key for decoding the hieroglyphs."],
  answer="D",
  explain="The goal asks <i>why</i> it helped. Only the last choice gives the reason: the same text appears in a language scholars could already read. The third choice lists the scripts but never says why that mattered.")

Q(id="RW-EXP-12", domain="EXPR", skill="Rhetorical Synthesis", diff=3, rule="synthesis",
  passage=notes(["Emily Dickinson (1830&ndash;1886) published fewer than a dozen poems during her lifetime.",
                 "After her death, her sister found nearly 1,800 poems among her belongings.",
                 "Franz Kafka (1883&ndash;1924) asked his friend Max Brod to burn his unpublished manuscripts after his death.",
                 "Brod instead published them, including the novel <i>The Trial</i>."]),
  stem="The student wants to emphasize a similarity between Dickinson and Kafka. " + SYN,
  choices=["Dickinson published fewer than a dozen poems, while Kafka wanted his manuscripts burned.",
           "Both Dickinson and Kafka had much of their writing published only after their deaths.",
           "Kafka's friend Max Brod published <i>The Trial</i> instead of burning it.",
           "Dickinson was born in 1830, more than fifty years before Kafka was born in 1883."],
  answer="B",
  explain="Only the second choice states something the two writers <i>share</i> (&ldquo;Both&hellip;&rdquo;): much of their writing was published only after they died, which both sets of notes support. The first and fourth choices present differences, and the third is about Kafka alone.")

Q(id="RW-EXP-13", domain="EXPR", skill="Rhetorical Synthesis", diff=2, rule="synthesis",
  passage=notes(["A pangram is a sentence that uses every letter of the alphabet at least once.",
                 "&ldquo;The quick brown fox jumps over the lazy dog&rdquo; is a well-known pangram.",
                 "Typists have used it to test typewriters and keyboards.",
                 "&ldquo;Sphinx of black quartz, judge my vow&rdquo; is a pangram with only 29 letters."]),
  stem="The student wants to define the term &ldquo;pangram&rdquo; and provide an example. " + SYN,
  choices=["&ldquo;The quick brown fox jumps over the lazy dog&rdquo; has been used to test typewriters and keyboards.",
           "&ldquo;Sphinx of black quartz, judge my vow&rdquo; contains only 29 letters.",
           "A pangram, such as &ldquo;The quick brown fox jumps over the lazy dog,&rdquo; is a sentence that uses every letter of the alphabet at least once.",
           "Pangrams are useful for testing typewriters and keyboards."],
  answer="C",
  explain="The goal has two parts, a definition and an example. Only the third choice does both. The others give an example or a use without defining the term.")

# ====================================================================== Craft and Structure
Q(id="RW-CRF-01", domain="CRAFT", skill="Words in Context", diff=2, rule="wordsincontext",
  passage=f"<p>Although the senator's speech ran for nearly an hour, her central argument was {B} she believed that public libraries deserved more funding, and she said so plainly and repeatedly.</p>",
  stem=WORD, choices=["convoluted", "straightforward", "ambiguous", "tentative"], answer="B",
  explain="The colon introduces a description of the argument: she said it &ldquo;plainly and repeatedly.&rdquo; Your own word might be &ldquo;simple,&rdquo; which matches &ldquo;straightforward.&rdquo; &ldquo;Although&rdquo; contrasts the argument with the long speech.")

Q(id="RW-CRF-02", domain="CRAFT", skill="Words in Context", diff=3, rule="wordsincontext",
  passage=f"<p>When the composer's first symphony premiered, many critics found its dissonant chords jarring. Over the following decades, however, audiences came to {B} those same chords as the most distinctive feature of her style rather than as a flaw.</p>",
  stem=WORD, choices=["tolerate", "appreciate", "disregard", "imitate"], answer="B",
  explain="&ldquo;However&rdquo; signals a shift from the critics' negative view, and &ldquo;the most distinctive feature &hellip; rather than &hellip; a flaw&rdquo; is positive. &ldquo;Appreciate&rdquo; fits. &ldquo;Tolerate&rdquo; is too weak: tolerating something still treats it as a flaw.")

Q(id="RW-CRF-03", domain="CRAFT", skill="Words in Context", diff=3, rule="wordsincontext",
  passage="<p>The photographer's large prints of glaciers collapsing into the sea are arresting: in the gallery, visitors often stand in front of a single image for several minutes without moving on.</p>",
  stem="As used in the text, what does the word &ldquo;arresting&rdquo; most nearly mean?",
  choices=["stopping", "captivating", "detaining", "alarming"], answer="B",
  explain="The colon explains the word: visitors are held by the images for minutes. That means they are &ldquo;captivating&rdquo;. &ldquo;Stopping&rdquo; and &ldquo;detaining&rdquo; are the common-meaning traps.")

Q(id="RW-CRF-04", domain="CRAFT", skill="Words in Context", diff=3, rule="wordsincontext",
  passage=f"<p>Reporters hoping for a clear answer were disappointed: the committee's report was notably {B} offering no firm recommendations and hedging nearly every claim with qualifications.</p>",
  stem=WORD, choices=["equivocal,", "incisive,", "exhaustive,", "partisan,"], answer="A",
  explain="The report offered &ldquo;no firm recommendations&rdquo; and hedged every claim, so it was vague and noncommittal: &ldquo;equivocal,&rdquo;. &ldquo;Incisive&rdquo; means the opposite (sharp and clear).")

Q(id="RW-CRF-05", domain="CRAFT", skill="Text Structure and Purpose", diff=3, rule="structure",
  passage="<p>In April 1815, Mount Tambora in present-day Indonesia produced the largest volcanic eruption in recorded history. The ash and sulfur gases it sent into the atmosphere lowered temperatures around the world, and the following year, 1816, became known in parts of Europe and North America as &ldquo;the Year Without a Summer.&rdquo; Snow fell in New England in June, and crops failed across both continents. Some historians have even linked the gloomy weather to the creation of Mary Shelley's <i>Frankenstein</i>, which she began writing that summer while kept indoors by cold, stormy weather near Lake Geneva.</p>",
  stem="Which choice best describes the function of the last sentence in the overall structure of the text?",
  choices=["It presents a cultural development that may be connected to the climate effects described earlier.",
           "It challenges the claim that the eruption affected global temperatures.",
           "It explains the scientific process by which volcanic gases cool the atmosphere.",
           "It provides an additional example of the crop failures mentioned in the previous sentence."],
  answer="A",
  explain="The last sentence moves from weather effects to a novel that may have been influenced by them, so it presents a cultural development possibly connected to the climate effects. It doesn't challenge anything, explain science, or concern crops.")

Q(id="RW-CRF-06", domain="CRAFT", skill="Text Structure and Purpose", diff=2, rule="structure",
  passage="<p>Many people believe that sharks must swim constantly in order to breathe. This is true of some species, such as the great white shark, which relies on water flowing over its gills as it moves forward. But other sharks, including the nurse shark, can actively pump water over their gills while resting motionless on the seafloor.</p>",
  stem="Which choice best describes the overall structure of the text?",
  choices=["It presents a common belief and then qualifies it by noting that the belief does not apply to all sharks.",
           "It describes a debate among scientists and then explains how the debate was resolved.",
           "It explains a biological process step by step, from beginning to end.",
           "It compares two theories about shark breathing and argues that one is correct."],
  answer="A",
  explain="The text states a belief, confirms it for some species, then gives an exception (&ldquo;But other sharks&hellip;&rdquo;). That pattern is qualifying a common belief. No scientists debate, no steps are listed, and no theories are compared.")

Q(id="RW-CRF-07", domain="CRAFT", skill="Cross-Text Connections", diff=2, rule="crosstext",
  passage="<p class='txtlabel'>Text 1</p><p>Some economists argue that raising the minimum wage reduces employment. When labor becomes more expensive, they reason, businesses respond by hiring fewer workers.</p>"
          "<p class='txtlabel'>Text 2</p><p>In a widely cited 1994 study, economists David Card and Alan Krueger compared fast-food restaurants in New Jersey, which had just raised its minimum wage, with restaurants in neighboring Pennsylvania, which had not. They found no evidence that the increase reduced employment in New Jersey.</p>",
  stem="Based on the texts, how would Card and Krueger (Text 2) most likely respond to the reasoning in Text 1?",
  choices=["By pointing to evidence that, in at least one case, a minimum wage increase did not reduce employment.",
           "By agreeing that higher labor costs always lead businesses to hire fewer workers.",
           "By arguing that businesses, rather than governments, should set minimum wages.",
           "By claiming that the fast-food industry is unaffected by changes in labor costs."],
  answer="A",
  explain="Card and Krueger's study is a counterexample to Text 1's prediction, so they would point to evidence that, in one case, the increase did not reduce employment. Their study doesn't support the &ldquo;always&rdquo; claim, says nothing about who should set wages, and doesn't claim that the industry is unaffected in general.")

Q(id="RW-CRF-08", domain="CRAFT", skill="Cross-Text Connections", diff=3, rule="crosstext",
  passage="<p class='txtlabel'>Text 1</p><p>For much of the twentieth century, many paleontologists pictured dinosaurs as sluggish, cold-blooded reptiles that dragged their tails along the ground.</p>"
          "<p class='txtlabel'>Text 2</p><p>The discovery of <i>Deinonychus</i> in the 1960s changed that picture. With its lightweight build and a large, curved claw on each foot that seemed suited to active hunting, <i>Deinonychus</i> led paleontologist John Ostrom to argue that at least some dinosaurs were agile, energetic animals.</p>",
  stem="Based on the texts, how would John Ostrom (Text 2) most likely describe the view presented in Text 1?",
  choices=["As incomplete, because it does not account for evidence that some dinosaurs were active and agile.",
           "As accurate for every dinosaur except <i>Deinonychus</i>.",
           "As supported by the discovery of <i>Deinonychus</i>.",
           "As irrelevant to questions about how dinosaurs behaved."],
  answer="A",
  explain="Ostrom argued that &ldquo;at least some&rdquo; dinosaurs were agile, which contradicts the sluggish picture for those species. So he'd call the older view incomplete. &ldquo;Every dinosaur except <i>Deinonychus</i>&rdquo; is too narrow; he generalized to some dinosaurs.")

# ====================================================================== Information and Ideas
Q(id="RW-INF-01", domain="INFO", skill="Command of Evidence", diff=3, rule="evidence",
  passage="<p>&ldquo;&lsquo;Hope&rsquo; is the thing with feathers&rdquo; is an 1861 poem by Emily Dickinson. In the poem, the speaker suggests that hope asks nothing of the person who holds it, even in the most desperate times.</p>",
  stem="Which quotation from the poem most effectively illustrates the claim?",
  choices=["&ldquo;&lsquo;Hope&rsquo; is the thing with feathers - / That perches in the soul -&rdquo;",
           "&ldquo;And sings the tune without the words - / And never stops - at all -&rdquo;",
           "&ldquo;I've heard it in the chillest land - / And on the strangest Sea -&rdquo;",
           "&ldquo;Yet - never - in Extremity, / It asked a crumb - of me.&rdquo;"],
  answer="D",
  explain="The claim has two parts: hope <i>asks nothing</i>, and that holds <i>even in the most desperate times</i>. &ldquo;Yet - never - in Extremity, / It asked a crumb - of me.&rdquo; matches both: &ldquo;Extremity&rdquo; is the most desperate time, and hope never &ldquo;asked a crumb.&rdquo; The quotation about the chillest land shows hope present in hard places but says nothing about asking; &ldquo;never stops&rdquo; is about persistence.")

Q(id="RW-INF-02", domain="INFO", skill="Command of Evidence", diff=2, rule="evidence",
  passage="<p>American crows live in family groups and often band together to harass predators that threaten them. Researchers hypothesized that American crows can recognize individual human faces and remember people who have threatened them.</p>",
  stem="Which finding, if true, would most directly support the researchers' hypothesis?",
  choices=["Crows that had been captured by researchers wearing a particular mask scolded people wearing that mask years later but ignored people wearing a different mask.",
           "Crows often gather in large groups to roost during the winter months.",
           "Crows have been observed using sticks as tools to pull insects out of tree bark.",
           "Crows frequently scold hawks and owls that fly near their nests."],
  answer="A",
  explain="Only the mask finding shows crows telling apart particular faces <i>and</i> remembering a threat: they react to one face but not another, years later. The other findings are true facts about crows but don't involve recognizing humans.")

Q(id="RW-INF-03", domain="INFO", skill="Command of Evidence", diff=3, rule="quant",
  passage="<p>A student examining results from four community gardens in a city's pilot program claims that larger plots did not necessarily produce larger harvests.</p>"
          "<table class='data'><tr><th>Garden</th><th>Plot area (square meters)</th><th>Harvest (kilograms)</th></tr>"
          "<tr><td>A</td><td>40</td><td>120</td></tr><tr><td>B</td><td>55</td><td>210</td></tr>"
          "<tr><td>C</td><td>70</td><td>180</td></tr><tr><td>D</td><td>30</td><td>95</td></tr></table>",
  stem="Which choice best describes data from the table that support the student's claim?",
  choices=["Garden D had both the smallest plot area and the smallest harvest.",
           "Garden C had the largest plot area but a smaller harvest than Garden B.",
           "Garden B produced the largest harvest of the four gardens.",
           "Garden A had a larger plot area than Garden C."],
  answer="B",
  explain="To show that bigger doesn't always mean more, you need a larger plot with a <i>smaller</i> harvest: Garden C had the largest plot area but a smaller harvest than Garden B (70 m&sup2; and 180 kg vs. 55 m&sup2; and 210 kg). The Garden D choice is accurate but fits the opposite pattern, the Garden B choice is accurate but irrelevant, and the Garden A choice is false.")

Q(id="RW-INF-04", domain="INFO", skill="Command of Evidence", diff=3, rule="quant",
  passage="<p>A city's transportation department surveyed residents in 2010 and 2020 about how they made their daily trips. An analyst claims that the increase in bicycling accounted for most of the decline in car trips.</p>"
          "<table class='data'><tr><th>Mode</th><th>2010 (% of trips)</th><th>2020 (% of trips)</th></tr>"
          "<tr><td>Car</td><td>72</td><td>64</td></tr><tr><td>Bus</td><td>15</td><td>14</td></tr>"
          "<tr><td>Bicycle</td><td>3</td><td>9</td></tr><tr><td>Walking</td><td>10</td><td>13</td></tr></table>",
  stem="Which choice best describes data from the table that support the analyst's claim?",
  choices=["The share of trips made by walking increased from 10 percent to 13 percent.",
           "The share of trips made by bicycle rose by 6 percentage points, while the share made by car fell by 8 percentage points.",
           "Buses remained the second most common way to travel in both years.",
           "The share of trips made by car fell from 72 percent to 54 percent."],
  answer="B",
  explain="The claim compares the bicycle increase to the car decline. The bicycle share rose by 6 percentage points while the car share fell by 8 percentage points: 6 of the 8 points is &ldquo;most.&rdquo; The walking and bus choices are accurate but don't address the claim, and the last choice misreads 64 as 54.")

Q(id="RW-INF-05", domain="INFO", skill="Inferences", diff=3, rule="inference",
  passage=f"<p>Many crops rely on bees for pollination. Tomato flowers release pollen most effectively when they are vibrated, a process called buzz pollination. Bumblebees grab the flowers and vibrate their flight muscles to shake the pollen loose, but honeybees cannot perform buzz pollination. In greenhouse studies, tomato plants visited by bumblebees produced larger fruit than plants left to pollinate without bees. These findings suggest that {B}</p>",
  stem=INFER,
  choices=["greenhouse growers seeking large tomatoes may benefit more from using bumblebees than from using honeybees.",
           "honeybees damage tomato flowers when they attempt to collect pollen.",
           "all fruit crops require buzz pollination to produce large fruit.",
           "tomato plants cannot produce any fruit without bees."],
  answer="A",
  explain="Bumblebees can buzz-pollinate, honeybees can't, and buzz pollination is linked to larger tomatoes. So growers seeking large tomatoes may benefit more from bumblebees. The other choices overreach: nothing suggests damage, &ldquo;all fruit crops&rdquo; goes beyond tomatoes, and the plants without bees still produced fruit.")

Q(id="RW-INF-06", domain="INFO", skill="Inferences", diff=3, rule="inference",
  passage=f"<p>At Jerimalai, a cave site in East Timor, archaeologists found the bones of tuna and other deep-ocean fish in layers dated to about 42,000 years ago. Catching such fish requires boats and specialized techniques, such as fishing in open water far from shore. The archaeologists therefore concluded that {B}</p>",
  stem=INFER,
  choices=["people living near the site had developed advanced seafaring and fishing skills by about 42,000 years ago.",
           "the cave was abandoned because the people living there overfished the surrounding waters.",
           "tuna lived much closer to shore 42,000 years ago than they do today.",
           "Jerimalai was the first place in the world where people ate fish."],
  answer="A",
  explain="If catching deep-ocean fish requires boats and specialized techniques, and those fish were caught 42,000 years ago, then people had seafaring skills by then. The other choices aren't supported: nothing mentions abandonment, the text doesn't discuss changes in tuna habitat, and &ldquo;the first place in the world&rdquo; overreaches.")

Q(id="RW-INF-07", domain="INFO", skill="Inferences", diff=2, rule="inference",
  passage=f"<p>Mercury is the planet closest to the Sun, and Venus is the second closest. Since Venus is farther from the Sun and is covered by thick clouds that reflect most incoming sunlight, one might expect it to be cooler than Mercury. However, Venus's dense carbon dioxide atmosphere traps heat so effectively that {B}</p>",
  stem=INFER,
  choices=["Venus's surface is hotter than Mercury's, even though Venus is farther from the Sun.",
           "Venus reflects less sunlight than any other planet.",
           "Mercury has a thicker atmosphere than Venus does.",
           "Venus is actually closer to the Sun than Mercury is."],
  answer="A",
  explain="&ldquo;However&rdquo; signals that the expectation (Venus is cooler) is wrong, and &ldquo;traps heat so effectively&rdquo; explains why: Venus's surface is hotter than Mercury's. The second choice contradicts the &ldquo;thick clouds&rdquo; that reflect light, and the last choice contradicts the first sentence.")

Q(id="RW-INF-08", domain="INFO", skill="Central Ideas and Details", diff=2, rule="mainidea",
  passage="<p>Tardigrades are microscopic animals that can survive conditions that would kill most other life forms. When their surroundings dry out, they curl into a dehydrated state called a tun and slow their metabolism almost to a stop. In this state, tardigrades have survived extreme cold, intense radiation, and even, in a 2007 experiment, exposure to the vacuum of space, reviving once they were rehydrated.</p>",
  stem="Which choice best states the main idea of the text?",
  choices=["Tardigrades can survive extreme conditions by entering a dormant, dehydrated state.",
           "Tardigrades were sent into space as part of an experiment in 2007.",
           "Most life forms cannot survive intense radiation or extreme cold.",
           "Tardigrades are the most common animals found in dry environments."],
  answer="A",
  explain="The whole passage explains how tardigrades survive extreme conditions by entering a dormant, dehydrated state. The space experiment is one supporting detail (too narrow), the claim about most life forms is background, and &ldquo;most common&rdquo; is never stated.")

Q(id="RW-INF-09", domain="INFO", skill="Central Ideas and Details", diff=3, rule="mainidea",
  passage="<p>The following text is from Jane Austen's 1813 novel <i>Pride and Prejudice</i>.</p><p>It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.</p>",
  stem="Which choice best states the main idea of the text?",
  choices=["Local families assume that any wealthy single man who moves to the area will marry one of their daughters, whatever his own wishes may be.",
           "Wealthy single men always want to find a wife as soon as they move to a new place.",
           "The narrator believes that newcomers to a neighborhood should share their views with local families.",
           "Families in the neighborhood resent wealthy newcomers and avoid them."],
  answer="A",
  explain="The narrator is ironic: the &ldquo;truth&rdquo; is really the families' assumption, made &ldquo;however little known&rdquo; the man's own feelings may be. So the main idea is that local families assume he'll marry one of their daughters, whatever his wishes. The second choice takes the ironic first sentence literally, which is the classic trap.")

Q(id="RW-INF-10", domain="INFO", skill="Central Ideas and Details", diff=2, rule="mainidea",
  passage="<p>For centuries, sailors navigated by the stars, but determining longitude at sea remained a dangerous guessing game. Finding longitude required knowing the exact time at a reference location while far from it, and pendulum clocks failed on rolling ships. In the eighteenth century, English clockmaker John Harrison spent decades building a series of increasingly precise sea clocks, or marine chronometers. His fourth design, completed in 1759, kept time accurately enough on long voyages to make reliable longitude measurements possible.</p>",
  stem="Which choice best states the main idea of the text?",
  choices=["John Harrison's marine chronometers solved the long-standing problem of determining longitude at sea by keeping accurate time aboard ships.",
           "Sailors in earlier centuries relied mainly on the stars to navigate.",
           "Pendulum clocks were the most accurate timekeeping devices of the eighteenth century.",
           "Harrison completed his fourth sea clock design in 1759."],
  answer="A",
  explain="The text sets up a problem (longitude) and presents its solution (Harrison's accurate sea clocks). The first choice covers both. The second and fourth choices are details, and the third contradicts the text, since pendulum clocks failed at sea.")


# ====================================================================== Calibration additions
# Official practice tests 4, 7 and 10 showed Words in Context is the single most common
# question type (31 of 198, about 16%), so the bank needed more of them, plus more reading
# (purpose, inference, data) and verb tense/form items.

Q(id="RW-CRF-09", domain="CRAFT", skill="Words in Context", diff=2, rule="wordsincontext",
  passage=f"<p>Although the new documentary covers the composer's entire career, it devotes the most attention to her early years in Havana, a period that earlier biographers had largely {B} in favor of her later international fame.</p>",
  stem=WORD, choices=["emphasized", "overlooked", "celebrated", "fabricated"], answer="B",
  explain="&ldquo;In favor of her later international fame&rdquo; tells you earlier biographers focused elsewhere, so they paid little attention to the early years: &ldquo;overlooked&rdquo;. &ldquo;Emphasized&rdquo; and &ldquo;celebrated&rdquo; reverse the logic, and nothing suggests anyone made anything up.")

Q(id="RW-CRF-10", domain="CRAFT", skill="Words in Context", diff=2, rule="wordsincontext",
  passage=f"<p>The engineers' initial design for the pedestrian bridge proved remarkably {B} in load tests, it supported nearly three times the weight required by the city's safety codes without any measurable damage.</p>",
  stem=WORD, choices=["fragile:", "robust:", "ornate:", "provisional:"], answer="B",
  explain="The colon introduces evidence: the bridge held three times the required weight without damage. That describes a strong design, so &ldquo;robust:&rdquo;. &ldquo;Fragile&rdquo; is the opposite, and &ldquo;ornate&rdquo; (decorative) and &ldquo;provisional&rdquo; (temporary) aren't supported.")

Q(id="RW-CRF-11", domain="CRAFT", skill="Words in Context", diff=3, rule="wordsincontext",
  passage=f"<p>Rather than {B} the earlier study's conclusions about sleep and memory, the new research builds on them, using a sample ten times larger to confirm the original findings and extend them to older adults.</p>",
  stem=WORD, choices=["refute", "corroborate", "replicate", "extend"], answer="A",
  explain="&ldquo;Rather than&rdquo; signals the opposite of what the new research does. It confirms and builds on the earlier conclusions, so the contrast is with disproving them: &ldquo;refute&rdquo;. &ldquo;Corroborate,&rdquo; &ldquo;replicate,&rdquo; and &ldquo;extend&rdquo; all describe what the new research actually does, which is the trap.")

Q(id="RW-CRF-12", domain="CRAFT", skill="Words in Context", diff=3, rule="wordsincontext",
  passage=f"<p>Many reviewers found the novel's ending {B} after hundreds of pages of slowly building tension between the two families, the conflict is resolved in a single abrupt paragraph that leaves several major questions unanswered.</p>",
  stem=WORD, choices=["perfunctory:", "meticulous:", "inevitable:", "sentimental:"], answer="A",
  explain="The explanation after the colon describes an ending that is rushed and incomplete (&ldquo;a single abrupt paragraph&rdquo;), so &ldquo;perfunctory:&rdquo; (done quickly and without care) fits. &ldquo;Meticulous&rdquo; is the opposite. Nothing suggests the ending was predictable or overly emotional.")

Q(id="RW-CRF-13", domain="CRAFT", skill="Words in Context", diff=2, rule="wordsincontext",
  passage=f"<p>The historian cautions that the surviving letters offer only a {B} picture of daily life in the colony: nearly all of them were written by a handful of wealthy merchants, so the experiences of farmers, laborers, and enslaved people are largely missing.</p>",
  stem=WORD, choices=["partial", "vivid", "fictional", "comprehensive"], answer="A",
  explain="&ldquo;Only&rdquo; and the explanation that most people's experiences are &ldquo;largely missing&rdquo; point to an incomplete picture: &ldquo;partial&rdquo;. &ldquo;Comprehensive&rdquo; is the opposite, and nothing suggests the letters are invented.")

Q(id="RW-CRF-14", domain="CRAFT", skill="Words in Context", diff=2, rule="wordsincontext",
  passage=f"<p>Oceanographer Sylvia Earle has spent more than five decades advocating for marine conservation. Her {B} efforts led her organization, Mission Blue, to recognize more than 100 &ldquo;Hope Spots,&rdquo; ocean areas that are critical to the health of the sea and deserve special protection.</p>",
  stem=WORD, choices=["sporadic", "tireless", "reluctant", "clandestine"], answer="B",
  explain="&ldquo;More than five decades&rdquo; of advocacy that produced more than 100 Hope Spots describes sustained, energetic work: &ldquo;tireless&rdquo;. &ldquo;Sporadic&rdquo; (occasional) and &ldquo;reluctant&rdquo; contradict decades of commitment, and &ldquo;clandestine&rdquo; (secret) doesn't fit public advocacy.")

Q(id="RW-CRF-15", domain="CRAFT", skill="Words in Context", diff=3, rule="wordsincontext",
  passage="<p>The following text is from Jack London's 1903 novel <i>The Call of the Wild</i>.</p><p>Buck did not read the newspapers, or he would have known that trouble was brewing, not alone for himself, but for every tide-water dog, strong of muscle and with warm, long hair, from Puget Sound to San Diego.</p>",
  stem="As used in the text, what does the word &ldquo;brewing&rdquo; most nearly mean?",
  choices=["fermenting", "developing", "steeping", "boiling"], answer="B",
  explain="Trouble that is &ldquo;brewing&rdquo; is trouble that is beginning to form and will soon arrive: &ldquo;developing&rdquo;. &ldquo;Fermenting,&rdquo; &ldquo;steeping,&rdquo; and &ldquo;boiling&rdquo; are literal meanings related to making drinks, which is the common-meaning trap.")

Q(id="RW-CRF-16", domain="CRAFT", skill="Words in Context", diff=2, rule="wordsincontext",
  passage="<p>The following text is from Herman Melville's 1851 novel <i>Moby-Dick</i>.</p><p>Call me Ishmael. Some years ago&mdash;never mind how long precisely&mdash;having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.</p>",
  stem="As used in the text, what does the word &ldquo;interest&rdquo; most nearly mean?",
  choices=["engage", "benefit", "alarm", "charge"], answer="A",
  explain="Ishmael has nothing on shore to hold his attention, so &ldquo;interest&rdquo; means to occupy or hold his attention: &ldquo;engage&rdquo;. &ldquo;Charge&rdquo; plays on the financial meaning of interest (prompted by the mention of money), which is the trap.")

Q(id="RW-CRF-17", domain="CRAFT", skill="Words in Context", diff=2, rule="wordsincontext",
  passage=f"<p>Because the theory makes {B} predictions, stating exactly how many arc seconds a planet's orbit should shift each century, scientists can test it directly against telescope observations.</p>",
  stem=WORD, choices=["vague", "precise", "controversial", "modest"], answer="B",
  explain="The text explains that the predictions state <i>exactly</i> how much the orbit should shift, and that is why they can be tested. So the predictions are &ldquo;precise&rdquo;. &ldquo;Vague&rdquo; is the opposite.")

Q(id="RW-CRF-18", domain="CRAFT", skill="Words in Context", diff=3, rule="wordsincontext",
  passage=f"<p>The architect's designs are deliberately {B} although her buildings use the clean lines and glass walls of modern architecture, they are organized around open courtyards modeled on traditional homes found throughout the region.</p>",
  stem=WORD, choices=["eclectic:", "austere:", "derivative:", "whimsical:"], answer="A",
  explain="The explanation after the colon describes designs that combine elements from different styles (modern and traditional), which is what &ldquo;eclectic:&rdquo; means. &ldquo;Derivative&rdquo; is negative and suggests mere copying, which the text doesn't imply. &ldquo;Austere&rdquo; and &ldquo;whimsical&rdquo; don't describe a combination.")

Q(id="RW-CRF-19", domain="CRAFT", skill="Text Structure and Purpose", diff=2, rule="structure",
  passage="<p>In 1977, Kenyan environmentalist Wangari Maathai founded the Green Belt Movement, which pays women in rural communities to plant trees. The trees help restore damaged soil and provide firewood, but Maathai saw the program as more than an environmental project: by earning income and organizing their communities, the women gained a voice in local decisions. In 2004, Maathai became the first African woman to receive the Nobel Peace Prize.</p>",
  stem="Which choice best states the main purpose of the text?",
  choices=["To describe an environmental program and show that its founder saw it as serving social goals as well",
           "To argue that tree planting is the most effective way to prevent soil erosion",
           "To compare Maathai's work with the work of other Nobel Peace Prize winners",
           "To explain how the trees planted by the program are used for firewood"],
  answer="A",
  explain="The text presents the Green Belt Movement and stresses that Maathai saw it as &ldquo;more than an environmental project,&rdquo; because it gave women income and a voice. The first choice captures both parts. No argument about the &ldquo;most effective&rdquo; method is made, no comparison appears, and firewood is a minor detail.")

Q(id="RW-CRF-20", domain="CRAFT", skill="Text Structure and Purpose", diff=3, rule="structure",
  passage="<p>The Venus flytrap's leaves snap shut when an insect touches the small trigger hairs on their inner surface. A single touch, however, is not enough: the trap closes only if a second hair is touched within about 20 seconds of the first. This two-touch requirement likely keeps the plant from wasting energy by closing on raindrops or bits of debris that brush against it only once.</p>",
  stem="Which choice best describes the function of the third sentence in the overall structure of the text?",
  choices=["It offers a likely explanation for the requirement described in the second sentence.",
           "It describes a second type of trap used by the Venus flytrap.",
           "It challenges the claim made in the first sentence about how the trap closes.",
           "It gives an example of an insect that triggers the trap."],
  answer="A",
  explain="The second sentence describes the two-touch requirement, and the third explains why it probably exists (to avoid wasting energy). So it offers a likely explanation for that requirement. It doesn't introduce a new trap, contradict the first sentence, or name an insect.")

Q(id="RW-INF-11", domain="INFO", skill="Inferences", diff=2, rule="inference",
  passage=f"<p>Many songbirds learn their songs by listening to adult birds during a sensitive period early in life. In classic experiments, young white-crowned sparrows raised without hearing adult songs developed abnormal songs, while those that heard recordings of adult songs during their first months developed normal ones. These findings suggest that {B}</p>",
  stem=INFER,
  choices=["hearing adult songs early in life is important for these sparrows to develop typical songs.",
           "all songbirds are born knowing the songs of their species.",
           "white-crowned sparrows cannot learn songs from recordings.",
           "adult sparrows deliberately teach songs to young birds through demonstration."],
  answer="A",
  explain="Birds that heard adult songs early developed normal songs, and birds that didn't developed abnormal ones, so hearing adult songs early in life is important for typical songs. The second choice is contradicted (the isolated birds' songs were abnormal), the third is contradicted (recordings worked), and the text never says adults teach deliberately.")

Q(id="RW-INF-12", domain="INFO", skill="Inferences", diff=3, rule="inference",
  passage=f"<p>Coral reefs cover less than 1 percent of the ocean floor, yet they are home to roughly a quarter of all known marine species. Because so many species depend on such a small area, {B}</p>",
  stem=INFER,
  choices=["damage to coral reefs could affect a disproportionately large share of the ocean's biodiversity.",
           "most marine species could easily move to other habitats if reefs were damaged.",
           "coral reefs are the only marine habitats that support more than one species.",
           "the ocean floor outside coral reefs supports no marine life."],
  answer="A",
  explain="If about 25 percent of species depend on less than 1 percent of the ocean floor, then harming that small area could harm a share of species far larger than its size: damage to coral reefs could affect a disproportionately large share of the ocean's biodiversity. The other choices are unsupported or contradicted (&ldquo;only,&rdquo; &ldquo;no marine life&rdquo;).")

Q(id="RW-INF-13", domain="INFO", skill="Command of Evidence", diff=3, rule="quant",
  passage="<p>A student researching a town's energy use claims that solar power overtook wind power as a source of the town's electricity during the period shown in the table.</p>"
          "<table class='data'><tr><th>Year</th><th>Solar (gigawatt-hours)</th><th>Wind (gigawatt-hours)</th></tr>"
          "<tr><td>2018</td><td>12</td><td>14</td></tr><tr><td>2019</td><td>15</td><td>13</td></tr><tr><td>2020</td><td>21</td><td>16</td></tr></table>",
  stem="Which choice best describes data from the table that support the student's claim?",
  choices=["Wind produced more electricity than solar in 2018, but solar produced more than wind in both 2019 and 2020.",
           "Solar production increased every year from 2018 to 2020.",
           "Wind production was highest in 2020.",
           "Solar produced more electricity than wind in every year shown."],
  answer="A",
  explain="&ldquo;Overtook&rdquo; requires wind to be ahead first and solar to be ahead later. Only the first choice shows both: wind led in 2018 (14 vs. 12), and solar led in 2019 and 2020. The second and third choices are true but don't show solar passing wind. The last choice is false, because wind led in 2018.")

Q(id="RW-SEC-37", domain="SEC", skill="Form, Structure, and Sense", diff=2, rule="tense",
  passage=f"<p>The first transcontinental railroad in the United States was completed in May 1869. By that time, workers {B} nearly 2,000 miles of track across mountains, deserts, and plains, connecting the eastern rail network to California.</p>",
  stem=CONV, choices=["lay", "have laid", "had laid", "will have laid"], answer="C",
  explain="&ldquo;By that time&rdquo; points to an action completed before another past event (the 1869 completion), which calls for the past perfect: &ldquo;had laid&rdquo;. &ldquo;Have laid&rdquo; connects to the present, and &ldquo;will have laid&rdquo; is future.")

Q(id="RW-SEC-38", domain="SEC", skill="Form, Structure, and Sense", diff=2, rule="tense",
  passage=f"<p>The Cassini spacecraft orbited Saturn for thirteen years. During that time, it {B} hundreds of thousands of images of the planet, its rings, and its moons before its mission ended with a planned plunge into Saturn's atmosphere in 2017.</p>",
  stem=CONV, choices=["captures", "has captured", "captured", "will capture"], answer="C",
  explain="The passage describes a mission that is over (&ldquo;orbited,&rdquo; &ldquo;ended &hellip; in 2017&rdquo;), so the simple past matches: &ldquo;captured&rdquo;. The present, present perfect, and future forms don't fit a finished past mission.")

Q(id="RW-SEC-39", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="verbform",
  passage=f"<p>After examining the chemical makeup of the glass ingots recovered from the ancient shipwreck, the archaeologists {B} that the glass had most likely been produced in workshops hundreds of miles from where the ship sank.</p>",
  stem=CONV, choices=["concluding", "to conclude", "concluded", "having concluded"], answer="C",
  explain="The subject &ldquo;the archaeologists&rdquo; needs a main verb, and only &ldquo;concluded&rdquo; is a finite verb. The other choices leave the sentence without one, making it a fragment.")

Q(id="RW-SEC-40", domain="SEC", skill="Form, Structure, and Sense", diff=3, rule="agreement",
  passage=f"<p>The James Webb Space Telescope's primary mirror, made of eighteen gold-coated hexagonal segments that unfolded after launch, {B} more than six times as much light-collecting area as the Hubble Space Telescope's mirror.</p>",
  stem=CONV, choices=["have", "has", "having", "to have"], answer="B",
  explain="The subject is &ldquo;mirror,&rdquo; which is singular; &ldquo;eighteen &hellip; segments&rdquo; is part of the description between the commas. The sentence needs a finite singular verb: &ldquo;has&rdquo;. &ldquo;Having&rdquo; and &ldquo;to have&rdquo; would leave the sentence without a main verb.")
