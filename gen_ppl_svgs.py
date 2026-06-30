# SVG diagram library for the PPL course. Theme: brand #2563eb, accent #f59e0b, ink #0f172a.

ROADMAP = '''<svg viewBox="0 0 980 200" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<defs><marker id="ar" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#94a3b8"/></marker></defs>
<text x="490" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">Zero to Private Pilot Certificate</text>
''' + ''.join(
  f'<rect x="{10+ i*138}" y="50" width="120" height="70" rx="10" fill="{c}" />'
  f'<text x="{70+i*138}" y="78" text-anchor="middle" font-size="22">{ic}</text>'
  f'<text x="{70+i*138}" y="104" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">{t}</text>'
  + ('' if i==6 else f'<line x1="{132+i*138}" y1="85" x2="{146+i*138}" y2="85" stroke="#94a3b8" stroke-width="2" marker-end="url(#ar)"/>')
  for i,(ic,t,c) in enumerate([
    ('\U0001F6E9️','Discovery flight','#dbeafe'),
    ('\U0001FA7A','Medical + Student cert','#fde68a'),
    ('\U0001F4D8','Ground school + Written','#dbeafe'),
    ('\U0001F501','Pre-solo training','#bbf7d0'),
    ('\U0001F538','First solo','#bbf7d0'),
    ('\U0001F5FA️','Cross-country + Night','#dbeafe'),
    ('✅','Checkride (oral+flight)','#fecaca'),
  ])
) + '''
<text x="490" y="150" text-anchor="middle" font-size="11" fill="#475569">Typically 3–9 months · 40+ flight hours (Part 61) · written test valid 24 calendar months</text>
</svg>'''

FOUR_FORCES = '''<svg viewBox="0 0 560 340" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<defs><marker id="f" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#2563eb"/></marker></defs>
<text x="280" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">The Four Forces of Flight</text>
<g transform="translate(280,180)">
<ellipse cx="0" cy="0" rx="70" ry="16" fill="#1e3a8a"/>
<rect x="-12" y="-46" width="24" height="46" rx="6" fill="#1e3a8a"/>
<rect x="-95" y="-6" width="190" height="12" rx="6" fill="#2563eb"/>
<rect x="48" y="-30" width="10" height="30" fill="#1e3a8a"/>
</g>
<line x1="280" y1="150" x2="280" y2="70" stroke="#2563eb" stroke-width="4" marker-end="url(#f)"/>
<text x="280" y="60" text-anchor="middle" font-size="13" font-weight="700" fill="#2563eb">LIFT</text>
<line x1="280" y1="210" x2="280" y2="290" stroke="#dc2626" stroke-width="4" marker-end="url(#f)" style="marker-end:url(#f)"/>
<text x="280" y="308" text-anchor="middle" font-size="13" font-weight="700" fill="#dc2626">WEIGHT</text>
<line x1="200" y1="180" x2="110" y2="180" stroke="#16a34a" stroke-width="4" marker-end="url(#f)"/>
<text x="95" y="184" text-anchor="end" font-size="13" font-weight="700" fill="#16a34a">DRAG</text>
<line x1="360" y1="180" x2="450" y2="180" stroke="#f59e0b" stroke-width="4" marker-end="url(#f)"/>
<text x="465" y="184" text-anchor="start" font-size="13" font-weight="700" fill="#f59e0b">THRUST</text>
<text x="280" y="332" text-anchor="middle" font-size="11" fill="#475569">In steady, level, unaccelerated flight: Lift = Weight and Thrust = Drag.</text>
</svg>'''

AIRSPACE = '''<svg viewBox="0 0 780 380" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<text x="390" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">U.S. Airspace Classes (profile view)</text>
<rect x="60" y="40" width="660" height="300" fill="#f1f5f9" stroke="#cbd5e1"/>
<!-- ground -->
<rect x="60" y="320" width="660" height="20" fill="#86efac"/>
<!-- Class A -->
<rect x="60" y="40" width="660" height="40" fill="#cbd5e1" opacity="0.6"/>
<text x="390" y="65" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">Class A — 18,000 ft MSL up to FL600 (IFR only)</text>
<!-- Class E shading -->
<rect x="60" y="80" width="660" height="240" fill="#dbeafe" opacity="0.4"/>
<text x="610" y="150" font-size="12" font-weight="700" fill="#1d4ed8">Class E</text>
<text x="610" y="166" font-size="10" fill="#475569">controlled</text>
<!-- Class B -->
<polygon points="120,320 120,200 300,200 300,160 360,160 360,320" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/>
<text x="240" y="270" text-anchor="middle" font-size="13" font-weight="700" fill="#1e3a8a">Class B</text>
<text x="240" y="288" text-anchor="middle" font-size="9.5" fill="#1e3a8a">(busy hubs)</text>
<!-- Class C -->
<polygon points="430,320 430,250 480,250 480,210 560,210 560,320" fill="#c4b5fd" stroke="#6d28d9" stroke-width="2"/>
<text x="500" y="290" text-anchor="middle" font-size="12" font-weight="700" fill="#5b21b6">Class C</text>
<!-- Class D -->
<polygon points="615,320 615,235 685,235 685,320" fill="#a5b4fc" stroke="#4338ca" stroke-width="2" stroke-dasharray="5 3"/>
<text x="650" y="295" text-anchor="middle" font-size="12" font-weight="700" fill="#3730a3">Class D</text>
<!-- Class G -->
<rect x="60" y="305" width="60" height="15" fill="#fcd34d"/>
<text x="90" y="300" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">G</text>
<text x="90" y="335" text-anchor="middle" font-size="9" fill="#475569">uncontrolled</text>
<text x="70" y="335" font-size="9" fill="#475569"></text>
<text x="390" y="362" text-anchor="middle" font-size="11" fill="#475569">B = surface to ~10,000′ · C = surface to ~4,000′ AGL · D = surface to ~2,500′ AGL · G below E</text>
</svg>'''

VFR_MIN = '''<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<text x="360" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">VFR Cloud Clearance &amp; Visibility (day, &lt;10,000′ MSL)</text>
''' + ''.join(
  f'<rect x="20" y="{45+i*42}" width="160" height="40" fill="{(i%2==0) and "#eff6ff" or "#fff"}" stroke="#e2e8f0"/>'
  f'<rect x="180" y="{45+i*42}" width="200" height="40" fill="{(i%2==0) and "#eff6ff" or "#fff"}" stroke="#e2e8f0"/>'
  f'<rect x="380" y="{45+i*42}" width="320" height="40" fill="{(i%2==0) and "#eff6ff" or "#fff"}" stroke="#e2e8f0"/>'
  f'<text x="30" y="{70+i*42}" font-size="12.5" font-weight="700" fill="#0f172a">{cls}</text>'
  f'<text x="190" y="{70+i*42}" font-size="12.5" fill="#1d4ed8">{vis}</text>'
  f'<text x="390" y="{70+i*42}" font-size="12" fill="#334155">{cc}</text>'
  for i,(cls,vis,cc) in enumerate([
    ('Airspace','Visibility','Cloud clearance'),
    ('Class B','3 SM','Clear of clouds'),
    ('Class C, D, E','3 SM','500′ below, 1,000′ above, 2,000′ horizontal'),
    ('Class G (≤1,200′ AGL, day)','1 SM','Clear of clouds'),
  ])
) + '''
<text x="360" y="290" text-anchor="middle" font-size="11" fill="#475569">Memory aid: "Cessna 152" → 1,000 above, 500 below, 2,000 horizontal.</text>
</svg>'''

TRAFFIC_PATTERN = '''<svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<defs><marker id="p" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2563eb"/></marker></defs>
<text x="320" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">Standard (left) Traffic Pattern</text>
<!-- runway -->
<rect x="150" y="120" width="36" height="200" rx="4" fill="#334155"/>
<line x1="168" y1="130" x2="168" y2="310" stroke="#fff" stroke-width="2" stroke-dasharray="10 10"/>
<!-- pattern legs -->
<rect x="168" y="70" width="330" height="250" fill="none" stroke="#2563eb" stroke-width="3"/>
<line x1="498" y1="200" x2="498" y2="195" stroke="#2563eb" stroke-width="3" marker-end="url(#p)"/>
<text x="333" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="#2563eb">CROSSWIND</text>
<text x="512" y="200" font-size="12" font-weight="700" fill="#2563eb">DOWNWIND</text>
<text x="333" y="338" text-anchor="middle" font-size="12" font-weight="700" fill="#2563eb">BASE</text>
<text x="150" y="200" font-size="12" font-weight="700" fill="#16a34a" text-anchor="end" transform="rotate(-90 150 200)" >UPWIND / DEPARTURE</text>
<line x1="168" y1="312" x2="168" y2="150" stroke="#16a34a" stroke-width="3" marker-end="url(#p)"/>
<text x="120" y="120" font-size="12" font-weight="700" fill="#dc2626">FINAL</text>
<line x1="168" y1="70" x2="168" y2="120" stroke="#dc2626" stroke-width="3"/>
<text x="320" y="352" text-anchor="middle" font-size="11" fill="#475569">Left turns are standard. Pattern altitude is typically 1,000′ AGL.</text>
</svg>'''

CG_ENVELOPE = '''<svg viewBox="0 0 560 380" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<text x="280" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">Weight &amp; Balance — CG Envelope</text>
<line x1="80" y1="320" x2="520" y2="320" stroke="#334155" stroke-width="2"/>
<line x1="80" y1="320" x2="80" y2="50" stroke="#334155" stroke-width="2"/>
<text x="300" y="356" text-anchor="middle" font-size="12" fill="#475569">Center of Gravity (inches aft of datum)</text>
<text x="30" y="190" text-anchor="middle" font-size="12" fill="#475569" transform="rotate(-90 30 190)">Weight (lb)</text>
<polygon points="150,300 360,300 420,120 230,120" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>
<text x="300" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">WITHIN LIMITS</text>
<circle cx="300" cy="210" r="6" fill="#2563eb"/>
<text x="312" y="206" font-size="11" font-weight="700" fill="#2563eb">Your loaded aircraft</text>
<circle cx="450" cy="140" r="6" fill="#dc2626"/>
<text x="462" y="138" font-size="11" font-weight="700" fill="#dc2626">Out of limits → unsafe</text>
<text x="280" y="372" text-anchor="middle" font-size="11" fill="#475569">Plot total weight vs. CG. The point must fall inside the envelope for every phase of flight.</text>
</svg>'''

PITOT_STATIC = '''<svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<text x="320" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">Pitot-Static System</text>
<rect x="40" y="120" width="120" height="26" rx="13" fill="#1e3a8a"/>
<rect x="150" y="128" width="40" height="10" fill="#1e3a8a"/>
<text x="100" y="170" text-anchor="middle" font-size="11" font-weight="700" fill="#1e3a8a">Pitot tube (ram air)</text>
<circle cx="70" cy="240" r="9" fill="#334155"/>
<text x="70" y="270" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">Static port</text>
<line x1="190" y1="133" x2="360" y2="100" stroke="#2563eb" stroke-width="3"/>
<line x1="79" y1="238" x2="360" y2="170" stroke="#16a34a" stroke-width="3"/>
<line x1="79" y1="240" x2="360" y2="240" stroke="#16a34a" stroke-width="3"/>
<line x1="79" y1="242" x2="360" y2="290" stroke="#16a34a" stroke-width="3"/>
''' + ''.join(
  f'<rect x="370" y="{80+i*70}" width="190" height="52" rx="8" fill="#eff6ff" stroke="#2563eb"/>'
  f'<text x="465" y="{102+i*70}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1d4ed8">{n}</text>'
  f'<text x="465" y="{120+i*70}" text-anchor="middle" font-size="10.5" fill="#475569">{d}</text>'
  for i,(n,d) in enumerate([
    ('Airspeed Indicator','Pitot (ram) + Static'),
    ('Altimeter','Static pressure'),
    ('Vertical Speed Ind.','Static (rate of change)'),
  ])
) + '''
<text x="320" y="312" text-anchor="middle" font-size="11" fill="#475569">A blocked pitot or static port causes predictable, testable instrument errors.</text>
</svg>'''

FRONTS = '''<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<text x="350" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">Cold Front vs. Warm Front (cross-section)</text>
<line x1="20" y1="250" x2="340" y2="250" stroke="#334155" stroke-width="2"/>
<text x="180" y="272" text-anchor="middle" font-size="12" font-weight="700" fill="#2563eb">COLD FRONT</text>
<path d="M40,250 L150,250 L120,120" fill="#bfdbfe" opacity="0.7"/>
<path d="M150,250 C150,180 130,150 120,120" fill="none" stroke="#2563eb" stroke-width="3"/>
<text x="60" y="160" font-size="11" fill="#1d4ed8">cold air</text>
<text x="220" y="150" font-size="11" fill="#b45309">warm air rises steeply</text>
<text x="180" y="240" font-size="10" fill="#475569">narrow band, storms</text>
<line x1="380" y1="250" x2="690" y2="250" stroke="#334155" stroke-width="2"/>
<text x="540" y="272" text-anchor="middle" font-size="12" font-weight="700" fill="#dc2626">WARM FRONT</text>
<path d="M400,250 L620,250 L660,150" fill="#fecaca" opacity="0.6"/>
<path d="M400,250 L660,150" stroke="#dc2626" stroke-width="3" fill="none"/>
<text x="430" y="200" font-size="11" fill="#b91c1c">warm air overrides gently</text>
<text x="600" y="240" font-size="10" fill="#475569">wide area, low ceilings</text>
</svg>'''

DENSITY_ALT = '''<svg viewBox="0 0 640 280" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<defs><marker id="d" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#f59e0b"/></marker></defs>
<text x="320" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">Density Altitude — the performance killer</text>
''' + ''.join(
  f'<rect x="{40+i*195}" y="60" width="170" height="50" rx="8" fill="#fef3c7" stroke="#f59e0b"/>'
  f'<text x="{125+i*195}" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">{t}</text>'
  for i,t in enumerate(['High temperature','High altitude','High humidity'])
) + '''
<line x1="320" y1="115" x2="320" y2="150" stroke="#f59e0b" stroke-width="3" marker-end="url(#d)"/>
<rect x="200" y="155" width="240" height="46" rx="8" fill="#fde68a" stroke="#b45309"/>
<text x="320" y="184" text-anchor="middle" font-size="14" font-weight="700" fill="#92400e">HIGH DENSITY ALTITUDE</text>
<line x1="320" y1="205" x2="320" y2="232" stroke="#f59e0b" stroke-width="3" marker-end="url(#d)"/>
<text x="320" y="256" text-anchor="middle" font-size="13" font-weight="700" fill="#dc2626">↓ Less lift, less thrust, longer takeoff &amp; climb</text>
<text x="320" y="274" text-anchor="middle" font-size="11" fill="#475569">"Hot, high, and humid" = degraded performance. Always run the numbers.</text>
</svg>'''

VOR = '''<svg viewBox="0 0 520 360" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<text x="260" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">VOR Navigation (radials)</text>
<circle cx="260" cy="200" r="120" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
<circle cx="260" cy="200" r="6" fill="#1e3a8a"/>
''' + ''.join(
  f'<line x1="260" y1="200" x2="{260+110*__import__("math").sin(__import__("math").radians(a))}" y2="{200-110*__import__("math").cos(__import__("math").radians(a))}" stroke="#93c5fd" stroke-width="1.5"/>'
  + f'<text x="{260+128*__import__("math").sin(__import__("math").radians(a))}" y="{204-128*__import__("math").cos(__import__("math").radians(a))}" text-anchor="middle" font-size="10" fill="#1d4ed8">{a:03d}</text>'
  for a in range(0,360,30)
) + '''
<line x1="260" y1="200" x2="370" y2="90" stroke="#dc2626" stroke-width="3"/>
<circle cx="370" cy="90" r="7" fill="#dc2626"/>
<text x="384" y="88" font-size="11" font-weight="700" fill="#dc2626">Aircraft on the 045° radial</text>
<text x="260" y="345" text-anchor="middle" font-size="11" fill="#475569">A radial is a magnetic course FROM the station. The OBS + CDI tell you where you are relative to it.</text>
</svg>'''

LOAD_FACTOR = '''<svg viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<text x="300" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">Load Factor Increases with Bank Angle</text>
<line x1="70" y1="250" x2="560" y2="250" stroke="#334155" stroke-width="2"/>
<line x1="70" y1="250" x2="70" y2="50" stroke="#334155" stroke-width="2"/>
<text x="315" y="285" text-anchor="middle" font-size="12" fill="#475569">Bank angle</text>
<text x="28" y="150" text-anchor="middle" font-size="12" fill="#475569" transform="rotate(-90 28 150)">Load factor (G)</text>
''' + ''.join(
  f'<circle cx="{70+ba*5.3}" cy="{250 - (g-1)*120}" r="5" fill="#2563eb"/>'
  f'<text x="{70+ba*5.3}" y="{238 - (g-1)*120}" text-anchor="middle" font-size="10" fill="#1d4ed8">{g}G</text>'
  f'<text x="{70+ba*5.3}" y="266" text-anchor="middle" font-size="10" fill="#475569">{ba}°</text>'
  for ba,g in [(0,1.0),(30,1.15),(45,1.41),(60,2.0),(75,3.86)]
) + '''
<path d="M70,250 Q300,235 327,170 Q380,60 467,55" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="4 4"/>
<text x="300" y="120" text-anchor="middle" font-size="11" fill="#dc2626">At 60° bank, you and the wings feel 2× weight — stall speed rises ~41%.</text>
</svg>'''

SIXPACK = '''<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<text x="270" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">The "Six-Pack" Instrument Panel</text>
''' + ''.join(
  f'<circle cx="{110+col*160}" cy="{90+row*100}" r="42" fill="#0f172a" stroke="#334155" stroke-width="3"/>'
  f'<text x="{110+col*160}" y="{86+row*100}" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{abbr}</text>'
  f'<text x="{110+col*160}" y="{102+row*100}" text-anchor="middle" font-size="8.5" fill="#cbd5e1">{src}</text>'
  for idx,(abbr,src) in enumerate([
    ('ASI','pitot-static'),('AI','gyro/vacuum'),('ALT','static'),
    ('TC','gyro/electric'),('HI','gyro/vacuum'),('VSI','static'),
  ]) for row,col in [(idx//3, idx%3)]
) + '''
<text x="270" y="262" text-anchor="middle" font-size="11" fill="#475569">Top: Airspeed · Attitude · Altimeter. Bottom: Turn Coordinator · Heading · Vertical Speed.</text>
</svg>'''
