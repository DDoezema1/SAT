"""Desmos alternatives for questions whose intended route is by hand.

The question stays tagged "By hand", but the solution also shows how Desmos could
get (or check) the answer. For a student working on Desmos fluency, seeing that most
algebra questions have a 30-second graphing route is the point.
"""
from .common import QUESTIONS

ALT = {
    "ALG-03": r"Graph \(3x+ky=7\) and \(kx+12y=14\) with a slider for \(k\). At \(k=6\) the lines lie on top of each other (infinitely many solutions). At \(k=-6\) they're parallel and separate (no solution).",
    "ALG-04": r"Plot \((8,1340)\) and \((20,860)\), type <code>y-1340=m(x-8)</code>, and set \(m=-40\). Click the \(y\)-intercept: 1,660.",
    "ALG-16": r"Type the equation exactly as written, using \(x\). Desmos draws a vertical line at the solution, \(x=6.5\).",
    "ALG-18": r"Graph \(650x+280y\le5000\) and \(x+y\ge10\), with \(x\) = laptops. Find the overlap and the largest whole-number \(x\) that has a whole-number \(y\) in it: \((5,5)\).",
    "ALG-21": r"Pick any line through \((2,-5)\), for example <code>f(x)=x-7</code>. Then graph <code>y=f(x-4)+3</code> and see which answer choice is on it.",
    "ALG-25": r"Graph \(3x-2y=11\) and \(x+4y=13\) (with \(x=a\), \(y=b\)). The intersection is \((5,2)\), so \(4a+2b=24\).",
    "ADV-11": r"Graph <code>y=a(x-2)(x-8)</code> with a slider. Click the vertex and adjust \(a\) until its \(y\)-value is \(-27\) (\(a=3\)). Then type <code>3(10-2)(10-8)</code>.",
    "ADV-12": r"Graph both \(y=\frac{6x^2+7x-10}{2x-1}\) and \(y=3x+5+\frac{r}{2x-1}\) with a slider for \(r\). The graphs overlap exactly at \(r=-5\).",
    "ADV-15": r"Graph \(x+y=10\) and \(x^2-y^2=40\). They intersect at \((7,3)\).",
    "ADV-16": r"Plug in any point that satisfies \(4x-6y=10\), such as \(x=2.5\), \(y=0\). Then type <code>9^{2.5}/27^0</code>: 243. Picking a convenient point is a powerful move whenever the answer can't depend on which point you pick.",
    "ADV-18": r"Define <code>f(x)=2x-3</code> and <code>g(x)=x^2+1</code> on separate lines, then type <code>f(g(-2))-g(f(-2))</code>: \(-43\).",
    "ADV-23": r"Graph <code>y=x^2+bx-15</code> with a slider and adjust \(b\) until the graph passes through \((-3,0)\). Then click the other \(x\)-intercept: 5.",
    "ADV-29": r"Graph <code>y=a(x+1)(x-7)</code> with a slider and adjust \(a\) until the graph passes through \((0,14)\) (\(a=-2\)). Then click the curve at \(x=5\): 24.",
    "ADV-30": r"Make a table with \((4,-3)\), \((6,5)\), and the mirror point \((2,5)\). Type <code>y_1 ~ a x_1^2 + b x_1 + c</code>, then <code>a+b+c</code>: 15.",
    "ADV-35": r"Graph \(y=x-\frac1x\) and \(y=3\). Click the positive intersection, \(x\approx3.303\), then evaluate \(x^2+\frac{1}{x^2}\) there: 11.",
    "ADV-36": r"Make a table with \((1,6)\) and \((3,54)\), and type <code>y_1 ~ a b^{x_1}</code>. Desmos gives \(a=2\), \(b=3\). Then <code>2(3)^4</code> = 162.",
    "PSD-09": r"Test a small example. Type <code>L=[1,2,6]</code>, then compare <code>stdev(L)</code> with <code>stdev(3L+5)</code>: exactly 3 times larger. Do the same with <code>mean</code>.",
    "PSD-24": r"Type <code>L=[1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,5,5]</code> and compare <code>mean(L)</code> (2.95) with <code>median(L)</code> (3).",
    "PSD-26": r"Type <code>stdev([10,12,14,16,18])</code> and <code>stdev([6,12,14,16,22])</code> and compare.",
    "GEO-02": r"Graph the equation exactly as written. Click the leftmost and rightmost points of the circle: their distance apart is \(2\sqrt{17}\approx8.25\), so \(r\approx4.12=\sqrt{17}\).",
    "GEO-07": r"In <b>degree</b> mode (wrench icon), graph \(y=\sin(x)\) and \(y=\cos(3x-10)\). The intersection with both angles acute is at \(x=25\).",
    "GEO-25": r"In radian mode, type <code>sin(pi+arctan(0.75))</code>: \(-0.6=-\frac35\).",
    "TOP-14": r"Graph <code>y=x^3+ax^2+bx-6</code> with sliders for \(a\) and \(b\), then adjust them until the graph crosses the \(x\)-axis at 3 and \(-1\) (\(a=0\), \(b=-7\)).",
}

for q in QUESTIONS:
    if q["id"] in ALT:
        assert not q["desmos"] and not q["tip"], q["id"]
        q["tip"] = ALT[q["id"]]
assert set(ALT) <= {q["id"] for q in QUESTIONS}
