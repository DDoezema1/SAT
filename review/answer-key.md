# Answer key (generated)

Every question below passed the automated checks in `tools/build_bank.py`. Questions marked *computed* had their answers re-derived independently by code; questions marked *reasoning* are interpretation questions that were reviewed by hand.

## Algebra

### ALG-01 · Linear equations in one variable · Hard · Desmos · computed

\[\frac{3x-5}{4}-\frac{x+1}{6}=\frac{x}{3}+2\]What value of \(x\) is the solution to the given equation?

**Answer:** 41/3

**Explanation:** Multiply every term by 12 (the least common denominator): \(3(3x-5)-2(x+1)=4x+24\). Expand: \(9x-15-2x-2=4x+24\), so \(7x-17=4x+24\). Then \(3x=41\) and \(x=\frac{41}{3}\). Acceptable entries include 41/3, 13.66, and 13.67.

### ALG-02 · Linear equations in one variable · Very hard · By hand · computed

\[k(3x-4)+2x=11x-(k+2c)\]In the given equation, \(k\) and \(c\) are constants. If the equation has infinitely many solutions, what is the value of \(c\)?

**Answer:** 9/2

**Explanation:** An equation has infinitely many solutions only when both sides are identical. Left side: \((3k+2)x-4k\). Right side: \(11x-k-2c\). Match the \(x\)-coefficients: \(3k+2=11\), so \(k=3\). Match the constants: \(-4k=-k-2c\), so \(-12=-3-2c\), giving \(2c=9\) and \(c=\frac{9}{2}\).

### ALG-03 · Systems of two linear equations in two variables · Very hard · By hand · computed

\[3x+ky=7\]\[kx+12y=14\]In the given system of equations, \(k\) is a constant. For which value of \(k\) does the system have no solution?

- A) \(-36\)
- B) \(-6\)
- C) \(6\)
- D) \(36\)

**Answer:** B

**Explanation:** A linear system has no solution when the lines are parallel but not identical: the coefficient ratios match but the constant ratio does not. \(\frac{3}{k}=\frac{k}{12}\) gives \(k^2=36\), so \(k=6\) or \(k=-6\). If \(k=6\): ratios are \(\frac{3}{6}=\frac{6}{12}=\frac{7}{14}=\frac12\) &mdash; the same line, so infinitely many solutions. If \(k=-6\): \(\frac{3}{-6}=\frac{-6}{12}=-\frac12\), but \(\frac{7}{14}=\frac12\). Parallel, distinct lines &rarr; no solution. So \(k=-6\).

### ALG-04 · Linear functions · Medium · By hand · computed

A water tank is drained at a constant rate. Eight minutes after draining begins, the tank holds 1,340 liters of water. Twenty minutes after draining begins, the tank holds 860 liters. How many liters of water were in the tank when draining began?

- A) 1,020
- B) 1,380
- C) 1,660
- D) 1,820

**Answer:** C

**Explanation:** The rate is \(\frac{860-1340}{20-8}=\frac{-480}{12}=-40\) liters per minute. Going back 8 minutes from 1,340 liters: \(1340+8(40)=1660\) liters.

### ALG-05 · Linear functions · Very hard · By hand · computed

The function \(g\) is linear with a positive slope, and \(g(g(x))=9x-8\) for all values of \(x\). What is the value of \(g(5)\)?

**Answer:** 13

**Explanation:** Write \(g(x)=mx+b\). Then \(g(g(x))=m(mx+b)+b=m^2x+(mb+b)\). Matching \(9x-8\): \(m^2=9\), so \(m=3\) (positive slope), and \(3b+b=-8\), so \(b=-2\). Thus \(g(x)=3x-2\) and \(g(5)=13\).

### ALG-06 · Systems of two linear equations in two variables · Medium · Desmos · computed

\[\tfrac{1}{2}x+\tfrac{2}{3}y=7\]\[0.4x-0.25y=0.9\]If \((x,y)\) is the solution to the given system of equations, what is the value of \(x+y\)?

**Answer:** 12

**Explanation:** Clear the fractions and decimals: multiply the first equation by 6 to get \(3x+4y=42\); multiply the second by 20 to get \(8x-5y=18\). Multiply the first by 5 and the second by 4 and add: \(15x+32x=210+72\), so \(47x=282\) and \(x=6\). Then \(4y=42-18=24\), \(y=6\). So \(x+y=12\).

### ALG-07 · Systems of two linear equations in two variables · Hard · By hand · computed

\[2x-3y=12\]\[(k-1)x+6y=c\]In the given system of equations, \(k\) and \(c\) are constants. The system has infinitely many solutions. What is the value of \(k+c\)?

**Answer:** -27

**Explanation:** For infinitely many solutions the second equation must be a multiple of the first. Since \(6y=-2(-3y)\), the multiplier is \(-2\). Then \(k-1=-2(2)=-4\), so \(k=-3\), and \(c=-2(12)=-24\). So \(k+c=-27\).

### ALG-08 · Systems of two linear equations in two variables · Hard · Desmos · computed

A theater sold 420 tickets for one performance. Adult tickets cost $14 each and student tickets cost $9 each. The total revenue from adult tickets was $590 more than the total revenue from student tickets. How many student tickets were sold?

**Answer:** 230

**Explanation:** Let \(a\) be adult tickets and \(s\) be student tickets: \(a+s=420\) and \(14a-9s=590\). Substitute \(a=420-s\): \(14(420-s)-9s=590\), so \(5880-23s=590\), \(23s=5290\), and \(s=230\).

### ALG-09 · Linear inequalities in one or two variables · Hard · Desmos · computed

\[y \gt 2x+3\]\[y \lt -\tfrac{1}{2}x+k\]In the given system of inequalities, \(k\) is a constant. The point \((-4,-1)\) is a solution to the system. Which of the following could be the value of \(k\)?

- A) \(-5\)
- B) \(-4\)
- C) \(-3\)
- D) \(-2\)

**Answer:** D

**Explanation:** Check the first inequality: \(-1 \gt 2(-4)+3=-5\). True. Second inequality: \(-1 \lt -\tfrac12(-4)+k=2+k\), so \(k \gt -3\). The inequality is strict, so \(k=-3\) does not work. Only \(-2\) is greater than \(-3\).

### ALG-10 · Linear inequalities in one or two variables · Hard · By hand · computed

A delivery van weighs 5,200 pounds when empty. The total weight of the van, the driver, and the cargo must not exceed 9,000 pounds. The driver weighs 180 pounds. The van is carrying 25 crates that each weigh 85 pounds and some boxes that each weigh 40 pounds. What is the maximum number of boxes the van can carry?

- A) \(37\)
- B) \(38\)
- C) \(41\)
- D) \(90\)

**Answer:** A

**Explanation:** \(5200+180+25(85)+40n\le 9000\). The fixed weight is \(5200+180+2125=7505\), so \(40n\le1495\) and \(n\le37.375\). The number of boxes must be a whole number, so the maximum is 37.

### ALG-11 · Linear equations in two variables · Hard · Desmos · computed

In the \(xy\)-plane, line \(\ell\) passes through the point \((-3,7)\) and is perpendicular to the graph of \(4x-6y=5\). What is the \(y\)-coordinate of the \(y\)-intercept of line \(\ell\)?

**Answer:** 5/2

**Explanation:** Rewrite \(4x-6y=5\) as \(y=\frac23x-\frac56\); its slope is \(\frac23\). A perpendicular slope is \(-\frac32\). Line \(\ell\): \(y-7=-\frac32(x+3)\). At \(x=0\): \(y=7-\frac92=\frac52\).

### ALG-12 · Linear equations in two variables · Hard · By hand · computed

In the \(xy\)-plane, line \(k\) has \(x\)-intercept \((a,0)\) and \(y\)-intercept \((0,b)\), where \(a\) and \(b\) are nonzero constants. Line \(k\) is parallel to the graph of \(5x+2y=3\). If \(a+b=21\), what is the value of \(b\)?

**Answer:** 15

**Explanation:** The slope through \((a,0)\) and \((0,b)\) is \(\frac{b-0}{0-a}=-\frac{b}{a}\). The line \(5x+2y=3\) has slope \(-\frac52\). So \(\frac ba=\frac52\), meaning \(b=\frac52a\). Then \(a+\frac52a=21\), so \(\frac72a=21\), \(a=6\), and \(b=15\).

### ALG-13 · Linear inequalities in one or two variables · Medium · Desmos · computed

Gym A charges a one-time fee of $60 plus $35 per month. Gym B charges a one-time fee of $20 plus $43 per month. What is the least number of whole months after which the total amount paid to Gym B is greater than the total amount paid to Gym A?

- A) \(4\)
- B) \(5\)
- C) \(6\)
- D) \(7\)

**Answer:** C

**Explanation:** \(20+43m \gt 60+35m\) gives \(8m \gt 40\), so \(m \gt 5\). At exactly 5 months the totals are equal ($235 each), so the least whole number of months is 6.

### ALG-14 · Linear functions · Medium · Desmos · computed

The height above the ground of a descending weather balloon is a linear function of time. The balloon is 195 meters above the ground 5 seconds after it starts descending and 39 meters above the ground 17 seconds after it starts descending. How many seconds after it starts descending does the balloon reach the ground?

- A) \(15\)
- B) \(17\)
- C) \(20\)
- D) \(23\)

**Answer:** C

**Explanation:** Slope: \(\frac{39-195}{17-5}=-13\) meters per second. Height: \(h(t)=195-13(t-5)=260-13t\). Setting \(h(t)=0\): \(t=20\).

### ALG-15 · Linear equations in two variables · Hard · By hand · computed

In the \(xy\)-plane, line \(p\) has a positive slope and a negative \(y\)-intercept. Line \(q\) is the reflection of line \(p\) across the \(y\)-axis. Which of the following must be true about line \(q\)?

- A) It has a positive slope and a positive \(y\)-intercept.
- B) It has a negative slope and a negative \(y\)-intercept.
- C) It has a negative slope and a positive \(y\)-intercept.
- D) It has a positive slope and a negative \(y\)-intercept.

**Answer:** B

**Explanation:** Reflecting across the \(y\)-axis replaces \(x\) with \(-x\): \(y=mx+b\) becomes \(y=-mx+b\). The slope changes sign (positive &rarr; negative), but the \(y\)-intercept lies on the mirror line, so it does not move and stays negative.

### ALG-16 · Linear equations in one variable · Medium · By hand · computed

\[\tfrac{2}{3}(9x-6)-5=\tfrac{1}{2}(8x+2)+3\]What value of \(x\) satisfies the given equation?

**Answer:** 13/2

**Explanation:** Distribute: \(6x-4-5=4x+1+3\), so \(6x-9=4x+4\). Then \(2x=13\) and \(x=\frac{13}{2}=6.5\).

### ALG-17 · Systems of two linear equations in two variables · Very hard · Desmos · computed

\[\frac{x}{3}+\frac{y}{4}=2\]\[\frac{x}{4}+\frac{y}{3}=\frac{5}{2}\]If \((x,y)\) is the solution to the given system of equations, what is the value of \(x+y\)?

**Answer:** 54/7

**Explanation:** You never need \(x\) and \(y\) separately. Add the two equations: \(x\left(\frac13+\frac14\right)+y\left(\frac14+\frac13\right)=2+\frac52\), so \(\frac{7}{12}(x+y)=\frac92\). Multiply by \(\frac{12}{7}\): \(x+y=\frac{54}{7}\). Acceptable entries include 54/7 and 7.714.

### ALG-18 · Linear inequalities in one or two variables · Hard · By hand · computed

A school has a budget of at most $5,000 to buy laptops and tablets. Each laptop costs $650 and each tablet costs $280. The school must buy at least 10 devices in total. What is the maximum number of laptops the school can buy?

**Answer:** 5

**Explanation:** Let \(L\) be laptops and \(T\) tablets: \(650L+280T\le5000\) and \(L+T\ge10\). To make room for as many laptops as possible, buy the fewest tablets allowed: \(T=10-L\). Then \(650L+280(10-L)\le5000\), so \(370L\le2200\) and \(L\le5.94\). Check \(L=5,T=5\): \(3250+1400=4650\le5000\). \(L=6,T=4\) costs \(5020\), which is too much. Maximum: 5.

### ALG-19 · Linear equations in two variables · Medium · Desmos · computed

In the \(xy\)-plane, a line has an \(x\)-intercept at \((4,0)\) and passes through the point \((-2,9)\). Which of the following is an equation of the line?

- A) \(3x+2y=12\)
- B) \(2x+3y=8\)
- C) \(3x-2y=12\)
- D) \(2x-3y=8\)

**Answer:** A

**Explanation:** Slope: \(\frac{9-0}{-2-4}=-\frac32\). Point-slope: \(y=-\frac32(x-4)\), so \(2y=-3x+12\), or \(3x+2y=12\). Check \((-2,9)\): \(-6+18=12\). ✓

### ALG-20 · Linear equations in two variables · Hard · Desmos · computed

In the \(xy\)-plane, the graph of \(y=kx+4\), where \(k\) is a constant, intersects the graph of \(2x+5y=20\) at a point on the \(x\)-axis. What is the value of \(k\)?

**Answer:** -2/5

**Explanation:** The graph of \(2x+5y=20\) meets the \(x\)-axis where \(y=0\): \(x=10\). So \((10,0)\) is on \(y=kx+4\): \(0=10k+4\), and \(k=-\frac25=-0.4\).

### ALG-21 · Linear functions · Hard · By hand · computed

The graph of the linear function \(f\) passes through the point \((2,-5)\) in the \(xy\)-plane. Through which of the following points must the graph of \(y=f(x-4)+3\) pass?

- A) \((6,-2)\)
- B) \((-2,-2)\)
- C) \((6,-8)\)
- D) \((-2,-8)\)

**Answer:** A

**Explanation:** \(y=f(x-4)+3\) shifts the graph of \(f\) right 4 units and up 3 units. The point \((2,-5)\) moves to \((2+4,-5+3)=(6,-2)\). Check: at \(x=6\), \(f(6-4)+3=f(2)+3=-5+3=-2\).

### ALG-22 · Linear equations in two variables · Medium · By hand · computed

A store sells pens in packs of 12 and pencils in packs of 20. The equation \(12x+20y=640\) represents the situation in which a teacher buys \(x\) packs of pens and \(y\) packs of pencils for a total of 640 writing utensils. If the teacher buys 5 more packs of pens, how must the number of packs of pencils change so that the total number of writing utensils is still 640?

- A) It must decrease by 3.
- B) It must decrease by 5.
- C) It must decrease by 12.
- D) It must increase by 3.

**Answer:** A

**Explanation:** 5 more packs of pens add \(5\times12=60\) utensils. To keep the total the same, remove 60 pencils: \(60\div20=3\) packs. So \(y\) decreases by 3.

### ALG-23 · Linear equations in one variable · Very hard · By hand · computed

\[a(x+3)-2(x-b)=5x+18\]In the given equation, \(a\) and \(b\) are constants. If the equation has infinitely many solutions, what is the value of \(b\)?

**Answer:** -3/2

**Explanation:** Expand the left side: \((a-2)x+(3a+2b)\). For infinitely many solutions it must equal \(5x+18\) exactly. So \(a-2=5\) (\(a=7\)) and \(3a+2b=18\): \(21+2b=18\), \(b=-\frac32=-1.5\).

### ALG-24 · Systems of two linear equations in two variables · Hard · Desmos · computed

\[y=0.5x+3.25\]\[1.75x-2.5y=-4.5\]The solution to the given system of equations is \((x,y)\). What is the value of \(x\)?

- A) \(5.5\)
- B) \(6.75\)
- C) \(7.25\)
- D) \(8.5\)

**Answer:** C

**Explanation:** Substitute: \(1.75x-2.5(0.5x+3.25)=-4.5\), so \(1.75x-1.25x-8.125=-4.5\). Then \(0.5x=3.625\), and \(x=7.25\).

### ALG-25 · Systems of two linear equations in two variables · Hard · By hand · computed

\[3a-2b=11\]\[a+4b=13\]If \((a,b)\) is the solution to the given system of equations, what is the value of \(4a+2b\)?

- A) \(12\)
- B) \(18\)
- C) \(24\)
- D) \(30\)

**Answer:** C

**Explanation:** Look for a shortcut before solving: adding the two equations gives \(4a+2b=24\) directly.

### ALG-26 · Linear equations in two variables · Hard · By hand · computed

The monthly cost \(C\), in dollars, of a phone plan is given by \(C=0.08m+0.12t+25\), where \(m\) is the number of minutes of calls and \(t\) is the number of text messages sent that month. If next month a customer sends 50 more text messages and uses 100 fewer minutes than this month, how will the customer's cost change?

- A) It will decrease by $2.00.
- B) It will increase by $2.00.
- C) It will decrease by $14.00.
- D) It will increase by $14.00.

**Answer:** A

**Explanation:** Change in cost: \(0.12(50)+0.08(-100)=6-8=-2\). The cost decreases by $2.00.

### ALG-27 · Linear functions · Medium · By hand · computed

In the \(xy\)-plane, the graph of the linear function \(f\) passes through the points \((-2,5)\) and \((4,-7)\). If \(f(x)=mx+b\), what is the value of \(m-b\)?

**Answer:** -3

**Explanation:** Slope: \(m=\frac{-7-5}{4-(-2)}=-2\). Using \((-2,5)\): \(5=-2(-2)+b\), so \(b=1\). Then \(m-b=-2-1=-3\).

### ALG-28 · Linear inequalities in one or two variables · Very hard · Desmos · computed

\[y\le -2x+10\]\[y\ge \tfrac12x\]\[x\ge0\]In the \(xy\)-plane, the solution region of the given system of inequalities is a triangle. What is the greatest possible \(y\)-coordinate of any point in the solution region?

**Answer:** 10

**Explanation:** The vertices of the triangle are where the boundary lines meet: \((0,0)\) from \(y=\frac12x\) and \(x=0\); \((0,10)\) from \(y=-2x+10\) and \(x=0\); and \((4,2)\) from \(-2x+10=\frac12x\). The greatest \(y\)-value in a triangle occurs at a vertex: 10.

### TOP-04 · Linear inequalities in one or two variables · Very hard · Desmos · computed

\[y\le3x+2\]\[y\le-x+10\]\[y\ge0\]Point \((x,y)\) lies in the solution region of the given system of inequalities. What is the maximum possible value of \(2x+y\)?

**Answer:** 20

**Explanation:** The region is a triangle with vertices \(\left(-\frac23,0\right)\), \((2,8)\), and \((10,0)\). A linear expression like \(2x+y\) is greatest at a vertex: \(-\frac43\), \(12\), and \(20\). The maximum is 20, at \((10,0)\). The trap is assuming the &ldquo;top&rdquo; corner \((2,8)\) wins.

### TOP-11 · Systems of two linear equations in two variables · Hard · Desmos · computed

\[0.35x+1.2y=8.95\]\[2.4x-0.75y=7.5\]If \((x,y)\) is the solution to the given system of equations, what is the value of \(xy\)?

**Answer:** 30

**Explanation:** Solving by elimination works but is slow with these decimals: the solution is \((5,6)\), so \(xy=30\).

### TOP-19 · Linear functions · Very hard · By hand · computed

The function \(f\) is linear, and \(f(3x+1)=6x+11\) for all values of \(x\). What is the value of \(f(7)\)?

**Answer:** 23

**Explanation:** Fast route: find the \(x\) that makes the input equal 7. \(3x+1=7\) gives \(x=2\), so \(f(7)=6(2)+11=23\). (General route: let \(u=3x+1\); then \(x=\frac{u-1}{3}\) and \(f(u)=2(u-1)+11=2u+9\).)

### TOP-24 · Systems of two linear equations in two variables · Hard · Desmos · computed

\[y=\tfrac23x+4\]\[y=kx-2\]In the given system of equations, \(k\) is a constant. The solution to the system has an \(x\)-coordinate of 9. What is the value of \(k\)?

**Answer:** 4/3

**Explanation:** At \(x=9\), the first equation gives \(y=6+4=10\). That point is on the second line: \(10=9k-2\), so \(k=\frac{12}{9}=\frac43\). Acceptable entries include 4/3 and 1.333.

### TOP-25 · Linear inequalities in one or two variables · Hard · By hand · computed

The solutions to the inequality \(4-3x\le k\), where \(k\) is a constant, are all values of \(x\) such that \(x\ge-2\). What is the value of \(k\)?

**Answer:** 10

**Explanation:** \(4-3x\le k\) gives \(-3x\le k-4\). Dividing by \(-3\) flips the inequality: \(x\ge\frac{4-k}{3}\). Setting \(\frac{4-k}{3}=-2\) gives \(k=10\). Check: \(4-3x\le10\) gives \(x\ge-2\). ✓

### TOP-26 · Linear equations in two variables · Hard · Desmos · computed

A line in the \(xy\)-plane passes through the point \((1,-4)\) and through the point where the graphs of \(3x-y=7\) and \(x+2y=7\) intersect. What is the slope of the line?

**Answer:** 3

**Explanation:** Solve the system: \(y=3x-7\), so \(x+2(3x-7)=7\), \(7x=21\), \(x=3\), \(y=2\). Slope from \((1,-4)\) to \((3,2)\): \(\frac{2-(-4)}{3-1}=3\).

### FIG-01 · Systems of two linear equations in two variables · Very hard · Desmos · computed

                                  x  y  -2  2  4  6  8  -4  -2  2  4  6  8  O       The graph of a system of two linear equations is shown. If the equation \(x+4y=15\) is added to the system, how many solutions \((x,y)\) will the resulting system of three equations have?

- A) Zero
- B) Exactly one
- C) Exactly two
- D) Infinitely many

**Answer:** B

**Explanation:** From the graph, the lines are \(y=-x+6\) (through \((0,6)\) and \((6,0)\)) and \(y=2x-3\) (through \((0,-3)\) with slope 2). They intersect at \((3,3)\). A solution to all three equations must be that point. Check \(x+4y=15\): \(3+4(3)=15\). ✓ So the third line passes through \((3,3)\), and the system has exactly one solution.

### FIG-13 · Linear equations in one variable · Hard · Desmos · computed

\[|-4x+9|=31\]What is the sum of the solutions to the given equation?

**Answer:** 9/2

**Explanation:** An absolute value equals 31 when the inside is 31 or \(-31\). \(-4x+9=31\) gives \(x=-5.5\); \(-4x+9=-31\) gives \(x=10\). The sum is \(4.5\).

## Advanced Math

### ADV-01 · Nonlinear equations in one variable and systems of equations in two variables · Hard · Desmos · computed

\[(k+2)x^2-6x+3=0\]In the given equation, \(k\) is a constant. For which of the following values of \(k\) does the equation have no real solutions?

- A) \(-2\)
- B) \(0\)
- C) \(1\)
- D) \(2\)

**Answer:** D

**Explanation:** If \(k=-2\), the equation becomes \(-6x+3=0\), which has the solution \(x=\frac12\). Otherwise it is quadratic, with discriminant \(36-4(k+2)(3)=12-12k\). No real solutions requires \(12-12k \lt 0\), so \(k \gt 1\). Of the choices only \(k=2\) works. (When \(k=1\) the discriminant is 0, which gives exactly one solution.)

### ADV-02 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

In the \(xy\)-plane, the graph of \(y=4x+c\), where \(c\) is a constant, intersects the graph of \(y=x^2-2x+7\) at exactly one point. What is the value of \(c\)?

**Answer:** -2

**Explanation:** Set the expressions equal: \(x^2-2x+7=4x+c\), so \(x^2-6x+(7-c)=0\). Exactly one intersection means the discriminant is 0: \(36-4(7-c)=0\), so \(36-28+4c=0\) and \(c=-2\). (The line is tangent to the parabola at \(x=3\).)

### ADV-03 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

\[\frac{x}{x-3}-\frac{2}{x+3}=\frac{18}{x^2-9}\]What is the solution to the given equation?

**Answer:** -4

**Explanation:** Multiply both sides by \(x^2-9=(x-3)(x+3)\): \(x(x+3)-2(x-3)=18\), so \(x^2+x+6=18\), or \(x^2+x-12=0\). Factor: \((x+4)(x-3)=0\). But \(x=3\) makes denominators 0 in the original equation, so it is extraneous. The only solution is \(x=-4\).

### ADV-04 · Nonlinear equations in one variable and systems of equations in two variables · Hard · Desmos · computed

\[\sqrt{2x+6}=x-1\]What is the solution to the given equation?

**Answer:** 5

**Explanation:** Square both sides: \(2x+6=x^2-2x+1\), so \(x^2-4x-5=0\) and \((x-5)(x+1)=0\). Check \(x=-1\): \(\sqrt{4}=2\) but \(-1-1=-2\), so it is extraneous. Check \(x=5\): \(\sqrt{16}=4=5-1\). ✓ The solution is 5.

### ADV-05 · Nonlinear functions · Very hard · Desmos · computed

The function \(f(t)=2{,}400(0.64)^{t}\) gives the estimated value, in dollars, of a machine \(t\) years after it was purchased. Which of the following functions is equivalent to \(f\) and shows, as a constant or base, the factor by which the value changes every half year?

- A) \(f(t)=2{,}400(0.8)^{2t}\)
- B) \(f(t)=2{,}400(0.8)^{t/2}\)
- C) \(f(t)=2{,}400(0.32)^{2t}\)
- D) \(f(t)=1{,}200(0.64)^{2t}\)

**Answer:** A

**Explanation:** Since \(0.64=0.8^2\), \((0.64)^t=(0.8^2)^t=(0.8)^{2t}\). So \(2{,}400(0.8)^{2t}\) is equivalent to \(f\). In that form, when \(t\) increases by \(\frac12\), the exponent \(2t\) increases by 1, so the value is multiplied by 0.8 (a 20% decrease every half year). The form \(2{,}400(0.8)^{t/2}\) would mean a factor of 0.8 every  2  years (and is not equivalent to \(f\)). The other two forms are not equivalent to \(f\) either.

### ADV-06 · Nonlinear functions · Hard · Desmos · computed

A quantity increases by 25% every 2 years. Which of the following is closest to the percent by which the quantity increases every year?

- A) 6.25%
- B) 11.8%
- C) 12.5%
- D) 25%

**Answer:** B

**Explanation:** Over 2 years the growth factor is 1.25. If the yearly factor is \(r\), then \(r^2=1.25\), so \(r=\sqrt{1.25}\approx1.118\), about 11.8% per year. 12.5% (half of 25%) is the trap: growth compounds, so \(1.125^2\approx1.266\), which is more than 1.25.

### ADV-07 · Nonlinear functions · Very hard · Desmos · computed

\[p(x)=2x^3+kx^2-11x+6\]In the polynomial function \(p\), \(k\) is a constant. If \(x-3\) is a factor of \(p(x)\), what is the sum of all the zeros of \(p\)?

**Answer:** 3/2

**Explanation:** Since \(x-3\) is a factor, \(p(3)=0\): \(54+9k-33+6=0\), so \(9k=-27\) and \(k=-3\). Then \(p(x)=2x^3-3x^2-11x+6=(x-3)(2x^2+3x-2)=(x-3)(2x-1)(x+2)\). The zeros are \(3,\frac12,-2\), and their sum is \(\frac32\). (Shortcut: for a cubic \(ax^3+bx^2+\dots\), the sum of the zeros is \(-\frac ba=\frac32\).)

### ADV-08 · Nonlinear functions · Hard · By hand · computed

For the polynomial function \(p\), \(p(3)=5\). Which of the following must be true?

- A) \(x+3\) is a factor of \(p(x)-5\).
- B) \(x-3\) is a factor of \(p(x)+5\).
- C) \(x-3\) is a factor of \(p(x)-5\).
- D) \(x-5\) is a factor of \(p(x)-3\).

**Answer:** C

**Explanation:** Let \(g(x)=p(x)-5\). Then \(g(3)=p(3)-5=0\), so 3 is a zero of \(g\), and by the factor theorem \(x-3\) is a factor of \(p(x)-5\). (Equivalently: dividing \(p(x)\) by \(x-3\) leaves remainder 5.) The other statements need extra information that is not given.

### ADV-09 · Nonlinear functions · Hard · Desmos · computed

The function \(f\) is defined by \(f(x)=x^2-6x+11\). In the \(xy\)-plane, the graph of \(y=f(x+2)-3\) has its vertex at \((h,k)\). What is the value of \(h+k\)?

**Answer:** 0

**Explanation:** Complete the square: \(f(x)=(x-3)^2+2\), with vertex \((3,2)\). The graph of \(y=f(x+2)-3\) is the graph of \(f\) shifted 2 units  left  and 3 units down, so its vertex is \((1,-1)\), and \(h+k=0\).

### ADV-10 · Nonlinear functions · Medium · Desmos · computed

The function \(h(t)=-16t^2+72t+5\) gives the height, in feet, of a ball \(t\) seconds after it is thrown. What is the maximum height, in feet, that the ball reaches?

- A) \(2.25\)
- B) \(81\)
- C) \(86\)
- D) \(167\)

**Answer:** C

**Explanation:** The vertex occurs at \(t=-\frac{72}{2(-16)}=2.25\). \(h(2.25)=-16(5.0625)+72(2.25)+5=-81+162+5=86\) feet.

### ADV-11 · Nonlinear functions · Very hard · By hand · computed

The function \(f\) is defined by \(f(x)=a(x-2)(x-8)\), where \(a\) is a constant. The minimum value of \(f\) is \(-27\). What is the value of \(f(10)\)?

- A) \(16\)
- B) \(24\)
- C) \(48\)
- D) \(96\)

**Answer:** C

**Explanation:** The vertex of a parabola is halfway between its zeros: \(x=\frac{2+8}{2}=5\). So \(f(5)=a(3)(-3)=-9a=-27\), and \(a=3\) (positive, consistent with a minimum). Then \(f(10)=3(8)(2)=48\).

### ADV-12 · Equivalent expressions · Hard · By hand · computed

The expression \(\dfrac{6x^2+7x-10}{2x-1}\) is equivalent to \(3x+5+\dfrac{r}{2x-1}\), where \(r\) is a constant and \(x\neq\frac12\). What is the value of \(r\)?

- A) \(-15\)
- B) \(-5\)
- C) \(5\)
- D) \(15\)

**Answer:** B

**Explanation:** Multiply both sides by \(2x-1\): \(6x^2+7x-10=(3x+5)(2x-1)+r=6x^2+7x-5+r\). So \(-10=-5+r\), and \(r=-5\). (\(r\) is the remainder when dividing by \(2x-1\).)

### ADV-13 · Equivalent expressions · Very hard · By hand · computed

\[(ax+3)(bx+7)=15x^2+cx+21\]The given equation is true for all values of \(x\), where \(a\), \(b\), and \(c\) are constants. If \(a+b=8\), what is the greatest possible value of \(c\)?

**Answer:** 44

**Explanation:** Expanding the left side: \(abx^2+(7a+3b)x+21\). So \(ab=15\) and \(c=7a+3b\). With \(a+b=8\) and \(ab=15\), the numbers \(a\) and \(b\) are 3 and 5 in some order. If \(a=3,b=5\): \(c=21+15=36\). If \(a=5,b=3\): \(c=35+9=44\). The greatest value is 44.

### ADV-14 · Nonlinear equations in one variable and systems of equations in two variables · Hard · Desmos · computed

\[y=x^2-4x+1\]\[y=2x-8\]The given system of equations has exactly one solution, \((a,b)\). What is the value of \(ab\)?

**Answer:** -6

**Explanation:** Substitute: \(x^2-4x+1=2x-8\), so \(x^2-6x+9=0\), or \((x-3)^2=0\). Then \(x=3\) and \(y=2(3)-8=-2\). So \(ab=3(-2)=-6\).

### ADV-15 · Nonlinear equations in one variable and systems of equations in two variables · Hard · By hand · computed

\[x+y=10\]\[x^2-y^2=40\]If \((x,y)\) is the solution to the given system of equations, what is the value of \(x\)?

**Answer:** 7

**Explanation:** Factor: \(x^2-y^2=(x+y)(x-y)\). So \(10(x-y)=40\), and \(x-y=4\). Adding \(x+y=10\) and \(x-y=4\): \(2x=14\), so \(x=7\).

### ADV-16 · Equivalent expressions · Very hard · By hand · computed

If \(4x-6y=10\), what is the value of \(\dfrac{9^{x}}{27^{y}}\)?

**Answer:** 243

**Explanation:** Rewrite with base 3: \(\frac{9^x}{27^y}=\frac{3^{2x}}{3^{3y}}=3^{2x-3y}\). Dividing \(4x-6y=10\) by 2 gives \(2x-3y=5\). So the value is \(3^5=243\).

### ADV-17 · Nonlinear equations in one variable and systems of equations in two variables · Hard · Desmos · computed

The function \(f\) is defined by \(f(x)=3^{x}+2^{x}\). What is the positive value of \(x\) for which \(f(x)=97\)?

- A) \(2\)
- B) \(3\)
- C) \(4\)
- D) \(5\)

**Answer:** C

**Explanation:** Try small integers: \(3^4+2^4=81+16=97\). Since \(f\) is always increasing, \(x=4\) is the only solution.

### ADV-18 · Nonlinear functions · Hard · By hand · computed

The functions \(f\) and \(g\) are defined by \(f(x)=2x-3\) and \(g(x)=x^2+1\). What is the value of \(f(g(-2))-g(f(-2))\)?

- A) \(-43\)
- B) \(-37\)
- C) \(43\)
- D) \(57\)

**Answer:** A

**Explanation:** \(g(-2)=5\), so \(f(g(-2))=f(5)=7\). \(f(-2)=-7\), so \(g(f(-2))=g(-7)=50\). The difference is \(7-50=-43\).

### ADV-19 · Nonlinear functions · Very hard · Desmos · computed

Town A has a population of 12,000 that increases by 3% each year. Town B has a population of 18,000 that decreases by 2% each year. What is the least number of whole years from now after which the population of Town A is greater than the population of Town B?

**Answer:** 9

**Explanation:** Solve \(12000(1.03)^n \gt 18000(0.98)^n\), which is \(\left(\frac{1.03}{0.98}\right)^n \gt 1.5\). At \(n=8\): A \(\approx15{,}201\), B \(\approx15{,}314\) (A is still smaller). At \(n=9\): A \(\approx15{,}657\), B \(\approx15{,}008\). The least whole number of years is 9.

### ADV-20 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

The equation \(2x^2-12x+k=0\), where \(k\) is a constant, has two real solutions. The difference between the two solutions is 4. What is the value of \(k\)?

**Answer:** 10

**Explanation:** Dividing by 2, the solutions add to \(\frac{12}{2}=6\). Two numbers that add to 6 and differ by 4 are 5 and 1. Their product is \(\frac k2\), so \(\frac k2=5\) and \(k=10\). Check: \(2x^2-12x+10=2(x-1)(x-5)\). ✓

### ADV-21 · Nonlinear equations in one variable and systems of equations in two variables · Hard · Desmos · computed

How many distinct real solutions does the equation \(x^4-5x^2-36=0\) have?

- A) Zero
- B) Two
- C) Three
- D) Four

**Answer:** B

**Explanation:** Treat it as a quadratic in \(x^2\): \((x^2-9)(x^2+4)=0\). \(x^2=9\) gives \(x=\pm3\); \(x^2=-4\) has no real solutions. So there are two.

### ADV-22 · Nonlinear functions · Hard · By hand · computed

The function \(f(t)=450(1.08)^{t/6}\) models the number of members of a club \(t\) years after the club was founded. Which of the following is the best interpretation of the number 1.08 in this context?

- A) The number of members increases by 8% each year.
- B) The number of members increases by 8% every 6 years.
- C) The number of members increases by 1.08% every 6 years.
- D) The number of members increases by 48% every 6 years.

**Answer:** B

**Explanation:** The exponent \(\frac t6\) increases by 1 each time \(t\) increases by 6. So every 6 years the number of members is multiplied by 1.08, an 8% increase every 6 years.

### ADV-23 · Nonlinear functions · Medium · By hand · computed

The function \(f\) is defined by \(f(x)=x^2+bx-15\), where \(b\) is a constant. If \(f(-3)=0\), what is the positive zero of \(f\)?

- A) \(2\)
- B) \(3\)
- C) \(5\)
- D) \(15\)

**Answer:** C

**Explanation:** \(f(-3)=9-3b-15=0\), so \(b=-2\). Then \(f(x)=x^2-2x-15=(x-5)(x+3)\), and the positive zero is 5. (Shortcut: the product of the zeros is \(-15\), and one zero is \(-3\), so the other is 5.)

### ADV-24 · Equivalent expressions · Hard · Desmos · computed

Which of the following is equivalent to \(\sqrt[3]{x^{2}}\cdot\sqrt{x^{3}}\), for \(x \gt 0\)?

- A) \(x^{\frac{13}{6}}\)
- B) \(x\)
- C) \(x^{\frac{5}{6}}\)
- D) \(x^{\frac{6}{13}}\)

**Answer:** A

**Explanation:** \(\sqrt[3]{x^2}=x^{2/3}\) and \(\sqrt{x^3}=x^{3/2}\). Multiplying adds exponents: \(\frac23+\frac32=\frac{4}{6}+\frac{9}{6}=\frac{13}{6}\).

### ADV-25 · Equivalent expressions · Medium · Desmos · computed

Which of the following is equivalent to \(\dfrac{1}{x+2}+\dfrac{1}{x-2}\), for \(x \gt 2\)?

- A) \(\dfrac{2x}{x^2-4}\)
- B) \(\dfrac{2}{x^2-4}\)
- C) \(\dfrac{2}{2x}\)
- D) \(\dfrac{2x}{x^2+4}\)

**Answer:** A

**Explanation:** Use the common denominator \((x+2)(x-2)=x^2-4\): \(\frac{(x-2)+(x+2)}{x^2-4}=\frac{2x}{x^2-4}\).

### ADV-26 · Nonlinear functions · Very hard · Desmos · computed

The function \(f\) is defined by \(f(x)=x^3-6x^2+9x+2\). For how many values of \(x\) does \(f(x)=4\)?

- A) One
- B) Two
- C) Three
- D) Four

**Answer:** C

**Explanation:** Solve \(x^3-6x^2+9x-2=0\). \(x=2\) works (\(8-24+18-2=0\)), so factor: \((x-2)(x^2-4x+1)=0\). The quadratic gives \(x=2\pm\sqrt3\), two more distinct real values. Total: three.

### ADV-27 · Nonlinear functions · Medium · By hand · computed

The function \(f\) is defined by \(f(x)=\dfrac{x+k}{x-3}\), where \(k\) is a constant. If \(f(5)=4\), what is the value of \(f(-1)\)?

- A) \(-2\)
- B) \(-\frac{1}{2}\)
- C) \(\frac{1}{2}\)
- D) \(2\)

**Answer:** B

**Explanation:** \(\frac{5+k}{2}=4\), so \(k=3\). Then \(f(-1)=\frac{-1+3}{-1-3}=\frac{2}{-4}=-\frac12\).

### ADV-28 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

If \(4^{x+2}-4^{x}=960\), what is the value of \(x\)?

**Answer:** 3

**Explanation:** Factor out \(4^x\): \(4^x(4^2-1)=960\), so \(15\cdot4^x=960\) and \(4^x=64=4^3\). So \(x=3\).

### ADV-29 · Nonlinear functions · Hard · By hand · computed

The quadratic function \(q\) has zeros at \(x=-1\) and \(x=7\), and \(q(0)=14\). What is the value of \(q(5)\)?

- A) \(-24\)
- B) \(12\)
- C) \(24\)
- D) \(48\)

**Answer:** C

**Explanation:** Write \(q(x)=a(x+1)(x-7)\). Then \(q(0)=-7a=14\), so \(a=-2\). \(q(5)=-2(6)(-2)=24\).

### ADV-30 · Nonlinear functions · Very hard · By hand · computed

In the \(xy\)-plane, the graph of \(y=ax^2+bx+c\), where \(a\), \(b\), and \(c\) are constants, has its vertex at \((4,-3)\) and passes through the point \((6,5)\). What is the value of \(a+b+c\)?

**Answer:** 15

**Explanation:** Vertex form: \(y=a(x-4)^2-3\). Through \((6,5)\): \(4a-3=5\), so \(a=2\). Key insight: \(a+b+c\) is just the value of \(y\) when \(x=1\). \(y(1)=2(1-4)^2-3=18-3=15\).

### ADV-31 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

\[y=x^2-8x+15\]\[y=-x^2+4x-1\]The graphs of the given equations in the \(xy\)-plane intersect at two points. What is the sum of the \(y\)-coordinates of the two points?

- A) \(-2\)
- B) \(2\)
- C) \(6\)
- D) \(8\)

**Answer:** B

**Explanation:** Set the expressions equal: \(x^2-8x+15=-x^2+4x-1\), so \(2x^2-12x+16=0\), or \(x^2-6x+8=0\), giving \(x=2\) or \(x=4\). \(y\)-values: \(4-16+15=3\) and \(16-32+15=-1\). Sum: \(2\). (6 is the trap: the sum of the \(x\)-coordinates.)

### ADV-32 · Nonlinear functions · Very hard · Desmos · computed

The function \(f\) is defined by \(f(x)=2x^3-3x^2-12x+7\). What is the minimum value of \(f(x)\) for \(0\le x\le5\)?

**Answer:** -13

**Explanation:** This question is designed for Desmos. Graph \(f\) on the interval: it decreases from \(f(0)=7\) to a low point at \(x=2\), then increases to \(f(5)=122\). The minimum value is \(f(2)=16-12-24+7=-13\).

### ADV-33 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

\[y=x^2+6x+c\]\[y=2x+1\]In the given system of equations, \(c\) is a constant. What is the greatest integer value of \(c\) for which the system has two distinct real solutions?

**Answer:** 4

**Explanation:** Substitute: \(x^2+6x+c=2x+1\), so \(x^2+4x+(c-1)=0\). Two distinct real solutions require a positive discriminant: \(16-4(c-1) \gt 0\), so \(c \lt 5\). The greatest integer is 4. (At \(c=5\), the line is tangent to the parabola: only one solution.)

### ADV-34 · Equivalent expressions · Very hard · By hand · computed

Which of the following is equivalent to \(x^2-4xy+4y^2-9\)?

- A) \((x-2y-3)(x-2y+3)\)
- B) \((x-2y-9)(x-2y+1)\)
- C) \((x+2y-3)(x+2y+3)\)
- D) \((x-4y-3)(x+y+3)\)

**Answer:** A

**Explanation:** The first three terms form a perfect square: \(x^2-4xy+4y^2=(x-2y)^2\). So the expression is \((x-2y)^2-3^2\), a difference of squares: \((x-2y-3)(x-2y+3)\).

### ADV-35 · Equivalent expressions · Very hard · By hand · computed

If \(x \gt 0\) and \(x-\dfrac{1}{x}=3\), what is the value of \(x^2+\dfrac{1}{x^2}\)?

**Answer:** 11

**Explanation:** Square both sides: \(\left(x-\frac1x\right)^2=x^2-2+\frac{1}{x^2}=9\). So \(x^2+\frac1{x^2}=11\).

### ADV-36 · Nonlinear functions · Hard · By hand · computed

The exponential function \(f\) is defined by \(f(x)=ab^{x}\), where \(a\) and \(b\) are positive constants. The graph of \(y=f(x)\) passes through the points \((1,6)\) and \((3,54)\). What is the value of \(f(4)\)?

- A) \(108\)
- B) \(162\)
- C) \(216\)
- D) \(486\)

**Answer:** B

**Explanation:** Divide: \(\frac{ab^3}{ab}=b^2=\frac{54}{6}=9\), so \(b=3\) and \(a=2\). Then \(f(4)=2\cdot3^4=162\). (108 is the trap from treating the function as linear: \(54+54\).)

### ADV-37 · Nonlinear equations in one variable and systems of equations in two variables · Hard · Desmos · computed

What is the real solution to the equation \(x^3-2x-21=0\)?

- A) \(-3\)
- B) \(3\)
- C) \(7\)
- D) \(21\)

**Answer:** B

**Explanation:** Test the choices: \(3^3-2(3)-21=27-6-21=0\). ✓ Factoring gives \((x-3)(x^2+3x+7)\), and the quadratic has no real roots (discriminant \(9-28 \lt 0\)), so 3 is the only real solution.

### ADV-38 · Nonlinear functions · Very hard · By hand · computed

In the \(xy\)-plane, the graph of \(y=ax^2+bx+c\), where \(a\), \(b\), and \(c\) are constants, is a parabola that opens downward and has its vertex in Quadrant II. Which of the following must be true?

- A) \(a \gt 0\)
- B) \(b \lt 0\)
- C) \(c \gt 0\)
- D) \(b \gt 0\)

**Answer:** B

**Explanation:** Opens downward, so \(a \lt 0\), not \(a \gt 0\). The vertex is in Quadrant II, so its \(x\)-coordinate \(-\frac{b}{2a}\) is negative. Since \(2a \lt 0\), \(-\frac{b}{2a} \lt 0\) means \(\frac{b}{2a} \gt 0\), so \(b\) has the same sign as \(a\): \(b \lt 0\). The \(y\)-intercept \(c\) can be positive or negative, depending on how high the vertex is and how steep the parabola is, so \(c \gt 0\) is not guaranteed.

### ADV-39 · Nonlinear functions · Very hard · Desmos · computed

The function \(p(t)=1{,}500(1.04)^{t}\) gives the value, in dollars, of an investment \(t\) years after it was made. What is the least whole number of years after which the value of the investment is greater than $2,500?

**Answer:** 14

**Explanation:** Solve \(1500(1.04)^t \gt 2500\), which is \((1.04)^t \gt \frac53\). Test values: \(1.04^{13}\approx1.665\), and \(1500(1.665)\approx2{,}497.60\), which is just  below  2,500. \(1.04^{14}\approx1.732\), and \(1500(1.732)\approx2{,}597.70\). So the answer is 14. (13 is the trap.)

### ADV-40 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

In the \(xy\)-plane, the graphs of \(y=3|x-2|\) and \(y=x+4\) intersect at two points. What is the sum of the \(x\)-coordinates of the two points?

**Answer:** 11/2

**Explanation:** Case \(x\ge2\): \(3(x-2)=x+4\), so \(2x=10\) and \(x=5\). Case \(x \lt 2\): \(-3(x-2)=x+4\), so \(-3x+6=x+4\) and \(x=\frac12\). Both satisfy their case conditions. Sum: \(5+\frac12=\frac{11}{2}=5.5\).

### TOP-01 · Nonlinear functions · Very hard · Desmos · computed

In the \(xy\)-plane, the graph of \(y=2x^2+bx+18\), where \(b\) is a negative constant, has exactly one \(x\)-intercept. What is the \(x\)-coordinate of that \(x\)-intercept?

**Answer:** 3

**Explanation:** Exactly one \(x\)-intercept means the vertex sits on the \(x\)-axis: discriminant \(b^2-4(2)(18)=0\), so \(b^2=144\) and \(b=-12\) (negative). The intercept is the vertex: \(x=-\frac{b}{2a}=\frac{12}{4}=3\). Check: \(2x^2-12x+18=2(x-3)^2\).

### TOP-02 · Nonlinear functions · Very hard · Desmos · computed

\[f(x)=x^3-3x^2-9x+c\]In the given function, \(c\) is a constant. The equation \(f(x)=0\) has exactly three distinct real solutions. What is the greatest possible integer value of \(c\)?

**Answer:** 26

**Explanation:** A cubic crosses the \(x\)-axis three times only if its local maximum is above the axis and its local minimum is below it. The turning points of \(x^3-3x^2-9x\) are at \(x=-1\) (local max, value 5) and \(x=3\) (local min, value \(-27\)). Adding \(c\) shifts the graph up by \(c\): we need \(5+c \gt 0\) and \(-27+c \lt 0\), so \(-5 \lt c \lt 27\). The greatest integer is 26. (At \(c=27\), the minimum touches the axis, giving only two distinct solutions.)

### TOP-03 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

How many real solutions does the equation \(2^{x}=x^{2}\) have?

- A) One
- B) Two
- C) Three
- D) Four

**Answer:** C

**Explanation:** Two solutions are easy to spot: \(x=2\) (\(4=4\)) and \(x=4\) (\(16=16\)). The trap is missing the third: for negative \(x\), \(2^x\) is between 0 and 1 while \(x^2\) grows, so the graphs cross once more, near \(x\approx-0.77\). For \(x \gt 4\), \(2^x\) stays above \(x^2\). Total: three.

### TOP-05 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

In the \(xy\)-plane, the graph of \(y=|x-3|\) and the graph of \(y=\frac12x+k\), where \(k\) is a constant, intersect at exactly one point. What is the value of \(k\)?

**Answer:** -3/2

**Explanation:** The V-shaped graph has its vertex at \((3,0)\) and arms with slopes \(\pm1\). The line has slope \(\frac12\), which is less steep than either arm. If the line is above the vertex, it crosses both arms (two points); if it's below, it misses the V entirely. Exactly one intersection happens only when the line passes through the vertex: \(0=\frac12(3)+k\), so \(k=-\frac32=-1.5\).

### TOP-07 · Nonlinear functions · Hard · Desmos · computed

The functions \(f\) and \(g\) are defined by \(f(x)=-0.5x^2+6x-10\) and \(g(x)=2x-4\). What is the maximum value of \(f(x)-g(x)\)?

**Answer:** 2

**Explanation:** \(f(x)-g(x)=-0.5x^2+4x-6\). The vertex is at \(x=-\frac{4}{2(-0.5)}=4\), and the value there is \(-8+16-6=2\).

### TOP-09 · Nonlinear functions · Very hard · Desmos · computed

The function \(f\) is defined by \(f(x)=a(1.5)^{x}+b\), where \(a\) and \(b\) are constants. The graph of \(y=f(x)\) passes through the points \((0,7)\) and \((2,12)\). What is the value of \(f(4)\)?

**Answer:** 93/4

**Explanation:** \(f(0)=a+b=7\) and \(f(2)=2.25a+b=12\). Subtracting gives \(1.25a=5\), so \(a=4\) and \(b=3\). Then \(f(4)=4(1.5)^4+3=4(5.0625)+3=23.25\).

### TOP-10 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

Which of the following equations has exactly two distinct real solutions?

- A) \(x^3-3x+3=0\)
- B) \(x^3-3x+1=0\)
- C) \(x^3-3x+2=0\)
- D) \(x^3-3x+5=0\)

**Answer:** C

**Explanation:** The graph of \(y=x^3-3x\) has a local maximum of 2 (at \(x=-1\)) and a local minimum of \(-2\) (at \(x=1\)). Adding a constant \(d\) shifts it up. With \(d=2\), the local minimum is exactly 0, so the graph touches the axis at \(x=1\) and crosses it once more: \(x^3-3x+2=(x-1)^2(x+2)\), with two distinct solutions. \(d=1\) gives three solutions; \(d=3\) and \(d=5\) give one.

### TOP-14 · Nonlinear functions · Very hard · By hand · computed

The polynomial \(p(x)=x^3+ax^2+bx-6\), where \(a\) and \(b\) are constants, has \(x-3\) and \(x+1\) as factors. What is the value of \(a+b\)?

**Answer:** -7

**Explanation:** \(p(3)=27+9a+3b-6=0\) gives \(3a+b=-7\). \(p(-1)=-1+a-b-6=0\) gives \(a-b=7\). Adding: \(4a=0\), so \(a=0\) and \(b=-7\). So \(a+b=-7\). (Shortcut: for this cubic the product of the roots is 6, so \(3\cdot(-1)\cdot r=6\) gives a third root \(r=-2\) and \(p(x)=(x-3)(x+1)(x+2)\). Then \(p(1)=(-2)(2)(3)=-12\), and also \(p(1)=1+a+b-6\), so \(a+b=-7\).)

### TOP-15 · Nonlinear functions · Hard · Desmos · computed

The function \(f\) is defined by \(f(x)=3x^2-12x+k\), where \(k\) is a constant. The minimum value of \(f(x)\) is 5. What is the value of \(k\)?

- A) \(5\)
- B) \(12\)
- C) \(17\)
- D) \(29\)

**Answer:** C

**Explanation:** The minimum occurs at the vertex, \(x=\frac{12}{6}=2\): \(f(2)=12-24+k=k-12\). Setting \(k-12=5\) gives \(k=17\).

### TOP-16 · Nonlinear equations in one variable and systems of equations in two variables · Very hard · Desmos · computed

In the \(xy\)-plane, the line \(y=c\), where \(c\) is a constant, intersects the parabola \(y=4x^2-20x+23\) at two points that are 3 units apart. What is the value of \(c\)?

**Answer:** 7

**Explanation:** The parabola is symmetric about \(x=\frac{20}{8}=2.5\), so two points 3 units apart are at \(x=2.5\pm1.5\), which is \(x=1\) and \(x=4\). Then \(c=4(1)^2-20(1)+23=7\). Check: \(4(16)-80+23=7\). ✓

### TOP-17 · Nonlinear functions · Hard · Desmos · computed

An investment earns 4.5% interest, compounded annually. What is the least whole number of years after which the value of the investment will be at least double its initial value?

- A) \(14\)
- B) \(15\)
- C) \(16\)
- D) \(22\)

**Answer:** C

**Explanation:** Solve \(1.045^n\ge2\). \(1.045^{15}\approx1.935\), which is not yet double, and \(1.045^{16}\approx2.022\). So 16 years. (22 is the trap from \(100\div4.5\), which ignores compounding.)

### TOP-21 · Nonlinear functions · Hard · By hand · computed

The function \(f\) is defined by \(f(x)=x^2-6x+5\). The function \(g\) is defined by \(g(x)=f(x-k)\), where \(k\) is a constant. The \(x\)-intercepts of the graph of \(y=g(x)\) are at \(x=4\) and \(x=8\). What is the value of \(k\)?

- A) \(-3\)
- B) \(2\)
- C) \(3\)
- D) \(7\)

**Answer:** C

**Explanation:** \(f(x)=(x-1)(x-5)\) has zeros 1 and 5. \(f(x-k)\) shifts the graph \(k\) units to the right, so the zeros become \(1+k\) and \(5+k\). These equal 4 and 8 when \(k=3\). (\(-3\) is the trap from shifting in the wrong direction.)

### FIG-02 · Nonlinear functions · Hard · Desmos · computed

                                x  y  -2  2  4  6  -6  -4  -2  2  4  6  O     (2, −4)    The graph of \(y=f(x)\) is shown, where \(f\) is a quadratic function. Its vertex is \((2,-4)\). Which equation defines \(f\)?

- A) \(f(x)=x(x-4)\)
- B) \(f(x)=(x+2)^2-4\)
- C) \(f(x)=-x(x-4)\)
- D) \(f(x)=(x-2)^2+4\)

**Answer:** A

**Explanation:** The graph crosses the \(x\)-axis at 0 and 4, so \(f(x)=a\,x(x-4)\). At the vertex, \(f(2)=a(2)(-2)=-4a=-4\), so \(a=1\). Vertex form gives the same function: \((x-2)^2-4=x^2-4x\). The traps \((x+2)^2-4\) and \((x-2)^2+4\) flip a sign, and \(-x(x-4)\) has the right zeros but opens downward.

### FIG-03 · Nonlinear functions · Very hard · Desmos · computed

                          x  y  -2  -1  1  2  3  4  8  16  24  O     (0, 3)   (2, 12)    The graph of the exponential function \(f\), where \(f(x)=ab^{x}\) and \(a\) and \(b\) are positive constants, passes through the points \((0,3)\) and \((2,12)\), as shown. What is the value of \(f(3)\)?

**Answer:** 24

**Explanation:** \(f(0)=a=3\). Then \(f(2)=3b^2=12\), so \(b^2=4\) and \(b=2\). So \(f(3)=3(2)^3=24\). (Reading the graph alone at \(x=3\) is hard to do precisely; use the two labeled points.)

## Problem-Solving and Data Analysis

### PSD-01 · Percentages · Medium · By hand · computed

The price of a jacket was increased by 20%. Later, the new price was decreased by 25%. The final price of the jacket was $81. What was the original price?

- A) $76.95
- B) $85.26
- C) $90.00
- D) $97.20

**Answer:** C

**Explanation:** The two changes multiply: \(1.20\times0.75=0.90\). So \(0.9P=81\), and \(P=90\). (Note that it is  not  a 5% decrease: the percents apply to different bases.)

### PSD-02 · Percentages · Hard · By hand · computed

The number \(x\) is 150% of \(y\), and \(y\) is 40% of \(z\). If \(z\neq0\), \(x\) is what percent of \(z\)?

- A) 16%
- B) 60%
- C) 110%
- D) 375%

**Answer:** B

**Explanation:** \(x=1.5y\) and \(y=0.4z\), so \(x=1.5(0.4z)=0.6z\). \(x\) is 60% of \(z\).

### PSD-03 · Percentages · Very hard · By hand · computed

At a high school, 60% of the students are in the band, and the rest are not. Of the students in the band, 25% wear glasses. Of the students not in the band, 40% wear glasses. Of the students who wear glasses, approximately what percent are in the band?

- A) 15%
- B) 31%
- C) 48%
- D) 52%

**Answer:** C

**Explanation:** Imagine 100 students. Band: 60 students, 25% of whom wear glasses: 15. Not band: 40 students, 40% of whom wear glasses: 16. Total wearing glasses: 31. Fraction in band: \(\frac{15}{31}\approx0.484\), or about 48%. (15% and 31% are the traps: they are percents of  all  students.)

### PSD-04 · Ratios, rates, proportional relationships, and units · Medium · By hand · computed

A printer prints 18 pages every 45 seconds. At this rate, how many minutes will it take the printer to print 600 pages?

- A) 10
- B) 25
- C) 40
- D) 1,500

**Answer:** B

**Explanation:** Rate: \(\frac{18}{45}=0.4\) pages per second. Time: \(\frac{600}{0.4}=1500\) seconds, and \(\frac{1500}{60}=25\) minutes.

### PSD-05 · Ratios, rates, proportional relationships, and units · Hard · By hand · computed

A car's fuel tank holds 14 gallons. In the city, the car travels 24 miles per gallon of fuel; on the highway, it travels 32 miles per gallon. Starting with a full tank, a driver travels 180 miles in the city and then continues on the highway. How many miles can the driver travel on the highway before the tank is empty?

- A) \(168\)
- B) \(208\)
- C) \(240\)
- D) \(268\)

**Answer:** B

**Explanation:** City fuel: \(\frac{180}{24}=7.5\) gallons. Remaining fuel: \(14-7.5=6.5\) gallons. Highway distance: \(6.5\times32=208\) miles.

### PSD-06 · Ratios, rates, proportional relationships, and units · Hard · By hand · computed

A metal block is shaped like a cube with an edge length of 4 centimeters. The metal has a density of 7.8 grams per cubic centimeter. What is the least number of these blocks needed to have a total mass of at least 10 kilograms? (1 kilogram = 1,000 grams)

- A) \(19\)
- B) \(20\)
- C) \(21\)
- D) \(22\)

**Answer:** C

**Explanation:** Volume of one block: \(4^3=64\) cm³. Mass: \(64\times7.8=499.2\) g. Number needed: \(\frac{10{,}000}{499.2}\approx20.03\). 20 blocks weigh only 9,984 g, which is not enough, so 21 blocks are needed.

### PSD-07 · One-variable data: distributions and measures of center and spread · Medium · By hand · computed

The mean of a list of 8 numbers is 15. When one number is removed from the list, the mean of the remaining 7 numbers is 13. What number was removed?

- A) \(2\)
- B) \(13\)
- C) \(15\)
- D) \(29\)

**Answer:** D

**Explanation:** Sum of 8 numbers: \(8\times15=120\). Sum of the remaining 7: \(7\times13=91\). The removed number is \(120-91=29\).

### PSD-08 · One-variable data: distributions and measures of center and spread · Very hard · By hand · computed

A data set consists of the 7 values 4, 7, 7, 9, 12, 15, and \(x\). The mean of the data set is equal to the median of the data set. If \(x\) is positive, what is the value of \(x\)?

**Answer:** 9

**Explanation:** The mean is \(\frac{54+x}{7}\). The median is the 4th value in order, which depends on \(x\). If \(x\le7\), the median is 7: \(54+x=49\) gives \(x=-5\), which is not positive. If \(7 \lt x \lt 9\), the median is \(x\): \(54+x=7x\) gives \(x=9\), which is not in that range. If \(x\ge9\), the median is 9: \(54+x=63\) gives \(x=9\). ✓ So \(x=9\).

### PSD-09 · One-variable data: distributions and measures of center and spread · Hard · By hand · computed

A data set has mean \(m\) and standard deviation \(s\), where \(s \gt 0\). A new data set is created by multiplying each value in the original data set by 3 and then adding 5. Which of the following gives the mean and standard deviation of the new data set?

- A) Mean: \(3m+5\); standard deviation: \(3s\)
- B) Mean: \(3m+5\); standard deviation: \(3s+5\)
- C) Mean: \(3m\); standard deviation: \(3s\)
- D) Mean: \(3m+5\); standard deviation: \(9s\)

**Answer:** A

**Explanation:** Every value is transformed the same way, so the mean is transformed the same way: \(3m+5\). Standard deviation measures spread. Adding 5 shifts every value without changing the distances between values, but multiplying by 3 triples every distance. New SD: \(3s\).

### PSD-10 · One-variable data: distributions and measures of center and spread · Very hard · By hand · computed

A list of 11 test scores has a median of 80 and a range of 30. Two new scores, 50 and 105, are added to the list. Which of the following must be true about the new list of 13 scores?

- A) The median is 80.
- B) The range is 55.
- C) The mean is greater than the mean of the original list.
- D) The range is 30.

**Answer:** A

**Explanation:** Since the range is 30 and the median is 80, the smallest original score is between 50 and 80 (the largest is the smallest plus 30, and it must be at least 80). So 50 is at or below every original score, and 105 is above the median. Adding one score at or below the median and one score above it keeps the middle (7th of 13) value at 80. The range depends on the original maximum, which could be anywhere from 80 to 110, so a range of 55 is not guaranteed. A range of 30 is impossible because 105 &minus; 50 &gt; 30. The mean could go up or down, so a greater mean is not guaranteed.

### PSD-11 · Probability and conditional probability · Hard · By hand · computed

A survey asked 200 students at a school whether they prefer online or in-person classes. The results are shown in the table.     Online  In-person  Total    Grade 10  34  56  90    Grade 11  48  62  110    Total  82  118  200   If one of the surveyed students who prefer online classes is selected at random, what is the probability that the student is in grade 11?

- A) \(\dfrac{48}{200}\)
- B) \(\dfrac{48}{110}\)
- C) \(\dfrac{48}{82}\)
- D) \(\dfrac{82}{200}\)

**Answer:** C

**Explanation:** The condition &ldquo;prefers online&rdquo; restricts the group to the Online column: 82 students. Of those, 48 are in grade 11. Probability: \(\frac{48}{82}\). \(\frac{48}{110}\) answers a different question: of the grade 11 students, the fraction who prefer online.

### PSD-12 · Probability and conditional probability · Hard · By hand · computed

A bag contains only red and blue marbles. The ratio of red marbles to blue marbles is 3 to 5. After 6 red marbles are added to the bag, the probability of randomly selecting a red marble is \(\frac12\). How many blue marbles are in the bag?

- A) \(9\)
- B) \(10\)
- C) \(15\)
- D) \(18\)

**Answer:** C

**Explanation:** Let there be \(3k\) red and \(5k\) blue marbles. After adding 6 red, a probability of \(\frac12\) means red equals blue: \(3k+6=5k\), so \(k=3\). Blue marbles: \(5(3)=15\).

### PSD-13 · Inference from sample statistics and margin of error · Medium · By hand · reasoning

A polling company selected 400 registered voters in a city at random and found that 54% of them support a proposed new park. The margin of error for this estimate is 3 percentage points at a 95% confidence level. Which of the following is the most appropriate conclusion?

- A) It is plausible that between 51% and 57% of all registered voters in the city support the new park.
- B) Exactly 54% of all registered voters in the city support the new park.
- C) Between 51% and 57% of the 400 sampled voters support the new park.
- D) The survey proves that a majority of all residents of the city support the new park.

**Answer:** A

**Explanation:** A margin of error describes uncertainty about the  population  value: \(54\%\pm3\%\) gives a plausible range of 51% to 57% for all registered voters. &ldquo;Exactly 54%&rdquo; ignores the uncertainty. The statement about the 400 sampled voters is wrong because the sample percentage is exactly 54%. The &ldquo;proves&rdquo; statement overstates the result (&ldquo;proves&rdquo;) and switches the population from registered voters to all residents.

### PSD-14 · Inference from sample statistics and margin of error · Hard · By hand · reasoning

A researcher wanted to estimate the average number of hours of sleep per night of high school students in a state. The researcher surveyed 250 randomly selected students from the members of one high school's varsity sports teams. The mean was 7.1 hours. Which of the following is the most appropriate conclusion?

- A) The mean sleep of all high school students in the state is about 7.1 hours.
- B) The mean sleep of all high school students in the state is less than 7.1 hours.
- C) The results can't be generalized to all high school students in the state, because the sample was not selected at random from that population.
- D) The sample size of 250 is too small to draw any conclusion about any group.

**Answer:** C

**Explanation:** A sample supports conclusions only about the population it was randomly selected from: here, varsity athletes at one school. That group is not representative of all high school students in the state. 250 is a reasonable sample size for the population that was actually sampled, so the claim that the sample is too small is wrong.

### PSD-15 · Evaluating statistical claims: observational studies and experiments · Hard · By hand · reasoning

A researcher recruited 300 adult volunteers. Half of them were randomly assigned to take a new vitamin supplement daily, and the other half were assigned to take a placebo. After 6 months, the group that took the supplement had significantly fewer colds. Which of the following conclusions is most appropriate?

- A) The supplement causes fewer colds for all adults.
- B) The supplement is likely to cause fewer colds for adults similar to the volunteers in the study.
- C) There is a relationship between the supplement and fewer colds, but no conclusion about cause can be made.
- D) No conclusion can be made because the participants were volunteers.

**Answer:** B

**Explanation:** Random  assignment  to treatments allows a cause-and-effect conclusion. But the participants were volunteers, not a random sample of all adults, so the conclusion should be limited to people similar to the volunteers. &ldquo;All adults&rdquo; over-generalizes; &ldquo;no conclusion about cause&rdquo; ignores the random assignment; and &ldquo;no conclusion can be made&rdquo; is too strict.

### PSD-16 · Two-variable data: models and scatterplots · Medium · By hand · computed

A scatterplot shows the relationship between two variables, \(x\) and \(y\). The line of best fit for the data is \(y=2.4x+15\). One of the data points is \((10,42)\). By how much does the actual \(y\)-value of this data point exceed the \(y\)-value predicted by the line of best fit?

- A) \(-3\)
- B) \(3\)
- C) \(39\)
- D) \(42\)

**Answer:** B

**Explanation:** Predicted value: \(2.4(10)+15=39\). The actual value 42 exceeds it by \(42-39=3\).

### PSD-17 · One-variable data: distributions and measures of center and spread · Medium · By hand · computed

Data set A contains 20 numbers with a mean of 42. Data set B contains 30 numbers with a mean of 52. What is the mean of the 50 numbers in the two data sets combined?

- A) \(46\)
- B) \(47\)
- C) \(48\)
- D) \(50\)

**Answer:** C

**Explanation:** Total: \(20(42)+30(52)=840+1560=2400\). Mean: \(\frac{2400}{50}=48\). (It is not 47, the average of the two means, because B has more values.)

### PSD-18 · Percentages · Hard · By hand · computed

Store A sells a lamp at a 30% discount from its original price of $92. Store B sells the same lamp at a price that is 15% greater than the wholesale cost. If the two stores sell the lamp for the same price, what is the wholesale cost of the lamp?

- A) $54.74
- B) $56.00
- C) $64.40
- D) $74.06

**Answer:** B

**Explanation:** Store A's price: \(0.70\times92=64.40\). Store B: \(1.15w=64.40\), so \(w=56\).

### PSD-19 · Percentages · Very hard · Desmos · computed

A stock's price decreased by \(p\%\) during one month and then increased by \(p\%\) during the next month, where \(p \gt 0\). The overall effect was a 4% decrease from the original price. What is the value of \(p\)?

**Answer:** 20

**Explanation:** \(\left(1-\frac p{100}\right)\left(1+\frac p{100}\right)=0.96\). The left side is \(1-\left(\frac p{100}\right)^2\), so \(\left(\frac p{100}\right)^2=0.04\), \(\frac p{100}=0.2\), and \(p=20\).

### PSD-20 · Ratios, rates, proportional relationships, and units · Hard · By hand · computed

Pipe A alone can fill a tank in 6 hours, and pipe B alone can fill the tank in 4 hours. A drain alone can empty the full tank in 8 hours. If the tank starts empty and both pipes and the drain are all open, how many hours will it take to fill the tank?

**Answer:** 24/7

**Explanation:** Combined rate: \(\frac16+\frac14-\frac18=\frac{4+6-3}{24}=\frac{7}{24}\) tank per hour. Time: \(\frac{24}{7}\approx3.43\) hours. Acceptable entries include 24/7, 3.428, and 3.429.

### PSD-21 · Ratios, rates, proportional relationships, and units · Hard · By hand · computed

Fertilizer is applied to a field at a rate of 2.5 kilograms per 100 square meters. The field is a rectangle that is 0.3 kilometer long and 120 meters wide. How many kilograms of fertilizer are needed for the whole field? (1 kilometer = 1,000 meters)

- A) 90
- B) 360
- C) 900
- D) 9,000

**Answer:** C

**Explanation:** Length: 0.3 km = 300 m. Area: \(300\times120=36{,}000\) m². Number of 100-m² units: 360. Fertilizer: \(360\times2.5=900\) kg.

### PSD-22 · Percentages · Hard · By hand · computed

A company had 1,250 employees in 2019 and 1,450 employees in 2021. If the number of employees increases by the same percent from 2021 to 2023 as it did from 2019 to 2021, how many employees will the company have in 2023?

- A) 1,650
- B) 1,682
- C) 1,700
- D) 1,740

**Answer:** B

**Explanation:** Percent increase from 2019 to 2021: \(\frac{1450-1250}{1250}=0.16\), or 16%. In 2023: \(1450\times1.16=1682\).

### PSD-23 · Two-variable data: models and scatterplots · Hard · Desmos · computed

The table shows five data points.   \(x\)  1  2  3  4  5    \(y\)  3.1  5.0  6.8  9.1  10.9   Which of the following equations best represents the linear model that fits the data?

- A) \(y=1.97x+1.07\)
- B) \(y=1.07x+1.97\)
- C) \(y=2.5x-0.5\)
- D) \(y=-1.97x+12.89\)

**Answer:** A

**Explanation:** The \(y\)-values increase by about 2 each time \(x\) increases by 1, so the slope is about 2. This rules out the equations with slope 1.07 and slope \(-1.97\). At \(x=3\), the model should give about the middle value: \(1.97(3)+1.07=6.98\), which is close to 6.8. The equation \(y=2.5x-0.5\) gives 7.0 at \(x=3\) but 12 at \(x=5\), far from 10.9. The least-squares line is \(y=1.97x+1.07\).

### PSD-24 · One-variable data: distributions and measures of center and spread · Very hard · By hand · computed

The frequency table summarizes a data set of 20 values.   Value  1  2  3  4  5    Frequency  3  5  4  6  2   Which of the following is true about the mean and the median of the data set?

- A) The mean is less than the median.
- B) The mean is equal to the median.
- C) The mean is greater than the median.
- D) There is not enough information to compare them.

**Answer:** A

**Explanation:** Mean: \(\frac{1(3)+2(5)+3(4)+4(6)+5(2)}{20}=\frac{59}{20}=2.95\). Median: the average of the 10th and 11th values. The cumulative counts are 3, 8, 12, &hellip;, so the 9th through 12th values are all 3, and the median is 3. Since \(2.95 \lt 3\), the mean is less than the median.

### PSD-25 · Inference from sample statistics and margin of error · Medium · By hand · computed

A town has 18,000 households. In a random sample of 250 of these households, 35 had solar panels. Based on the sample, which of the following is the best estimate of the number of households in the town that have solar panels?

- A) 2,520
- B) 3,500
- C) 4,500
- D) 6,300

**Answer:** A

**Explanation:** Sample proportion: \(\frac{35}{250}=0.14\). Estimate: \(0.14\times18{,}000=2{,}520\).

### PSD-26 · One-variable data: distributions and measures of center and spread · Medium · By hand · computed

Data set X consists of the values 10, 12, 14, 16, and 18. Data set Y consists of the values 6, 12, 14, 16, and 22. Which of the following is true?

- A) The data sets have different means, and the standard deviation of X is greater.
- B) The data sets have the same mean, and the standard deviation of X is greater.
- C) The data sets have the same mean, and the standard deviation of Y is greater.
- D) The data sets have the same mean and the same standard deviation.

**Answer:** C

**Explanation:** Both sums are 70, so both means are 14. The two sets differ only in their end values: Y's extreme values (6 and 22) are farther from 14 than X's (10 and 18), so Y is more spread out and has the greater standard deviation.

### PSD-27 · Percentages · Very hard · By hand · computed

In 2020, 30% of a company's employees worked remotely. In 2022, the number of employees was 25% greater than in 2020, and the number of employees who worked remotely was 60% greater than in 2020. What percent of the company's employees worked remotely in 2022?

- A) 36%
- B) 38.4%
- C) 48%
- D) 54%

**Answer:** B

**Explanation:** Imagine 100 employees in 2020, 30 of them remote. In 2022: \(125\) employees and \(30\times1.6=48\) remote. Percent: \(\frac{48}{125}=0.384=38.4\%\). 48% is the trap: 48 is the number of remote workers, but there are 125 employees, not 100.

### PSD-28 · Two-variable data: models and scatterplots · Medium · Desmos · computed

A line of best fit for a scatterplot passes through the points \((2,14)\) and \((10,46)\). Based on the line of best fit, what is the predicted value of \(y\) when \(x=7\)?

**Answer:** 34

**Explanation:** Slope: \(\frac{46-14}{10-2}=4\). Line: \(y=14+4(x-2)=4x+6\). At \(x=7\): \(y=34\).

### PSD-29 · Two-variable data: models and scatterplots · Very hard · Desmos · computed

An exponential model of the form \(y=ab^{x}\), where \(a\) and \(b\) are positive constants, is fit to a scatterplot. The model predicts \(y=1{,}200\) when \(x=0\) and \(y=867\) when \(x=2\). Which of the following is closest to the value of \(y\) that the model predicts when \(x=4\)?

- A) \(534\)
- B) \(600\)
- C) \(626\)
- D) \(650\)

**Answer:** C

**Explanation:** \(a=1200\). Then \(b^2=\frac{867}{1200}=0.7225\), so \(b=0.85\). At \(x=4\): \(y=1200(b^2)^2=1200(0.7225)^2\approx626.4\). 534 is the trap from treating the model as linear (subtracting 333 twice).

### PSD-30 · Probability and conditional probability · Hard · By hand · computed

A club has 120 members: 45 juniors and 75 seniors. Of the juniors, 18 play a musical instrument; of the seniors, 42 play a musical instrument. If a member who does  not  play a musical instrument is selected at random, what is the probability that the member is a junior?

**Answer:** 9/20

**Explanation:** Members who don't play: juniors \(45-18=27\), seniors \(75-42=33\), total 60. Probability of a junior: \(\frac{27}{60}=\frac{9}{20}=0.45\). (\(\frac{27}{120}\) and \(\frac{27}{45}\) are the traps; the condition limits the group to the 60 non-players.)

### PSD-31 · Probability and conditional probability · Very hard · By hand · computed

An integer from 1 to 60, inclusive, is selected at random. What is the probability that the integer is a multiple of 4 or a multiple of 6 (or both)?

**Answer:** 1/3

**Explanation:** Multiples of 4: 15. Multiples of 6: 10. Multiples of both, which are the multiples of 12: 5, and these were counted twice. Total: \(15+10-5=20\). Probability: \(\frac{20}{60}=\frac13\). Acceptable entries include 1/3, .3333, and 0.333.

### PSD-32 · Evaluating statistical claims: observational studies and experiments · Hard · By hand · reasoning

Researchers surveyed 1,000 randomly selected adults in a country. Adults who reported walking at least 30 minutes per day had lower average blood pressure than adults who did not. Which of the following is the most appropriate conclusion?

- A) Walking at least 30 minutes per day causes lower blood pressure for adults in the country.
- B) There is an association between daily walking and lower blood pressure for adults in the country, but a cause-and-effect conclusion can't be made.
- C) There is an association between daily walking and lower blood pressure for all adults in the world.
- D) No conclusion about adults in the country can be made, because the adults were not assigned to walk.

**Answer:** B

**Explanation:** The adults were randomly  selected , so the results generalize to adults in that country. But they were not randomly  assigned  to walk; this is an observational study. So it shows an association, not cause and effect. (Other differences, such as diet or age, could explain the pattern.) The claim about all adults in the world over-generalizes, and an association can still be concluded without assignment.

### PSD-33 · Evaluating statistical claims: observational studies and experiments · Hard · By hand · reasoning

A principal wants to know whether a new online study tool improves test scores for the students at her school. Which of the following study designs would best allow her to conclude that using the tool  causes  higher scores for students at the school?

- A) Let students choose whether to use the tool, then compare the scores of users and nonusers.
- B) Select a random sample of students at the school, randomly assign half of them to use the tool and half not to, and compare the scores of the two groups.
- C) Have every student in one class use the tool, and compare that class's scores with another class's scores.
- D) Ask students who already use the tool whether they think it improved their scores.

**Answer:** B

**Explanation:** A cause-and-effect conclusion requires random  assignment  to the treatment, and generalizing to the school requires a random  sample  from the school. Letting students choose introduces self-selection: motivated students may both use the tool and score higher. Comparing two existing classes confounds the tool with the teacher and class. Self-reports measure opinions, not scores.

### TOP-06 · One-variable data: distributions and measures of center and spread · Hard · Desmos · computed

A data set consists of the values 12, 15, 15, 18, 21, 24, 26, 29, 33, and 37. The value 37 is replaced with 47. Which of the following statements about the new data set, compared with the original, are true? I. The mean increases by 1. II. The median does not change. III. The standard deviation increases. 

- A) I and II only
- B) I and III only
- C) II and III only
- D) I, II, and III

**Answer:** D

**Explanation:** I: the sum increases by 10 across 10 values, so the mean increases by \(\frac{10}{10}=1\). ✓ II: the median is the average of the 5th and 6th values (21 and 24), and neither changes. ✓ III: the largest value moves farther from the mean, so the spread increases. ✓

### TOP-12 · Two-variable data: models and scatterplots · Hard · Desmos · computed

The table shows five data points that lie exactly on the graph of a quadratic function.   \(x\)  0  1  2  3  4    \(y\)  3  2  3  6  11   What is the value of \(y\) when \(x=7\)?

**Answer:** 38

**Explanation:** The \(y\)-values change by \(-1,1,3,5\); the second differences are constant at 2, so \(a=\frac22=1\). With \(c=3\) (the value at \(x=0\)) and \(1+b+3=2\), \(b=-2\). So \(y=x^2-2x+3\), and at \(x=7\): \(49-14+3=38\).

### TOP-20 · One-variable data: distributions and measures of center and spread · Very hard · By hand · computed

A list of 5 positive integers has a mean of 12 and a median of 13. The list has a unique mode of 15. What is the greatest possible value of the smallest integer in the list?

**Answer:** 8

**Explanation:** The sum is \(5\times12=60\). In order, the list is \(a\le b\le13\le d\le e\). A unique mode of 15 needs at least two 15s, and both must be above the median, so \(d=e=15\). Then \(a+b=60-13-30=17\). For 15 to be the  unique  mode, \(a\neq b\) and \(b\neq13\). Making \(a\) as large as possible with \(a \lt b\): \(a=8\), \(b=9\).

### TOP-23 · One-variable data: distributions and measures of center and spread · Hard · Desmos · computed

Each of the following data sets has a mean of 6. Which data set has the greatest standard deviation?

- A) 2, 4, 6, 8, 10
- B) 1, 5, 6, 7, 11
- C) 4, 5, 6, 7, 8
- D) 1, 1, 6, 11, 11

**Answer:** D

**Explanation:** Standard deviation measures typical distance from the mean. In 1, 1, 6, 11, 11, four of the five values are 5 away from the mean, more than in any other set. (1, 5, 6, 7, 11 has the same range, but most of its values are clustered near 6.)

### FIG-05 · One-variable data: distributions and measures of center and spread · Hard · By hand · computed

     2   3    4      5       6     7    8   9   10   11   12    13   The dot plot shows the 12 values in a data set. If the value 12 is removed from the data set, which of the following is true about the mean and median of the remaining 11 values compared with those of the original 12 values?

- A) The mean decreases, and the median stays the same.
- B) The mean decreases, and the median decreases.
- C) The mean stays the same, and the median stays the same.
- D) The mean stays the same, and the median decreases.

**Answer:** A

**Explanation:** Mean: the original sum is 66, so the mean is \(\frac{66}{12}=5.5\); without 12 it is \(\frac{54}{11}\approx4.9\), a decrease. Median: the original median is the average of the 6th and 7th values (both 5), so it's 5. The new median is the 6th of 11 values, which is also 5. An extreme value pulls the mean but barely affects the median.

### FIG-06 · One-variable data: distributions and measures of center and spread · Hard · By hand · computed

    0   2   4   6   8   10   12       0  10  20  30  40    Frequency  50   The histogram summarizes the distribution of 30 values in a data set. Each bar includes its left endpoint but not its right endpoint (for example, the first bar represents values from 0 up to but not including 10). Which of the following could be the median of the data set?

- A) \(12\)
- B) \(18\)
- C) \(24\)
- D) \(35\)

**Answer:** C

**Explanation:** With 30 values, the median is the average of the 15th and 16th values. Counting from the left: 3 values below 10, then 8 more (11 total) below 20, then 10 more (21 total) below 30. So the 15th and 16th values are both between 20 and 30, and the median must be in that interval. Only 24 is.

### FIG-07 · Two-variable data: models and scatterplots · Medium · By hand · computed

                                        x  y  2  4  6  8  10  12  14  16  2  4  6  8  10  12  O                The scatterplot shows the relationship between two variables, \(x\) and \(y\), along with a line of best fit that passes through \((0,2)\) and \((10,7)\). Based on the line of best fit, what is the predicted value of \(y\) when \(x=14\)?

**Answer:** 9

**Explanation:** The slope of the line is \(\frac{7-2}{10-0}=0.5\), so the line is \(y=0.5x+2\). At \(x=14\): \(y=0.5(14)+2=9\).

### FIG-08 · Two-variable data: models and scatterplots · Hard · By hand · computed

                                 x  y  2  4  6  8  10  12  2  4  6  8  O                The scatterplot shows 10 data points and a line of best fit, \(y=0.5x+2\). For how many of the data points is the actual \(y\)-value greater than the \(y\)-value predicted by the line of best fit?

**Answer:** 5

**Explanation:** Points above the line have actual values greater than predicted. The points at \(x=1,3,5,7,9\) lie above the line (for example, at \(x=3\) the actual value is 3.9 and the predicted value is 3.5). The points at \(x=2,4,6,8,10\) lie below it. That makes 5.

### FIG-09 · Percentages · Hard · By hand · computed

    0   10   20   30   40   50   60   70      Q1  Q2  Q3  Q4    Sales (thousands of $)   The bar graph shows a company's sales, in thousands of dollars, for each quarter of a year. By what percent did sales increase from the first quarter (Q1) to the third quarter (Q3)?

**Answer:** 125/2

**Explanation:** From the graph, Q1 sales were 40 and Q3 sales were 65 (thousand dollars). Percent increase: \(\frac{65-40}{40}\times100=62.5\). Enter 62.5 (no percent sign).

### FIG-12 · Ratios, rates, proportional relationships, and units · Very hard · By hand · computed

A car accelerates at a constant rate of 3.2 meters per second squared. What is this rate in kilometers per minute squared? (1 kilometer = 1,000 meters)

**Answer:** 11.52

**Explanation:** Convert meters to kilometers (divide by 1,000) and seconds squared to minutes squared. Since 1 minute = 60 seconds, 1 minute squared = \(60^2=3{,}600\) seconds squared, so multiply by 3,600: \(3.2\times\frac{3600}{1000}=11.52\) kilometers per minute squared. The trap is multiplying by 60 instead of \(60^2\), which gives 0.192.

## Geometry and Trigonometry

### GEO-01 · Circles · Hard · By hand · computed

\[x^2+10x+y^2-6y=k\]In the \(xy\)-plane, the graph of the given equation is a circle with a diameter of 14. What is the value of \(k\)?

**Answer:** 15

**Explanation:** Complete the square: \((x+5)^2-25+(y-3)^2-9=k\), so \((x+5)^2+(y-3)^2=k+34\). The radius is 7, so \(k+34=49\) and \(k=15\).

### GEO-02 · Circles · Very hard · By hand · computed

\[2x^2+2y^2+12x-20y=-34\]In the \(xy\)-plane, the graph of the given equation is a circle. What is the radius of the circle?

- A) \(\sqrt{17}\)
- B) \(17\)
- C) \(\sqrt{34}\)
- D) \(2\sqrt{17}\)

**Answer:** A

**Explanation:** First divide every term by 2: \(x^2+y^2+6x-10y=-17\). Complete the square: \((x+3)^2+(y-5)^2=-17+9+25=17\). So \(r^2=17\) and \(r=\sqrt{17}\). (Forgetting to divide by 2 first is the most common mistake.)

### GEO-03 · Circles · Hard · By hand · computed

In a circle with center \(O\), central angle \(AOB\) has a measure of \(\frac{2\pi}{5}\) radians. The length of arc \(AB\) (the arc intercepted by the angle) is \(6\pi\). What is the circumference of the circle?

- A) \(12\pi\)
- B) \(15\pi\)
- C) \(30\pi\)
- D) \(60\pi\)

**Answer:** C

**Explanation:** Arc length \(=r\theta\): \(r\cdot\frac{2\pi}{5}=6\pi\), so \(r=15\). Circumference \(=2\pi r=30\pi\). (Or: \(\frac{2\pi}{5}\) is \(\frac15\) of a full turn, so the circumference is \(5\times6\pi=30\pi\).)

### GEO-04 · Circles · Hard · By hand · computed

Points \(A\) and \(B\) lie on a circle with center \(O\) and radius 10. The length of chord \(AB\) is 12. What is the distance from \(O\) to chord \(AB\)?

- A) \(4\)
- B) \(6\)
- C) \(8\)
- D) \(2\sqrt{34}\)

**Answer:** C

**Explanation:** The perpendicular from the center to a chord bisects the chord, forming a right triangle with hypotenuse 10 (a radius) and leg 6 (half of the chord). The distance is \(\sqrt{100-36}=8\).

### GEO-05 · Circles · Very hard · Desmos · computed

In the \(xy\)-plane, the point \((5,3)\) lies on the circle \((x-2)^2+(y+1)^2=25\). What is the slope of the line tangent to the circle at \((5,3)\)?

**Answer:** -3/4

**Explanation:** The center is \((2,-1)\). The radius to \((5,3)\) has slope \(\frac{3-(-1)}{5-2}=\frac43\). A tangent line is perpendicular to the radius at the point of tangency, so its slope is \(-\frac34\).

### GEO-06 · Right triangles and trigonometry · Hard · By hand · computed

In right triangle \(ABC\), angle \(C\) is a right angle and \(\sin A=\frac{12}{13}\). What is the value of \(\tan B\)?

**Answer:** 5/12

**Explanation:** \(\sin A=\frac{BC}{AB}=\frac{12}{13}\), so take \(BC=12\) and \(AB=13\). Then \(AC=\sqrt{169-144}=5\). For angle \(B\), the opposite side is \(AC\) and the adjacent side is \(BC\): \(\tan B=\frac{5}{12}\). Acceptable entries include 5/12, .4166, and .4167.

### GEO-07 · Right triangles and trigonometry · Hard · By hand · computed

\[\sin(x^\circ)=\cos\big((3x-10)^\circ\big)\]In the given equation, the angles that measure \(x^\circ\) and \((3x-10)^\circ\) are both acute. What is the value of \(x\)?

**Answer:** 25

**Explanation:** For acute angles, \(\sin a^\circ=\cos b^\circ\) exactly when the angles are complementary: \(a+b=90\). So \(x+(3x-10)=90\). So \(4x=100\) and \(x=25\).

### GEO-08 · Area and volume · Hard · By hand · computed

An equilateral triangle has an area of \(36\sqrt3\) square units. What is the perimeter, in units, of the triangle?

- A) \(12\)
- B) \(18\)
- C) \(36\)
- D) \(36\sqrt3\)

**Answer:** C

**Explanation:** Area of an equilateral triangle: \(\frac{\sqrt3}{4}s^2=36\sqrt3\), so \(s^2=144\) and \(s=12\). Perimeter: \(3(12)=36\).

### GEO-09 · Lines, angles, and triangles · Very hard · By hand · computed

In triangle \(ABC\), point \(D\) lies on \(\overline{AB}\) and point \(E\) lies on \(\overline{AC}\) such that \(\overline{DE}\) is parallel to \(\overline{BC}\). The length of \(AD\) is 6, the length of \(DB\) is 4, and the area of triangle \(ADE\) is 54. What is the area of quadrilateral \(DBCE\)?

**Answer:** 96

**Explanation:** Triangles \(ADE\) and \(ABC\) are similar (parallel lines give equal corresponding angles), with scale factor \(\frac{AB}{AD}=\frac{10}{6}=\frac53\). Areas scale by the square: \(\left(\frac53\right)^2=\frac{25}{9}\). Area of \(ABC=54\cdot\frac{25}{9}=150\). Area of \(DBCE=150-54=96\).

### GEO-10 · Area and volume · Hard · By hand · computed

A right circular cylinder has a volume of \(72\pi\) cubic inches. A right circular cone has the same radius as the cylinder and twice the height of the cylinder. What is the volume, in cubic inches, of the cone?

- A) \(24\pi\)
- B) \(36\pi\)
- C) \(48\pi\)
- D) \(144\pi\)

**Answer:** C

**Explanation:** Cylinder: \(\pi r^2h=72\pi\). Cone: \(\frac13\pi r^2(2h)=\frac23(\pi r^2h)=\frac23(72\pi)=48\pi\).

### GEO-11 · Area and volume · Hard · By hand · computed

The length of a rectangular prism is increased by 20%, its width is decreased by 20%, and its height is increased by 50%. By what percent does the volume of the prism increase?

**Answer:** 44

**Explanation:** Volume scales by \(1.2\times0.8\times1.5=1.44\), a 44% increase.

### GEO-12 · Area and volume · Hard · By hand · computed

A sphere has a surface area of \(144\pi\) square centimeters. The volume of the sphere is \(k\pi\) cubic centimeters. What is the value of \(k\)?

**Answer:** 288

**Explanation:** \(4\pi r^2=144\pi\), so \(r=6\). Volume: \(\frac43\pi(6)^3=\frac43(216)\pi=288\pi\). So \(k=288\).

### GEO-13 · Lines, angles, and triangles · Medium · By hand · computed

In triangle \(PQR\), the measure of angle \(P\) is \(40^\circ\) greater than the measure of angle \(Q\), and the measure of angle \(R\) is twice the measure of angle \(Q\). What is the measure, in degrees, of angle \(P\)?

- A) \(35\)
- B) \(70\)
- C) \(75\)
- D) \(85\)

**Answer:** C

**Explanation:** Let angle \(Q=x\). Then \(x+(x+40)+2x=180\), so \(4x=140\) and \(x=35\). Angle \(P=35+40=75^\circ\).

### GEO-14 · Area and volume · Very hard · By hand · computed

A rectangular box has a square base and a height of 9 inches. The length of a diagonal of the box that runs from one corner through the interior to the opposite corner is 17 inches. What is the area, in square inches, of the base of the box?

**Answer:** 104

**Explanation:** For a box with dimensions \(a,b,c\), the space diagonal is \(\sqrt{a^2+b^2+c^2}\). With base side \(s\): \(s^2+s^2+9^2=17^2\), so \(2s^2=208\) and \(s^2=104\). The base area is \(s^2=104\). (No need to find \(s\) itself.)

### GEO-15 · Right triangles and trigonometry · Very hard · By hand · computed

In triangle \(ABC\), \(AB=AC=10\) and \(BC=12\). What is the value of \(\sin A\)?

**Answer:** 24/25

**Explanation:** Draw the altitude from \(A\) to \(\overline{BC}\). It bisects \(BC\), so it splits the triangle into two right triangles with legs 6 and \(\sqrt{100-36}=8\). The area of \(ABC\) is \(\frac12(12)(8)=48\). The area also equals \(\frac12(AB)(AC)\sin A=50\sin A\). So \(\sin A=\frac{48}{50}=\frac{24}{25}=0.96\).

### GEO-16 · Circles · Medium · By hand · computed

A sector of a circle with radius 8 has a central angle of \(135^\circ\). The area of the sector is \(k\pi\). What is the value of \(k\)?

- A) \(6\)
- B) \(12\)
- C) \(24\)
- D) \(48\)

**Answer:** C

**Explanation:** The sector is \(\frac{135}{360}=\frac38\) of the circle. Area: \(\frac38\cdot64\pi=24\pi\). So \(k=24\).

### GEO-17 · Circles · Hard · By hand · computed

Points \(A\), \(B\), and \(C\) lie on a circle with center \(O\) and radius 18. Inscribed angle \(ABC\) intercepts minor arc \(AC\) and has a measure of \(35^\circ\). What is the length of minor arc \(AC\)?

- A) \(\dfrac{7\pi}{2}\)
- B) \(7\pi\)
- C) \(14\pi\)
- D) \(35\pi\)

**Answer:** B

**Explanation:** An inscribed angle is half its intercepted arc, so arc \(AC\) measures \(70^\circ\). Arc length: \(\frac{70}{360}\cdot2\pi(18)=\frac{7}{36}\cdot36\pi=7\pi\). \(\frac{7\pi}{2}\) is the trap from using \(35^\circ\) as the arc measure.

### GEO-18 · Lines, angles, and triangles · Hard · Desmos · computed

In the \(xy\)-plane, the graphs of \(y=2x\), \(y=-x+9\), and the \(x\)-axis form a triangle. What is the area of the triangle?

**Answer:** 27

**Explanation:** The lines meet where \(2x=-x+9\): \(x=3\), \(y=6\). \(y=2x\) meets the \(x\)-axis at \((0,0)\), and \(y=-x+9\) meets it at \((9,0)\). Base 9, height 6: area \(=\frac12(9)(6)=27\).

### GEO-19 · Right triangles and trigonometry · Medium · By hand · computed

The lengths of the legs of a right triangle are in the ratio 5 to 12. The length of the hypotenuse is 39. What is the perimeter of the triangle?

- A) \(60\)
- B) \(78\)
- C) \(90\)
- D) \(117\)

**Answer:** C

**Explanation:** Sides are \(5k\), \(12k\), \(13k\) (a 5-12-13 triangle). \(13k=39\), so \(k=3\): sides 15, 36, 39. Perimeter \(=90\).

### GEO-20 · Area and volume · Hard · By hand · computed

What is the area of a regular hexagon with a side length of 6?

- A) \(27\sqrt3\)
- B) \(36\sqrt3\)
- C) \(54\sqrt3\)
- D) \(108\sqrt3\)

**Answer:** C

**Explanation:** A regular hexagon splits into 6 equilateral triangles with side 6. Each has area \(\frac{\sqrt3}{4}(36)=9\sqrt3\). Total: \(54\sqrt3\).

### GEO-21 · Area and volume · Medium · By hand · computed

A circle is inscribed in a square, so the circle touches all four sides of the square. The area of the square is 196 square units. What is the area, in square units, of the region inside the square but outside the circle?

- A) \(196-196\pi\)
- B) \(196-49\pi\)
- C) \(196-14\pi\)
- D) \(196-7\pi\)

**Answer:** B

**Explanation:** Side of the square: \(\sqrt{196}=14\), which is the circle's diameter, so \(r=7\). Circle area: \(49\pi\). Region: \(196-49\pi\).

### GEO-22 · Right triangles and trigonometry · Very hard · By hand · computed

In right triangle \(ABC\), the right angle is at \(C\). The altitude from \(C\) meets hypotenuse \(\overline{AB}\) at point \(D\). If \(AD=4\) and \(DB=9\), what is the length of \(\overline{CD}\)?

**Answer:** 6

**Explanation:** The altitude to the hypotenuse creates two triangles similar to each other: \(\triangle ACD\sim\triangle CBD\). So \(\frac{AD}{CD}=\frac{CD}{DB}\), which gives \(CD^2=AD\cdot DB=36\) and \(CD=6\).

### GEO-23 · Circles · Very hard · Desmos · computed

In the \(xy\)-plane, the line \(y=x+1\) intersects the circle \(x^2+y^2=25\) at two points. What is the distance between these two points?

- A) \(7\)
- B) \(5\sqrt2\)
- C) \(7\sqrt2\)
- D) \(14\)

**Answer:** C

**Explanation:** Substitute: \(x^2+(x+1)^2=25\), so \(2x^2+2x-24=0\), or \(x^2+x-12=0\). Then \(x=3\) or \(x=-4\), giving points \((3,4)\) and \((-4,-3)\). Distance: \(\sqrt{7^2+7^2}=7\sqrt2\).

### GEO-24 · Circles · Very hard · Desmos · computed

In the \(xy\)-plane, the line \(y=2x-3\) intersects the circle \((x-3)^2+(y+2)^2=20\) at two points. What is the product of the \(x\)-coordinates of the two points?

- A) \(-2\)
- B) \(-1\)
- C) \(2\)
- D) \(4\)

**Answer:** A

**Explanation:** Substitute \(y=2x-3\): \((x-3)^2+(2x-1)^2=20\). Expand: \(x^2-6x+9+4x^2-4x+1=20\), so \(5x^2-10x-10=0\), or \(x^2-2x-2=0\). The product of the roots of \(x^2+bx+c\) is \(c\), so the product is \(-2\). (The roots are \(1\pm\sqrt3\), and \((1+\sqrt3)(1-\sqrt3)=1-3=-2\).)

### GEO-25 · Right triangles and trigonometry · Very hard · By hand · computed

Angle \(\theta\) is measured in radians, with \(\pi \lt \theta \lt \frac{3\pi}{2}\), and \(\tan\theta=\frac34\). What is the value of \(\sin\theta\)?

- A) \(-\dfrac45\)
- B) \(-\dfrac35\)
- C) \(\dfrac35\)
- D) \(\dfrac45\)

**Answer:** B

**Explanation:** An angle between \(\pi\) and \(\frac{3\pi}{2}\) is in Quadrant III, where sine and cosine are both negative (and tangent is positive). \(\tan\theta=\frac34\) means a 3-4-5 reference triangle with opposite 3 and adjacent 4, so \(|\sin\theta|=\frac35\). In Quadrant III, \(\sin\theta=-\frac35\).

### GEO-26 · Lines, angles, and triangles · Hard · Desmos · computed

In the \(xy\)-plane, a triangle has vertices at \((-2,1)\), \((4,1)\), and \((1,7)\). What is the perimeter of the triangle?

- A) \(6+6\sqrt5\)
- B) \(12+3\sqrt5\)
- C) \(18\)
- D) \(6+3\sqrt5\)

**Answer:** A

**Explanation:** The base from \((-2,1)\) to \((4,1)\) has length 6. Each slanted side runs 3 horizontally and 6 vertically: \(\sqrt{3^2+6^2}=\sqrt{45}=3\sqrt5\). Perimeter: \(6+2(3\sqrt5)=6+6\sqrt5\).

### GEO-27 · Circles · Hard · By hand · computed

In the \(xy\)-plane, a circle passes through the points \((0,0)\), \((8,0)\), and \((0,6)\). What is the radius of the circle?

**Answer:** 5

**Explanation:** The points \((8,0)\), \((0,0)\), and \((0,6)\) form a right angle at the origin. An inscribed right angle intercepts a semicircle, so the segment from \((8,0)\) to \((0,6)\) is a diameter. Its length is \(\sqrt{64+36}=10\), so the radius is 5.

### GEO-28 · Lines, angles, and triangles · Hard · By hand · computed

Two parallel lines are intersected by a transversal. Two same-side interior angles formed by the transversal have measures \((5x+10)^\circ\) and \((3x+30)^\circ\). What is the value of \(x\)?

**Answer:** 35/2

**Explanation:** Same-side interior angles between parallel lines are supplementary: \((5x+10)+(3x+30)=180\). So \(8x=140\) and \(x=17.5\). (Setting the angles  equal  is the trap; that applies to alternate interior angles.)

### GEO-29 · Area and volume · Very hard · By hand · computed

A right circular cone has a height of 12 centimeters and a slant height of 13 centimeters. A cylinder has the same base radius as the cone and the same volume as the cone. What is the height, in centimeters, of the cylinder?

- A) \(4\)
- B) \(5\)
- C) \(12\)
- D) \(36\)

**Answer:** A

**Explanation:** The cone's radius is \(\sqrt{13^2-12^2}=5\), but you don't actually need it: equal volumes with equal radii give \(\pi r^2h=\frac13\pi r^2(12)\), so \(h=4\). (The slant height is extra information. 5 is the trap: that's the radius.)

### TOP-08 · Circles · Very hard · Desmos · computed

In the \(xy\)-plane, a circle with center \((4,3)\) and radius \(r\) is tangent to the line \(y=-\frac34x+2\). What is the value of \(r\)?

**Answer:** 16/5

**Explanation:** The radius to a point of tangency is perpendicular to the tangent line, so \(r\) is the distance from \((4,3)\) to the line \(3x+4y-8=0\): \(\frac{|3(4)+4(3)-8|}{\sqrt{3^2+4^2}}=\frac{16}{5}=3.2\).

### TOP-13 · Right triangles and trigonometry · Hard · Desmos · computed

In right triangle \(ABC\), angle \(B\) is a right angle, the measure of angle \(A\) is \(32^\circ\), and \(AC=25\). Which of the following is closest to the length of \(\overline{BC}\)?

- A) \(12.5\)
- B) \(13.2\)
- C) \(15.6\)
- D) \(21.2\)

**Answer:** B

**Explanation:** \(\overline{AC}\) is the hypotenuse, and \(\overline{BC}\) is opposite angle \(A\): \(BC=25\sin32^\circ\approx13.2\). 21.2 comes from using cosine (that gives \(AB\)), and 15.6 comes from tangent.

### TOP-18 · Circles · Very hard · Desmos · computed

In the \(xy\)-plane, the circles \(x^2+y^2=25\) and \((x-6)^2+y^2=13\) intersect at two points. What is the distance between these two points?

**Answer:** 6

**Explanation:** Subtract the equations: \(x^2-(x-6)^2=12\), so \(12x-36=12\) and \(x=4\). Then \(y^2=25-16=9\), so the points are \((4,3)\) and \((4,-3)\), which are 6 apart.

### TOP-22 · Lines, angles, and triangles · Very hard · By hand · computed

In the \(xy\)-plane, a triangle has vertices at \((0,0)\), \((10,0)\), and \((4,8)\). What is the length of the altitude from \((0,0)\) to the opposite side?

**Answer:** 8

**Explanation:** Area using the base on the \(x\)-axis: \(\frac12(10)(8)=40\). The side opposite \((0,0)\) runs from \((10,0)\) to \((4,8)\) and has length \(\sqrt{36+64}=10\). The same area with that side as the base: \(\frac12(10)h=40\), so \(h=8\).

### FIG-04 · Circles · Hard · Desmos · computed

                                    x  y  -8  -6  -4  -2  2  4  -4  -2  2  4  6  O     (−2, 1)   (1, 5)    The circle shown in the \(xy\)-plane has its center at \((-2,1)\) and passes through the point \((1,5)\). Which of the following is an equation of the circle?

- A) \((x+2)^2+(y-1)^2=25\)
- B) \((x-2)^2+(y+1)^2=25\)
- C) \((x+2)^2+(y-1)^2=5\)
- D) \((x-2)^2+(y+1)^2=5\)

**Answer:** A

**Explanation:** The radius is the distance from \((-2,1)\) to \((1,5)\): \(\sqrt{3^2+4^2}=5\), so \(r^2=25\). With center \((h,k)=(-2,1)\), the equation is \((x+2)^2+(y-1)^2=25\). The other choices flip the signs of the center or forget to square the radius.

### FIG-10 · Lines, angles, and triangles · Hard · By hand · computed

      ℓ  m  (3x + 15)°  (5x − 25)°  y°   Note: Figure not drawn to scale.  In the figure, line \(\ell\) is parallel to line \(m\), and both are intersected by a transversal. The angle marked \((3x+15)^\circ\) and the angle marked \((5x-25)^\circ\) are corresponding angles, each lying above its line and to the right of the transversal. The angle marked \(y^\circ\) lies below line \(m\) and to the right of the transversal. What is the value of \(y\)?

**Answer:** 105

**Explanation:** Corresponding angles formed by parallel lines are equal: \(3x+15=5x-25\), so \(x=20\) and each angle is \(75^\circ\). The angle \(y^\circ\) and the \(75^\circ\) angle at line \(m\) are adjacent and share the part of \(m\) to the right of the transversal; their other sides point in opposite directions along the transversal. So they form a linear pair and are supplementary: \(y=180-75=105\).

### FIG-11 · Right triangles and trigonometry · Very hard · By hand · computed

      A  B  C  D  15  20   In right triangle \(ABC\), angle \(C\) is a right angle, \(AC=15\), and \(BC=20\). Point \(D\) lies on \(\overline{AB}\) such that \(\overline{CD}\) is perpendicular to \(\overline{AB}\). What is the length of \(\overline{AD}\)?

**Answer:** 9

**Explanation:** \(AB=\sqrt{15^2+20^2}=25\). Triangles \(ADC\) and \(ACB\) are similar (each has a right angle and shares angle \(A\)), so \(\frac{AD}{AC}=\frac{AC}{AB}\). That gives \(AD=\frac{15^2}{25}=9\).

