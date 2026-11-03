from sympy import Rational as R, symbols, solve, Eq, Matrix, sqrt
from .common import Q

x, y, k, c, m, b, a, s, t = symbols("x y k c m b a s t")

L1 = "Linear equations in one variable"
LF = "Linear functions"
L2 = "Linear equations in two variables"
SY = "Systems of two linear equations in two variables"
IN = "Linear inequalities in one or two variables"

# ---------------------------------------------------------------------------
Q(id="ALG-01", domain="ALG", skill=L1, diff=2, desmos=True,
  stem=r"\[\frac{3x-5}{4}-\frac{x+1}{6}=\frac{x}{3}+2\]What value of \(x\) is the solution to the given equation?",
  answer="41/3",
  verify=lambda: solve(Eq((3*x - 5)/4 - (x + 1)/6, x/3 + 2), x)[0],
  explain=r"Multiply every term by 12 (the least common denominator): \(3(3x-5)-2(x+1)=4x+24\). "
          r"Expand: \(9x-15-2x-2=4x+24\), so \(7x-17=4x+24\). Then \(3x=41\) and \(x=\frac{41}{3}\). "
          r"Acceptable entries include 41/3, 13.66, and 13.67.",
  tip=r"Type the whole equation into Desmos exactly as written. Desmos draws a vertical line at the solution; click it to read \(x\approx13.667\). Enter 41/3 or 13.66/13.67.")

Q(id="ALG-02", domain="ALG", skill=L1, diff=3, desmos=False,
  stem=r"\[k(3x-4)+2x=11x-(k+2c)\]In the given equation, \(k\) and \(c\) are constants. If the equation has infinitely many solutions, what is the value of \(c\)?",
  answer="9/2",
  verify=lambda: (lambda kk: solve(Eq(-4*kk, -kk - 2*c), c)[0])(solve(Eq(3*k + 2, 11), k)[0]),
  explain=r"An equation has infinitely many solutions only when both sides are identical. "
          r"Left side: \((3k+2)x-4k\). Right side: \(11x-k-2c\). "
          r"Match the \(x\)-coefficients: \(3k+2=11\), so \(k=3\). "
          r"Match the constants: \(-4k=-k-2c\), so \(-12=-3-2c\), giving \(2c=9\) and \(c=\frac{9}{2}\).")

def _alg03():
    sols = []
    for kv in solve(Eq(3*12 - k*k, 0), k):          # determinant = 0
        M = Matrix([[3, kv], [kv, 12]])
        aug = Matrix([[3, kv, 7], [kv, 12, 14]])
        if M.rank() < aug.rank():                     # inconsistent -> no solution
            sols.append(kv)
    assert len(sols) == 1
    return sols[0]

Q(id="ALG-03", domain="ALG", skill=SY, diff=3, desmos=False,
  stem=r"\[3x+ky=7\]\[kx+12y=14\]In the given system of equations, \(k\) is a constant. For which value of \(k\) does the system have no solution?",
  choices=[r"\(-36\)", r"\(-6\)", r"\(6\)", r"\(36\)"], vals=[-36, -6, 6, 36], answer="B",
  verify=_alg03,
  explain=r"A linear system has no solution when the lines are parallel but not identical: the coefficient ratios match but the constant ratio does not. "
          r"\(\frac{3}{k}=\frac{k}{12}\) gives \(k^2=36\), so \(k=6\) or \(k=-6\). "
          r"If \(k=6\): ratios are \(\frac{3}{6}=\frac{6}{12}=\frac{7}{14}=\frac12\) &mdash; the same line, so infinitely many solutions. "
          r"If \(k=-6\): \(\frac{3}{-6}=\frac{-6}{12}=-\frac12\), but \(\frac{7}{14}=\frac12\). Parallel, distinct lines &rarr; no solution. So \(k=-6\).")

Q(id="ALG-04", domain="ALG", skill=LF, diff=1, desmos=False,
  stem=r"A water tank is drained at a constant rate. Eight minutes after draining begins, the tank holds 1,340 liters of water. Twenty minutes after draining begins, the tank holds 860 liters. How many liters of water were in the tank when draining began?",
  answer="1660",
  verify=lambda: (lambda sl: 1340 - sl*8)(R(860 - 1340, 20 - 8)),
  explain=r"The rate is \(\frac{860-1340}{20-8}=\frac{-480}{12}=-40\) liters per minute. "
          r"Going back 8 minutes from 1,340 liters: \(1340+8(40)=1660\) liters.")

def _alg05():
    sols = solve([Eq(m*m, 9), Eq(m*b + b, -8)], [m, b], dict=True)
    sols = [d for d in sols if d[m] > 0]
    assert len(sols) == 1
    return sols[0][m]*5 + sols[0][b]

Q(id="ALG-05", domain="ALG", skill=LF, diff=3, desmos=False,
  stem=r"The function \(g\) is linear with a positive slope, and \(g(g(x))=9x-8\) for all values of \(x\). What is the value of \(g(5)\)?",
  answer="13",
  verify=_alg05,
  explain=r"Write \(g(x)=mx+b\). Then \(g(g(x))=m(mx+b)+b=m^2x+(mb+b)\). "
          r"Matching \(9x-8\): \(m^2=9\), so \(m=3\) (positive slope), and \(3b+b=-8\), so \(b=-2\). "
          r"Thus \(g(x)=3x-2\) and \(g(5)=13\).")

Q(id="ALG-06", domain="ALG", skill=SY, diff=1, desmos=True,
  stem=r"\[\tfrac{1}{2}x+\tfrac{2}{3}y=7\]\[0.4x-0.25y=0.9\]If \((x,y)\) is the solution to the given system of equations, what is the value of \(x+y\)?",
  answer="12",
  verify=lambda: (lambda d: d[x] + d[y])(solve([Eq(R(1, 2)*x + R(2, 3)*y, 7), Eq(R(2, 5)*x - R(1, 4)*y, R(9, 10))], [x, y])),
  explain=r"Clear the fractions and decimals: multiply the first equation by 6 to get \(3x+4y=42\); multiply the second by 20 to get \(8x-5y=18\). "
          r"Multiply the first by 5 and the second by 4 and add: \(15x+32x=210+72\), so \(47x=282\) and \(x=6\). Then \(4y=42-18=24\), \(y=6\). So \(x+y=12\).",
  tip=r"Type both equations into Desmos and click the intersection point: \((6,6)\). Add the coordinates.")

Q(id="ALG-07", domain="ALG", skill=SY, diff=2, desmos=False,
  stem=r"\[2x-3y=12\]\[(k-1)x+6y=c\]In the given system of equations, \(k\) and \(c\) are constants. The system has infinitely many solutions. What is the value of \(k+c\)?",
  answer="-27",
  verify=lambda: (lambda kk: kk + 12*(-2))(solve(Eq((k - 1)*(-3), 2*6), k)[0]),
  explain=r"For infinitely many solutions the second equation must be a multiple of the first. Since \(6y=-2(-3y)\), the multiplier is \(-2\). "
          r"Then \(k-1=-2(2)=-4\), so \(k=-3\), and \(c=-2(12)=-24\). So \(k+c=-27\).")

Q(id="ALG-08", domain="ALG", skill=SY, diff=2, desmos=True,
  stem=r"A theater sold 420 tickets for one performance. Adult tickets cost $14 each and student tickets cost $9 each. The total revenue from adult tickets was $590 more than the total revenue from student tickets. How many student tickets were sold?",
  answer="230",
  verify=lambda: solve([Eq(a + s, 420), Eq(14*a - 9*s, 590)], [a, s])[s],
  explain=r"Let \(a\) be adult tickets and \(s\) be student tickets: \(a+s=420\) and \(14a-9s=590\). "
          r"Substitute \(a=420-s\): \(14(420-s)-9s=590\), so \(5880-23s=590\), \(23s=5290\), and \(s=230\).",
  tip=r"Graph \(x+y=420\) and \(14x-9y=590\) (with \(x\) = adult, \(y\) = student). The intersection is \((190,230)\).")

def _alg09():
    good = [kv for kv in (-5, -4, -3, -2) if (-1 > 2*(-4) + 3) and (-1 < R(-1, 2)*(-4) + kv)]
    assert len(good) == 1
    return good[0]

Q(id="ALG-09", domain="ALG", skill=IN, diff=2, desmos=True,
  stem=r"\[y>2x+3\]\[y<-\tfrac{1}{2}x+k\]In the given system of inequalities, \(k\) is a constant. The point \((-4,-1)\) is a solution to the system. Which of the following could be the value of \(k\)?",
  choices=[r"\(-5\)", r"\(-4\)", r"\(-3\)", r"\(-2\)"], vals=[-5, -4, -3, -2], answer="D",
  verify=_alg09,
  explain=r"Check the first inequality: \(-1>2(-4)+3=-5\). True. "
          r"Second inequality: \(-1<-\tfrac12(-4)+k=2+k\), so \(k>-3\). The inequality is strict, so \(k=-3\) does not work. Only \(-2\) is greater than \(-3\).",
  tip=r"Enter both inequalities with a slider for \(k\), and plot the point \((-4,-1)\). Slide \(k\) to see which values put the point inside the doubly shaded region. Watch the dashed (strict) boundary at \(k=-3\).")

Q(id="ALG-10", domain="ALG", skill=IN, diff=2, desmos=False,
  stem=r"A delivery van weighs 5,200 pounds when empty. The total weight of the van, the driver, and the cargo must not exceed 9,000 pounds. The driver weighs 180 pounds. The van is carrying 25 crates that each weigh 85 pounds and some boxes that each weigh 40 pounds. What is the maximum number of boxes the van can carry?",
  answer="37",
  verify=lambda: max(n for n in range(0, 500) if 5200 + 180 + 25*85 + 40*n <= 9000),
  explain=r"\(5200+180+25(85)+40n\le 9000\). The fixed weight is \(5200+180+2125=7505\), so \(40n\le1495\) and \(n\le37.375\). The number of boxes must be a whole number, so the maximum is 37.")

def _alg11():
    m_given = solve(Eq(4*x - 6*y, 5), y)[0].coeff(x)
    mp = -1/m_given
    return 7 - mp*(-3)            # y-intercept: y = 7 + mp*(0 - (-3))

Q(id="ALG-11", domain="ALG", skill=L2, diff=2, desmos=True,
  stem=r"In the \(xy\)-plane, line \(\ell\) passes through the point \((-3,7)\) and is perpendicular to the graph of \(4x-6y=5\). What is the \(y\)-coordinate of the \(y\)-intercept of line \(\ell\)?",
  answer="5/2",
  verify=_alg11,
  explain=r"Rewrite \(4x-6y=5\) as \(y=\frac23x-\frac56\); its slope is \(\frac23\). A perpendicular slope is \(-\frac32\). "
          r"Line \(\ell\): \(y-7=-\frac32(x+3)\). At \(x=0\): \(y=7-\frac92=\frac52\).",
  tip=r"Graph \(4x-6y=5\), then type \(y-7=m(x+3)\) and set \(m=-3/2\). Click where the new line crosses the \(y\)-axis: \((0,2.5)\).")

Q(id="ALG-12", domain="ALG", skill=L2, diff=2, desmos=False,
  stem=r"In the \(xy\)-plane, line \(k\) has \(x\)-intercept \((a,0)\) and \(y\)-intercept \((0,b)\), where \(a\) and \(b\) are nonzero constants. Line \(k\) is parallel to the graph of \(5x+2y=3\). If \(a+b=21\), what is the value of \(b\)?",
  answer="15",
  verify=lambda: solve([Eq(-b/a, R(-5, 2)), Eq(a + b, 21)], [a, b], dict=True)[0][b],
  explain=r"The slope through \((a,0)\) and \((0,b)\) is \(\frac{b-0}{0-a}=-\frac{b}{a}\). The line \(5x+2y=3\) has slope \(-\frac52\). "
          r"So \(\frac ba=\frac52\), meaning \(b=\frac52a\). Then \(a+\frac52a=21\), so \(\frac72a=21\), \(a=6\), and \(b=15\).")

Q(id="ALG-13", domain="ALG", skill=IN, diff=1, desmos=True,
  stem=r"Gym A charges a one-time fee of $60 plus $35 per month. Gym B charges a one-time fee of $20 plus $43 per month. What is the least number of whole months after which the total amount paid to Gym B is greater than the total amount paid to Gym A?",
  answer="6",
  verify=lambda: min(n for n in range(1, 100) if 20 + 43*n > 60 + 35*n),
  explain=r"\(20+43m>60+35m\) gives \(8m>40\), so \(m>5\). At exactly 5 months the totals are equal ($235 each), so the least whole number of months is 6.",
  tip=r"Graph \(y=60+35x\) and \(y=20+43x\). They intersect at \(x=5\); the Gym B line is above after that, so the first whole month is 6.")

Q(id="ALG-14", domain="ALG", skill=LF, diff=1, desmos=True,
  stem=r"The height above the ground of a descending weather balloon is a linear function of time. The balloon is 195 meters above the ground 5 seconds after it starts descending and 39 meters above the ground 17 seconds after it starts descending. How many seconds after it starts descending does the balloon reach the ground?",
  answer="20",
  verify=lambda: (lambda sl: solve(Eq(195 + sl*(t - 5), 0), t)[0])(R(39 - 195, 17 - 5)),
  explain=r"Slope: \(\frac{39-195}{17-5}=-13\) meters per second. Height: \(h(t)=195-13(t-5)=260-13t\). Setting \(h(t)=0\): \(t=20\).",
  tip=r"Plot the points \((5,195)\) and \((17,39)\), or type the line through them, and click the \(x\)-intercept: \((20,0)\).")

def _alg15():
    # sample line p: y = 2x - 3 ; reflection over y-axis: y = p(-x)
    f = 2*(-x) - 3
    sl, yi = f.coeff(x), f.subs(x, 0)
    return {(1, 1): "A", (-1, -1): "B", (-1, 1): "C", (1, -1): "D"}[(1 if sl > 0 else -1, 1 if yi > 0 else -1)]

Q(id="ALG-15", domain="ALG", skill=L2, diff=2, desmos=False,
  stem=r"In the \(xy\)-plane, line \(p\) has a positive slope and a negative \(y\)-intercept. Line \(q\) is the reflection of line \(p\) across the \(y\)-axis. Which of the following must be true about line \(q\)?",
  choices=["It has a positive slope and a positive \\(y\\)-intercept.",
           "It has a negative slope and a negative \\(y\\)-intercept.",
           "It has a negative slope and a positive \\(y\\)-intercept.",
           "It has a positive slope and a negative \\(y\\)-intercept."],
  answer="B", verify=_alg15,
  explain=r"Reflecting across the \(y\)-axis replaces \(x\) with \(-x\): \(y=mx+b\) becomes \(y=-mx+b\). The slope changes sign (positive &rarr; negative), "
          r"but the \(y\)-intercept lies on the mirror line, so it does not move and stays negative.")

Q(id="ALG-16", domain="ALG", skill=L1, diff=1, desmos=False,
  stem=r"\[\tfrac{2}{3}(9x-6)-5=\tfrac{1}{2}(8x+2)+3\]What value of \(x\) satisfies the given equation?",
  answer="13/2",
  verify=lambda: solve(Eq(R(2, 3)*(9*x - 6) - 5, R(1, 2)*(8*x + 2) + 3), x)[0],
  explain=r"Distribute: \(6x-4-5=4x+1+3\), so \(6x-9=4x+4\). Then \(2x=13\) and \(x=\frac{13}{2}=6.5\).")

Q(id="ALG-17", domain="ALG", skill=SY, diff=3, desmos=True,
  stem=r"\[\frac{x}{3}+\frac{y}{4}=2\]\[\frac{x}{4}+\frac{y}{3}=\frac{5}{2}\]If \((x,y)\) is the solution to the given system of equations, what is the value of \(x+y\)?",
  answer="54/7",
  verify=lambda: (lambda d: d[x] + d[y])(solve([Eq(x/3 + y/4, 2), Eq(x/4 + y/3, R(5, 2))], [x, y])),
  explain=r"You never need \(x\) and \(y\) separately. Add the two equations: \(x\left(\frac13+\frac14\right)+y\left(\frac14+\frac13\right)=2+\frac52\), "
          r"so \(\frac{7}{12}(x+y)=\frac92\). Multiply by \(\frac{12}{7}\): \(x+y=\frac{54}{7}\). Acceptable entries include 54/7 and 7.714.",
  tip=r"Graph both equations and click the intersection: about \((2.571, 5.143)\). Their sum is about 7.714. For an exact answer, add the equations by hand (see explanation) and enter 54/7.")

def _alg18():
    best = None
    for L in range(0, 20):
        for T in range(0, 40):
            if 650*L + 280*T <= 5000 and L + T >= 10:
                best = L if best is None else max(best, L)
    return best

Q(id="ALG-18", domain="ALG", skill=IN, diff=2, desmos=False,
  stem=r"A school has a budget of at most $5,000 to buy laptops and tablets. Each laptop costs $650 and each tablet costs $280. The school must buy at least 10 devices in total. What is the maximum number of laptops the school can buy?",
  answer="5",
  verify=_alg18,
  explain=r"Let \(L\) be laptops and \(T\) tablets: \(650L+280T\le5000\) and \(L+T\ge10\). To make room for as many laptops as possible, buy the fewest tablets allowed: \(T=10-L\). "
          r"Then \(650L+280(10-L)\le5000\), so \(370L\le2200\) and \(L\le5.94\). Check \(L=5,T=5\): \(3250+1400=4650\le5000\). \(L=6,T=4\) costs \(5020\), which is too much. Maximum: 5.")

def _alg19():
    pts = [(4, 0), (-2, 9)]
    eqs = {"A": lambda X, Y: 3*X + 2*Y == 12, "B": lambda X, Y: 2*X + 3*Y == 8,
           "C": lambda X, Y: 3*X - 2*Y == 12, "D": lambda X, Y: 2*X - 3*Y == 8}
    good = [L for L, f in eqs.items() if all(f(*p) for p in pts)]
    assert len(good) == 1
    return good[0]

Q(id="ALG-19", domain="ALG", skill=L2, diff=1, desmos=True,
  stem=r"In the \(xy\)-plane, a line has an \(x\)-intercept at \((4,0)\) and passes through the point \((-2,9)\). Which of the following is an equation of the line?",
  choices=[r"\(3x+2y=12\)", r"\(2x+3y=8\)", r"\(3x-2y=12\)", r"\(2x-3y=8\)"], answer="A",
  verify=_alg19,
  explain=r"Slope: \(\frac{9-0}{-2-4}=-\frac32\). Point-slope: \(y=-\frac32(x-4)\), so \(2y=-3x+12\), or \(3x+2y=12\). Check \((-2,9)\): \(-6+18=12\). ✓",
  tip=r"Plot the two points and type each answer choice. Only \(3x+2y=12\) passes through both points.")

Q(id="ALG-20", domain="ALG", skill=L2, diff=2, desmos=True,
  stem=r"In the \(xy\)-plane, the graph of \(y=kx+4\), where \(k\) is a constant, intersects the graph of \(2x+5y=20\) at a point on the \(x\)-axis. What is the value of \(k\)?",
  answer="-2/5",
  verify=lambda: solve(Eq(k*solve(Eq(2*x, 20), x)[0] + 4, 0), k)[0],
  explain=r"The graph of \(2x+5y=20\) meets the \(x\)-axis where \(y=0\): \(x=10\). So \((10,0)\) is on \(y=kx+4\): \(0=10k+4\), and \(k=-\frac25=-0.4\).",
  tip=r"Graph \(2x+5y=20\) to find the \(x\)-intercept \((10,0)\). Then add \(y=kx+4\) with a slider and adjust \(k\) until the line passes through \((10,0)\).")

Q(id="ALG-21", domain="ALG", skill=LF, diff=2, desmos=False,
  stem=r"The graph of the linear function \(f\) passes through the point \((2,-5)\) in the \(xy\)-plane. Through which of the following points must the graph of \(y=f(x-4)+3\) pass?",
  choices=[r"\((6,-2)\)", r"\((-2,-2)\)", r"\((6,-8)\)", r"\((-2,-8)\)"], vals=[(6, -2), (-2, -2), (6, -8), (-2, -8)], answer="A",
  verify=lambda: (2 + 4, -5 + 3),
  explain=r"\(y=f(x-4)+3\) shifts the graph of \(f\) right 4 units and up 3 units. The point \((2,-5)\) moves to \((2+4,-5+3)=(6,-2)\). "
          r"Check: at \(x=6\), \(f(6-4)+3=f(2)+3=-5+3=-2\).")

def _alg22():
    pens = 12*5
    return -R(pens, 20)

Q(id="ALG-22", domain="ALG", skill=L2, diff=1, desmos=False,
  stem=r"A store sells pens in packs of 12 and pencils in packs of 20. The equation \(12x+20y=640\) represents the situation in which a teacher buys \(x\) packs of pens and \(y\) packs of pencils for a total of 640 writing utensils. If the teacher buys 5 more packs of pens, how must the number of packs of pencils change so that the total number of writing utensils is still 640?",
  choices=["It must decrease by 3.", "It must decrease by 5.", "It must decrease by 12.", "It must increase by 3."],
  vals=[-3, -5, -12, 3], answer="A", verify=_alg22,
  explain=r"5 more packs of pens add \(5\times12=60\) utensils. To keep the total the same, remove 60 pencils: \(60\div20=3\) packs. So \(y\) decreases by 3.")

Q(id="ALG-23", domain="ALG", skill=L1, diff=3, desmos=False,
  stem=r"\[a(x+3)-2(x-b)=5x+18\]In the given equation, \(a\) and \(b\) are constants. If the equation has infinitely many solutions, what is the value of \(b\)?",
  answer="-3/2",
  verify=lambda: (lambda aa: solve(Eq(3*aa + 2*b, 18), b)[0])(solve(Eq(a - 2, 5), a)[0]),
  explain=r"Expand the left side: \((a-2)x+(3a+2b)\). For infinitely many solutions it must equal \(5x+18\) exactly. "
          r"So \(a-2=5\) (\(a=7\)) and \(3a+2b=18\): \(21+2b=18\), \(b=-\frac32=-1.5\).")
