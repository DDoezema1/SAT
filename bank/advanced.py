import math
import random
from sympy import (Rational as R, symbols, solve, Eq, sqrt, Poly, real_roots, expand,
                   simplify, factor, S, nsolve, log)
from .common import Q

x, y, k, c, a, b, t = symbols("x y k c a b t")

EQ = "Equivalent expressions"
NE = "Nonlinear equations in one variable and systems of equations in two variables"
NF = "Nonlinear functions"


def _real_solution_count(expr):
    p = Poly(expr, x)
    if p.degree() == 0:
        return 0 if p.as_expr() != 0 else math.inf
    return len(set(real_roots(p)))

def _adv01():
    good = [kv for kv in (-2, 0, 1, 2) if _real_solution_count((kv + 2)*x**2 - 6*x + 3) == 0]
    assert len(good) == 1
    return good[0]

Q(id="ADV-01", domain="ADV", skill=NE, diff=2, desmos=True,
  stem=r"\[(k+2)x^2-6x+3=0\]In the given equation, \(k\) is a constant. For which of the following values of \(k\) does the equation have no real solutions?",
  choices=[r"\(-2\)", r"\(0\)", r"\(1\)", r"\(2\)"], vals=[-2, 0, 1, 2], answer="D",
  verify=_adv01,
  explain=r"If \(k=-2\), the equation becomes \(-6x+3=0\), which has the solution \(x=\frac12\). Otherwise it is quadratic, with discriminant \(36-4(k+2)(3)=12-12k\). "
          r"No real solutions requires \(12-12k<0\), so \(k>1\). Of the choices only \(k=2\) works. (When \(k=1\) the discriminant is 0, which gives exactly one solution.)",
  tip=r"Graph \(y=(k+2)x^2-6x+3\) with a slider for \(k\). Try each choice: only at \(k=2\) does the parabola stay entirely above the \(x\)-axis.")

Q(id="ADV-02", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"In the \(xy\)-plane, the graph of \(y=4x+c\), where \(c\) is a constant, intersects the graph of \(y=x^2-2x+7\) at exactly one point. What is the value of \(c\)?",
  answer="-2",
  verify=lambda: solve(Eq((-6)**2 - 4*1*(7 - c), 0), c)[0],
  explain=r"Set the expressions equal: \(x^2-2x+7=4x+c\), so \(x^2-6x+(7-c)=0\). Exactly one intersection means the discriminant is 0: "
          r"\(36-4(7-c)=0\), so \(36-28+4c=0\) and \(c=-2\). (The line is tangent to the parabola at \(x=3\).)",
  tip=r"Graph the parabola and \(y=4x+c\) with a slider. Adjust \(c\) until the line just touches the parabola. It happens at \(c=-2\).")

def _adv03():
    sols = solve(Eq(x/(x - 3) - 2/(x + 3), 18/(x**2 - 9)), x)
    assert len(sols) == 1
    return sols[0]

Q(id="ADV-03", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"\[\frac{x}{x-3}-\frac{2}{x+3}=\frac{18}{x^2-9}\]What is the solution to the given equation?",
  answer="-4", verify=_adv03,
  explain=r"Multiply both sides by \(x^2-9=(x-3)(x+3)\): \(x(x+3)-2(x-3)=18\), so \(x^2+x+6=18\), or \(x^2+x-12=0\). "
          r"Factor: \((x+4)(x-3)=0\). But \(x=3\) makes denominators 0 in the original equation, so it is extraneous. The only solution is \(x=-4\).",
  tip=r"Graph \(y=\frac{x}{x-3}-\frac{2}{x+3}\) and \(y=\frac{18}{x^2-9}\). They intersect only at \(x=-4\). Desmos shows no intersection at \(x=3\), which confirms that it is extraneous.")

def _adv04():
    sols = [v for v in solve(Eq(2*x + 6, (x - 1)**2), x) if sqrt(2*v + 6) == v - 1]
    assert len(sols) == 1
    return sols[0]

Q(id="ADV-04", domain="ADV", skill=NE, diff=2, desmos=True,
  stem=r"\[\sqrt{2x+6}=x-1\]What is the solution to the given equation?",
  answer="5", verify=_adv04,
  explain=r"Square both sides: \(2x+6=x^2-2x+1\), so \(x^2-4x-5=0\) and \((x-5)(x+1)=0\). "
          r"Check \(x=-1\): \(\sqrt{4}=2\) but \(-1-1=-2\), so it is extraneous. Check \(x=5\): \(\sqrt{16}=4=5-1\). ✓ The solution is 5.",
  tip=r"Graph \(y=\sqrt{2x+6}\) and \(y=x-1\). There is only one intersection, at \((5,4)\). Squaring creates the fake solution \(-1\), which Desmos never shows.")

Q(id="ADV-05", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"The function \(f(t)=2{,}400(0.64)^{t}\) gives the estimated value, in dollars, of a machine \(t\) years after it was purchased. Which of the following functions is equivalent to \(f\) and shows, as a constant or base, the factor by which the value changes every half year?",
  choices=[r"\(f(t)=2{,}400(0.8)^{2t}\)", r"\(f(t)=2{,}400(0.8)^{t/2}\)", r"\(f(t)=2{,}400(0.32)^{2t}\)", r"\(f(t)=1{,}200(0.64)^{2t}\)"],
  vals=["2400*(4/5)**(2*t)", "2400*(4/5)**(t/2)", "2400*(8/25)**(2*t)", "1200*(16/25)**(2*t)"], answer="A",
  verify=lambda: 2400*R(16, 25)**t,
  explain=r"Since \(0.64=0.8^2\), \((0.64)^t=(0.8^2)^t=(0.8)^{2t}\). So \(2{,}400(0.8)^{2t}\) is equivalent to \(f\). "
          r"In that form, when \(t\) increases by \(\frac12\), the exponent \(2t\) increases by 1, so the value is multiplied by 0.8 (a 20% decrease every half year). "
          r"The form \(2{,}400(0.8)^{t/2}\) would mean a factor of 0.8 every <em>2</em> years (and is not equivalent to \(f\)). The other two forms are not equivalent to \(f\) either.",
  tip=r"Graph \(f\) and each choice. Only the graph of \(2400(0.8)^{2t}\) lies exactly on top of \(f(t)=2400(0.64)^t\).")

Q(id="ADV-06", domain="ADV", skill=NF, diff=2, desmos=True,
  stem=r"A quantity increases by 25% every 2 years. Which of the following is closest to the percent by which the quantity increases every year?",
  choices=[r"6.25%", r"11.8%", r"12.5%", r"25%"], vals=[6.25, 11.8, 12.5, 25], answer="B",
  verify=lambda: round((math.sqrt(1.25) - 1)*100, 1),
  explain=r"Over 2 years the growth factor is 1.25. If the yearly factor is \(r\), then \(r^2=1.25\), so \(r=\sqrt{1.25}\approx1.118\), about 11.8% per year. "
          r"12.5% (half of 25%) is the trap: growth compounds, so \(1.125^2\approx1.266\), which is more than 1.25.",
  tip=r"Type \(\sqrt{1.25}\) into Desmos: 1.118, so about 11.8%.")

def _adv07():
    kk = solve(Eq((2*x**3 + k*x**2 - 11*x + 6).subs(x, 3), 0), k)[0]
    roots = solve(2*x**3 + kk*x**2 - 11*x + 6, x)
    return sum(roots)

Q(id="ADV-07", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"\[p(x)=2x^3+kx^2-11x+6\]In the polynomial function \(p\), \(k\) is a constant. If \(x-3\) is a factor of \(p(x)\), what is the sum of all the zeros of \(p\)?",
  answer="3/2", verify=_adv07,
  explain=r"Since \(x-3\) is a factor, \(p(3)=0\): \(54+9k-33+6=0\), so \(9k=-27\) and \(k=-3\). "
          r"Then \(p(x)=2x^3-3x^2-11x+6=(x-3)(2x^2+3x-2)=(x-3)(2x-1)(x+2)\). The zeros are \(3,\frac12,-2\), and their sum is \(\frac32\). "
          r"(Shortcut: for a cubic \(ax^3+bx^2+\dots\), the sum of the zeros is \(-\frac ba=\frac32\).)",
  tip=r"After finding \(k=-3\) by hand, graph \(p(x)=2x^3-3x^2-11x+6\) and click the three \(x\)-intercepts: \(-2\), \(0.5\), \(3\).")

def _adv08():
    # Try many random polynomials with p(3)=5 and test each claim.
    claims = {
        "A": lambda P: Poly(P - 5, x).eval(-3) == 0,
        "B": lambda P: Poly(P + 5, x).eval(3) == 0,
        "C": lambda P: Poly(P - 5, x).eval(3) == 0,
        "D": lambda P: Poly(P - 3, x).eval(5) == 0,
    }
    rnd = random.Random(7)
    always = set(claims)
    for _ in range(40):
        q = sum(rnd.randint(-5, 5)*x**i for i in range(4))
        P = expand((x - 3)*q + 5)
        always = {L for L in always if claims[L](P)}
    assert len(always) == 1
    return always.pop()

Q(id="ADV-08", domain="ADV", skill=NF, diff=2, desmos=False,
  stem=r"For the polynomial function \(p\), \(p(3)=5\). Which of the following must be true?",
  choices=[r"\(x+3\) is a factor of \(p(x)-5\).", r"\(x-3\) is a factor of \(p(x)+5\).",
           r"\(x-3\) is a factor of \(p(x)-5\).", r"\(x-5\) is a factor of \(p(x)-3\)."],
  answer="C", verify=_adv08,
  explain=r"Let \(g(x)=p(x)-5\). Then \(g(3)=p(3)-5=0\), so 3 is a zero of \(g\), and by the factor theorem \(x-3\) is a factor of \(p(x)-5\). "
          r"(Equivalently: dividing \(p(x)\) by \(x-3\) leaves remainder 5.) The other statements need extra information that is not given.")

def _adv09():
    f = lambda X: X**2 - 6*X + 11
    g = f(x + 2) - 3
    h = solve(g.diff(x), x)[0]
    return h + g.subs(x, h)

Q(id="ADV-09", domain="ADV", skill=NF, diff=2, desmos=True,
  stem=r"The function \(f\) is defined by \(f(x)=x^2-6x+11\). In the \(xy\)-plane, the graph of \(y=f(x+2)-3\) has its vertex at \((h,k)\). What is the value of \(h+k\)?",
  answer="0", verify=_adv09,
  explain=r"Complete the square: \(f(x)=(x-3)^2+2\), with vertex \((3,2)\). The graph of \(y=f(x+2)-3\) is the graph of \(f\) shifted 2 units <em>left</em> and 3 units down, "
          r"so its vertex is \((1,-1)\), and \(h+k=0\).",
  tip=r"Define \(f(x)=x^2-6x+11\) in Desmos, then graph \(y=f(x+2)-3\) and click the vertex: \((1,-1)\).")

Q(id="ADV-10", domain="ADV", skill=NF, diff=1, desmos=True,
  stem=r"The function \(h(t)=-16t^2+72t+5\) gives the height, in feet, of a ball \(t\) seconds after it is thrown. What is the maximum height, in feet, that the ball reaches?",
  answer="86",
  verify=lambda: (-16*t**2 + 72*t + 5).subs(t, solve((-32*t + 72), t)[0]),
  explain=r"The vertex occurs at \(t=-\frac{72}{2(-16)}=2.25\). \(h(2.25)=-16(5.0625)+72(2.25)+5=-81+162+5=86\) feet.",
  tip=r"Graph \(y=-16x^2+72x+5\) and click the maximum point: \((2.25,86)\).")

Q(id="ADV-11", domain="ADV", skill=NF, diff=3, desmos=False,
  stem=r"The function \(f\) is defined by \(f(x)=a(x-2)(x-8)\), where \(a\) is a constant. The minimum value of \(f\) is \(-27\). What is the value of \(f(10)\)?",
  answer="48",
  verify=lambda: (lambda av: av*(10 - 2)*(10 - 8))(solve(Eq(a*(5 - 2)*(5 - 8), -27), a)[0]),
  explain=r"The vertex of a parabola is halfway between its zeros: \(x=\frac{2+8}{2}=5\). So \(f(5)=a(3)(-3)=-9a=-27\), and \(a=3\) (positive, consistent with a minimum). "
          r"Then \(f(10)=3(8)(2)=48\).")

def _adv12():
    q, r = (6*x**2 + 7*x - 10).as_poly(x).div((2*x - 1).as_poly(x))
    return r.as_expr()

Q(id="ADV-12", domain="ADV", skill=EQ, diff=2, desmos=False,
  stem=r"The expression \(\dfrac{6x^2+7x-10}{2x-1}\) is equivalent to \(3x+5+\dfrac{r}{2x-1}\), where \(r\) is a constant and \(x\neq\frac12\). What is the value of \(r\)?",
  answer="-5", verify=_adv12,
  explain=r"Multiply both sides by \(2x-1\): \(6x^2+7x-10=(3x+5)(2x-1)+r=6x^2+7x-5+r\). So \(-10=-5+r\), and \(r=-5\). (\(r\) is the remainder when dividing by \(2x-1\).)")

def _adv13():
    best = None
    for sol in solve([Eq(a*b, 15), Eq(a + b, 8)], [a, b], dict=True):
        cv = expand((sol[a]*x + 3)*(sol[b]*x + 7)).coeff(x, 1)
        best = cv if best is None else max(best, cv)
    return best

Q(id="ADV-13", domain="ADV", skill=EQ, diff=3, desmos=False,
  stem=r"\[(ax+3)(bx+7)=15x^2+cx+21\]The given equation is true for all values of \(x\), where \(a\), \(b\), and \(c\) are constants. If \(a+b=8\), what is the greatest possible value of \(c\)?",
  answer="44", verify=_adv13,
  explain=r"Expanding the left side: \(abx^2+(7a+3b)x+21\). So \(ab=15\) and \(c=7a+3b\). With \(a+b=8\) and \(ab=15\), the numbers \(a\) and \(b\) are 3 and 5 in some order. "
          r"If \(a=3,b=5\): \(c=21+15=36\). If \(a=5,b=3\): \(c=35+9=44\). The greatest value is 44.")

def _adv14():
    sols = solve([Eq(y, x**2 - 4*x + 1), Eq(y, 2*x - 8)], [x, y], dict=True)
    assert len(sols) == 1
    return sols[0][x]*sols[0][y]

Q(id="ADV-14", domain="ADV", skill=NE, diff=2, desmos=True,
  stem=r"\[y=x^2-4x+1\]\[y=2x-8\]The given system of equations has exactly one solution, \((a,b)\). What is the value of \(ab\)?",
  answer="-6", verify=_adv14,
  explain=r"Substitute: \(x^2-4x+1=2x-8\), so \(x^2-6x+9=0\), or \((x-3)^2=0\). Then \(x=3\) and \(y=2(3)-8=-2\). So \(ab=3(-2)=-6\).",
  tip=r"Graph both equations. The line touches the parabola at a single point, \((3,-2)\). Multiply: \(-6\).")

Q(id="ADV-15", domain="ADV", skill=NE, diff=2, desmos=False,
  stem=r"\[x+y=10\]\[x^2-y^2=40\]If \((x,y)\) is the solution to the given system of equations, what is the value of \(x\)?",
  answer="7",
  verify=lambda: solve([Eq(x + y, 10), Eq(x**2 - y**2, 40)], [x, y], dict=True)[0][x],
  explain=r"Factor: \(x^2-y^2=(x+y)(x-y)\). So \(10(x-y)=40\), and \(x-y=4\). Adding \(x+y=10\) and \(x-y=4\): \(2x=14\), so \(x=7\).")

Q(id="ADV-16", domain="ADV", skill=EQ, diff=3, desmos=False,
  stem=r"If \(4x-6y=10\), what is the value of \(\dfrac{9^{x}}{27^{y}}\)?",
  answer="243",
  verify=lambda: simplify((S(9)**x/S(27)**y).subs(x, (10 + 6*y)/4)),
  explain=r"Rewrite with base 3: \(\frac{9^x}{27^y}=\frac{3^{2x}}{3^{3y}}=3^{2x-3y}\). Dividing \(4x-6y=10\) by 2 gives \(2x-3y=5\). So the value is \(3^5=243\).")

def _adv17():
    sols = [v for v in range(1, 50) if 3**v + 2**v == 97]
    assert len(sols) == 1
    # f is strictly increasing for x>0, so this is the only positive solution
    return sols[0]

Q(id="ADV-17", domain="ADV", skill=NE, diff=2, desmos=True,
  stem=r"The function \(f\) is defined by \(f(x)=3^{x}+2^{x}\). What is the positive value of \(x\) for which \(f(x)=97\)?",
  answer="4", verify=_adv17,
  explain=r"Try small integers: \(3^4+2^4=81+16=97\). Since \(f\) is always increasing, \(x=4\) is the only solution.",
  tip=r"Graph \(y=3^x+2^x\) and \(y=97\). Click the intersection: \((4,97)\).")

Q(id="ADV-18", domain="ADV", skill=NF, diff=2, desmos=False,
  stem=r"The functions \(f\) and \(g\) are defined by \(f(x)=2x-3\) and \(g(x)=x^2+1\). What is the value of \(f(g(-2))-g(f(-2))\)?",
  answer="-43",
  verify=lambda: (lambda f, g: f(g(-2)) - g(f(-2)))(lambda X: 2*X - 3, lambda X: X**2 + 1),
  explain=r"\(g(-2)=5\), so \(f(g(-2))=f(5)=7\). \(f(-2)=-7\), so \(g(f(-2))=g(-7)=50\). The difference is \(7-50=-43\).")

def _adv19():
    n = 1
    while 12000*1.03**n <= 18000*0.98**n:
        n += 1
    return n

Q(id="ADV-19", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"Town A has a population of 12,000 that increases by 3% each year. Town B has a population of 18,000 that decreases by 2% each year. What is the least number of whole years from now after which the population of Town A is greater than the population of Town B?",
  answer="9", verify=_adv19,
  explain=r"Solve \(12000(1.03)^n>18000(0.98)^n\), which is \(\left(\frac{1.03}{0.98}\right)^n>1.5\). "
          r"At \(n=8\): A \(\approx15{,}201\), B \(\approx15{,}314\) (A is still smaller). At \(n=9\): A \(\approx15{,}657\), B \(\approx15{,}008\). The least whole number of years is 9.",
  tip=r"Graph \(y=12000(1.03)^x\) and \(y=18000(0.98)^x\). They intersect at \(x\approx8.15\), so the first whole year is 9.")

def _adv20():
    kk = symbols("kk")
    # roots r, r+4 with sum 6 (from -(-12)/2)
    r = solve(Eq(2*x + 4, 6), x)[0]
    return 2*r*(r + 4)

Q(id="ADV-20", domain="ADV", skill=NE, diff=3, desmos=False,
  stem=r"The equation \(2x^2-12x+k=0\), where \(k\) is a constant, has two real solutions. The difference between the two solutions is 4. What is the value of \(k\)?",
  answer="10", verify=_adv20,
  explain=r"Dividing by 2, the solutions add to \(\frac{12}{2}=6\). Two numbers that add to 6 and differ by 4 are 5 and 1. "
          r"Their product is \(\frac k2\), so \(\frac k2=5\) and \(k=10\). Check: \(2x^2-12x+10=2(x-1)(x-5)\). ✓")

Q(id="ADV-21", domain="ADV", skill=NE, diff=2, desmos=True,
  stem=r"How many distinct real solutions does the equation \(x^4-5x^2-36=0\) have?",
  choices=["Zero", "Two", "Three", "Four"], vals=[0, 2, 3, 4], answer="B",
  verify=lambda: _real_solution_count(x**4 - 5*x**2 - 36),
  explain=r"Treat it as a quadratic in \(x^2\): \((x^2-9)(x^2+4)=0\). \(x^2=9\) gives \(x=\pm3\); \(x^2=-4\) has no real solutions. So there are two.",
  tip=r"Graph \(y=x^4-5x^2-36\). It crosses the \(x\)-axis exactly twice, at \(-3\) and \(3\).")

def _adv22():
    f = lambda T: 450*1.08**(T/6)
    ratio6 = f(13)/f(7)
    ratio1 = f(8)/f(7)
    if abs(ratio6 - 1.08) < 1e-12 and abs(ratio1 - 1.08) > 1e-3:
        return "B"
    return "?"

Q(id="ADV-22", domain="ADV", skill=NF, diff=2, desmos=False,
  stem=r"The function \(f(t)=450(1.08)^{t/6}\) models the number of members of a club \(t\) years after the club was founded. Which of the following is the best interpretation of the number 1.08 in this context?",
  choices=["The number of members increases by 8% each year.",
           "The number of members increases by 8% every 6 years.",
           "The number of members increases by 1.08% every 6 years.",
           "The number of members increases by 48% every 6 years."],
  answer="B", verify=_adv22,
  explain=r"The exponent \(\frac t6\) increases by 1 each time \(t\) increases by 6. So every 6 years the number of members is multiplied by 1.08, an 8% increase every 6 years.")

def _adv23():
    bb = solve(Eq((x**2 + b*x - 15).subs(x, -3), 0), b)[0]
    return max(solve(x**2 + bb*x - 15, x))

Q(id="ADV-23", domain="ADV", skill=NF, diff=1, desmos=False,
  stem=r"The function \(f\) is defined by \(f(x)=x^2+bx-15\), where \(b\) is a constant. If \(f(-3)=0\), what is the positive zero of \(f\)?",
  answer="5", verify=_adv23,
  explain=r"\(f(-3)=9-3b-15=0\), so \(b=-2\). Then \(f(x)=x^2-2x-15=(x-5)(x+3)\), and the positive zero is 5. "
          r"(Shortcut: the product of the zeros is \(-15\), and one zero is \(-3\), so the other is 5.)")

Q(id="ADV-24", domain="ADV", skill=EQ, diff=2, desmos=True,
  stem=r"Which of the following is equivalent to \(\sqrt[3]{x^{2}}\cdot\sqrt{x^{3}}\), for \(x>0\)?",
  choices=[r"\(x^{\frac{13}{6}}\)", r"\(x\)", r"\(x^{\frac{5}{6}}\)", r"\(x^{\frac{6}{13}}\)"],
  vals=["x**(13/6)", "x", "x**(5/6)", "x**(6/13)"], answer="A",
  verify=lambda: x**R(2, 3)*x**R(3, 2),
  explain=r"\(\sqrt[3]{x^2}=x^{2/3}\) and \(\sqrt{x^3}=x^{3/2}\). Multiplying adds exponents: \(\frac23+\frac32=\frac{4}{6}+\frac{9}{6}=\frac{13}{6}\).",
  tip=r"Graph \(y=\sqrt[3]{x^2}\sqrt{x^3}\) and each choice. Only \(x^{13/6}\) overlaps it exactly for \(x>0\).")

Q(id="ADV-25", domain="ADV", skill=EQ, diff=1, desmos=True,
  stem=r"Which of the following is equivalent to \(\dfrac{1}{x+2}+\dfrac{1}{x-2}\), for \(x>2\)?",
  choices=[r"\(\dfrac{2x}{x^2-4}\)", r"\(\dfrac{2}{x^2-4}\)", r"\(\dfrac{2}{2x}\)", r"\(\dfrac{2x}{x^2+4}\)"],
  vals=["2*x/(x**2-4)", "2/(x**2-4)", "2/(2*x)", "2*x/(x**2+4)"], answer="A",
  verify=lambda: 1/(x + 2) + 1/(x - 2),
  explain=r"Use the common denominator \((x+2)(x-2)=x^2-4\): \(\frac{(x-2)+(x+2)}{x^2-4}=\frac{2x}{x^2-4}\).",
  tip=r"Graph the original expression and each choice. The matching graph lies exactly on top of it.")

def _adv26():
    return _real_solution_count(x**3 - 6*x**2 + 9*x + 2 - 4)

Q(id="ADV-26", domain="ADV", skill=NF, diff=3, desmos=True,
  stem=r"The function \(f\) is defined by \(f(x)=x^3-6x^2+9x+2\). For how many values of \(x\) does \(f(x)=4\)?",
  choices=["One", "Two", "Three", "Four"], vals=[1, 2, 3, 4], answer="C", verify=_adv26,
  explain=r"Solve \(x^3-6x^2+9x-2=0\). \(x=2\) works (\(8-24+18-2=0\)), so factor: \((x-2)(x^2-4x+1)=0\). "
          r"The quadratic gives \(x=2\pm\sqrt3\), two more distinct real values. Total: three.",
  tip=r"Graph \(y=x^3-6x^2+9x+2\) and \(y=4\). The horizontal line crosses the cubic three times.")

Q(id="ADV-27", domain="ADV", skill=NF, diff=1, desmos=False,
  stem=r"The function \(f\) is defined by \(f(x)=\dfrac{x+k}{x-3}\), where \(k\) is a constant. If \(f(5)=4\), what is the value of \(f(-1)\)?",
  answer="-1/2",
  verify=lambda: (lambda kk: (-1 + kk)/(-1 - 3))(solve(Eq((5 + k)/(5 - 3), 4), k)[0]),
  explain=r"\(\frac{5+k}{2}=4\), so \(k=3\). Then \(f(-1)=\frac{-1+3}{-1-3}=\frac{2}{-4}=-\frac12\).")

Q(id="ADV-28", domain="ADV", skill=NE, diff=3, desmos=True,
  stem=r"If \(4^{x+2}-4^{x}=960\), what is the value of \(x\)?",
  answer="3",
  verify=lambda: [v for v in solve(Eq(S(4)**(x + 2) - S(4)**x, 960), x) if v.is_real][0],
  explain=r"Factor out \(4^x\): \(4^x(4^2-1)=960\), so \(15\cdot4^x=960\) and \(4^x=64=4^3\). So \(x=3\).",
  tip=r"Graph \(y=4^{x+2}-4^x\) and \(y=960\). Zoom out and click the intersection: \(x=3\).")

Q(id="ADV-29", domain="ADV", skill=NF, diff=2, desmos=False,
  stem=r"The quadratic function \(q\) has zeros at \(x=-1\) and \(x=7\), and \(q(0)=14\). What is the value of \(q(5)\)?",
  answer="24",
  verify=lambda: (lambda av: av*(5 + 1)*(5 - 7))(solve(Eq(a*(0 + 1)*(0 - 7), 14), a)[0]),
  explain=r"Write \(q(x)=a(x+1)(x-7)\). Then \(q(0)=-7a=14\), so \(a=-2\). \(q(5)=-2(6)(-2)=24\).")

def _adv30():
    av = solve(Eq(a*(6 - 4)**2 - 3, 5), a)[0]
    poly = expand(av*(x - 4)**2 - 3)
    return sum(Poly(poly, x).all_coeffs())

Q(id="ADV-30", domain="ADV", skill=NF, diff=3, desmos=False,
  stem=r"In the \(xy\)-plane, the graph of \(y=ax^2+bx+c\), where \(a\), \(b\), and \(c\) are constants, has its vertex at \((4,-3)\) and passes through the point \((6,5)\). What is the value of \(a+b+c\)?",
  answer="15", verify=_adv30,
  explain=r"Vertex form: \(y=a(x-4)^2-3\). Through \((6,5)\): \(4a-3=5\), so \(a=2\). "
          r"Key insight: \(a+b+c\) is just the value of \(y\) when \(x=1\). \(y(1)=2(1-4)^2-3=18-3=15\).")
