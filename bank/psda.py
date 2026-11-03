import random
import statistics
from fractions import Fraction as F
from sympy import Rational as R, symbols, solve, Eq, sqrt
from .common import Q

x, p, kk = symbols("x p kk")

RT = "Ratios, rates, proportional relationships, and units"
PC = "Percentages"
D1 = "One-variable data: distributions and measures of center and spread"
D2 = "Two-variable data: models and scatterplots"
PR = "Probability and conditional probability"
IF = "Inference from sample statistics and margin of error"
EV = "Evaluating statistical claims: observational studies and experiments"

Q(id="PSD-01", domain="PSD", skill=PC, diff=1, desmos=False,
  stem=r"The price of a jacket was increased by 20%. Later, the new price was decreased by 25%. The final price of the jacket was $81. What was the original price?",
  answer="90", verify=lambda: R(81) / (R(6, 5)*R(3, 4)),
  explain=r"The two changes multiply: \(1.20\times0.75=0.90\). So \(0.9P=81\), and \(P=90\). (Note that it is <em>not</em> a 5% decrease: the percents apply to different bases.)")

Q(id="PSD-02", domain="PSD", skill=PC, diff=2, desmos=False,
  stem=r"The number \(x\) is 150% of \(y\), and \(y\) is 40% of \(z\). If \(z\neq0\), \(x\) is what percent of \(z\)?",
  answer="60", verify=lambda: R(3, 2)*R(2, 5)*100,
  explain=r"\(x=1.5y\) and \(y=0.4z\), so \(x=1.5(0.4z)=0.6z\). \(x\) is 60% of \(z\).")

Q(id="PSD-03", domain="PSD", skill=PC, diff=3, desmos=False,
  stem=r"At a high school, 60% of the students are in the band, and the rest are not. Of the students in the band, 25% wear glasses. Of the students not in the band, 40% wear glasses. Of the students who wear glasses, approximately what percent are in the band?",
  choices=["15%", "31%", "48%", "52%"], vals=[15, 31, 48, 52], answer="C",
  verify=lambda: round(float(R(60*25, 100) / (R(60*25, 100) + R(40*40, 100))*100)),
  explain=r"Imagine 100 students. Band: 60 students, 25% of whom wear glasses: 15. Not band: 40 students, 40% of whom wear glasses: 16. "
          r"Total wearing glasses: 31. Fraction in band: \(\frac{15}{31}\approx0.484\), or about 48%. (15% and 31% are the traps: they are percents of <em>all</em> students.)")

Q(id="PSD-04", domain="PSD", skill=RT, diff=1, desmos=False,
  stem=r"A printer prints 18 pages every 45 seconds. At this rate, how many minutes will it take the printer to print 600 pages?",
  answer="25", verify=lambda: R(600) / R(18, 45) / 60,
  explain=r"Rate: \(\frac{18}{45}=0.4\) pages per second. Time: \(\frac{600}{0.4}=1500\) seconds, and \(\frac{1500}{60}=25\) minutes.")

Q(id="PSD-05", domain="PSD", skill=RT, diff=2, desmos=False,
  stem=r"A car's fuel tank holds 14 gallons. In the city, the car travels 24 miles per gallon of fuel; on the highway, it travels 32 miles per gallon. Starting with a full tank, a driver travels 180 miles in the city and then continues on the highway. How many miles can the driver travel on the highway before the tank is empty?",
  answer="208", verify=lambda: (14 - R(180, 24))*32,
  explain=r"City fuel: \(\frac{180}{24}=7.5\) gallons. Remaining fuel: \(14-7.5=6.5\) gallons. Highway distance: \(6.5\times32=208\) miles.")

Q(id="PSD-06", domain="PSD", skill=RT, diff=2, desmos=False,
  stem=r"A metal block is shaped like a cube with an edge length of 4 centimeters. The metal has a density of 7.8 grams per cubic centimeter. What is the least number of these blocks needed to have a total mass of at least 10 kilograms? (1 kilogram = 1,000 grams)",
  answer="21", verify=lambda: min(n for n in range(1, 100) if n*4**3*R(78, 10) >= 10000),
  explain=r"Volume of one block: \(4^3=64\) cm³. Mass: \(64\times7.8=499.2\) g. Number needed: \(\frac{10{,}000}{499.2}\approx20.03\). "
          r"20 blocks weigh only 9,984 g, which is not enough, so 21 blocks are needed.")

Q(id="PSD-07", domain="PSD", skill=D1, diff=1, desmos=False,
  stem=r"The mean of a list of 8 numbers is 15. When one number is removed from the list, the mean of the remaining 7 numbers is 13. What number was removed?",
  answer="29", verify=lambda: 8*15 - 7*13,
  explain=r"Sum of 8 numbers: \(8\times15=120\). Sum of the remaining 7: \(7\times13=91\). The removed number is \(120-91=29\).")

def _psd08():
    base = [4, 7, 7, 9, 12, 15]
    hits = []
    for num in range(-400, 401):                       # x in steps of 1/4 from -100 to 100
        xv = F(num, 4)
        data = sorted(base + [xv])
        if F(sum(data), 7) == data[3]:
            hits.append(xv)
    assert hits == [F(-5), F(9)], hits
    return [h for h in hits if h > 0][0]

Q(id="PSD-08", domain="PSD", skill=D1, diff=3, desmos=False,
  stem=r"A data set consists of the 7 values 4, 7, 7, 9, 12, 15, and \(x\). The mean of the data set is equal to the median of the data set. If \(x\) is positive, what is the value of \(x\)?",
  answer="9", verify=_psd08,
  explain=r"The mean is \(\frac{54+x}{7}\). The median is the 4th value in order, which depends on \(x\). "
          r"If \(x\le7\), the median is 7: \(54+x=49\) gives \(x=-5\), which is not positive. "
          r"If \(7<x<9\), the median is \(x\): \(54+x=7x\) gives \(x=9\), which is not in that range. "
          r"If \(x\ge9\), the median is 9: \(54+x=63\) gives \(x=9\). ✓ So \(x=9\).")

def _psd09():
    data = [3, 8, 10, 15, 21, 30]
    m, sd = statistics.mean(data), statistics.pstdev(data)
    new = [3*v + 5 for v in data]
    m2, sd2 = statistics.mean(new), statistics.pstdev(new)
    opts = {"A": (3*m + 5, 3*sd), "B": (3*m + 5, 3*sd + 5), "C": (3*m, 3*sd), "D": (3*m + 5, 9*sd)}
    good = [L for L, (mm, ss) in opts.items() if abs(mm - m2) < 1e-9 and abs(ss - sd2) < 1e-9]
    assert len(good) == 1
    return good[0]

Q(id="PSD-09", domain="PSD", skill=D1, diff=2, desmos=False,
  stem=r"A data set has mean \(m\) and standard deviation \(s\), where \(s>0\). A new data set is created by multiplying each value in the original data set by 3 and then adding 5. Which of the following gives the mean and standard deviation of the new data set?",
  choices=[r"Mean: \(3m+5\); standard deviation: \(3s\)", r"Mean: \(3m+5\); standard deviation: \(3s+5\)",
           r"Mean: \(3m\); standard deviation: \(3s\)", r"Mean: \(3m+5\); standard deviation: \(9s\)"],
  answer="A", verify=_psd09,
  explain=r"Every value is transformed the same way, so the mean is transformed the same way: \(3m+5\). "
          r"Standard deviation measures spread. Adding 5 shifts every value without changing the distances between values, but multiplying by 3 triples every distance. New SD: \(3s\).")

def _psd10():
    rnd = random.Random(11)
    claims = {"A": lambda old, new: statistics.median(new) == 80,
              "B": lambda old, new: max(new) - min(new) == 55,
              "C": lambda old, new: statistics.mean(new) > statistics.mean(old),
              "D": lambda old, new: max(new) - min(new) == 30}
    always = set(claims)
    tried = 0
    while tried < 4000:
        lo = rnd.randint(50, 80)
        vals = sorted([lo, lo + 30] + [rnd.randint(lo, lo + 30) for _ in range(9)])
        if vals[5] != 80:
            continue
        tried += 1
        new = vals + [50, 105]
        always = {L for L in always if claims[L](vals, new)}
    assert len(always) == 1, always
    return always.pop()

Q(id="PSD-10", domain="PSD", skill=D1, diff=3, desmos=False,
  stem=r"A list of 11 test scores has a median of 80 and a range of 30. Two new scores, 50 and 105, are added to the list. Which of the following must be true about the new list of 13 scores?",
  choices=["The median is 80.", "The range is 55.", "The mean is greater than the mean of the original list.", "The range is 30."],
  answer="A", verify=_psd10,
  explain=r"Since the range is 30 and the median is 80, the smallest original score is between 50 and 80 (the largest is the smallest plus 30, and it must be at least 80). "
          r"So 50 is at or below every original score, and 105 is above the median. Adding one score at or below the median and one score above it keeps the middle (7th of 13) value at 80. "
          r"The range depends on the original maximum, which could be anywhere from 80 to 110, so a range of 55 is not guaranteed. A range of 30 is impossible because 105 &minus; 50 &gt; 30. "
          r"The mean could go up or down, so a greater mean is not guaranteed.")

Q(id="PSD-11", domain="PSD", skill=PR, diff=2, desmos=False,
  stem=r"A survey asked 200 students at a school whether they prefer online or in-person classes. The results are shown in the table."
       r"<table class='data'><tr><th></th><th>Online</th><th>In-person</th><th>Total</th></tr>"
       r"<tr><th>Grade 10</th><td>34</td><td>56</td><td>90</td></tr>"
       r"<tr><th>Grade 11</th><td>48</td><td>62</td><td>110</td></tr>"
       r"<tr><th>Total</th><td>82</td><td>118</td><td>200</td></tr></table>"
       r"If one of the surveyed students who prefer online classes is selected at random, what is the probability that the student is in grade 11?",
  choices=[r"\(\dfrac{48}{200}\)", r"\(\dfrac{48}{110}\)", r"\(\dfrac{48}{82}\)", r"\(\dfrac{82}{200}\)"],
  vals=[R(48, 200), R(48, 110), R(48, 82), R(82, 200)], answer="C",
  verify=lambda: R(48, 34 + 48),
  explain=r"The condition &ldquo;prefers online&rdquo; restricts the group to the Online column: 82 students. Of those, 48 are in grade 11. Probability: \(\frac{48}{82}\). "
          r"\(\frac{48}{110}\) answers a different question: of the grade 11 students, the fraction who prefer online.")

Q(id="PSD-12", domain="PSD", skill=PR, diff=2, desmos=False,
  stem=r"A bag contains only red and blue marbles. The ratio of red marbles to blue marbles is 3 to 5. After 6 red marbles are added to the bag, the probability of randomly selecting a red marble is \(\frac12\). How many blue marbles are in the bag?",
  answer="15", verify=lambda: 5*solve(Eq(3*kk + 6, 5*kk), kk)[0],
  explain=r"Let there be \(3k\) red and \(5k\) blue marbles. After adding 6 red, a probability of \(\frac12\) means red equals blue: \(3k+6=5k\), so \(k=3\). Blue marbles: \(5(3)=15\).")

Q(id="PSD-13", domain="PSD", skill=IF, diff=1, desmos=False, reasoning=True,
  stem=r"A polling company selected 400 registered voters in a city at random and found that 54% of them support a proposed new park. The margin of error for this estimate is 3 percentage points at a 95% confidence level. Which of the following is the most appropriate conclusion?",
  choices=["It is plausible that between 51% and 57% of all registered voters in the city support the new park.",
           "Exactly 54% of all registered voters in the city support the new park.",
           "Between 51% and 57% of the 400 sampled voters support the new park.",
           "The survey proves that a majority of all residents of the city support the new park."],
  answer="A", verify=None,
  explain=r"A margin of error describes uncertainty about the <em>population</em> value: \(54\%\pm3\%\) gives a plausible range of 51% to 57% for all registered voters. "
          r"&ldquo;Exactly 54%&rdquo; ignores the uncertainty. The statement about the 400 sampled voters is wrong because the sample percentage is exactly 54%. The &ldquo;proves&rdquo; statement overstates the result (&ldquo;proves&rdquo;) and switches the population from registered voters to all residents.")

Q(id="PSD-14", domain="PSD", skill=IF, diff=2, desmos=False, reasoning=True,
  stem=r"A researcher wanted to estimate the average number of hours of sleep per night of high school students in a state. The researcher surveyed 250 randomly selected students from the members of one high school's varsity sports teams. The mean was 7.1 hours. Which of the following is the most appropriate conclusion?",
  choices=["The mean sleep of all high school students in the state is about 7.1 hours.",
           "The mean sleep of all high school students in the state is less than 7.1 hours.",
           "The results can't be generalized to all high school students in the state, because the sample was not selected at random from that population.",
           "The sample size of 250 is too small to draw any conclusion about any group."],
  answer="C", verify=None,
  explain=r"A sample supports conclusions only about the population it was randomly selected from: here, varsity athletes at one school. "
          r"That group is not representative of all high school students in the state. 250 is a reasonable sample size for the population that was actually sampled, so the claim that the sample is too small is wrong.")

Q(id="PSD-15", domain="PSD", skill=EV, diff=2, desmos=False, reasoning=True,
  stem=r"A researcher recruited 300 adult volunteers. Half of them were randomly assigned to take a new vitamin supplement daily, and the other half were assigned to take a placebo. After 6 months, the group that took the supplement had significantly fewer colds. Which of the following conclusions is most appropriate?",
  choices=["The supplement causes fewer colds for all adults.",
           "The supplement is likely to cause fewer colds for adults similar to the volunteers in the study.",
           "There is a relationship between the supplement and fewer colds, but no conclusion about cause can be made.",
           "No conclusion can be made because the participants were volunteers."],
  answer="B", verify=None,
  explain=r"Random <em>assignment</em> to treatments allows a cause-and-effect conclusion. But the participants were volunteers, not a random sample of all adults, "
          r"so the conclusion should be limited to people similar to the volunteers. &ldquo;All adults&rdquo; over-generalizes; &ldquo;no conclusion about cause&rdquo; ignores the random assignment; and &ldquo;no conclusion can be made&rdquo; is too strict.")

Q(id="PSD-16", domain="PSD", skill=D2, diff=1, desmos=False,
  stem=r"A scatterplot shows the relationship between two variables, \(x\) and \(y\). The line of best fit for the data is \(y=2.4x+15\). One of the data points is \((10,42)\). By how much does the actual \(y\)-value of this data point exceed the \(y\)-value predicted by the line of best fit?",
  answer="3", verify=lambda: 42 - (R(24, 10)*10 + 15),
  explain=r"Predicted value: \(2.4(10)+15=39\). The actual value 42 exceeds it by \(42-39=3\).")

Q(id="PSD-17", domain="PSD", skill=D1, diff=1, desmos=False,
  stem=r"Data set A contains 20 numbers with a mean of 42. Data set B contains 30 numbers with a mean of 52. What is the mean of the 50 numbers in the two data sets combined?",
  answer="48", verify=lambda: R(20*42 + 30*52, 50),
  explain=r"Total: \(20(42)+30(52)=840+1560=2400\). Mean: \(\frac{2400}{50}=48\). (It is not 47, the average of the two means, because B has more values.)")

Q(id="PSD-18", domain="PSD", skill=PC, diff=2, desmos=False,
  stem=r"Store A sells a lamp at a 30% discount from its original price of $92. Store B sells the same lamp at a price that is 15% greater than the wholesale cost. If the two stores sell the lamp for the same price, what is the wholesale cost of the lamp?",
  answer="56", verify=lambda: R(7, 10)*92 / R(115, 100),
  explain=r"Store A's price: \(0.70\times92=64.40\). Store B: \(1.15w=64.40\), so \(w=56\).")

Q(id="PSD-19", domain="PSD", skill=PC, diff=3, desmos=False,
  stem=r"A stock's price decreased by \(p\%\) during one month and then increased by \(p\%\) during the next month, where \(p>0\). The overall effect was a 4% decrease from the original price. What is the value of \(p\)?",
  answer="20", verify=lambda: [v for v in solve(Eq((1 - p/100)*(1 + p/100), R(96, 100)), p) if v > 0][0],
  explain=r"\(\left(1-\frac p{100}\right)\left(1+\frac p{100}\right)=0.96\). The left side is \(1-\left(\frac p{100}\right)^2\), so \(\left(\frac p{100}\right)^2=0.04\), \(\frac p{100}=0.2\), and \(p=20\).")

Q(id="PSD-20", domain="PSD", skill=RT, diff=2, desmos=False,
  stem=r"Pipe A alone can fill a tank in 6 hours, and pipe B alone can fill the tank in 4 hours. A drain alone can empty the full tank in 8 hours. If the tank starts empty and both pipes and the drain are all open, how many hours will it take to fill the tank?",
  answer="24/7", verify=lambda: 1 / (R(1, 6) + R(1, 4) - R(1, 8)),
  explain=r"Combined rate: \(\frac16+\frac14-\frac18=\frac{4+6-3}{24}=\frac{7}{24}\) tank per hour. Time: \(\frac{24}{7}\approx3.43\) hours. Acceptable entries include 24/7, 3.428, and 3.429.")

Q(id="PSD-21", domain="PSD", skill=RT, diff=2, desmos=False,
  stem=r"Fertilizer is applied to a field at a rate of 2.5 kilograms per 100 square meters. The field is a rectangle that is 0.3 kilometer long and 120 meters wide. How many kilograms of fertilizer are needed for the whole field? (1 kilometer = 1,000 meters)",
  answer="900", verify=lambda: R(300*120, 100)*R(25, 10),
  explain=r"Length: 0.3 km = 300 m. Area: \(300\times120=36{,}000\) m². Number of 100-m² units: 360. Fertilizer: \(360\times2.5=900\) kg.")

Q(id="PSD-22", domain="PSD", skill=PC, diff=2, desmos=False,
  stem=r"A company had 1,250 employees in 2019 and 1,450 employees in 2021. If the number of employees increases by the same percent from 2021 to 2023 as it did from 2019 to 2021, how many employees will the company have in 2023?",
  answer="1682", verify=lambda: 1450*R(1450, 1250),
  explain=r"Percent increase from 2019 to 2021: \(\frac{1450-1250}{1250}=0.16\), or 16%. In 2023: \(1450\times1.16=1682\).")
