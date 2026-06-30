#!/usr/bin/env python3
"""Generates the FE Mechanical course content as JSON for HallTestPrep."""
import json, os

def P(pid, prompt, choices, answer, explanation):
    return {"id": pid, "prompt": prompt, "choices": choices, "answer": answer, "explanation": explanation}

sections = []

# 6.1 Mathematics
sections.append({
  "id": "math", "title": "Mathematics", "questions": "6-9", "weight": "~7%", "priority": "High",
  "guide": {
    "overview": "Mathematics is the toolkit every other section borrows from: analytic geometry, vectors, calculus (derivatives, integrals, basic differential equations), and linear algebra. On the FE you rarely derive anything — you recognize the form and execute fast.",
    "objectives": [
      "Work fluently with vectors: components, dot and cross products, magnitudes and angles.",
      "Differentiate and integrate standard functions; apply the chain, product, and quotient rules.",
      "Recognize and solve first-order and simple second-order differential equations.",
      "Solve small linear systems using substitution, Cramer's rule, or matrices."
    ],
    "prereqs": "Algebra, trigonometry, and the standard calculus sequence.",
    "watchOuts": [
      "Radians vs. degrees — set your calculator correctly before trig.",
      "Dropping the constant of integration when an initial condition is given.",
      "Cross product gives a vector (with direction); dot product gives a scalar.",
      "Sign errors when resolving vectors into components."
    ]
  },
  "keyEquations": [
    {"name": "Dot product", "formula": "A.B = |A||B|cos(t) = AxBx + AyBy + AzBz", "where": "Vectors"},
    {"name": "Cross product magnitude", "formula": "|AxB| = |A||B|sin(t)", "where": "Vectors"},
    {"name": "Derivative of product", "formula": "(uv)' = u'v + uv'", "where": "Differential Calculus"},
    {"name": "Integration by parts", "formula": "INT u dv = uv - INT v du", "where": "Integral Calculus"},
    {"name": "Quadratic formula", "formula": "x = (-b +/- sqrt(b^2-4ac)) / 2a", "where": "Algebra"}
  ],
  "lesson": [
    {"heading": "Vectors are your workhorse", "body": "A vector has magnitude and direction. Resolve it into components with Ax = A cos(t) and Ay = A sin(t), then recombine with |A| = sqrt(Ax^2+Ay^2) and t = atan2(Ay, Ax). The dot product A.B = |A||B|cos(t) tells you how aligned two vectors are (zero means perpendicular). The cross product AxB is perpendicular to both, with magnitude |A||B|sin(t) - used constantly for moments (M = r x F) and areas."},
    {"heading": "Calculus you actually need", "body": "Memorize the derivative and integral of polynomials, exponentials, logs, and the six trig functions. The chain rule d/dx f(g(x)) = f'(g)*g'(x) shows up everywhere. For integrals, recognize the form first: power rule, u-substitution, or integration by parts. Definite integrals give area, accumulated change, average value, and centroids."},
    {"heading": "Differential equations on the FE", "body": "Most FE ODEs are first-order linear (dy/dx + Py = Q) or separable. For y' = ky the solution is y = y0*e^(kt) - growth/decay. Simple second-order constant-coefficient equations (ay'' + by' + cy = 0) are solved with the characteristic equation a*r^2+b*r+c = 0; the roots tell you whether the response is overdamped, critically damped, or oscillatory."},
    {"heading": "Linear algebra, fast", "body": "For 2x2 and 3x3 systems, Cramer's rule is quick: x_i = det(A_i)/det(A). The determinant of a 2x2 [[a,b],[c,d]] is ad - bc. A zero determinant means no unique solution. Matrix multiplication is row-times-column; it is not commutative."}
  ],
  "practiceProblems": [
    P("math-p1", "Given A = 3i + 4j and B = 1i + 2j, find A.B (the dot product).", ["7", "11", "10", "5"], 1,
      "Dot product = AxBx + AyBy = (3)(1) + (4)(2) = 3 + 8 = 11. Remember the dot product returns a scalar."),
    P("math-p2", "What is the derivative of f(x) = x^2 * sin(x)?", ["2x*cos(x)", "2x*sin(x) + x^2*cos(x)", "x^2*cos(x)", "2x*sin(x) - x^2*cos(x)"], 1,
      "Use the product rule (uv)' = u'v + uv'. With u = x^2 (u' = 2x) and v = sin(x) (v' = cos x): f' = 2x*sin(x) + x^2*cos(x)."),
    P("math-p3", "Evaluate the definite integral of 3x^2 from 0 to 2.", ["6", "8", "12", "4"], 1,
      "The antiderivative of 3x^2 is x^3. Evaluate from 0 to 2: (2)^3 - (0)^3 = 8."),
    P("math-p4", "The general solution of dy/dt = 0.5y is:", ["y = 0.5t + C", "y = y0*e^(0.5t)", "y = e^0.5 * t", "y = 0.5e^t"], 1,
      "This is exponential growth: dy/dt = ky gives y = y0*e^(kt). Here k = 0.5, so y = y0*e^(0.5t).")
  ],
  "quiz": [
    P("math-q1", "|AxB| for |A|=5, |B|=2, angle 30 deg between them:", ["5", "10", "8.66", "2.5"], 0,
      "|AxB| = |A||B|sin(t) = 5*2*sin(30) = 10*0.5 = 5."),
    P("math-q2", "The determinant of [[2,1],[4,3]] is:", ["2", "10", "6", "-2"], 0,
      "det = ad - bc = (2)(3) - (1)(4) = 6 - 4 = 2."),
    P("math-q3", "d/dx [ln(3x)] =", ["1/(3x)", "3/x", "1/x", "3"], 2,
      "d/dx ln(3x) = (1/3x)*3 = 1/x by the chain rule."),
    P("math-q4", "The integral of cos(x) dx =", ["-sin(x)+C", "sin(x)+C", "-cos(x)+C", "tan(x)+C"], 1,
      "The antiderivative of cos(x) is sin(x) + C.")
  ]
})

# 6.2 Probability & Statistics
sections.append({
  "id": "prob-stats", "title": "Probability & Statistics", "questions": "4-6", "weight": "~5%", "priority": "Medium",
  "guide": {
    "overview": "A compact, high-yield section: descriptive statistics (mean, median, standard deviation), basic probability rules, and the normal distribution. Most problems are plug-and-chug if you know which formula to grab.",
    "objectives": [
      "Compute mean, median, mode, variance, and standard deviation.",
      "Apply addition and multiplication rules; handle independent and mutually exclusive events.",
      "Use the normal distribution and z-scores.",
      "Recognize permutations vs. combinations."
    ],
    "prereqs": "Basic algebra and summation notation.",
    "watchOuts": [
      "Population vs. sample standard deviation (dividing by N vs. N-1).",
      "Confusing 'and' (multiply) with 'or' (add) in probability.",
      "Permutations count order; combinations do not."
    ]
  },
  "keyEquations": [
    {"name": "Mean", "formula": "xbar = (sum of xi)/n", "where": "Statistics"},
    {"name": "Sample std dev", "formula": "s = sqrt[ sum(xi-xbar)^2 / (n-1) ]", "where": "Statistics"},
    {"name": "Addition rule", "formula": "P(A or B) = P(A)+P(B)-P(A and B)", "where": "Probability"},
    {"name": "Combinations", "formula": "C(n,r) = n! / [r!(n-r)!]", "where": "Probability"},
    {"name": "z-score", "formula": "z = (x - mu)/sigma", "where": "Normal Distribution"}
  ],
  "lesson": [
    {"heading": "Describing data", "body": "The mean is the average; the median is the middle value (robust to outliers); the mode is most frequent. Standard deviation measures spread. Use n-1 in the denominator for a sample, n for a full population - the FE usually specifies. Variance is the square of standard deviation."},
    {"heading": "Probability rules", "body": "For 'or' events use the addition rule P(A or B) = P(A)+P(B)-P(A and B); if mutually exclusive the overlap is zero. For 'and' with independent events, multiply: P(A and B) = P(A)P(B). Conditional probability is P(A|B) = P(A and B)/P(B)."},
    {"heading": "Counting", "body": "Permutations P(n,r) = n!/(n-r)! count ordered arrangements. Combinations C(n,r) = n!/[r!(n-r)!] count selections where order does not matter. Ask yourself: does swapping two items create a new outcome? If yes, permutation."},
    {"heading": "The normal distribution", "body": "Convert any value to a z-score z = (x-mu)/sigma, then read the standard-normal table (provided in the handbook). Remember the 68-95-99.7 rule: about 68% of data lies within +/-1 sigma, 95% within +/-2 sigma, 99.7% within +/-3 sigma."}
  ],
  "practiceProblems": [
    P("ps-p1", "Find the mean of 4, 8, 10, 14.", ["9", "8", "10", "11"], 0,
      "Mean = (4+8+10+14)/4 = 36/4 = 9."),
    P("ps-p2", "A fair die is rolled. P(rolling a 2 OR a 5)?", ["1/6", "1/3", "1/2", "2/3"], 1,
      "Mutually exclusive events: P = 1/6 + 1/6 = 2/6 = 1/3."),
    P("ps-p3", "How many ways to choose 2 people from 5 (order doesn't matter)?", ["10", "20", "25", "5"], 0,
      "Combination C(5,2) = 5!/(2!*3!) = (5*4)/(2*1) = 10."),
    P("ps-p4", "For mu=50, sigma=5, what is the z-score of x=60?", ["1", "2", "0.5", "10"], 1,
      "z = (x-mu)/sigma = (60-50)/5 = 2. The value is two standard deviations above the mean.")
  ],
  "quiz": [
    P("ps-q1", "Two independent events have P(A)=0.4, P(B)=0.5. P(A and B)?", ["0.9", "0.2", "0.1", "0.45"], 1,
      "Independent 'and' means multiply: 0.4 * 0.5 = 0.2."),
    P("ps-q2", "The median of 3, 7, 9, 12, 100 is:", ["26.2", "9", "12", "7"], 1,
      "Median is the middle of the sorted list: 9. It is unaffected by the outlier 100."),
    P("ps-q3", "Variance is:", ["the square root of std dev", "the square of std dev", "the mean of squares", "the range"], 1,
      "Variance = (standard deviation)^2."),
    P("ps-q4", "Permutations differ from combinations because they:", ["use factorials", "count order", "ignore order", "require replacement"], 1,
      "Permutations count ordered arrangements; combinations ignore order.")
  ]
})

# 6.3 Ethics
sections.append({
  "id": "ethics", "title": "Ethics & Professional Practice", "questions": "3-5", "weight": "~4%", "priority": "High (easy points)",
  "guide": {
    "overview": "Pure points if you internalize one principle: the engineer's paramount duty is to protect public health, safety, and welfare. Questions test the NCEES/NSPE code, professional obligations, conflicts of interest, and basic agency ideas.",
    "objectives": [
      "State the engineer's paramount obligation (public safety).",
      "Identify conflicts of interest and how to handle them.",
      "Apply rules on competence, confidentiality, and honest representation.",
      "Recognize when to act as a faithful agent or trustee."
    ],
    "prereqs": "None - read the NSPE Code of Ethics once.",
    "watchOuts": [
      "When in doubt, the answer almost always protects the public.",
      "Engineers must only work in their area of competence.",
      "Disclose conflicts of interest; never accept gifts that compromise judgment."
    ]
  },
  "keyEquations": [
    {"name": "Paramount duty", "formula": "Public health, safety & welfare > client/employer interest", "where": "NSPE Code"},
    {"name": "Competence", "formula": "Practice only in areas of qualification", "where": "NSPE Code"}
  ],
  "lesson": [
    {"heading": "The hierarchy of obligations", "body": "Engineers hold paramount the safety, health, and welfare of the public. This outranks duty to client, employer, and self. If an exam answer pits 'finish on schedule' or 'save the client money' against 'public safety,' choose public safety every time."},
    {"heading": "Competence and honesty", "body": "Perform services only in your areas of competence. Issue public statements only in an objective and truthful manner. Avoid deceptive acts. Sign and seal only work you have prepared or directly supervised."},
    {"heading": "Conflicts of interest", "body": "Disclose all known or potential conflicts to clients or employers. Do not accept compensation from more than one party for the same project unless all parties consent. Do not accept gifts or favors that could influence professional judgment."},
    {"heading": "Faithful agent", "body": "Act for each employer or client as a faithful agent or trustee. Keep client information confidential. Do not solicit or accept work on a contingent basis that would compromise judgment."}
  ],
  "practiceProblems": [
    P("eth-p1", "An engineer discovers a design flaw that could endanger the public, but fixing it will delay the project. The engineer should:", ["Stay silent to meet the deadline", "Report the flaw and ensure it is addressed", "Wait until after launch", "Ask for a bonus first"], 1,
      "Public safety is paramount and outranks schedule. The engineer must report and ensure the flaw is corrected."),
    P("eth-p2", "An engineer is asked to stamp drawings prepared by someone they did not supervise. They should:", ["Stamp them to be helpful", "Refuse unless they reviewed/supervised the work", "Stamp for a fee", "Stamp only structural sheets"], 1,
      "Engineers may seal only work they prepared or directly supervised. Stamping unreviewed work is unethical."),
    P("eth-p3", "Accepting a valuable gift from a vendor bidding on your project is:", ["Fine if under $100", "A conflict of interest to avoid or disclose", "Standard practice", "Acceptable if the bid is lowest"], 1,
      "Gifts that could influence judgment create a conflict of interest and must be avoided or disclosed."),
    P("eth-p4", "An engineer is offered a project outside their expertise. The ethical action is:", ["Take it and learn as you go", "Decline or associate with a qualified expert", "Subcontract secretly", "Take it for the fee"], 1,
      "Engineers must work only within their competence - decline or bring in qualified expertise.")
  ],
  "quiz": [
    P("eth-q1", "The engineer's paramount duty is to:", ["the employer", "the public's safety, health & welfare", "the client's budget", "the profession"], 1,
      "Protecting public health, safety, and welfare is the paramount obligation."),
    P("eth-q2", "Confidential client information should be:", ["shared with competitors", "kept confidential", "published", "sold"], 1,
      "Engineers act as faithful agents and keep client information confidential."),
    P("eth-q3", "Public statements by engineers must be:", ["persuasive", "objective and truthful", "optimistic", "brief"], 1,
      "Engineers must be objective and truthful in public statements."),
    P("eth-q4", "Working outside your area of competence is:", ["encouraged", "a code violation", "fine with disclosure only", "required for growth"], 1,
      "Practicing outside your competence violates the code unless you associate with qualified experts.")
  ]
})

# 6.4 Engineering Economics
sections.append({
  "id": "econ", "title": "Engineering Economics", "questions": "4-6", "weight": "~5%", "priority": "High (easy points)",
  "guide": {
    "overview": "Time value of money. Master the factor notation in the handbook and these become near-automatic: present worth, future worth, annuities, and simple comparisons. High reward for low effort.",
    "objectives": [
      "Move money across time with P, F, and A factors.",
      "Read and apply the (F/P, i, n) style factor tables.",
      "Compare alternatives using present worth and annual cost.",
      "Handle simple vs. compound interest and effective rates."
    ],
    "prereqs": "Algebra and exponentials.",
    "watchOuts": [
      "Match the interest rate period to the number of periods (monthly i with monthly n).",
      "Effective annual rate is not the nominal rate when compounding more than once a year.",
      "Read whether a value is given as present (now) or future (later)."
    ]
  },
  "keyEquations": [
    {"name": "Single payment compound", "formula": "F = P(1+i)^n", "where": "Eng. Economics"},
    {"name": "Present worth", "formula": "P = F(1+i)^-n", "where": "Eng. Economics"},
    {"name": "Sinking fund", "formula": "A = F * [ i / ((1+i)^n - 1) ]", "where": "Eng. Economics"},
    {"name": "Capital recovery", "formula": "A = P * [ i(1+i)^n / ((1+i)^n - 1) ]", "where": "Eng. Economics"},
    {"name": "Effective annual rate", "formula": "i_eff = (1 + r/m)^m - 1", "where": "Eng. Economics"}
  ],
  "lesson": [
    {"heading": "The core idea: money has a time value", "body": "A dollar today is worth more than a dollar later because it can earn interest. Every problem is about shifting cash flows to a common point in time - usually 'now' (present worth P) or 'the end' (future worth F) - using the interest rate i and number of periods n."},
    {"heading": "Single payments", "body": "To push a present amount forward: F = P(1+i)^n. To pull a future amount back: P = F(1+i)^-n. The FE handbook lists these as factors written (F/P, i%, n) and (P/F, i%, n) - you just multiply the known amount by the tabulated factor."},
    {"heading": "Uniform series (annuities)", "body": "When equal payments A occur each period, use the capital-recovery factor to convert a present amount into payments (A/P), or the sinking-fund factor to build a future amount (A/F). Loan payments, depreciation, and recurring costs all use these."},
    {"heading": "Comparing alternatives", "body": "Bring every option's cash flows to the same basis - present worth or equivalent annual cost - then pick the better number (lowest cost or highest worth). Make sure compounding periods match the payment periods before you compute."}
  ],
  "practiceProblems": [
    P("econ-p1", "You invest $1,000 at 6% annual compound interest for 5 years. Future value?", ["$1,300", "$1,338", "$1,500", "$1,060"], 1,
      "F = P(1+i)^n = 1000(1.06)^5 = 1000(1.3382) = $1,338."),
    P("econ-p2", "What is the present worth of $5,000 received 4 years from now at 8%?", ["$3,675", "$4,200", "$3,403", "$4,630"], 0,
      "P = F(1+i)^-n = 5000/(1.08)^4 = 5000/1.3605 = $3,675."),
    P("econ-p3", "A nominal 12% rate compounded monthly has an effective annual rate of about:", ["12.0%", "12.68%", "13.2%", "11.4%"], 1,
      "i_eff = (1 + 0.12/12)^12 - 1 = (1.01)^12 - 1 = 0.1268 = 12.68%."),
    P("econ-p4", "Simple interest on $2,000 at 5% for 3 years equals:", ["$300", "$315", "$100", "$30"], 0,
      "Simple interest I = P*i*n = 2000(0.05)(3) = $300 (no compounding).")
  ],
  "quiz": [
    P("econ-q1", "F = P(1+i)^n converts:", ["future to present", "present to future", "annuity to present", "rate to period"], 1,
      "It pushes a present amount P forward to a future amount F."),
    P("econ-q2", "If compounding is monthly, n for 3 years is:", ["3", "12", "36", "30"], 2,
      "Monthly periods over 3 years: 3 * 12 = 36."),
    P("econ-q3", "To compare two projects fairly you should:", ["use different rates", "bring cash flows to a common time basis", "ignore time", "use only first cost"], 1,
      "Convert all cash flows to a common basis (present worth or annual cost) before comparing."),
    P("econ-q4", "Effective annual rate exceeds nominal rate when:", ["compounding is annual", "compounding is more than once per year", "rate is zero", "n is one"], 1,
      "More frequent compounding raises the effective rate above the nominal rate.")
  ]
})

# 6.5 Electricity & Magnetism
sections.append({
  "id": "electrical", "title": "Electricity & Magnetism", "questions": "5-8", "weight": "~7%", "priority": "Medium-High",
  "guide": {
    "overview": "DC and basic AC circuits: Ohm's law, series/parallel resistance, Kirchhoff's laws, power, capacitors and inductors, and simple AC impedance. Mechanical candidates often under-study this - don't.",
    "objectives": [
      "Apply Ohm's law and the power relations.",
      "Reduce series and parallel resistor networks.",
      "Use Kirchhoff's voltage and current laws.",
      "Handle capacitor/inductor energy and basic AC impedance."
    ],
    "prereqs": "Algebra and complex numbers for AC.",
    "watchOuts": [
      "Resistors in parallel: the equivalent is smaller than the smallest resistor.",
      "Watch units: mA, kOhm, microF.",
      "In AC, use RMS values for power unless told otherwise."
    ]
  },
  "keyEquations": [
    {"name": "Ohm's law", "formula": "V = IR", "where": "Circuits"},
    {"name": "Power", "formula": "P = VI = I^2 R = V^2/R", "where": "Circuits"},
    {"name": "Parallel resistance", "formula": "1/Req = 1/R1 + 1/R2 + ...", "where": "Circuits"},
    {"name": "Capacitor energy", "formula": "E = 0.5 C V^2", "where": "Circuits"},
    {"name": "Capacitive reactance", "formula": "Xc = 1/(2 pi f C)", "where": "AC Circuits"}
  ],
  "lesson": [
    {"heading": "Ohm's law and power", "body": "The foundation: V = IR. Power dissipated by a resistor is P = VI, and by substitution P = I^2 R = V^2/R. Pick the form that uses the quantities you already know."},
    {"heading": "Combining resistors", "body": "In series, resistances add: Req = R1 + R2 + ... and the same current flows through each. In parallel, 1/Req = sum(1/Ri) and the same voltage appears across each; the equivalent is always less than the smallest branch. For two parallel resistors, Req = R1*R2/(R1+R2)."},
    {"heading": "Kirchhoff's laws", "body": "KCL: the sum of currents into a node equals the sum out (charge is conserved). KVL: around any closed loop the voltage rises equal the drops (energy is conserved). These let you solve any network too complex for simple series/parallel reduction."},
    {"heading": "Energy storage and AC", "body": "A capacitor stores E = 0.5 C V^2; an inductor stores E = 0.5 L I^2. In AC circuits, capacitors and inductors present frequency-dependent reactance: Xc = 1/(2 pi f C) and Xl = 2 pi f L. Impedance Z combines resistance and reactance as a complex quantity, and power calculations use RMS values."}
  ],
  "practiceProblems": [
    P("elec-p1", "A 12 V source drives a 4 Ohm resistor. The current is:", ["48 A", "3 A", "0.33 A", "16 A"], 1,
      "Ohm's law: I = V/R = 12/4 = 3 A."),
    P("elec-p2", "Two resistors, 6 Ohm and 3 Ohm, in parallel give:", ["9 Ohm", "2 Ohm", "4.5 Ohm", "0.5 Ohm"], 1,
      "Req = R1*R2/(R1+R2) = (6*3)/(6+3) = 18/9 = 2 Ohm. Always less than the smaller resistor."),
    P("elec-p3", "Power dissipated by a 10 Ohm resistor carrying 2 A:", ["20 W", "40 W", "5 W", "100 W"], 1,
      "P = I^2 R = (2)^2 (10) = 4*10 = 40 W."),
    P("elec-p4", "Energy stored in a 100 microF capacitor charged to 50 V:", ["0.125 J", "2.5 J", "0.25 J", "5 J"], 0,
      "E = 0.5 C V^2 = 0.5(100e-6)(50^2) = 0.5(1e-4)(2500) = 0.125 J.")
  ],
  "quiz": [
    P("elec-q1", "Resistors in series:", ["add reciprocals", "add directly", "always reduce below smallest", "share voltage equally"], 1,
      "Series resistances add directly: Req = R1 + R2 + ..."),
    P("elec-q2", "KCL is a statement of conservation of:", ["energy", "charge", "voltage", "power"], 1,
      "Kirchhoff's current law conserves charge at a node."),
    P("elec-q3", "Capacitive reactance Xc as frequency increases:", ["increases", "decreases", "stays constant", "becomes infinite"], 1,
      "Xc = 1/(2 pi f C) - it decreases as frequency rises."),
    P("elec-q4", "For a 9 V battery and 3 Ohm resistor, power delivered is:", ["3 W", "27 W", "12 W", "81 W"], 1,
      "P = V^2/R = 81/3 = 27 W.")
  ]
})

# 6.6 Statics
sections.append({
  "id": "statics", "title": "Statics", "questions": "9-14", "weight": "~10%", "priority": "Very High",
  "guide": {
    "overview": "Bodies in equilibrium: force resultants, free-body diagrams, equilibrium of rigid bodies, trusses and frames, centroids and moments of inertia, and friction. One of the largest buckets and the foundation of the solid-mechanics chapters.",
    "objectives": [
      "Resolve forces into components; find resultants and moments.",
      "Draw correct free-body diagrams and write equilibrium equations.",
      "Solve trusses by joints and sections; analyze frames and machines.",
      "Locate centroids and compute moments of inertia (including parallel-axis).",
      "Apply static friction (impending motion, F = mu*N)."
    ],
    "prereqs": "Vectors and trigonometry. Precise free-body diagrams are the whole game.",
    "watchOuts": [
      "Incomplete or wrong free-body diagrams (missing a reaction or force).",
      "Moment sign/direction errors; wrong moment arm (perpendicular distance).",
      "Assuming friction is at maximum when motion isn't actually impending.",
      "Forgetting the parallel-axis term when shifting moment of inertia."
    ]
  },
  "keyEquations": [
    {"name": "Equilibrium (2D)", "formula": "sum Fx = 0, sum Fy = 0, sum M = 0", "where": "Statics - Equilibrium"},
    {"name": "Moment", "formula": "M = F*d (d = perpendicular distance)", "where": "Statics - Moments"},
    {"name": "Parallel-axis theorem", "formula": "I = Ic + A*d^2", "where": "Moments of Inertia"},
    {"name": "Static friction", "formula": "F <= mu_s * N (max at impending motion)", "where": "Friction"},
    {"name": "Composite centroid", "formula": "xbar = sum(xi*Ai)/sum(Ai)", "where": "Centroids"}
  ],
  "lesson": [
    {"heading": "Everything starts with a free-body diagram", "body": "Isolate the body, draw every external force and reaction acting on it, and label known dimensions. Most statics errors are FBD errors - a missing reaction, a force in the wrong direction, or a mislabeled angle. Get the FBD right and the three equilibrium equations (sum Fx = 0, sum Fy = 0, sum M = 0) usually finish the problem."},
    {"heading": "Moments and the smart pivot", "body": "A moment is force times perpendicular distance: M = F*d. Choose your moment center wisely - summing moments about a point where an unknown acts eliminates that unknown from the equation, often solving for a reaction in one step."},
    {"heading": "Trusses and frames", "body": "For trusses, use the method of joints when a joint has 2 or fewer unknown member forces, or the method of sections (cut through 3 or fewer members) when you want a specific member directly. Two-force members carry force only along their length. Frames and machines have multi-force members; analyze each member with its own FBD."},
    {"heading": "Centroids, inertia, and friction", "body": "For composite areas, xbar = sum(xi*Ai)/sum(Ai). To find moment of inertia about a non-centroidal axis, add the transfer term: I = Ic + A*d^2. For friction, the resisting force can be anything up to F_max = mu_s*N - it only equals mu_s*N at impending motion, so don't assume maximum friction unless the problem says sliding is about to start."}
  ],
  "practiceProblems": [
    P("stat-p1", "A 10 m simply-supported beam carries a 200 N load 3 m from the left support A. Find R_A.", ["60 N", "140 N", "100 N", "200 N"], 1,
      "Sum moments about B: R_A(10) - 200(10-3) = 0, so R_A(10) = 1400 and R_A = 140 N. (R_B = 60 N by sum Fy.)"),
    P("stat-p2", "A 100 N block sits on a surface with mu_s = 0.3. Horizontal force to initiate motion?", ["3 N", "30 N", "300 N", "33 N"], 1,
      "Normal force N = 100 N. F_max = mu_s*N = 0.3 * 100 = 30 N."),
    P("stat-p3", "A force of 50 N acts 0.4 m from a pivot, perpendicular. The moment is:", ["12.5 N*m", "20 N*m", "125 N*m", "50 N*m"], 1,
      "M = F*d = 50 * 0.4 = 20 N*m."),
    P("stat-p4", "Moment of inertia of an area is shifted a distance d from the centroid. You must add:", ["A*d", "A*d^2", "Ic*d", "d^2/A"], 1,
      "Parallel-axis theorem: I = Ic + A*d^2. The transfer term is the area times distance squared.")
  ],
  "quiz": [
    P("stat-q1", "For 2D equilibrium, how many independent equations are available?", ["1", "2", "3", "6"], 2,
      "Three: sum Fx = 0, sum Fy = 0, and sum M = 0."),
    P("stat-q2", "A two-force member carries force:", ["perpendicular to its length", "along its length", "at 45 degrees", "as a couple"], 1,
      "Two-force members carry force only along the line connecting the two pins."),
    P("stat-q3", "Method of sections works best by cutting through at most:", ["1 member", "2 members", "3 members", "4 members"], 2,
      "Cut through 3 or fewer members so the three equilibrium equations can solve them."),
    P("stat-q4", "Static friction force before impending motion is:", ["exactly mu*N", "less than or equal to mu*N", "greater than mu*N", "zero"], 1,
      "Friction is <= mu_s*N and only reaches mu_s*N at impending motion.")
  ]
})

# 6.7 Dynamics
sections.append({
  "id": "dynamics", "title": "Dynamics, Kinematics & Vibrations", "questions": "9-14", "weight": "~10%", "priority": "Very High",
  "guide": {
    "overview": "Motion and its causes: kinematics (position, velocity, acceleration), Newton's second law, work-energy and impulse-momentum methods, and simple harmonic vibration. Decide early whether energy or momentum is the faster route.",
    "objectives": [
      "Relate position, velocity, and acceleration (constant and variable a).",
      "Apply sum F = ma and the work-energy theorem.",
      "Use impulse-momentum and conservation of momentum.",
      "Analyze simple harmonic motion and natural frequency."
    ],
    "prereqs": "Statics (free-body diagrams), calculus (v = dx/dt), and energy concepts.",
    "watchOuts": [
      "Mixing up average and instantaneous quantities.",
      "Forgetting that work-energy is a scalar method (no directions to track).",
      "Sign conventions in momentum (velocity direction matters)."
    ]
  },
  "keyEquations": [
    {"name": "Constant acceleration", "formula": "v = v0 + at;  v^2 = v0^2 + 2a(dx)", "where": "Kinematics"},
    {"name": "Newton's second law", "formula": "sum F = ma", "where": "Dynamics"},
    {"name": "Work-energy", "formula": "W = dKE = 0.5 m (v^2 - v0^2)", "where": "Energy Methods"},
    {"name": "Impulse-momentum", "formula": "F*dt = m*dv", "where": "Momentum"},
    {"name": "Natural frequency", "formula": "wn = sqrt(k/m)", "where": "Vibrations"}
  ],
  "lesson": [
    {"heading": "Kinematics first", "body": "If acceleration is constant, use v = v0 + at, dx = v0*t + 0.5*a*t^2, and v^2 = v0^2 + 2a*dx. If acceleration varies, fall back to calculus: v = dx/dt, a = dv/dt, and integrate. Projectile motion is just two independent constant-acceleration problems (horizontal a=0, vertical a=-g)."},
    {"heading": "Newton's second law", "body": "Draw the FBD, then apply sum F = ma along each axis. The acceleration points in the direction of the net force. For systems of connected bodies, write sum F = ma for each mass and link them through the shared acceleration or tension."},
    {"heading": "Energy vs. momentum - pick the shortcut", "body": "Work-energy (W = dKE) is best when you know forces and distances and want a speed; it's scalar, so no angles to chase. Impulse-momentum (F*dt = m*dv) and conservation of momentum shine for collisions and impacts where time or interacting masses matter. Recognizing which to use saves the most time."},
    {"heading": "Vibrations", "body": "A spring-mass system oscillates at natural frequency wn = sqrt(k/m) rad/s, with f = wn/(2 pi). Adding damping reduces amplitude over time. The FE keeps this basic: find wn, period T = 2 pi/wn, or the frequency."}
  ],
  "practiceProblems": [
    P("dyn-p1", "A car accelerates from rest at 3 m/s^2 for 5 s. Final speed?", ["8 m/s", "15 m/s", "1.67 m/s", "45 m/s"], 1,
      "v = v0 + at = 0 + 3(5) = 15 m/s."),
    P("dyn-p2", "A 2 kg mass has a net force of 10 N. Its acceleration is:", ["20 m/s^2", "5 m/s^2", "0.2 m/s^2", "12 m/s^2"], 1,
      "a = F/m = 10/2 = 5 m/s^2."),
    P("dyn-p3", "A 1,000 kg car moving at 20 m/s has kinetic energy:", ["20,000 J", "200,000 J", "400,000 J", "10,000 J"], 1,
      "KE = 0.5 m v^2 = 0.5(1000)(20^2) = 0.5(1000)(400) = 200,000 J."),
    P("dyn-p4", "A spring-mass system with k = 200 N/m and m = 2 kg has natural frequency wn of:", ["10 rad/s", "100 rad/s", "20 rad/s", "5 rad/s"], 0,
      "wn = sqrt(k/m) = sqrt(200/2) = sqrt(100) = 10 rad/s.")
  ],
  "quiz": [
    P("dyn-q1", "Work-energy methods are best when you want:", ["time of impact", "a speed from forces and distance", "collision outcomes", "natural frequency"], 1,
      "Work-energy directly relates force, distance, and speed change."),
    P("dyn-q2", "In a perfectly inelastic collision, what is conserved?", ["kinetic energy", "momentum", "both", "neither"], 1,
      "Momentum is always conserved; kinetic energy is not in inelastic collisions."),
    P("dyn-q3", "Period of a spring-mass system is:", ["2 pi sqrt(m/k)", "sqrt(k/m)", "2 pi sqrt(k/m)", "k/m"], 0,
      "T = 2 pi/wn = 2 pi sqrt(m/k)."),
    P("dyn-q4", "Projectile horizontal acceleration (no drag) is:", ["g", "0", "-g", "9.81 m/s^2"], 1,
      "Horizontal acceleration is zero; only gravity acts vertically.")
  ]
})

# 6.8 Mechanics of Materials
sections.append({
  "id": "mechanics-materials", "title": "Mechanics of Materials", "questions": "9-14", "weight": "~10%", "priority": "Very High",
  "guide": {
    "overview": "How solids respond to load: stress and strain, axial/torsion/bending, the stress-strain curve, beam shear and moment, and combined loading. Builds directly on Statics.",
    "objectives": [
      "Compute axial, shear, bearing, and thermal stress/strain.",
      "Apply Hooke's law and use E, G, and Poisson's ratio.",
      "Find bending stress (sigma = Mc/I) and torsional shear (tau = Tr/J).",
      "Sketch shear and moment diagrams."
    ],
    "prereqs": "Statics (internal reactions, centroids, I). Know section properties.",
    "watchOuts": [
      "Confusing area moment of inertia I with polar moment J.",
      "Using diameter where radius is needed (c, r).",
      "Forgetting thermal strain delta = alpha*L*dT in constrained members."
    ]
  },
  "keyEquations": [
    {"name": "Axial stress", "formula": "sigma = P/A", "where": "Stress"},
    {"name": "Hooke's law", "formula": "sigma = E*epsilon", "where": "Stress-Strain"},
    {"name": "Bending stress", "formula": "sigma = Mc/I", "where": "Beams"},
    {"name": "Torsional shear", "formula": "tau = Tr/J", "where": "Torsion"},
    {"name": "Thermal deformation", "formula": "delta = alpha*L*dT", "where": "Thermal"}
  ],
  "lesson": [
    {"heading": "Stress and strain", "body": "Normal stress sigma = P/A (force over area). Normal strain epsilon = delta/L (deformation over original length). In the elastic region they're proportional via Hooke's law sigma = E*epsilon, where E is Young's modulus. Shear stress tau = V/A and shear strain relate through the shear modulus G."},
    {"heading": "The stress-strain curve", "body": "Loading a ductile material: a linear elastic region (slope E), then the yield point, plastic deformation, ultimate strength, and finally fracture. The proportional limit ends the straight line; the yield strength is the design-critical value. Poisson's ratio links lateral to axial strain."},
    {"heading": "Bending and torsion", "body": "A beam in bending develops sigma = Mc/I, where c is the distance from the neutral axis to the outer fiber and I is the area moment of inertia. A shaft in torsion develops tau = Tr/J, where J is the polar moment of inertia. Don't mix up I (bending) and J (torsion), and watch radius vs. diameter."},
    {"heading": "Shear and moment diagrams", "body": "Start from the support reactions (a statics problem), then track shear V along the beam: point loads cause jumps, distributed loads cause slopes. The moment diagram is the integral of shear - maximum moment occurs where shear crosses zero, and that's usually where bending stress is critical."}
  ],
  "practiceProblems": [
    P("mom-p1", "A 5,000 N axial load acts on a 10 mm^2 cross-section. The stress is:", ["50 MPa", "500 MPa", "0.5 MPa", "5 MPa"], 1,
      "sigma = P/A = 5000 N / (10e-6 m^2) = 5e8 Pa = 500 MPa."),
    P("mom-p2", "A steel rod (E = 200 GPa) has strain 0.001. The stress is:", ["20 MPa", "200 MPa", "2 GPa", "0.2 MPa"], 1,
      "sigma = E*epsilon = (200e9)(0.001) = 2e8 Pa = 200 MPa."),
    P("mom-p3", "In sigma = Mc/I, the term c represents:", ["centroid location", "distance to the outer fiber", "the load", "cross-section area"], 1,
      "c is the distance from the neutral axis to the extreme (outer) fiber, where bending stress is largest."),
    P("mom-p4", "A bar of length 2 m, alpha = 12e-6 per C, heated 50 C, free to expand. Elongation?", ["1.2 mm", "0.6 mm", "12 mm", "0.12 mm"], 0,
      "delta = alpha*L*dT = (12e-6)(2)(50) = 1.2e-3 m = 1.2 mm.")
  ],
  "quiz": [
    P("mom-q1", "Young's modulus E is the slope of:", ["the plastic region", "the elastic stress-strain line", "the shear curve", "the moment diagram"], 1,
      "E is the slope of the linear elastic portion of the stress-strain curve."),
    P("mom-q2", "Torsional shear stress uses which property?", ["I", "J", "A", "c only"], 1,
      "tau = Tr/J uses the polar moment of inertia J."),
    P("mom-q3", "Maximum bending moment along a beam typically occurs where:", ["shear is maximum", "shear crosses zero", "the load is applied", "at the supports"], 1,
      "The moment is the integral of shear, so it peaks where shear = 0."),
    P("mom-q4", "Poisson's ratio relates:", ["stress to strain", "lateral to axial strain", "shear to torsion", "load to area"], 1,
      "Poisson's ratio = -(lateral strain)/(axial strain).")
  ]
})

# 6.9 Material Properties
sections.append({
  "id": "materials", "title": "Material Properties & Processing", "questions": "4-6", "weight": "~5%", "priority": "Medium",
  "guide": {
    "overview": "Properties (mechanical, thermal, electrical), the structure-property link, phase diagrams and heat treatment, and failure modes like fatigue and creep. More conceptual than computational.",
    "objectives": [
      "Distinguish strength, stiffness, ductility, hardness, and toughness.",
      "Read a binary phase diagram (lever rule, eutectic).",
      "Explain heat treatment effects (annealing, quenching, tempering).",
      "Recognize fatigue, creep, and brittle vs. ductile failure."
    ],
    "prereqs": "Basic chemistry and the stress-strain curve.",
    "watchOuts": [
      "Strength (stress to fail) is not stiffness (resistance to deflection, set by E).",
      "Toughness is area under the stress-strain curve, not hardness.",
      "Fatigue failure happens below the static yield stress under cyclic load."
    ]
  },
  "keyEquations": [
    {"name": "Lever rule", "formula": "wt% phase = (opposite arm)/(total tie line)", "where": "Phase Diagrams"},
    {"name": "Toughness", "formula": "approx area under stress-strain curve", "where": "Properties"}
  ],
  "lesson": [
    {"heading": "Properties vocabulary", "body": "Strength is the stress a material withstands before yielding or fracturing. Stiffness is resistance to elastic deflection, governed by E (a stiff material isn't necessarily strong). Ductility is how much it deforms before fracture; brittleness is the opposite. Hardness resists indentation; toughness is the energy absorbed before fracture (area under the stress-strain curve)."},
    {"heading": "Structure determines properties", "body": "Crystal structure (BCC, FCC, HCP), grain size, and defects control behavior. Smaller grains generally mean higher strength (Hall-Petch). Alloying and cold work strengthen metals; they also typically reduce ductility."},
    {"heading": "Phase diagrams and heat treatment", "body": "A binary phase diagram maps phases vs. composition and temperature. The lever rule gives the fraction of each phase in a two-phase region. Heat treatment changes microstructure: annealing softens and relieves stress; quenching (rapid cooling) hardens steel by forming martensite; tempering then restores some toughness."},
    {"heading": "Failure modes", "body": "Fatigue is failure under repeated cyclic loading, often well below the static strength - the endurance limit matters for steels. Creep is slow deformation under sustained load at high temperature. Ductile failure shows necking and warning; brittle failure is sudden with little deformation."}
  ],
  "practiceProblems": [
    P("mat-p1", "Stiffness of a material is primarily set by its:", ["yield strength", "modulus of elasticity E", "hardness", "ductility"], 1,
      "Stiffness (resistance to elastic deflection) is governed by Young's modulus E."),
    P("mat-p2", "Quenching steel produces a hard phase called:", ["austenite", "martensite", "ferrite", "pearlite"], 1,
      "Rapid cooling (quenching) traps carbon, forming hard, brittle martensite."),
    P("mat-p3", "Failure under repeated cyclic loading below the yield stress is:", ["creep", "fatigue", "fracture toughness", "yielding"], 1,
      "That's fatigue - cracks initiate and grow under cyclic stress, failing below the static strength."),
    P("mat-p4", "Toughness corresponds to:", ["the slope of the elastic line", "area under the stress-strain curve", "the yield point only", "hardness number"], 1,
      "Toughness is the energy absorbed before fracture - the area under the stress-strain curve.")
  ],
  "quiz": [
    P("mat-q1", "A material that deforms a lot before breaking is:", ["brittle", "ductile", "stiff", "hard"], 1,
      "Large deformation before fracture means ductile."),
    P("mat-q2", "Annealing primarily:", ["hardens", "softens and relieves stress", "adds carbon", "causes fatigue"], 1,
      "Annealing softens the metal and relieves internal stresses."),
    P("mat-q3", "Creep is significant at:", ["low temperature", "high temperature under sustained load", "high frequency", "zero load"], 1,
      "Creep is time-dependent deformation at elevated temperature under constant load."),
    P("mat-q4", "The lever rule gives:", ["modulus", "phase fractions in a two-phase region", "grain size", "hardness"], 1,
      "The lever rule computes the weight fraction of each phase in a two-phase field.")
  ]
})

# 6.10 Fluid Mechanics
sections.append({
  "id": "fluids", "title": "Fluid Mechanics", "questions": "9-14", "weight": "~10%", "priority": "Very High",
  "guide": {
    "overview": "Fluids at rest and in motion: hydrostatic pressure, buoyancy, continuity, Bernoulli's equation, the energy equation with head loss, and the meaning of Reynolds number. A heavy hitter for mechanical candidates.",
    "objectives": [
      "Compute hydrostatic pressure and forces on surfaces.",
      "Apply buoyancy (Archimedes).",
      "Use continuity (A1*V1 = A2*V2) and Bernoulli's equation.",
      "Classify flow with Reynolds number and account for head loss."
    ],
    "prereqs": "Statics, energy concepts, and unit fluency.",
    "watchOuts": [
      "Gauge vs. absolute pressure.",
      "Bernoulli assumes steady, incompressible, frictionless flow along a streamline.",
      "Use consistent units; density of water is about 1000 kg/m^3."
    ]
  },
  "keyEquations": [
    {"name": "Hydrostatic pressure", "formula": "P = rho*g*h", "where": "Fluid Statics"},
    {"name": "Buoyancy", "formula": "Fb = rho_fluid * g * V_displaced", "where": "Buoyancy"},
    {"name": "Continuity", "formula": "A1*V1 = A2*V2", "where": "Flow"},
    {"name": "Bernoulli", "formula": "P + 0.5*rho*V^2 + rho*g*z = constant", "where": "Energy"},
    {"name": "Reynolds number", "formula": "Re = rho*V*D/mu", "where": "Flow Regime"}
  ],
  "lesson": [
    {"heading": "Fluid statics", "body": "Pressure increases linearly with depth: P = rho*g*h (gauge). This drives forces on dam walls, tank sides, and submerged gates - the resultant acts at the centroid of the pressure distribution. Manometers use the same relation across fluid columns. Always note whether pressure is gauge or absolute."},
    {"heading": "Buoyancy", "body": "Archimedes' principle: the buoyant force equals the weight of displaced fluid, Fb = rho_fluid * g * V_displaced. An object floats when its weight equals the buoyant force at partial submersion; it sinks when its density exceeds the fluid's."},
    {"heading": "Continuity and Bernoulli", "body": "Mass conservation for incompressible flow gives A1*V1 = A2*V2 - narrower pipe, faster flow. Bernoulli's equation, P + 0.5*rho*V^2 + rho*g*z = constant, trades pressure, kinetic, and potential energy along a streamline. It assumes steady, incompressible, frictionless flow - handy for nozzles, Venturi meters, and pitot tubes."},
    {"heading": "Real flow: Reynolds and head loss", "body": "Reynolds number Re = rho*V*D/mu predicts the regime: laminar below about 2,300, turbulent above about 4,000 (in pipes). Real pipe flow loses energy to friction; the energy equation adds a head-loss term, often from the Darcy-Weisbach equation with a friction factor read off the Moody chart."}
  ],
  "practiceProblems": [
    P("flu-p1", "Gauge pressure at 5 m depth in water (rho=1000, g=9.81):", ["49.05 kPa", "4.9 kPa", "490 kPa", "5 kPa"], 0,
      "P = rho*g*h = 1000(9.81)(5) = 49,050 Pa = about 49.05 kPa."),
    P("flu-p2", "Water flows in a pipe that narrows from 0.1 m^2 to 0.05 m^2. If V1 = 2 m/s, V2 =", ["1 m/s", "4 m/s", "2 m/s", "8 m/s"], 1,
      "Continuity: A1*V1 = A2*V2, so V2 = (0.1*2)/0.05 = 4 m/s."),
    P("flu-p3", "Buoyant force on a 0.02 m^3 object fully submerged in water:", ["196 N", "20 N", "1962 N", "0.2 N"], 0,
      "Fb = rho*g*V = 1000(9.81)(0.02) = 196.2 N."),
    P("flu-p4", "A Reynolds number of 800 in a pipe indicates flow that is:", ["turbulent", "laminar", "transitional", "compressible"], 1,
      "Re below about 2,300 in a pipe is laminar flow.")
  ],
  "quiz": [
    P("flu-q1", "Bernoulli's equation assumes flow is:", ["compressible and viscous", "steady, incompressible, frictionless", "always turbulent", "unsteady"], 1,
      "Bernoulli applies to steady, incompressible, frictionless flow along a streamline."),
    P("flu-q2", "If a pipe's area halves, the velocity:", ["halves", "doubles", "stays the same", "quadruples"], 1,
      "Continuity: smaller area means proportionally higher velocity, so it doubles."),
    P("flu-q3", "Hydrostatic pressure depends on:", ["surface area", "fluid density and depth", "pipe length", "velocity"], 1,
      "P = rho*g*h - density and depth only (not the shape or area)."),
    P("flu-q4", "Reynolds number compares:", ["pressure to area", "inertial to viscous forces", "mass to volume", "heat to work"], 1,
      "Re is the ratio of inertial to viscous forces.")
  ]
})

# 6.11 Thermodynamics
sections.append({
  "id": "thermo", "title": "Thermodynamics (incl. HVAC)", "questions": "10-15", "weight": "~11%", "priority": "Very High",
  "guide": {
    "overview": "Energy and its transformations: properties and states, the first and second laws, ideal gases, cycles (Carnot, Rankine, refrigeration), and basic psychrometrics for HVAC. Often the single largest topic.",
    "objectives": [
      "Apply the first law (energy balance) to closed and open systems.",
      "Use ideal gas relations and property tables.",
      "Compute thermal efficiency and COP for cycles.",
      "Read a psychrometric chart for HVAC basics."
    ],
    "prereqs": "Algebra, unit conversions, and reading property tables.",
    "watchOuts": [
      "Absolute temperature (K or R) in all gas-law and efficiency formulas.",
      "Sign conventions for heat and work.",
      "COP can exceed 1; efficiency cannot."
    ]
  },
  "keyEquations": [
    {"name": "First law (closed)", "formula": "Q - W = dU", "where": "Energy Balance"},
    {"name": "Ideal gas law", "formula": "PV = mRT", "where": "Ideal Gas"},
    {"name": "Carnot efficiency", "formula": "eta = 1 - T_cold/T_hot", "where": "Cycles"},
    {"name": "COP (refrigeration)", "formula": "COP = Q_cold / W_in", "where": "Refrigeration"},
    {"name": "Thermal efficiency", "formula": "eta = W_net / Q_in", "where": "Power Cycles"}
  ],
  "lesson": [
    {"heading": "States and properties", "body": "A pure substance's state is fixed by two independent intensive properties (e.g., P and T, or P and quality x). Use steam/refrigerant tables to look up internal energy u, enthalpy h, and entropy s. In the two-phase region, properties are interpolated by quality: h = hf + x*hfg."},
    {"heading": "First law: conserve energy", "body": "For a closed system, Q - W = dU. For an open system (control volume) at steady state, energy in equals energy out, including flow work - leading to the enthalpy form for turbines, pumps, nozzles, and heat exchangers. Track sign conventions: heat in positive, work out positive (in the common convention)."},
    {"heading": "Ideal gases", "body": "PV = mRT (or Pv = RT per unit mass), with T in absolute units. For specific processes - isothermal, isobaric, isochoric, adiabatic - particular relations apply, and du = cv*dT, dh = cp*dT for ideal gases."},
    {"heading": "Cycles and HVAC", "body": "Power cycles convert heat to work: thermal efficiency eta = W_net/Q_in, capped by the Carnot limit eta = 1 - T_cold/T_hot (absolute temps). Refrigeration and heat pumps are rated by COP = useful heat/work in, which can exceed 1. For HVAC, the psychrometric chart relates dry-bulb temperature, humidity ratio, relative humidity, and enthalpy of moist air."}
  ],
  "practiceProblems": [
    P("thr-p1", "A closed system absorbs 500 J of heat and does 200 J of work. dU =", ["700 J", "300 J", "-300 J", "100 J"], 1,
      "First law: dU = Q - W = 500 - 200 = 300 J."),
    P("thr-p2", "A Carnot engine operates between 600 K and 300 K. Max efficiency?", ["50%", "100%", "30%", "200%"], 0,
      "eta = 1 - T_cold/T_hot = 1 - 300/600 = 0.5 = 50%. Temperatures must be absolute."),
    P("thr-p3", "A refrigerator removes 2,000 J from the cold space using 500 J of work. COP =", ["0.25", "4", "2500", "1.5"], 1,
      "COP = Q_cold/W_in = 2000/500 = 4. COP above 1 is normal for refrigeration."),
    P("thr-p4", "For an ideal gas at constant volume, boundary work done is:", ["P*dV", "zero", "mR*dT", "nonzero and positive"], 1,
      "Boundary work W = integral of P dV; at constant volume dV = 0, so W = 0.")
  ],
  "quiz": [
    P("thr-q1", "Temperatures in efficiency formulas must be in:", ["Celsius", "absolute (K or R)", "Fahrenheit", "any unit"], 1,
      "Carnot and gas-law relations require absolute temperature."),
    P("thr-q2", "Thermal efficiency of a power cycle is:", ["Q_in/W_net", "W_net/Q_in", "Q_out/Q_in", "1 + T_c/T_h"], 1,
      "eta = W_net/Q_in."),
    P("thr-q3", "In the two-phase region, quality x represents:", ["temperature", "mass fraction that is vapor", "pressure ratio", "entropy"], 1,
      "Quality is the fraction of the mixture mass that is vapor."),
    P("thr-q4", "A COP greater than 1 means:", ["the device is impossible", "more heat moved than work input", "100% efficiency", "a violation of the first law"], 1,
      "COP > 1 simply means the heat moved exceeds the work input - perfectly allowed.")
  ]
})

# 6.12 Heat Transfer
sections.append({
  "id": "heat-transfer", "title": "Heat Transfer", "questions": "5-8", "weight": "~7%", "priority": "High",
  "guide": {
    "overview": "The three modes - conduction, convection, radiation - plus fins, the thermal-resistance network, and basic heat exchangers. Treat it like a resistance circuit and it gets much easier.",
    "objectives": [
      "Apply Fourier's law for conduction.",
      "Use Newton's law of cooling for convection.",
      "Combine resistances in series/parallel (the thermal circuit).",
      "Understand radiation (Stefan-Boltzmann) and basic heat exchangers."
    ],
    "prereqs": "Algebra and the resistance-network analogy from circuits.",
    "watchOuts": [
      "Conduction resistance is L/(kA); convection is 1/(hA).",
      "Radiation uses absolute temperature to the 4th power.",
      "Keep area and thickness consistent."
    ]
  },
  "keyEquations": [
    {"name": "Conduction (Fourier)", "formula": "q = k*A*dT/L", "where": "Conduction"},
    {"name": "Convection", "formula": "q = h*A*dT", "where": "Convection"},
    {"name": "Radiation", "formula": "q = e*sigma*A*T^4", "where": "Radiation"},
    {"name": "Conduction resistance", "formula": "R = L/(kA)", "where": "Thermal Circuit"},
    {"name": "Convection resistance", "formula": "R = 1/(hA)", "where": "Thermal Circuit"}
  ],
  "lesson": [
    {"heading": "Three modes", "body": "Conduction moves heat through solids by molecular interaction: q = k*A*dT/L (Fourier's law). Convection moves heat between a surface and a moving fluid: q = h*A*dT (Newton's law of cooling). Radiation transfers heat as electromagnetic waves, no medium needed: q = e*sigma*A*T^4, with T absolute."},
    {"heading": "The thermal-resistance analogy", "body": "Heat flow is like current, temperature difference like voltage, and thermal resistance like electrical resistance: q = dT/R_total. Conduction resistance is R = L/(kA); convection resistance is R = 1/(hA). Layers in series add resistances - perfect for composite walls."},
    {"heading": "Fins and lumped systems", "body": "Fins add surface area to boost convective heat loss. A lumped-capacitance analysis (valid when the Biot number is small) treats an object as a single temperature that decays exponentially toward the surroundings."},
    {"heading": "Heat exchangers", "body": "Heat exchangers transfer heat between two fluid streams. The rate is q = U*A*dT_lm, where U is the overall heat transfer coefficient and dT_lm is the log-mean temperature difference. Counterflow arrangements are more effective than parallel flow."}
  ],
  "practiceProblems": [
    P("ht-p1", "A wall: k=0.5 W/m.K, A=10 m^2, L=0.2 m, dT=30 C. Heat rate?", ["75 W", "750 W", "7.5 W", "300 W"], 1,
      "q = k*A*dT/L = 0.5(10)(30)/0.2 = 150/0.2 = 750 W."),
    P("ht-p2", "Convection: h=25 W/m^2.K, A=2 m^2, dT=40 C. Heat rate?", ["2000 W", "200 W", "500 W", "1000 W"], 0,
      "q = h*A*dT = 25(2)(40) = 2000 W."),
    P("ht-p3", "Thermal resistance of conduction is:", ["1/(hA)", "L/(kA)", "kA/L", "hA"], 1,
      "Conduction resistance R = L/(kA)."),
    P("ht-p4", "Radiation heat transfer depends on temperature to the:", ["1st power", "2nd power", "4th power", "1/2 power"], 2,
      "Stefan-Boltzmann: q is proportional to T^4 (absolute temperature).")
  ],
  "quiz": [
    P("ht-q1", "Newton's law of cooling describes:", ["conduction", "convection", "radiation", "evaporation"], 1,
      "q = h*A*dT is convection (Newton's law of cooling)."),
    P("ht-q2", "Composite wall layers in series have resistances that:", ["add", "multiply", "average", "cancel"], 0,
      "Series thermal resistances add, just like series electrical resistors."),
    P("ht-q3", "Radiation requires:", ["a solid medium", "a fluid", "no medium", "vacuum only"], 2,
      "Radiation needs no medium - it transfers through vacuum."),
    P("ht-q4", "Counterflow heat exchangers are generally:", ["less effective", "more effective than parallel flow", "the same", "only for gases"], 1,
      "Counterflow maintains a more favorable temperature difference and is more effective.")
  ]
})

# 6.13 Measurements & Controls
sections.append({
  "id": "controls", "title": "Measurements, Instrumentation & Controls", "questions": "4-7", "weight": "~6%", "priority": "Medium",
  "guide": {
    "overview": "Sensors and measurement basics (error, calibration, signal conditioning) plus introductory control systems: block diagrams, feedback, transfer functions, and stability concepts.",
    "objectives": [
      "Distinguish accuracy, precision, resolution, and error types.",
      "Describe common sensors (thermocouples, strain gauges, pressure transducers).",
      "Reduce simple control block diagrams and find transfer functions.",
      "Understand open vs. closed loop and basic stability."
    ],
    "prereqs": "Algebra, basic differential equations, and circuits.",
    "watchOuts": [
      "Accuracy (closeness to true value) vs. precision (repeatability).",
      "Closed-loop transfer function = G/(1+GH) for negative feedback.",
      "Systematic error shifts the mean; random error spreads it."
    ]
  },
  "keyEquations": [
    {"name": "Closed-loop TF", "formula": "T = G/(1 + GH)", "where": "Controls"},
    {"name": "Percent error", "formula": "%err = (measured - true)/true * 100", "where": "Measurement"}
  ],
  "lesson": [
    {"heading": "Measurement fundamentals", "body": "Accuracy is how close a reading is to the true value; precision is how repeatable readings are. Resolution is the smallest detectable change. Systematic (bias) errors consistently shift results and can be calibrated out; random errors scatter around the mean and are reduced by averaging."},
    {"heading": "Common sensors", "body": "Thermocouples produce a voltage from a temperature difference (Seebeck effect). Strain gauges change resistance with deformation, usually read by a Wheatstone bridge. Pressure transducers, RTDs, and accelerometers each convert a physical quantity into an electrical signal that is then conditioned and digitized."},
    {"heading": "Control block diagrams", "body": "Systems are modeled as blocks with transfer functions in the Laplace domain. Series blocks multiply; parallel blocks add. For a negative-feedback loop with forward gain G and feedback H, the closed-loop transfer function is T = G/(1 + GH)."},
    {"heading": "Open vs. closed loop and stability", "body": "Open-loop control acts without measuring the output; closed-loop (feedback) control corrects based on the measured error, improving accuracy and disturbance rejection. A system is stable if its response stays bounded - in terms of poles, all must lie in the left half of the s-plane."}
  ],
  "practiceProblems": [
    P("ctl-p1", "A scale reads 10.1 kg for a true 10.0 kg mass, every time. This is:", ["random error", "systematic (bias) error", "high precision and accuracy", "resolution limit"], 1,
      "A consistent offset is a systematic/bias error - it can be calibrated out."),
    P("ctl-p2", "For G = 10 and H = 1 (negative feedback), the closed-loop gain is:", ["10", "0.5", "11", "10/11 (about 0.91)"], 3,
      "T = G/(1+GH) = 10/(1+10) = 10/11 = about 0.91."),
    P("ctl-p3", "A thermocouple measures temperature using the:", ["photoelectric effect", "Seebeck effect", "Hall effect", "Doppler effect"], 1,
      "Thermocouples rely on the Seebeck effect - a voltage from a temperature gradient across dissimilar metals."),
    P("ctl-p4", "Series-connected blocks in a block diagram have transfer functions that:", ["add", "multiply", "subtract", "divide"], 1,
      "Cascaded (series) blocks multiply their transfer functions.")
  ],
  "quiz": [
    P("ctl-q1", "Precision refers to:", ["closeness to true value", "repeatability of readings", "smallest division", "bias"], 1,
      "Precision is repeatability; accuracy is closeness to the true value."),
    P("ctl-q2", "Closed-loop control uses:", ["no measurement", "feedback of the output", "only feedforward", "manual adjustment"], 1,
      "Closed-loop control feeds the measured output back to correct error."),
    P("ctl-q3", "A strain gauge is typically read with a:", ["thermocouple", "Wheatstone bridge", "tachometer", "manometer"], 1,
      "Small resistance changes are measured with a Wheatstone bridge."),
    P("ctl-q4", "Averaging many readings reduces:", ["systematic error", "random error", "resolution", "bias"], 1,
      "Averaging reduces random error; it does not remove systematic bias.")
  ]
})

# 6.14 Mechanical Design
sections.append({
  "id": "mech-design", "title": "Mechanical Design & Analysis", "questions": "9-14", "weight": "~10%", "priority": "Very High",
  "guide": {
    "overview": "Designing components to carry load safely: factor of safety, static and fatigue failure theories, stress concentrations, and machine elements (bolts, welds, springs, gears, bearings, shafts). Synthesizes statics, mechanics of materials, and materials.",
    "objectives": [
      "Apply factor of safety to allowable stress.",
      "Use failure theories (max shear / distortion energy) for static loading.",
      "Account for stress concentration and fatigue (endurance limit).",
      "Size basic machine elements (bolts, springs, gears, shafts)."
    ],
    "prereqs": "Mechanics of Materials and Material Properties.",
    "watchOuts": [
      "Apply stress-concentration factors at notches, holes, and fillets.",
      "Fatigue strength is well below static strength under cyclic load.",
      "Factor of safety = strength / actual stress (keep it consistent)."
    ]
  },
  "keyEquations": [
    {"name": "Factor of safety", "formula": "FS = strength / actual stress", "where": "Design"},
    {"name": "Max stress at notch", "formula": "sigma_max = Kt * sigma_nominal", "where": "Stress Concentration"},
    {"name": "Spring force", "formula": "F = k*x", "where": "Springs"},
    {"name": "Helical spring rate", "formula": "k = G*d^4 / (8*D^3*N)", "where": "Springs"}
  ],
  "lesson": [
    {"heading": "Factor of safety", "body": "Design components so the material strength comfortably exceeds the actual stress: FS = strength/actual stress, or the allowable stress = strength/FS. Choose FS based on uncertainty, consequences of failure, and load type. A higher factor of safety means a more conservative (heavier, costlier) design."},
    {"heading": "Static failure theories", "body": "For ductile materials, the distortion-energy (von Mises) theory and the maximum-shear-stress theory predict yielding under combined loading. For brittle materials, the maximum-normal-stress theory applies. Compute the relevant equivalent stress and compare it to the yield (or ultimate) strength."},
    {"heading": "Stress concentration and fatigue", "body": "Geometric discontinuities - holes, fillets, notches, keyways - amplify local stress by a factor Kt: sigma_max = Kt * sigma_nominal. Under cyclic loading this drives fatigue. Steels show an endurance limit (stress below which infinite life is possible); designing below it, with modifying factors, prevents fatigue failure."},
    {"heading": "Machine elements", "body": "Bolts are sized for tensile and shear stress and preload. Springs follow F = k*x with helical spring rate k = G*d^4/(8*D^3*N). Gears transmit torque through meshing teeth with a velocity ratio set by tooth counts. Shafts carry combined bending and torsion - designed using a combined-stress or fatigue criterion."}
  ],
  "practiceProblems": [
    P("md-p1", "A part's material yields at 250 MPa and the actual stress is 100 MPa. Factor of safety?", ["2.5", "0.4", "150", "350"], 0,
      "FS = strength/actual stress = 250/100 = 2.5."),
    P("md-p2", "A hole gives Kt = 2.5 in a member with nominal stress 80 MPa. Peak stress?", ["32 MPa", "200 MPa", "82.5 MPa", "160 MPa"], 1,
      "sigma_max = Kt * sigma_nominal = 2.5 * 80 = 200 MPa at the edge of the hole."),
    P("md-p3", "A spring with k = 500 N/m is compressed 0.04 m. Force?", ["20 N", "12,500 N", "0.08 N", "504 N"], 0,
      "F = k*x = 500 * 0.04 = 20 N."),
    P("md-p4", "The endurance limit is relevant to:", ["static tension only", "fatigue (cyclic) loading", "thermal stress", "buckling"], 1,
      "The endurance limit is the cyclic stress below which steels can have effectively infinite fatigue life.")
  ],
  "quiz": [
    P("md-q1", "A higher factor of safety generally yields a design that is:", ["lighter", "more conservative", "cheaper", "less reliable"], 1,
      "Higher FS means more margin - a more conservative (and usually heavier/costlier) design."),
    P("md-q2", "Von Mises (distortion energy) theory predicts failure of:", ["brittle materials", "ductile materials", "fluids", "composites only"], 1,
      "The distortion-energy theory is used for ductile material yielding."),
    P("md-q3", "Stress concentration factor Kt is largest at:", ["uniform sections", "notches, holes, fillets", "the centroid", "supports"], 1,
      "Geometric discontinuities concentrate stress, raising Kt."),
    P("md-q4", "Helical spring rate increases most with:", ["more coils", "larger wire diameter d", "larger coil diameter D", "lower G"], 1,
      "k = G*d^4/(8*D^3*N) - the wire diameter d to the 4th power dominates.")
  ]
})

def q(qid, prompt, choices, ans, exp):
    return P(qid, prompt, choices, ans, exp)

practice_tests = [
  {
    "id": "pt1", "title": "Practice Test 1 - Mixed Fundamentals", "time": "30 min",
    "questions": [
      q("pt1-1","A 8 V source drives a 2 Ohm resistor. Power dissipated?",["16 W","32 W","4 W","8 W"],1,"P = V^2/R = 64/2 = 32 W."),
      q("pt1-2","Mean of 2, 4, 6, 8, 10:",["5","6","30","4"],1,"(2+4+6+8+10)/5 = 30/5 = 6."),
      q("pt1-3","A simply supported 8 m beam has a 400 N load at midspan. Each reaction?",["100 N","200 N","400 N","800 N"],1,"By symmetry each support carries half: 200 N."),
      q("pt1-4","sigma = P/A for 6000 N over 3e-4 m^2:",["20 MPa","2 MPa","200 MPa","0.02 MPa"],0,"6000/3e-4 = 2e7 Pa = 20 MPa."),
      q("pt1-5","Gauge pressure at 10 m water depth:",["98.1 kPa","9.81 kPa","981 kPa","100 kPa"],0,"P = rho*g*h = 1000(9.81)(10) = 98,100 Pa = about 98.1 kPa."),
      q("pt1-6","Carnot efficiency between 800 K and 400 K:",["50%","40%","100%","25%"],0,"1 - 400/800 = 0.5 = 50%."),
      q("pt1-7","Derivative of 4x^3:",["12x^2","4x^2","x^4","12x"],0,"d/dx 4x^3 = 12x^2."),
      q("pt1-8","FS for 300 MPa strength and 120 MPa stress:",["2.5","0.4","180","2.0"],0,"300/120 = 2.5."),
      q("pt1-9","Two 4 Ohm resistors in parallel:",["8 Ohm","2 Ohm","4 Ohm","1 Ohm"],1,"4*4/(4+4) = 16/8 = 2 Ohm."),
      q("pt1-10","F = ma for m = 5 kg, a = 4 m/s^2:",["20 N","1.25 N","9 N","0.8 N"],0,"F = 5*4 = 20 N.")
    ]
  },
  {
    "id": "pt2", "title": "Practice Test 2 - Mechanical Core", "time": "30 min",
    "questions": [
      q("pt2-1","Continuity: pipe area drops from 0.2 to 0.1 m^2, V1 = 3 m/s. V2?",["1.5 m/s","6 m/s","3 m/s","9 m/s"],1,"A1*V1=A2*V2, so V2 = 0.2*3/0.1 = 6 m/s."),
      q("pt2-2","Conduction q for k=2, A=4 m^2, dT=20, L=0.1 m:",["1600 W","160 W","16 W","320 W"],0,"q = k*A*dT/L = 2*4*20/0.1 = 160/0.1 = 1600 W."),
      q("pt2-3","KE of 800 kg car at 30 m/s:",["360,000 J","24,000 J","12,000 J","720,000 J"],0,"0.5*800*30^2 = 0.5*800*900 = 360,000 J."),
      q("pt2-4","Bending stress sigma = Mc/I; doubling c (others equal):",["halves sigma","doubles sigma","no change","quarters sigma"],1,"sigma is proportional to c, so doubling c doubles stress."),
      q("pt2-5","First law: Q=800 J in, W=300 J out. dU?",["1100 J","500 J","-500 J","300 J"],1,"dU = Q - W = 800 - 300 = 500 J."),
      q("pt2-6","Re = rho*V*D/mu; Re = 5000 indicates:",["laminar","turbulent","static","transitional only"],1,"Re above about 4000 in pipes is turbulent."),
      q("pt2-7","Spring k=1000 N/m stretched 0.02 m. Force?",["20 N","50 N","2 N","1020 N"],0,"F = k*x = 1000*0.02 = 20 N."),
      q("pt2-8","Present worth of $2000 in 3 yr at 10%:",["$1503","$1818","$2662","$1400"],0,"P = 2000/1.1^3 = 2000/1.331 = $1503."),
      q("pt2-9","Moment of 80 N at 0.25 m perpendicular:",["20 N*m","320 N*m","2 N*m","80 N*m"],0,"M = F*d = 80*0.25 = 20 N*m."),
      q("pt2-10","COP of fridge: 3000 J removed, 750 J work:",["0.25","4","2250","3.75"],1,"COP = 3000/750 = 4.")
    ]
  }
]

course = {
  "id": "fe-mechanical",
  "title": "FE Mechanical",
  "subtitle": "Fundamentals of Engineering - Computer-Based Test",
  "tagline": "Everything you need to pass the FE Mechanical exam: structured lessons, worked practice, quizzes, and full practice tests across all 14 knowledge areas.",
  "examFacts": {
    "questions": 110, "hours": 6, "areas": 14, "handbook": "NCEES FE Reference Handbook",
    "passNote": "No fixed passing percentage - NCEES uses a criterion-referenced cut score (community estimates around 50-60% correct). No penalty for wrong answers, so never leave a blank."
  },
  "priceMonthly": 10,
  "priceOneTime": 100,
  "sections": sections,
  "practiceTests": practice_tests
}

catalog = {
  "courses": [
    {"id": "fe-mechanical", "title": "FE Mechanical", "status": "available",
      "blurb": "Full prep for the FE Mechanical CBT - 14 knowledge areas, hundreds of practice questions.",
      "color": "#2563eb"},
    {"id":"fe-civil","title":"FE Civil","status":"coming-soon","blurb":"Structural, geotechnical, water resources, transportation, and more.","color":"#0891b2"},
    {"id":"fe-electrical","title":"FE Electrical & Computer","status":"coming-soon","blurb":"Circuits, electronics, signals, and computer systems.","color":"#7c3aed"},
    {"id":"pe-mechanical","title":"PE Mechanical","status":"coming-soon","blurb":"The next step after the FE - professional licensure prep.","color":"#dc2626"}
  ]
}

out_dir = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "course-fe-mechanical.json"), "w") as f:
    json.dump(course, f, indent=2, ensure_ascii=False)
with open(os.path.join(out_dir, "catalog.json"), "w") as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

nq = sum(len(s["practiceProblems"]) + len(s["quiz"]) for s in sections) + sum(len(t["questions"]) for t in practice_tests)
print(f"Sections: {len(sections)}")
print(f"Total questions (practice+quiz+tests): {nq}")
print("Wrote data/course-fe-mechanical.json and data/catalog.json")
