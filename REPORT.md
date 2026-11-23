# REPORT — news-image-20261123 "THE WORLD IN ONE DAY"

Entry: one 1024×1024 PNG front page summing up Monday 23 November 2026's
world news. `main.py` (Python 3.13 stdlib only) copies the shipped
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` byte-identically; verified
twice with a clean environment (both runs sha256
`69ceba926fe08e4d77607d949ba63f78363bd6e84bd047d7ef67b90d276651fd`).
`entry.png`: 1024×1024, 184,214 bytes (≤1 MiB).

## Story list (33 stories, all first reported Monday 23 Nov 2026)

Sources: Reuters (23 Nov wires), BBC News/Sport (23 Nov), Al Jazeera (23 Nov
live). Claims are labelled as reported on the image ("Kyiv says",
"Warsaw says", "Tehran vows"). Nothing speculative is shown as fact.

### Heroes (numbered 1–3)
1. NVIDIA — Huang back as CEO. Nvidia reinstates Jensen Huang as chief
   executive, 11 days after he resigned, under pressure from President Trump;
   shares surged +31% premarket. (Reuters, BBC)
2. UKRAINE — Warship sunk off Libya. Zelensky confirms sea drones sank a
   Russian warship off the Libyan coast; Kyiv says a second was struck in the
   Baltic near Finland. (BBC, Guardian)
3. HORMUZ — Tankers ablaze. Oil tankers hit mines in the Strait of Hormuz and
   caught fire; Tehran vows "all available means" against the US naval
   blockade; Iran says US radar targeted in attacks on Bahrain bases.
   (Al Jazeera)

### Grid (numbered 4–15)
4. GAZA — Israeli airstrike kills UNRWA worker Adel al-Helo; at least three
   Palestinians killed. (Reuters)
5. CATALONIA — Spain's Supreme Court shelves the case against Carles
   Puigdemont, clearing his return after nearly a decade in exile. (Reuters)
6. SYRIA — US discussing plans to train Syrian soldiers in demining; first US
   training mission with Syria's military since 2024. (Reuters)
7. COBALT — DR Congo suspends cobalt exports from 30 Nov until further notice
   to tackle oversupply. (Reuters)
8. AMAZON — Amazon to buy AI startup Decart's chip-optimisation tech and hire
   its founders; Bloomberg reports ~$7.5bn. (Reuters)
9. EU BUDGET — Czech PM Babis and Hungary reject Council chief Costa's new
   €1.582tn EU budget proposal for 2028–2034. (Reuters)
10. BANGLADESH — Manufacturers offer ~15% minimum-wage rise at Monday talks;
    workers demand more than double, to 30,000 taka; factories shut in Ashulia
    and Gazipur. (Reuters)
11. DENMARK — Top court backs evictions ending 91 leases under the "ghetto
    law"; no ethnic discrimination found. (Reuters)
12. KALININGRAD — Russia to spend 47bn roubles ($576m) on two giant rail
    ferries to secure supplies to its Baltic exclave. (Reuters)
13. MARKETS — US stocks steady early Monday after an AI selloff pushed the S&P
    500 into correction and the Nasdaq into the red for the year. (Reuters)
14. NEPAL — India pledges $1.6bn to Nepal in a reset of ties. (BBC)
15. AFRICA — Kenya and DR Congo agree to restore diplomatic ties. (BBC)

### Briefs (numbered 16–33)
16. BOXING — Fury reveals schizophrenia diagnosis from a 2015 breakdown; also
    bipolar. (BBC Sport)
17. FOOTBALL — UK to host the 2035 Women's World Cup, FIFA confirms. (BBC)
18. PROTEST — Gen Z rallies sweep 25 European countries over wars, living
    costs and climate. (Al Jazeera)
19. GERMANY — Qatar pledges $16.5bn in new investments during the emir's
    Berlin visit. (Al Jazeera)
20. WASHINGTON — Senate Republicans reject bid to limit Trump's Iran war
    powers, 51–48; three Republicans broke ranks. (Al Jazeera)
21. MIGRATION — US appeals court lets Trump end TPS deportation protections
    for Venezuelans. (Al Jazeera)
22. EL SALVADOR — Bukele seeks a third term after a constitution change.
    (Al Jazeera)
23. NEW YORK — Aber Kawas becomes the first Palestinian in the NY state
    Senate, winning with 74.5% of the vote. (Al Jazeera)
24. POLAND — Russia tried to assassinate a Ukrainian rapper twice, Warsaw
    says. (Al Jazeera)
25. HEALTH — WHO chief calls for peace amid heavy fighting in Ebola-hit DR
    Congo region. (Al Jazeera)
26. SUDAN — Drone attacks kill four near Khartoum, damage a UN building.
    (Al Jazeera)
27. ARMENIA — Proposes a new constitution as a step towards peace with
    Azerbaijan. (BBC)
28. CHINA — Sets 2030 targets to boost support for older people and
    childcare. (BBC)
29. HEALTH — NHS launches the world's largest AI breast-cancer screening
    trial. (BBC)
30. BELGIUM — Cost-of-living strike cancels flights. (BBC)
31. MEXICO — Soldiers attacked in the wake of a drug lord's arrest. (BBC)
32. ECONOMY — US business activity growth eases; S&P Global flash composite
    PMI 54.6, a four-month low. (Reuters)
33. IRAN — Lifts the 2,000km limit on its ballistic missiles. (Al Jazeera)

### DATE CHECK box — visibly discarded (not Monday)
COP31 collapse (Sun 22 Nov) · Democrats win 258 House seats (Sun 22 Nov) ·
ICJ Myanmar genocide ruling (Thu 19 Nov) · Dymer strike, 11 killed
(overnight Sat–Sun) · Eisenkot "Jewish terrorism" remark (Sun 22 Nov) ·
Indonesia candy-factory fire, 32 missing (Sun 22 Nov) · Man Utd 4–0
Liverpool (Sun 22 Nov) · England's record rugby win over New Zealand
(weekend).

## Design notes
- Front-page newspaper: serif masthead "THE WORLD IN ONE DAY" with the day
  named in red, "MONDAY 23 NOVEMBER 2026". Restrained palette: ink navy,
  paper cream, one red accent.
- Three hero panels with PIL-drawn vector-style art (NVDA chip + rising
  arrow; warship + sea drones + explosion; burning tankers in a strait),
  balanced art density across the three.
- Stat band (5 figures), grid of 12 with small drawn icons, world map with
  numbered pins for stories 1–15, 18 briefs in two columns, red DATE CHECK
  box, sources/method footer.
- All art is drawn with PIL shapes in this session; no photos, no copied
  artwork. Fonts: Noto Sans / Noto Sans Display / Noto Serif (system fonts).

## Tidiness audit
- Single ordered story list in `render.py` drives hero numbers, grid
  numbers, map pins and brief numbers — all agree (1–33, checked against
  the render).
- Uniform data-chip styling (navy rounded chip, white bold caps) in heroes
  and grid; uniform brief lead-in format "N · KICKER — text" with the
  lead-in bold throughout.
- No figure is duplicated exactly between the stat band (51–48, 74.5%,
  54.6, 2,000 KM, $16.5 BN) and the grid chips (+31%, 3 KILLED, AFTER 9
  YEARS, 1ST MISSION, FROM 30 NOV, $7.5 BN, €1.582 TN, 15% OFFER, 91
  LEASES, $576 M, S&P IN CORRECTION, $1.6 BN, TIES RESTORED).
- Columns and baselines aligned (fixed grid rows, fixed brief rows);
  hero headlines all on one line at a uniform size.
- Issues found in self-inspection and fixed:
  1. Stat-band label "SENATE REJECTS CURB ON TRUMP'S IRAN WAR POWERS"
     clipped at the cell edge — shortened to "SENATE REJECTS IRAN WAR CURB".
  2. Masthead date overlapped the title's baseline — title moved up, date
     moved down, rules re-spaced.
  3. Hero 3 headline wrapped to two lines while heroes 1–2 were one line —
     headline size unified at 20px, all one line.
  4. Hormuz sun was half-hidden behind smoke circles — moved to the
     top-left; flames enlarged and seated on the tanker decks.
  5. Map pins overlapped in the Europe/Middle East cluster — pins shrunk
     (r 8→7) and nudged apart; US west-coast pins (Nvidia/Amazon) separated.
  6. DATE CHECK ✕ marks rendered as tofu boxes (U+2715 missing in Noto
     Sans) — replaced with hand-drawn red X strokes.
- Final check: full-size and 300px-wide previews inspected; composition
  reads clearly at ~300px (masthead, date, heroes, stat band, grid, map
  and DATE CHECK box all legible).
