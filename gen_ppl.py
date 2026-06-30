#!/usr/bin/env python3
import json, os
from gen_ppl_svgs import *

def P(pid, prompt, choices, answer, explanation):
    return {"id": pid, "prompt": prompt, "choices": choices, "answer": answer, "explanation": explanation}

FAA_LINKS_CORE = [
  {"label":"FAA — Become a Private Pilot","url":"https://www.faa.gov/pilots/become/rec_private","note":"the official starting point"},
  {"label":"Pilot's Handbook of Aeronautical Knowledge (PHAK)","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak","note":"free FAA-H-8083-25 ground-school bible"},
  {"label":"Airplane Flying Handbook (FAA-H-8083-3)","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/airplane_handbook","note":"how the maneuvers are flown"},
  {"label":"Private Pilot ACS (FAA-S-ACS-6)","url":"https://www.faa.gov/training_testing/testing/acs","note":"exactly what the written & checkride test"},
]

sections = []

# 1. PATH / ROADMAP
sections.append({
  "id":"roadmap","title":"Your Path to the Certificate","questions":"—","weight":"Start here","priority":"Read first",
  "factsLabel":"Part 61 minimums (§ 61.109 / 61.103)",
  "conceptsLabel":"The steps, in order",
  "guide":{
    "overview":"This is the map from your first lesson to a private pilot certificate in your wallet. The path is the same everywhere in the U.S.: meet the basic eligibility, get a medical and student pilot certificate, learn the knowledge (and pass the written), build flight experience including solo and cross-country, then pass the checkride. Under 14 CFR Part 61 the minimum is 40 flight hours — most people finish in 55–75.",
    "objectives":[
      "Know the milestones from discovery flight to checkride and the order they happen in.",
      "Know the Part 61 minimum experience requirements and what 'minimum' really means.",
      "Get your medical and student pilot certificate set up correctly the first time.",
      "Understand how the written test, the ACS, and the checkride fit together."
    ],
    "prereqs":"None — this is day one. Be at least 16 to solo and 17 to earn the certificate, and able to read, speak, and understand English.",
    "watchOuts":[
      "'40 hours' is a legal minimum, not a typical finish time — budget for ~60–75.",
      "Get your medical early; a deferral can stall you for months.",
      "Your written-test result is valid for 24 calendar months — don't take it too early.",
      "Fly consistently (2–3×/week). Long gaps mean re-learning and more cost."
    ]
  },
  "keyEquations":[
    {"name":"Total flight time","formula":"40 hours minimum","where":"§ 61.109(a)"},
    {"name":"Dual (with instructor)","formula":"20 hours minimum","where":"§ 61.109(a)"},
    {"name":"Solo flight","formula":"10 hours minimum","where":"§ 61.109(a)"},
    {"name":"Cross-country training","formula":"3 hours dual","where":"§ 61.109(a)(2)"},
    {"name":"Night training","formula":"3 hrs incl. 100 NM XC + 10 T/O & ldg","where":"§ 61.109(a)(2)"},
    {"name":"Instrument training","formula":"3 hours (basic attitude)","where":"§ 61.109(a)(3)"},
    {"name":"Solo cross-country","formula":"5 hrs incl. one 150 NM, 3 stops","where":"§ 61.109(a)(5)"},
    {"name":"Test-prep with instructor","formula":"3 hrs within 2 calendar months of checkride","where":"§ 61.109(a)(4)"},
  ],
  "lesson":[
    {"heading":"The whole journey at a glance","body":"There are seven milestones: (1) a discovery flight to make sure you love it, (2) a medical certificate and student pilot certificate, (3) ground school and the FAA knowledge (written) test, (4) pre-solo training, (5) your first solo, (6) cross-country and night experience, and (7) the checkride — an oral exam plus a practical flight test. You can overlap ground school with flight training; most people study at home while flying a few times a week.","diagram":ROADMAP},
    {"heading":"Step 1 — Discovery flight & choosing a school","body":"Book an introductory 'discovery flight' at a local school (for you, that's the KHYI area). Decide between a Part 61 school (flexible, 40-hour minimum) and a Part 141 school (structured syllabus, 35-hour minimum). For most part-time students Part 61 is the norm. Pick a school with available instructors and aircraft — scheduling, not talent, is what usually slows people down."},
    {"heading":"Step 2 — Medical & student pilot certificate","body":"Schedule a third-class medical with an FAA Aviation Medical Examiner (AME) using MedXPress. Separately, apply for your student pilot certificate through IACRA (iacra.faa.gov) with your instructor; it's processed by TSA and mailed in a couple of weeks. You need the student certificate before you solo, so start both early. If you've held an FAA medical since July 2006, BasicMed is an alternative for later flying."},
    {"heading":"Step 3 — Knowledge (written) test","body":"Study the knowledge areas in this course (regulations, airspace, weather, aerodynamics, navigation, performance, aeromedical). Get an instructor or online-course endorsement, then take the FAA Private Pilot Airplane knowledge test at a PSI testing center: 65 questions (60 scored), 70% to pass, 2 hours. Your passing result is valid for 24 calendar months, so time it to land a few months before your checkride."},
    {"heading":"Steps 4–6 — Solo, cross-country, and night","body":"You'll train pattern work and maneuvers until your instructor endorses you to solo. After solo you build the required solo time, including a 150-NM cross-country with full-stop landings at three airports, plus night training with a 100-NM night cross-country and 10 night takeoffs and landings. This is where the 40-hour minimum quietly becomes 60+ for most people."},
    {"heading":"Step 7 — The checkride","body":"When you meet all the experience requirements and your instructor signs you off, you take the practical test with a Designated Pilot Examiner (DPE). It's an oral exam followed by a flight, both graded against the Airman Certification Standards (ACS). Pass, and you walk away a certificated private pilot — able to carry passengers and fly nationwide in day and night VFR."},
  ],
  "links":[
    {"label":"14 CFR 61.109 — Aeronautical experience","url":"https://www.ecfr.gov/current/title-14/chapter-I/subchapter-D/part-61/subpart-E/section-61.109","note":"the exact hour requirements"},
    {"label":"14 CFR 61.103 — Eligibility","url":"https://www.law.cornell.edu/cfr/text/14/61.103","note":"age, language, basic rules"},
    {"label":"IACRA — student pilot application","url":"https://iacra.faa.gov","note":"create your FTN and apply"},
    {"label":"FAA Medical Certification (find an AME, MedXPress)","url":"https://www.faa.gov/pilots/medical_certification","note":"schedule your third-class medical"},
    {"label":"BasicMed","url":"https://www.faa.gov/licenses_certificates/airmen_certification/basic_med","note":"medical alternative once eligible"},
    {"label":"EAA — Learn to Fly","url":"https://www.eaa.org/eaa/learn-to-fly","note":"friendly step-by-step + scholarships"},
  ] + FAA_LINKS_CORE,
  "practiceProblems":[
    P("rm-p1","What is the minimum total flight time for a private pilot certificate (airplane, Part 61)?",["20 hours","35 hours","40 hours","60 hours"],2,
      "Part 61 (§61.109) requires at least 40 hours total. Part 141 allows 35. Most students actually need 55–75."),
    P("rm-p2","Before you can fly solo, you must have a:",["Commercial certificate","Student pilot certificate and a solo endorsement","Third-class medical only","Passing checkride"],1,
      "You need a student pilot certificate (via IACRA) plus your instructor's solo endorsement; the medical is also required to act as PIC."),
    P("rm-p3","An FAA knowledge (written) test result is valid for:",["6 calendar months","12 calendar months","24 calendar months","It never expires"],2,
      "The written is valid for 24 calendar months — you must pass the checkride within that window."),
    P("rm-p4","The minimum solo cross-country requirement includes one flight of at least:",["50 NM total","100 NM total","150 NM total with landings at 3 points","250 NM total"],2,
      "§61.109(a)(5): one solo XC of 150 NM total, full-stop landings at three points, with one segment over 50 NM between takeoff and landing."),
  ],
  "quiz":[
    P("rm-q1","Minimum age to be issued a private pilot certificate (airplane):",["15","16","17","18"],2,"17 for the certificate; you can solo an airplane at 16."),
    P("rm-q2","The FAA Private Pilot Airplane knowledge test passing score is:",["60%","70%","75%","80%"],1,"70% — about 42 of 60 scored questions."),
    P("rm-q3","Minimum dual (instructor) flight training under Part 61 is:",["10 hours","15 hours","20 hours","40 hours"],2,"§61.109(a): at least 20 hours of training and 10 hours solo."),
    P("rm-q4","Which document set defines what the written and checkride test?",["The AIM","The ACS","The POH","NOTAMs"],1,"The Airman Certification Standards (ACS) align the knowledge test and the practical test."),
  ]
})

# 2. PRINCIPLES OF FLIGHT
sections.append({
  "id":"aerodynamics","title":"Principles of Flight","questions":"~","weight":"Core","priority":"High",
  "factsLabel":"Key relationships",
  "guide":{
    "overview":"Why an airplane flies, stays controllable, and stalls. You'll learn the four forces, how lift is produced and controlled by angle of attack, why a wing stalls, and how bank angle multiplies load on the airplane and on you.",
    "objectives":["Explain the four forces and their balance in steady flight.","Relate lift to angle of attack and recognize the critical angle.","Explain why an airplane stalls and how to recover.","Describe how load factor grows with bank angle."],
    "prereqs":"None.",
    "watchOuts":["A wing stalls at a critical angle of attack — at ANY airspeed or attitude.","Stall speed increases with bank angle (load factor).","Lift and weight balance only in level, unaccelerated flight.","Don't confuse angle of attack with pitch attitude."]
  },
  "keyEquations":[
    {"name":"Steady level flight","formula":"Lift = Weight, Thrust = Drag","where":"PHAK ch. 5"},
    {"name":"Load factor in a level turn","formula":"n = 1 / cos(bank)","where":"PHAK"},
    {"name":"Stall speed vs. load","formula":"Vs grows with sqrt(load factor)","where":"PHAK"},
    {"name":"60° bank, level","formula":"n = 2.0 G (stall speed +41%)","where":"PHAK"},
  ],
  "lesson":[
    {"heading":"The four forces","body":"Four forces act on an airplane: lift (up), weight (down), thrust (forward), and drag (back). In steady, level, unaccelerated flight lift equals weight and thrust equals drag. Change any one and the airplane accelerates until a new balance is reached — add thrust and it climbs or speeds up; raise the nose and lift momentarily exceeds weight.","diagram":FOUR_FORCES},
    {"heading":"Lift and angle of attack","body":"Lift comes from the wing deflecting air downward; it depends on airspeed, air density, wing area, and angle of attack (the angle between the wing's chord line and the oncoming air). For a given speed, more angle of attack means more lift — up to a point. Pilots control angle of attack with the elevator."},
    {"heading":"Stalls — the critical angle of attack","body":"Beyond the critical angle of attack (about 15–18° for typical trainers) airflow separates from the top of the wing and lift drops sharply — a stall. Crucially, a wing can stall at any airspeed and any attitude if that angle is exceeded, such as in an aggressive turn. Recovery is the same every time: reduce angle of attack (lower the nose), add power, and level the wings."},
    {"heading":"Load factor and turns","body":"In a turn the wings must support more than the airplane's weight, so load factor (G) rises. At 60° of bank in level flight the load factor is 2.0 G — the airplane effectively weighs twice as much and its stall speed increases about 41%. This is why steep turns and abrupt maneuvering near stall speed are dangerous.","diagram":LOAD_FACTOR},
  ],
  "links":[
    {"label":"PHAK Ch. 5 — Aerodynamics of Flight","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak","note":"the source chapter"},
  ]+FAA_LINKS_CORE[:2],
  "practiceProblems":[
    P("aero-p1","In steady, level, unaccelerated flight, lift is:",["Greater than weight","Equal to weight","Less than weight","Equal to thrust"],1,
      "Lift = weight and thrust = drag in steady level flight."),
    P("aero-p2","A wing always stalls when it exceeds its:",["Never-exceed speed","Critical angle of attack","Maneuvering speed","Maximum weight"],1,
      "Stalls happen at the critical angle of attack, regardless of airspeed or attitude."),
    P("aero-p3","At 60° of bank in level flight, load factor is about:",["1.0 G","1.4 G","2.0 G","4.0 G","" ][:4],2,
      "n = 1/cos(60°) = 1/0.5 = 2.0 G; stall speed rises about 41%."),
    P("aero-p4","The correct first action to recover from a stall is to:",["Pull back on the yoke","Reduce angle of attack (lower the nose)","Add full flaps","Raise the nose and add power"],1,
      "Reduce the angle of attack first (lower the nose), then add power and level the wings."),
  ],
  "quiz":[
    P("aero-q1","Angle of attack is the angle between the chord line and the:",["Horizon","Relative wind","Longitudinal axis","Flight path of the tail"],1,"It's measured against the relative wind (oncoming air)."),
    P("aero-q2","Increasing bank angle in level flight causes stall speed to:",["Decrease","Stay the same","Increase","Become zero"],2,"Higher load factor raises stall speed."),
    P("aero-q3","Which controls angle of attack directly?",["Throttle","Rudder","Elevator","Flaps"],2,"The elevator changes pitch and thus angle of attack."),
    P("aero-q4","Thrust is produced by the:",["Wings","Propeller/engine","Elevator","Rudder"],1,"The powerplant/propeller produces thrust."),
  ]
})

# 3. AIRCRAFT SYSTEMS & INSTRUMENTS
sections.append({
  "id":"systems","title":"Aircraft Systems & Instruments","questions":"~","weight":"Core","priority":"High",
  "factsLabel":"Quick reference",
  "guide":{
    "overview":"What the major systems do and how the flight instruments get their information — so you can spot a failure and respond. Covers the powerplant, fuel, electrical, and the pitot-static and gyroscopic instruments.",
    "objectives":["Describe the basic powerplant, fuel, and electrical systems.","Explain the pitot-static instruments and their failure modes.","Explain the gyroscopic instruments and the magnetic compass.","Identify the six primary flight instruments (the 'six-pack')."],
    "prereqs":"None.",
    "watchOuts":["A blocked pitot tube freezes the airspeed indicator; a blocked static port affects ALT, ASI, and VSI.","The magnetic compass has predictable turning and acceleration errors (ANDS / UNOS).","Carburetor ice can occur even on warm days — use carb heat.","Know your aircraft's specific fuel quantity and electrical layout from the POH."]
  },
  "keyEquations":[
    {"name":"Pitot-static instruments","formula":"ASI, Altimeter, VSI","where":"PHAK ch. 8"},
    {"name":"Gyroscopic instruments","formula":"Attitude, Heading, Turn coord.","where":"PHAK ch. 8"},
    {"name":"Compass acceleration error","formula":"ANDS (Acc-North, Dec-South)","where":"PHAK"},
    {"name":"Compass turning error","formula":"UNOS (Undershoot N, Overshoot S)","where":"PHAK"},
  ],
  "lesson":[
    {"heading":"Powerplant, fuel, and electrical","body":"Trainers use a four-stroke piston engine (intake, compression, power, exhaust) turning a propeller. Fuel flows from the tanks to the engine by gravity (high-wing) or pump (low-wing); the mixture control adjusts the fuel-air ratio for altitude. A belt-driven alternator charges the battery and powers the electrical bus; the battery starts the engine and is a backup. The magnetos make their own spark independent of the battery — which is why the engine keeps running if the alternator fails."},
    {"heading":"Pitot-static instruments","body":"Three instruments run on air pressure. The airspeed indicator compares ram air (pitot tube) to static pressure. The altimeter and vertical speed indicator use static pressure only. Because they share the static system, a blocked static port corrupts all three. Knowing which blockage causes which error is classic checkride material.","diagram":PITOT_STATIC},
    {"heading":"Gyroscopic instruments and the compass","body":"The attitude indicator, heading indicator, and turn coordinator use spinning gyros (vacuum- or electrically-driven). The magnetic compass needs no power but lies during turns and acceleration: remember ANDS (Accelerate-North, Decelerate-South) and UNOS (Undershoot North, Overshoot South) in the Northern Hemisphere.","diagram":SIXPACK},
  ],
  "links":[
    {"label":"PHAK Ch. 7–8 — Systems & Flight Instruments","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak","note":"systems + instruments"},
  ]+FAA_LINKS_CORE[:1],
  "practiceProblems":[
    P("sys-p1","A blocked static port will affect which instruments?",["Airspeed only","Altimeter, VSI, and airspeed","Attitude indicator only","Heading indicator"],1,
      "The altimeter, VSI, and airspeed indicator all use static pressure."),
    P("sys-p2","If the alternator fails in flight, the engine:",["Stops immediately","Keeps running because magnetos are self-powered","Loses fuel flow","Loses oil pressure"],1,
      "Magnetos generate their own ignition spark, so the engine runs even with total electrical failure."),
    P("sys-p3","Carburetor heat is used to:",["Increase power","Prevent or remove carb ice","Lean the mixture","Cool the engine"],1,
      "Carb heat melts/prevents induction icing; expect a small RPM drop when applied."),
    P("sys-p4","The instrument that uses BOTH pitot and static pressure is the:",["Altimeter","Vertical speed indicator","Airspeed indicator","Heading indicator"],2,
      "The airspeed indicator compares ram (pitot) pressure to static pressure."),
  ],
  "quiz":[
    P("sys-q1","The 'six-pack' top row, left to right, is:",["ALT, AI, ASI","ASI, AI, ALT","AI, ASI, VSI","TC, HI, VSI"],1,"Airspeed, Attitude, Altimeter on top; Turn coordinator, Heading, VSI on the bottom."),
    P("sys-q2","Compass acceleration error in the Northern Hemisphere follows:",["UNOS","ANDS","LCDH","ARROW"],1,"Accelerate-North, Decelerate-South (ANDS) on east/west headings."),
    P("sys-q3","Most gyroscopic instruments in a trainer are driven by:",["The pitot tube","A vacuum (or electric) system","The fuel pump","Static pressure"],1,"Vacuum-driven (some electric) gyros."),
    P("sys-q4","The mixture control adjusts:",["Propeller pitch","Fuel-to-air ratio","Flap position","Electrical load"],1,"It leans/enrichens the fuel-air mixture for altitude."),
  ]
})

# 4. WEATHER
sections.append({
  "id":"weather","title":"Weather","questions":"~","weight":"Core","priority":"High",
  "guide":{
    "overview":"Weather is the number-one go/no-go decision for VFR pilots. Learn the atmosphere basics, fronts, clouds and stability, the hazards (thunderstorms, icing, fog, wind shear), and how to read a METAR and TAF.",
    "objectives":["Explain pressure, temperature, and moisture's effect on flight.","Distinguish cold and warm fronts and their weather.","Decode a METAR and TAF.","Identify major hazards and where to find weather briefings."],
    "prereqs":"None.",
    "watchOuts":["Thunderstorms: avoid by at least 20 NM; never fly under or through.","Freezing rain/visible moisture near 0°C means structural icing risk.","A small temperature/dew-point spread means fog or low ceilings are likely.","Always get a standard weather briefing (1800wxbrief / aviationweather.gov)."]
  },
  "keyEquations":[
    {"name":"Standard atmosphere","formula":"15°C & 29.92 inHg at sea level","where":"PHAK ch. 12"},
    {"name":"Temperature lapse rate","formula":"~2°C per 1,000 ft","where":"PHAK"},
    {"name":"Fog risk","formula":"Temp–dewpoint spread small","where":"PHAK"},
    {"name":"Thunderstorm avoidance","formula":"At least 20 NM","where":"AIM"},
  ],
  "lesson":[
    {"heading":"The atmosphere and stability","body":"The standard atmosphere is 15°C and 29.92 inHg at sea level, cooling about 2°C per 1,000 ft. Air that resists vertical motion is stable (smooth air, stratus clouds, poor visibility); unstable air rises freely (bumps, cumulus clouds, good visibility, and showers). Moisture plus lifting plus instability is the recipe for thunderstorms."},
    {"heading":"Fronts","body":"A front is the boundary between two air masses. A cold front pushes under warm air steeply, producing a narrow band of strong weather that passes quickly. A warm front slides up and over cold air gently, producing a wide area of low ceilings, rain, and reduced visibility that lingers. Wind shifts and pressure changes mark a frontal passage.","diagram":FRONTS},
    {"heading":"Hazards","body":"Thunderstorms (avoid by 20 NM), structural icing (visible moisture near or below freezing), fog (small temperature/dew-point spread), and wind shear (especially near fronts and thunderstorms) are the big killers. As a VFR pilot your defense is information and margins — when in doubt, don't go."},
    {"heading":"METARs and TAFs","body":"A METAR is a current observation; a TAF is a forecast for a 5-SM radius of an airport. Read them left to right: station, time (Zulu), wind, visibility, weather, sky condition (FEW/SCT/BKN/OVC with heights in hundreds of feet), temperature/dew point, and altimeter. 'KHYI 151853Z 18010KT 10SM FEW050 30/18 A2992' means wind 180° at 10 kt, 10 SM visibility, few clouds at 5,000 ft, 30°C/18°C, altimeter 29.92."},
  ],
  "links":[
    {"label":"aviationweather.gov — official briefings, METAR/TAF","url":"https://aviationweather.gov","note":"current weather + forecasts"},
    {"label":"1800wxbrief.com (Leidos) — standard briefing","url":"https://www.1800wxbrief.com","note":"file & brief"},
    {"label":"PHAK Ch. 12–13 — Weather Theory & Services","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak","note":"the weather chapters"},
  ],
  "practiceProblems":[
    P("wx-p1","In the standard atmosphere, sea-level pressure and temperature are:",["29.92 inHg and 15°C","30.00 inHg and 20°C","29.92 inHg and 0°C","28.00 inHg and 15°C"],0,
      "Standard: 29.92 inHg and 15°C, lapse ~2°C/1,000 ft."),
    P("wx-p2","A small spread between temperature and dew point indicates:",["High thunderstorm risk","Likely fog or low ceilings","Strong winds aloft","Stable, clear skies"],1,
      "When temperature and dew point are close, the air is near saturation — fog/low clouds."),
    P("wx-p3","Compared to a warm front, a cold front typically brings weather that is:",["Widespread and slow-moving","Narrow and fast-moving","Always clear","Only at night"],1,
      "Cold fronts produce a narrow, intense band that passes quickly; warm fronts are wide and lingering."),
    P("wx-p4","In a METAR, 'BKN025' means:",["Broken clouds at 250 ft","Broken clouds at 2,500 ft","Visibility 25 SM","Wind 25 kt"],1,
      "Cloud heights are in hundreds of feet AGL, so 025 = 2,500 ft; BKN = broken (5–7 oktas)."),
  ],
  "quiz":[
    P("wx-q1","You should avoid thunderstorms by at least:",["5 NM","10 NM","20 NM","2 NM"],2,"At least 20 NM; severe turbulence and hail extend well outside the cloud."),
    P("wx-q2","Stable air is typically associated with:",["Cumulus clouds and good visibility","Stratus clouds and poor visibility","Thunderstorms","Clear skies always"],1,"Stable air → stratiform clouds, smooth air, often poor visibility."),
    P("wx-q3","A TAF is a forecast valid for about a:",["50 NM radius","5 SM radius of the airport","Entire state","1 NM radius"],1,"A TAF covers roughly a 5-statute-mile radius of the station."),
    P("wx-q4","'A2992' in a METAR is the:",["Temperature","Altimeter setting (29.92 inHg)","Wind","Visibility"],1,"Altimeter setting in inches of mercury."),
  ]
})

# 5. AIRSPACE & VFR MINIMUMS
sections.append({
  "id":"airspace","title":"Airspace & VFR Weather Minimums","questions":"~","weight":"Core","priority":"Very High",
  "guide":{
    "overview":"Where you can fly, who you must talk to, and the visibility and cloud-clearance rules that keep VFR traffic safe. This is one of the most-tested areas on the written and a checkride favorite.",
    "objectives":["Identify Class A, B, C, D, E, and G airspace and entry requirements.","State VFR weather minimums by airspace.","Recognize special use airspace.","Know equipment and communication requirements (e.g., Mode C, ADS-B)."],
    "prereqs":"None.",
    "watchOuts":["Class B requires an explicit 'cleared into the Bravo' before entry.","Mode C / ADS-B Out is required within 30 NM of a Class B (the 'Mode C veil').","Class G minimums change at 1,200 ft AGL and at night.","Memorize the 3-152 cloud clearance pattern."]
  },
  "factsLabel":"VFR minimums (quick)",
  "keyEquations":[
    {"name":"Class B","formula":"3 SM vis, clear of clouds","where":"§ 91.155"},
    {"name":"Class C/D/E (<10,000 MSL)","formula":"3 SM, 152 cloud clearance","where":"§ 91.155"},
    {"name":"Class G day (≤1,200 AGL)","formula":"1 SM, clear of clouds","where":"§ 91.155"},
    {"name":"'152' clearance","formula":"1,000 above / 500 below / 2,000 horiz.","where":"§ 91.155"},
  ],
  "lesson":[
    {"heading":"The classes, in a picture","body":"U.S. airspace runs from Class A (18,000 ft MSL and up, IFR only) down to Class G (uncontrolled). Class B surrounds the busiest airports (upside-down wedding cake, explicit clearance required), Class C is moderate (two-way radio + Mode C/ADS-B), Class D is a control-tower airport (two-way radio), Class E is controlled airspace that isn't A/B/C/D, and Class G is uncontrolled. As a student/private pilot you'll live mostly in D, E, and G.","diagram":AIRSPACE},
    {"heading":"VFR weather minimums","body":"Each class sets a minimum flight visibility and how far you must stay from clouds. The workhorse pattern for Class C, D, and E below 10,000 ft is '3-152': 3 SM visibility, and 1,000 ft above, 500 ft below, 2,000 ft horizontally from clouds. Class B is simpler — 3 SM and just 'clear of clouds.' Class G near the surface in daytime relaxes to 1 SM and clear of clouds.","diagram":VFR_MIN},
    {"heading":"Equipment and special use airspace","body":"A transponder with Mode C and ADS-B Out is required in and above Class B and C, and within the 30-NM Mode C veil around Class B, and at/above 10,000 ft MSL. Watch for special use airspace: Prohibited (never), Restricted (permission/active times), Military Operations Areas, and Temporary Flight Restrictions (TFRs). Always check NOTAMs and TFRs before you fly."},
  ],
  "links":[
    {"label":"14 CFR 91.155 — Basic VFR weather minimums","url":"https://www.ecfr.gov/current/title-14/part-91/section-91.155","note":"the cloud-clearance rule"},
    {"label":"Aeronautical Information Manual (AIM) Ch. 3 — Airspace","url":"https://www.faa.gov/air_traffic/publications/atpubs/aim_html/","note":"airspace explained"},
    {"label":"FAA VFR charts & Chart Supplement","url":"https://www.faa.gov/air_traffic/flight_info/aeronav","note":"sectionals + airport data"},
  ],
  "practiceProblems":[
    P("as-p1","To enter Class B airspace you must:",["Simply monitor the frequency","Receive an explicit clearance to enter","Have an instrument rating","Stay below 1,000 ft"],1,
      "You must hear the words 'cleared into the Class Bravo' before entering."),
    P("as-p2","In Class D airspace below 10,000 ft, the VFR minimums are:",["1 SM, clear of clouds","3 SM and 1,000 above / 500 below / 2,000 horizontal","5 SM and 1,000 above","Clear of clouds only"],1,
      "Class D uses the standard 3-152 pattern."),
    P("as-p3","Class A airspace begins at:",["10,000 ft MSL","14,500 ft MSL","18,000 ft MSL","FL600"],2,
      "Class A is 18,000 ft MSL up to FL600 and is IFR-only."),
    P("as-p4","Within 30 NM of a Class B primary airport ('Mode C veil'), you generally need:",["Nothing special","A transponder with Mode C / ADS-B Out","An instrument rating","A flight plan"],1,
      "The Mode C veil requires an operating transponder with Mode C and ADS-B Out."),
  ],
  "quiz":[
    P("as-q1","Which airspace is uncontrolled?",["Class A","Class C","Class E","Class G"],3,"Class G is uncontrolled airspace."),
    P("as-q2","The '152' in cloud clearance stands for:",["1,000 above, 500 below, 2,000 horizontal","1 SM, 5,000 ft, 2 NM","150 kt, 2 G","Nothing"],0,"1,000 ft above, 500 ft below, 2,000 ft horizontal."),
    P("as-q3","A control-tower airport with no radar service is typically Class:",["B","C","D","A"],2,"Class D surrounds towered airports without the traffic of B/C."),
    P("as-q4","A TFR is a:",["Type of cloud","Temporary Flight Restriction","Towered Field Rule","Transponder code"],1,"Temporary Flight Restriction — check before every flight."),
  ]
})

# 6. REGULATIONS
sections.append({
  "id":"regulations","title":"Regulations & Required Documents","questions":"~","weight":"Core","priority":"High",
  "factsLabel":"Numbers to memorize",
  "guide":{
    "overview":"The Federal Aviation Regulations (14 CFR) you actually use as a private pilot: what documents must be aboard, currency to carry passengers, right-of-way, fuel reserves, and privileges and limitations of your certificate.",
    "objectives":["List required aircraft documents (ARROW) and pilot documents.","State passenger-carrying currency (3 takeoffs/landings in 90 days).","Apply right-of-way and minimum-altitude rules.","Know VFR fuel reserves and private pilot privileges/limitations."],
    "prereqs":"None.",
    "watchOuts":["Night passenger currency requires 3 full-stop landings in 90 days.","VFR day fuel reserve is 30 min; night is 45 min.","A private pilot may not fly for compensation or hire.","Carry a photo ID, pilot certificate, and medical (or BasicMed) on every flight."]
  },
  "keyEquations":[
    {"name":"Passenger currency","formula":"3 T/O & landings in 90 days","where":"§ 61.57"},
    {"name":"Night currency","formula":"3 full-stop landings (night) in 90 days","where":"§ 61.57(b)"},
    {"name":"VFR fuel reserve","formula":"Day 30 min / Night 45 min","where":"§ 91.151"},
    {"name":"Required docs (aircraft)","formula":"ARROW","where":"§ 91.9/91.203"},
    {"name":"Flight review","formula":"Every 24 calendar months","where":"§ 61.56"},
  ],
  "lesson":[
    {"heading":"Documents you must carry","body":"The aircraft needs ARROW aboard: Airworthiness certificate, Registration, Radio license (international only), Operating limitations (POH/placards), and Weight & balance data. You, the pilot, must carry a government photo ID, your pilot (or student) certificate, and a current medical certificate or BasicMed qualification. No documents, no legal flight."},
    {"heading":"Currency and the flight review","body":"To carry passengers you need 3 takeoffs and landings in the preceding 90 days in the same category/class; for night passenger carrying those landings must be to a full stop. Beyond solo privileges, you must complete a flight review with an instructor every 24 calendar months to act as PIC. Currency (recent experience) and the flight review are different things — you need both."},
    {"heading":"Right-of-way, altitudes, and fuel","body":"Key rules: an aircraft in distress has the right of way; when converging, the less maneuverable aircraft (balloon > glider > airplane) has priority; aircraft approaching head-on each turn right. Minimum safe altitudes: over congested areas, 1,000 ft above the highest obstacle within 2,000 ft; elsewhere, 500 ft from people/vessels/structures. VFR fuel reserves are 30 minutes (day) and 45 minutes (night) beyond your destination at normal cruise."},
    {"heading":"Privileges and limitations","body":"As a private pilot you may carry passengers and property, day or night, in VFR conditions nationwide. You may share operating expenses pro-rata with passengers, but you may not fly for compensation or hire. You can't fly in IMC without an instrument rating, and you must operate within your aircraft's limitations and your own currency."},
  ],
  "links":[
    {"label":"14 CFR Part 91 — General Operating Rules","url":"https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-91","note":"the rules you fly under"},
    {"label":"14 CFR 61.57 — Recent flight experience","url":"https://www.ecfr.gov/current/title-14/part-61/section-61.57","note":"passenger & night currency"},
    {"label":"14 CFR 91.151 — VFR fuel requirements","url":"https://www.ecfr.gov/current/title-14/part-91/section-91.151","note":"fuel reserves"},
  ],
  "practiceProblems":[
    P("reg-p1","To carry passengers during the day you must have made, in the last 90 days:",["1 takeoff and landing","3 takeoffs and landings","3 full-stop landings","A flight review"],1,
      "§61.57(a): 3 takeoffs and 3 landings in 90 days (full-stop required only at night)."),
    P("reg-p2","Minimum VFR fuel reserve at night is enough to fly for:",["30 minutes","45 minutes","60 minutes","No requirement"],1,
      "§91.151: 30 min day, 45 min night, at normal cruise beyond the destination."),
    P("reg-p3","The 'ARROW' documents are required to be:",["Memorized","Aboard the aircraft","Filed with the FAA","Carried by the passengers"],1,
      "Airworthiness, Registration, Radio (intl), Operating limitations, Weight & balance must be in the aircraft."),
    P("reg-p4","A private pilot may:",["Fly for hire","Share operating expenses pro-rata with passengers","Fly in IMC without a rating","Carry cargo for pay"],1,
      "You can share costs pro-rata but cannot fly for compensation or hire."),
  ],
  "quiz":[
    P("reg-q1","A flight review is required every:",["12 months","24 calendar months","6 months","36 months"],1,"§61.56: every 24 calendar months."),
    P("reg-q2","Two aircraft approaching head-on should each:",["Climb","Turn right","Turn left","Descend"],1,"Each turns to the right."),
    P("reg-q3","Over a congested area, minimum altitude is 1,000 ft above the highest obstacle within:",["500 ft","1,000 ft","2,000 ft","1 NM"],2,"1,000 ft above the highest obstacle within a 2,000-ft horizontal radius."),
    P("reg-q4","Night passenger currency requires landings that are:",["Touch-and-go","To a full stop","At a towered airport","Solo"],1,"Three full-stop landings at night in the preceding 90 days."),
  ]
})

# 7. NAVIGATION
sections.append({
  "id":"navigation","title":"Navigation & Charts","questions":"~","weight":"Core","priority":"High",
  "factsLabel":"Navigation facts",
  "guide":{
    "overview":"Finding your way: pilotage and dead reckoning, the sectional chart, VOR and GPS, and accounting for wind and magnetic variation. This is the knowledge behind every cross-country flight and the Excel nav log you'll use.",
    "objectives":["Plan a course using pilotage and dead reckoning.","Read a sectional chart and the Chart Supplement.","Use VOR radials and understand GPS basics.","Correct for wind (wind triangle) and magnetic variation."],
    "prereqs":"Basic arithmetic.",
    "watchOuts":["True vs. magnetic: 'East is least, West is best' when applying variation.","A VOR radial is a course FROM the station.","Always have a backup to GPS (chart + VOR/pilotage).","Wind correction angle changes your heading from your course."]
  },
  "keyEquations":[
    {"name":"Time = Distance / Speed","formula":"t = d / GS","where":"Nav log"},
    {"name":"Magnetic variation","formula":"East is least, West is best","where":"PHAK ch. 16"},
    {"name":"Ground speed","formula":"TAS ± wind component","where":"PHAK"},
    {"name":"VOR radial","formula":"Magnetic course FROM the station","where":"PHAK"},
  ],
  "lesson":[
    {"heading":"Pilotage, dead reckoning, and charts","body":"Pilotage is navigating by visual landmarks; dead reckoning is computing heading, ground speed, and time from your planned course, airspeed, and the wind. A VFR sectional chart shows terrain, airspace, airports, and obstacles; the Chart Supplement (formerly A/FD) gives airport details. Together they let you plan and fly a cross-country leg by leg — exactly what a nav log organizes."},
    {"heading":"Wind and variation","body":"Your true airspeed plus the wind gives ground speed and a wind correction angle — solved with an E6B or the wind triangle. Charts are drawn to true north, but your compass reads magnetic, so you apply magnetic variation: 'east is least (subtract), west is best (add).' Get this backwards and your heading is off by twice the variation."},
    {"heading":"VOR and GPS","body":"A VOR transmits 360 radials; with the OBS and CDI you can fly to or from the station on a chosen radial. GPS gives direct, precise position and is the modern primary — but the FAA still expects you to navigate by pilotage, dead reckoning, and VOR as a backup. Cross-check everything; don't follow the magenta line blindly.","diagram":VOR},
  ],
  "links":[
    {"label":"PHAK Ch. 16 — Navigation","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak","note":"pilotage, DR, VOR, GPS"},
    {"label":"FAA Aeronautical Charts (VFR sectionals)","url":"https://www.faa.gov/air_traffic/flight_info/aeronav","note":"download current charts"},
    {"label":"SkyVector — online sectionals & planning","url":"https://skyvector.com","note":"plan routes online"},
  ],
  "practiceProblems":[
    P("nav-p1","A VOR radial is best described as a magnetic course:",["TO the station","FROM the station","Around the station","To true north"],1,
      "Radials are magnetic courses radiating outward FROM the VOR."),
    P("nav-p2","Variation is 5°E. To convert a true course of 090° to magnetic, you get:",["095°","085°","090°","100°"],1,
      "'East is least' — subtract easterly variation: 090 − 5 = 085° magnetic."),
    P("nav-p3","At 120 kt ground speed, a 60-NM leg takes:",["20 minutes","30 minutes","45 minutes","60 minutes"],1,
      "t = d/GS = 60/120 = 0.5 hr = 30 minutes."),
    P("nav-p4","Navigating by visual reference to landmarks is called:",["Dead reckoning","Pilotage","Radar vectoring","Triangulation"],1,
      "Pilotage uses visible landmarks; dead reckoning uses computed heading/time."),
  ],
  "quiz":[
    P("nav-q1","Sectional charts are oriented to:",["Magnetic north","True north","Grid north","The nearest VOR"],1,"Charts use true north; you apply variation for magnetic."),
    P("nav-q2","The wind correction angle makes your heading differ from your:",["Altitude","Course","Airspeed","Squawk"],1,"You crab into the wind, so heading ≠ course."),
    P("nav-q3","Which gives detailed airport information (runways, frequencies, services)?",["Sectional only","The Chart Supplement","The METAR","The POH"],1,"The Chart Supplement (formerly Airport/Facility Directory)."),
    P("nav-q4","Ground speed equals true airspeed:",["Times two","Plus or minus the wind component","Minus variation","Divided by distance"],1,"GS = TAS adjusted for the headwind/tailwind component."),
  ]
})

# 8. PERFORMANCE & W&B
sections.append({
  "id":"performance","title":"Performance, Weight & Balance","questions":"~","weight":"Core","priority":"Very High",
  "factsLabel":"Formulas",
  "guide":{
    "overview":"Whether the airplane can safely take off, climb, and land with today's load and conditions — and whether it's loaded within limits. This drives the Weight & Balance and performance Excel tools in this course.",
    "objectives":["Compute weight, moment, and center of gravity.","Check the loaded aircraft against the CG envelope.","Explain density altitude and its effect on performance.","Use POH performance charts for takeoff and landing distance."],
    "prereqs":"Basic arithmetic.",
    "watchOuts":["Moment = weight × arm; CG = total moment / total weight.","An aft CG hurts stability; a forward CG raises stall speed and control forces.","High density altitude dramatically lengthens takeoff and reduces climb.","Always verify both weight limit AND CG range — being under gross is not enough."]
  },
  "keyEquations":[
    {"name":"Moment","formula":"Moment = Weight × Arm","where":"POH / PHAK ch. 10"},
    {"name":"Center of gravity","formula":"CG = Σ Moments / Σ Weights","where":"POH"},
    {"name":"Density altitude","formula":"Pressure alt + 120 ft per °C above ISA","where":"PHAK"},
    {"name":"Useful load","formula":"Max gross − empty weight","where":"POH"},
  ],
  "lesson":[
    {"heading":"Weight and balance math","body":"Every item (empty airplane, fuel, pilot, passengers, baggage) has a weight and an arm (distance from the datum). Multiply to get each moment, sum the weights and moments, then divide total moment by total weight to find the center of gravity. The airplane is legal only if total weight is at or below max gross AND the CG falls within the published range for that weight.","diagram":CG_ENVELOPE},
    {"heading":"Why CG matters","body":"A center of gravity that's too far forward makes the airplane nose-heavy: higher stall speed, heavier controls, longer takeoff. Too far aft makes it unstable and hard to recover from a stall — the dangerous one. That's why you re-check balance as fuel burns and for different passenger/baggage loads, not just at takeoff."},
    {"heading":"Density altitude and performance","body":"Density altitude is pressure altitude corrected for non-standard temperature — the altitude the airplane 'feels.' Hot, high, and humid conditions raise density altitude, which means less lift, less thrust, longer takeoff rolls, and weaker climb. On a hot Texas afternoon a runway that's fine in winter can become marginal. Always run the POH numbers.","diagram":DENSITY_ALT},
    {"heading":"Using POH performance charts","body":"The Pilot's Operating Handbook has charts for takeoff and landing distance, climb rate, and cruise. You enter them with pressure altitude, temperature, weight, and wind to read the expected distances — then add safety margin. The checkride examiner will ask you to compute real numbers for the day's conditions."},
  ],
  "links":[
    {"label":"PHAK Ch. 10–11 — Weight & Balance, Performance","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak","note":"the math + charts"},
    {"label":"Airplane Flying Handbook","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/airplane_handbook","note":"applying performance in flight"},
  ],
  "practiceProblems":[
    P("perf-p1","Moment is calculated as:",["Weight ÷ Arm","Weight × Arm","Arm ÷ Weight","Weight + Arm"],1,
      "Moment = Weight × Arm. CG = total moment ÷ total weight."),
    P("perf-p2","High density altitude results in:",["Better climb performance","Shorter takeoff roll","Longer takeoff roll and reduced climb","No effect on performance"],2,
      "Hot/high/humid raises density altitude, degrading takeoff and climb."),
    P("perf-p3","An aft center of gravity makes an airplane:",["More stable","Less stable and harder to recover from stalls","Nose-heavy","Heavier overall"],1,
      "Aft CG reduces longitudinal stability — the more dangerous condition."),
    P("perf-p4","Total weight 2,300 lb and total moment 100,000 lb-in gives a CG of about:",["43.5 in","23 in","100 in","2.3 in"],0,
      "CG = 100,000 / 2,300 ≈ 43.5 inches aft of datum."),
  ],
  "quiz":[
    P("perf-q1","To be legal, the airplane must be within weight limits AND have its CG:",["Anywhere","Within the published range","As far aft as possible","At the datum"],1,"Both weight and CG must be within limits."),
    P("perf-q2","Density altitude is pressure altitude corrected for:",["Wind","Non-standard temperature","Magnetic variation","Fuel weight"],1,"It accounts for temperature (and humidity) vs. standard."),
    P("perf-q3","Useful load equals max gross weight minus:",["Fuel","Empty weight","Baggage","Passengers"],1,"Useful load = max gross − empty weight."),
    P("perf-q4","A forward CG tends to:",["Lower stall speed","Raise stall speed and control forces","Reduce stability","Have no effect"],1,"Forward CG increases stall speed and control forces."),
  ]
})

# 9. AIRPORT OPS & COMMS
sections.append({
  "id":"airport-ops","title":"Airport Operations & Communications","questions":"~","weight":"Core","priority":"High",
  "guide":{
    "overview":"Operating safely on and around airports: the traffic pattern, runway and taxiway markings, lighting, and radio communications — towered and non-towered. Runway incursions are a real risk, and clear radio work prevents them.",
    "objectives":["Fly a standard traffic pattern and use correct entry.","Interpret runway/taxiway markings and airport lighting.","Use proper radio phraseology at towered and non-towered fields.","Avoid runway incursions through readbacks and position awareness."],
    "prereqs":"None.",
    "watchOuts":["Always read back hold-short and runway clearances.","At non-towered fields, announce position on CTAF and use standard left patterns.","Solid lines mean hold; never cross a hold-short line without clearance.","Set your radios and review the airport diagram before taxiing."]
  },
  "factsLabel":"Quick reference",
  "keyEquations":[
    {"name":"Standard pattern","formula":"Left turns, ~1,000 ft AGL","where":"AIM ch. 4"},
    {"name":"Pattern entry","formula":"45° to the downwind","where":"AIM"},
    {"name":"Non-towered freq.","formula":"CTAF / UNICOM","where":"AIM"},
    {"name":"Hold-short line","formula":"2 solid + 2 dashed yellow","where":"AIM"},
  ],
  "lesson":[
    {"heading":"The traffic pattern","body":"The traffic pattern is a standard rectangular path around the runway: upwind/departure, crosswind, downwind (flown opposite landing direction at pattern altitude, usually 1,000 ft AGL), base, and final. Turns are to the left unless the airport specifies right traffic. At non-towered fields you typically enter on a 45° leg to the downwind and announce each leg on the CTAF.","diagram":TRAFFIC_PATTERN},
    {"heading":"Markings and lighting","body":"Runway markings are white (numbers are magnetic heading ÷ 10); taxiway markings are yellow. The hold-short marking — two solid and two dashed yellow lines — means stop on the solid side until cleared. Airport beacons, runway edge lights (white), and the threshold (green/red) help at night, and a VASI/PAPI gives a visual glide path to the runway."},
    {"heading":"Radio communications","body":"Use the who-you're-calling / who-you-are / where / what format: 'San Marcos Tower, Cessna 12345, ten miles south, inbound for landing.' Read back all hold-short and runway crossing/clearance instructions. At non-towered airports there's no controller — you self-announce on the CTAF and see-and-avoid. Clear, standard phraseology is your best defense against runway incursions and traffic conflicts."},
  ],
  "links":[
    {"label":"AIM Ch. 4 — Air Traffic Control & Procedures","url":"https://www.faa.gov/air_traffic/publications/atpubs/aim_html/","note":"patterns, comms, markings"},
    {"label":"PHAK Ch. 14 — Airport Operations","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak","note":"markings, lighting, signs"},
  ],
  "practiceProblems":[
    P("ap-p1","The standard traffic pattern uses:",["Right turns at 500 ft","Left turns at ~1,000 ft AGL","No turns","Random entry"],1,
      "Standard pattern = left turns, typically 1,000 ft AGL, unless right traffic is specified."),
    P("ap-p2","A runway number of '18' indicates a magnetic heading of about:",["18°","108°","180°","810°"],2,
      "Runway numbers are the magnetic heading divided by 10, so 18 → ~180°."),
    P("ap-p3","Two solid and two dashed yellow lines mark a:",["Taxiway centerline","Hold-short line","Closed runway","Displaced threshold"],1,
      "That's the hold-short marking; stop on the solid side until cleared."),
    P("ap-p4","At a non-towered airport, you communicate on the:",["Tower frequency","CTAF/UNICOM and self-announce","Emergency frequency","Center frequency"],1,
      "Use the CTAF to self-announce; there is no controller."),
  ],
  "quiz":[
    P("ap-q1","Standard pattern entry at a non-towered field is usually:",["Straight-in","45° to the downwind","Base leg","Over the numbers"],1,"A 45° entry to the downwind at pattern altitude is standard."),
    P("ap-q2","Taxiway markings are:",["White","Yellow","Red","Blue"],1,"Taxiways are yellow; runways are white."),
    P("ap-q3","You must read back which instruction?",["Wind information","Hold-short / runway clearances","The ATIS","Traffic advisories"],1,"Always read back hold-short and runway crossing/clearance instructions."),
    P("ap-q4","A PAPI or VASI provides:",["Wind direction","A visual glide path to the runway","Runway length","Radio frequency"],1,"It gives a visual approach slope indication."),
  ]
})

# 10. AEROMEDICAL & CHECKRIDE
sections.append({
  "id":"checkride","title":"Aeromedical Factors & Checkride Prep","questions":"~","weight":"Finish strong","priority":"High",
  "guide":{
    "overview":"Two finish-line topics: the human factors that affect you as pilot-in-command, and exactly how to prepare for and pass the checkride. The examiner tests both your knowledge (oral) and your flying (practical) against the ACS.",
    "objectives":["Recognize hypoxia, hyperventilation, spatial disorientation, and other hazards.","Apply self-assessment (IMSAFE) and aeronautical decision-making.","Know what the checkride covers and what to bring.","Build a study and readiness plan using the ACS."],
    "prereqs":"All other sections.",
    "watchOuts":["Alcohol: 8 hours 'bottle to throttle' and below 0.04% BAC (and not impaired).","Trust your instruments over your senses in low visibility (spatial disorientation).","Hypoxia sneaks up — use oxygen per regs at altitude.","Bring all required documents and endorsements, or the checkride won't start."]
  },
  "factsLabel":"Personal minimums & rules",
  "keyEquations":[
    {"name":"Alcohol rule","formula":"8 hrs + below 0.04% BAC","where":"§ 91.17"},
    {"name":"Self-assessment","formula":"IMSAFE checklist","where":"AIM / PHAK"},
    {"name":"Supplemental O2 (crew)","formula":"Above 12,500 ft >30 min","where":"§ 91.211"},
    {"name":"Decision-making","formula":"DECIDE / 3P model","where":"PHAK ch. 2"},
  ],
  "lesson":[
    {"heading":"Aeromedical factors","body":"Your body has limits. Hypoxia (oxygen starvation) causes euphoria and poor judgment with few warnings — use oxygen at altitude. Hyperventilation mimics hypoxia; slow your breathing. Spatial disorientation happens when your senses disagree with reality in low visibility — trust the instruments. Other hazards: carbon monoxide from a cracked exhaust/heater, dehydration, fatigue, and the effects of medication, alcohol, and stress."},
    {"heading":"Decision-making and self-assessment","body":"Most accidents trace to decisions, not stick-and-rudder skill. Before every flight, run IMSAFE (Illness, Medication, Stress, Alcohol, Fatigue, Eating/Emotion) on yourself and assess the flight risk (the 3P or PAVE model: Pilot, Aircraft, enVironment, External pressures). Set personal minimums and respect them — the strongest pilot skill is saying 'not today.'"},
    {"heading":"What the checkride is","body":"The practical test has two parts: an oral exam where the DPE probes your knowledge of regulations, weather, systems, performance, and decision-making, followed by a flight where you demonstrate maneuvers and procedures to the tolerances in the Airman Certification Standards (ACS). Plan a cross-country the examiner assigns, then fly diverts, maneuvers, takeoffs/landings, and emergencies."},
    {"heading":"Getting ready — and what to bring","body":"Study straight from the ACS so there are no surprises. Bring: photo ID; pilot/student certificate; medical (or BasicMed); logbook with all required endorsements and experience; the aircraft's documents and current POH; your knowledge-test report; and a completed IACRA application with your instructor's sign-off. Fly with your CFI until you're consistently inside ACS tolerances, then go get it."},
  ],
  "links":[
    {"label":"Private Pilot ACS (FAA-S-ACS-6) — study from this","url":"https://www.faa.gov/training_testing/testing/acs","note":"the exact standards"},
    {"label":"PHAK Ch. 2–17 — full knowledge","url":"https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak","note":"aeromedical (ch.17), ADM (ch.2)"},
    {"label":"14 CFR 91.17 — Alcohol and drugs","url":"https://www.ecfr.gov/current/title-14/part-91/section-91.17","note":"bottle-to-throttle rule"},
    {"label":"FAA WINGS / FAASTeam safety","url":"https://www.faasafety.gov","note":"free safety courses"},
  ],
  "practiceProblems":[
    P("med-p1","The minimum time from drinking alcohol to acting as a required crewmember is:",["4 hours","8 hours","12 hours","24 hours"],1,
      "§91.17: 8 hours 'bottle to throttle,' below 0.04% BAC, and not impaired."),
    P("med-p2","In low visibility, when your senses disagree with the instruments you should:",["Trust your senses","Trust the instruments","Close your eyes","Descend immediately"],1,
      "Spatial disorientation: believe the instruments, not your inner ear."),
    P("med-p3","The IMSAFE checklist is used to assess:",["The aircraft","The weather","Your own fitness to fly","The route"],2,
      "IMSAFE is a pilot self-assessment: Illness, Medication, Stress, Alcohol, Fatigue, Eating/Emotion."),
    P("med-p4","The checkride flight is graded against the:",["AIM","ACS","METAR","POH only"],1,
      "Maneuvers are flown to Airman Certification Standards (ACS) tolerances."),
  ],
  "quiz":[
    P("ck-q1","Hypoxia is dangerous mainly because it:",["Is painful","Impairs judgment with little warning","Stops the engine","Affects the radios"],1,"It degrades judgment and vision insidiously."),
    P("ck-q2","Required crew oxygen is needed above 12,500 ft MSL when the flight exceeds:",["Any time","30 minutes","2 hours","Never"],1,"§91.211: above 12,500 ft for more than 30 minutes."),
    P("ck-q3","Which model assesses Pilot, Aircraft, enVironment, External pressures?",["IMSAFE","PAVE","ARROW","ANDS"],1,"PAVE is the risk-assessment model; IMSAFE is the pilot self-check."),
    P("ck-q4","The best single source to study for the checkride is the:",["AIM","ACS","NOTAMs","Sectional"],1,"Study directly from the ACS."),
  ]
})

course = {
  "id":"ppl",
  "title":"Private Pilot (PPL)",
  "subtitle":"FAA Private Pilot Certificate — Airplane Single-Engine Land",
  "tagline":"Everything you need to go from your first discovery flight to a private pilot certificate: the step-by-step path, full ground-school knowledge with diagrams, the links that matter, practice, and quizzes.",
  "examFacts":{
    "questions":60,"hours":40,"areas":10,"handbook":"PHAK · Airplane Flying Handbook · ACS-6C",
    "questionsLabel":"Written questions","hoursLabel":"Min flight hours","areasLabel":"Knowledge areas",
    "passNote":"Knowledge test: 65 questions (60 scored), 70% to pass, valid 24 calendar months. Be 17 to earn the certificate (16 to solo), able to read/speak/understand English, and hold a third-class medical or BasicMed."
  },
  "priceMonthly":10,"priceOneTime":100,
  "heroDiagram":ROADMAP,
  "sections":sections,
  "practiceTests":[
    {"id":"ppl-pt1","title":"Practice Test 1 - Regs, Airspace & Weather","time":"25 min","questions":[
      P("p1-1","Minimum total flight time for a Part 61 private pilot certificate:",["20 hr","35 hr","40 hr","50 hr"],2,"Part 61 minimum is 40 hours."),
      P("p1-2","VFR visibility in Class D below 10,000 ft MSL:",["1 SM","3 SM","5 SM","Clear of clouds"],1,"3 SM with 1,000/500/2,000 cloud clearance."),
      P("p1-3","Night VFR fuel reserve:",["30 min","45 min","60 min","None"],1,"§91.151: 45 minutes at night."),
      P("p1-4","Class A airspace begins at:",["14,500 ft","18,000 ft MSL","10,000 ft","FL600"],1,"18,000 ft MSL up to FL600, IFR only."),
      P("p1-5","A small temperature/dew-point spread suggests:",["Thunderstorms","Fog/low ceilings","High winds","Clear skies"],1,"Air near saturation → fog/low clouds."),
      P("p1-6","Passenger-carrying day currency:",["1 landing/90 days","3 T/O & landings/90 days","3 full-stop/90 days","Flight review only"],1,"3 takeoffs and landings within 90 days."),
      P("p1-7","Avoid thunderstorms by at least:",["5 NM","10 NM","20 NM","2 NM"],2,"At least 20 NM."),
      P("p1-8","To enter Class B you must have:",["Mode C only","An explicit ATC clearance","An instrument rating","A flight plan"],1,"'Cleared into the Bravo.'"),
      P("p1-9","Required aircraft documents are remembered as:",["IMSAFE","ARROW","PAVE","ANDS"],1,"Airworthiness, Registration, Radio(intl), Operating limits, Weight & balance."),
      P("p1-10","Standard pattern altitude is typically:",["500 ft AGL","1,000 ft AGL","2,500 ft AGL","3,000 ft MSL"],1,"About 1,000 ft AGL with left turns."),
    ]},
    {"id":"ppl-pt2","title":"Practice Test 2 - Aero, Performance & Navigation","time":"25 min","questions":[
      P("p2-1","In steady level flight, lift equals:",["Thrust","Weight","Drag","Zero"],1,"Lift = weight, thrust = drag."),
      P("p2-2","At 60° bank in level flight, load factor is:",["1.0 G","1.4 G","2.0 G","3.0 G"],2,"n = 1/cos60° = 2.0 G."),
      P("p2-3","A wing stalls when it exceeds its:",["Vne","Critical angle of attack","Max weight","Va"],1,"Critical angle of attack, at any speed."),
      P("p2-4","High density altitude causes:",["Shorter takeoff","Longer takeoff & weaker climb","Better climb","No change"],1,"Hot/high/humid degrades performance."),
      P("p2-5","CG equals total moment divided by:",["Total arm","Total weight","Fuel weight","Useful load"],1,"CG = ΣMoments / ΣWeight."),
      P("p2-6","A VOR radial is a magnetic course:",["TO the station","FROM the station","To true north","Around the field"],1,"Radials go FROM the station."),
      P("p2-7","True course 100°, variation 6°W. Magnetic course:",["94°","106°","100°","112°"],1,"'West is best' — add: 100 + 6 = 106°."),
      P("p2-8","A blocked static port affects:",["ASI only","ALT, VSI, and ASI","AI only","HI only"],1,"All static instruments."),
      P("p2-9","60 NM at 90 kt ground speed takes:",["30 min","40 min","45 min","60 min"],1,"t = 60/90 = 0.667 hr = 40 minutes."),
      P("p2-10","An aft CG makes the airplane:",["More stable","Less stable","Nose-heavy","Heavier"],1,"Aft CG reduces stability."),
    ]},
  ]
}

out = os.path.join(os.path.dirname(__file__),"data","course-ppl.json")
with open(out,"w") as f: json.dump(course,f,ensure_ascii=False,indent=2)
nq = sum(len(s["practiceProblems"])+len(s["quiz"]) for s in sections)+sum(len(t["questions"]) for t in course["practiceTests"])
print("sections:",len(sections),"questions:",nq,"-> wrote",out)
