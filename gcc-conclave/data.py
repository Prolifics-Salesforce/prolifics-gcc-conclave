# -*- coding: utf-8 -*-
"""Prolifics GCC Conclave, Hyderabad, 17 Dec 2026: the invite list. Built 21 Nov 2026 from research-lifesciences.md,
research-bfsi-tech.md and research-ecosystem.md (every role has a 2025 or 2026 source there). Apollo column: result of a
free Apollo people search on 21 Nov 2026 (no credits used). Emails are not pulled yet: that needs approval (credits)."""

# tier: S = speaker or anchor, C = marquee CEO or CXO, G = GCC leader guest, R = reserve
# fields: tier, name, title, org, sector, founder, center, why, session, path, apollo, conf, src
P = []
def add(*a):
    keys = "tier name title org sector founder center why session path apollo conf src".split()
    P.append(dict(zip(keys, a)))

# ---------- Speakers and anchors (12) ----------
add("S", "D. Sridhar Babu", "Minister for IT, Electronics and Communications, Industries and Commerce", "Government of Telangana", "Government", "",
    "Owns the state GCC push and the draft GCC policy", "Inaugurated the Mars GCC (12 Nov 2026); a minister in the room lifts acceptance from every GCC head",
    "Chief guest, opening address", "Formal letter to the Minister's office from Satya, plus a request through HYSEA", "Not checked", "High",
    "https://www.deccanchronicle.com/amp/southern-states/telangana/sridhar-babu-inaugurates-mars-global-capability-centre-in-hyderabad-2003765")
add("S", "Mamatha Madireddy", "Managing Director and Head, HSBC Global Service Centres India; GCC Council Chair, Nasscom", "HSBC", "BFSI", "",
    "HSBC Technology and service centres across Hyderabad, Pune and Bengaluru", "Hyderabad's most visible GCC voice; gave the chair's address at the Nasscom GCC Summit",
    "Keynote: the state of Hyderabad's GCCs", "Satya direct, then Nasscom GCC council", "Verified: Managing Director, HSBC", "Medium (council scope differs by source)",
    "https://thenasscomgccsummit2026.sched.com/list/descriptions")
add("S", "Lalit Ahuja", "Co-founder and CEO", "ANSR", "GCC enabler", "Built many",
    "ANSR has set up more than 250 GCCs, about 30% of them in Hyderabad, including Marriott Tech Accelerator", "Knows every founder on the list; the natural moderator for the founders panel",
    "Moderator, Panel 1 (founders)", "Satya direct; ANSR also helps fill the room", "Verified: Co-founder and CEO, ANSR", "Medium",
    "https://www.deccanchronicle.com/nation/in-other-news/gccx-hyderabad-2026-concludes-as-south-indias-largest-gcc-ai-leadership-summit-1975497")
add("S", "Pari Natarajan", "CEO and Co-founder", "Zinnov", "GCC enabler", "",
    "Co-publisher of the Nasscom and Zinnov India GCC Landscape FY2026", "Brings the data; a draw for heads who track the benchmarks",
    "Moderator, Panel 2 (AI in production)", "Satya direct", "Not checked", "High",
    "https://zinnov.com/centers-of-excellence/zinnov-nasscom-india-gcc-landscape-2026-report/")
add("S", "Naveen Gullapalli", "Managing Director, Amgen India", "Amgen", "Life sciences", "Yes (Amgen, and built Novartis Hyderabad before that)",
    "Opened Feb 2025 in HITEC City, USD 200M, capacity up to 3,000", "Has founded two of Hyderabad's largest pharma GCCs: the strongest builder story in the city",
    "Panel 1: built here from zero", "Satya direct letter, LinkedIn note from Satya", "Verified: Managing Director, Amgen India", "High",
    "https://www.business-standard.com/technology/tech-news/amgen-opens-200-million-technology-and-innovation-hub-in-hyderabad-125022401027_1.html")
add("S", "Manish Arora", "Managing Director, Lilly Capability Centre India, Hyderabad", "Eli Lilly", "Life sciences", "Yes",
    "Announced Jan 2025, opened Aug 2025 in Phoenix Equinox, Gachibowli; plan 1,500 people", "Took Lilly's Hyderabad center from announcement to opening in seven months",
    "Panel 1: built here from zero", "Satya direct letter, LinkedIn note from Satya", "Verified: Managing Director, Lilly Hyderabad", "High",
    "https://www.indianpharmapost.com/news/lilly-to-establish-new-global-capability-centre-in-hyderabad-16647")
add("S", "Venkatesh Natarajan", "Principal and Head of Vanguard India", "Vanguard", "BFSI", "Yes",
    "First India GCC, opened Nov 2025; about 300 people by end 2025, target about 2,300 by 2029", "Built one of the world's largest fund managers' first India center in under a year",
    "Panel 1: built here from zero", "Satya direct letter, LinkedIn note from Satya", "Verified: Managing Director, Vanguard India", "High",
    "https://www.business-standard.com/companies/news/vanguard-global-value-center-hyderabad-125110301174_1.html")
add("S", "Vineeth Suresh", "Director and India Head, HEINEKEN Business Services", "Heineken", "Consumer", "Yes",
    "First Heineken GCC, opened 29 Apr 2026 in the Financial District; about 1,600 projected", "The newest consumer GCC founder; brings the setup lessons fresh",
    "Panel 1: built here from zero", "Satya direct letter, LinkedIn note from Satya", "Verified: Director and India Head, HBS", "High",
    "https://telanganatoday.com/heineken-opens-global-capability-centre-in-hyderabad")
add("S", "Sumeet Mathur", "SVP and Managing Director, ServiceNow India Technology and Business Centre", "ServiceNow", "Technology", "",
    "ServiceNow's largest site outside the US, Hyderabad", "Runs a product engineering site with a strong AI productivity story",
    "Panel 2: AI in production", "Satya direct; Prolifics ServiceNow practice", "Verified: SVP and MD, ServiceNow India", "High",
    "https://yourstory.com/enterprise-story/2025/07/hyderabad-servicenow-india-hopes-to-ride-ai-wave")
add("S", "Mrinal Duggal", "Head of Sanofi Global Services, Hyderabad Hub", "Sanofi", "Life sciences", "Yes (grew the hub from zero to 3,000)",
    "Expanded 16 Feb 2026 to a capacity of about 4,500 in Hitech City", "GCC Country Leader of the Year 2025; a builder and an AI scale story in one",
    "Panel 2: AI in production", "Satya direct letter, LinkedIn note from Satya", "Verified: Head of Sanofi Global Services, Hyderabad Hub", "High",
    "https://www.sanofi.com/assets/countries/india/docs/Media/press-releases/2026/press-release-sanofi-expands-its-Hyderabad-GCC-to-grow-capabilities-and-drive-innovation.pdf")
add("S", "Kamal Sharma", "GCC Leader (China, India and Mexico) and CDO AMEA, Carrier", "Carrier", "Industrial", "Yes (first employee of Carrier's digital hub, 2019)",
    "Carrier Digital Hub; Hyderabad address is Raheja Mindspace, Madhapur", "A Mindspace neighbour and a founder; AIM Top 25 GCC Head 2026",
    "Panel 2: AI in production", "Mindspace neighbour: walk-over invite plus Satya letter", "Verified: GCC Leader and CDO AMEA, Carrier", "High",
    "https://analyticsindiamag.com/lists/top-25-gcc-heads-in-india-2026/kamal-sharma")
add("S", "Atul Kapoor", "Vice President and Hyderabad Center Head, HCA Healthcare India", "HCA Healthcare", "Healthcare", "Yes",
    "Opened Sep 2025; pre-leased 644,000 sq ft in Mindspace Building 8 from Sep 2027", "Fastest scaling healthcare GCC in the city and Mindspace's newest big tenant",
    "Panel 2: AI in production", "Mindspace neighbour (incoming) plus Satya letter", "Verified: VP, Hyderabad Center Head, HCA Healthcare India", "High",
    "https://www.constructionworld.in/policy-updates-and-economic-news/hca-global-services-pre-leases-644000-sq-ft-at-mindspace/100456")

# ---------- Marquee CEOs and CXOs (4) ----------
add("C", "G.V. Prasad", "Co-Chairman and Managing Director", "Dr. Reddy's Laboratories", "Life sciences", "",
    "Hyderabad pharma leader", "A marquee Hyderabad CEO who draws the life sciences GCC heads", "Guest of honour at the dinner",
    "Satya direct call", "Not checked", "High", "https://medicaldialogues.in/amp/news/industry/pharma/dr-reddys-labs-reappoints-g-v-prasad-as-co-chairman-md-148080")
add("C", "Krishna Bodanapu", "Executive Vice Chairman and Managing Director", "Cyient", "Engineering", "",
    "Hyderabad engineering services leader", "Peer CEO from a Hyderabad-born global firm", "Guest; closing roundtable voice",
    "Satya direct call", "Not checked", "Medium", "https://www.whalesbook.com/corporate-news/English/tech/Cyient-Board-Approves-Bodanapu-as-MD-Shareholder-Vote-Required/69cbf2673f30946a723a42fc")
add("C", "B.V.R. Mohan Reddy", "Founder Chairman, Cyient; former Nasscom chairman", "Cyient", "Engineering", "Built Cyient",
    "Founding director of T-Hub", "Elder statesman of Hyderabad tech; draws founders and GCC heads", "Guest of honour; alternate chief guest",
    "Satya direct call", "Not checked", "Medium", "https://newsmeter.in/business/interview-dr-bvr-mohan-reddy-explains-cyients-push-for-grassroots-ai-education-in-govt-schools-764061")
add("C", "Rajiv Kumar", "Managing Director and President, Microsoft India Development Center", "Microsoft", "Technology", "",
    "IDC headquartered in Hyderabad since 1998; new campus opened 2025", "Leads one of the largest US GCCs in Hyderabad", "Guest; stretch keynote",
    "Satya direct letter", "Not found in Apollo search", "High", "https://analyticsindiamag.com/ai-news-updates/microsoft-opens-new-hyderabad-campus-partners-with-telangana-govt-for-ai-growth/")

# ---------- GCC leader guests (14) ----------
add("G", "Pradeep Menon", "Country Head and Managing Director, Schwab India", "Charles Schwab", "BFSI", "Yes",
    "Opened 19 Aug 2026 in Phoenix Equinox Tower 2, Gachibowli; about 2,000 by end 2027", "Newest large US brokerage GCC; ran HSBC's India technology GCC before",
    "Guest; Panel 1 backup", "Satya letter, LinkedIn", "Verified: Country Head and MD, Charles Schwab India", "High",
    "https://analyticsindiamag.com/ai-news/charles-schwab-opens-hyderabad-tech-centre-as-telangana-bets-big-on-capital-markets-gcc/")
add("G", "Deshant Kaila", "Head, McDonald's Global Business Services India", "McDonald's", "Consumer", "Yes",
    "Global Office opened 29 Oct 2025 in RMZ Nexity, HITEC City; 1,200 to 1,500 seats", "Founding head of one of McDonald's largest offices outside the US",
    "Guest; Panel 1 backup", "Satya letter, LinkedIn", "Verified: Head McDonald's GBS Operations", "Medium (title varies by source)",
    "https://www.projectstoday.ai/News/McDonalds-opens-new-global-office-in-Hyderabad")
add("G", "Sirisha Voruganti", "CEO and Managing Director, Lloyds Technology Centre", "Lloyds Banking Group", "BFSI", "Yes",
    "Opened 2023 in Knowledge City", "Founding CEO of a UK bank's first India tech centre; Nasscom executive council member",
    "Guest; Panel 2 backup", "Satya letter, Nasscom", "Apollo shows Nasscom Executive Council Member as her main record: confirm the Lloyds role", "High (2026 speaker listing)",
    "https://asia.money2020.com/program/speakers/sirisha-voruganti-s101-110601")
add("G", "Krishna Kallepalli", "VP and Global Head of Innovation, India", "Southwest Airlines", "Travel", "Likely",
    "First Southwest innovation center outside the US, opened 20 May 2026 at Sattva Knowledge City", "A first-of-its-kind airline GCC, 2026 opening",
    "Guest", "Satya letter, LinkedIn", "Verified: VP and Global Head of Innovation, India", "High",
    "https://www.deccanchronicle.com/amp/business/companies/krishna-kallepalli-on-southwest-airlines-building-its-future-from-hyderabad-1957981")
add("G", "Vamsi Tekuru", "VP Technology and Managing Director, Hyderabad", "Bristol Myers Squibb", "Life sciences", "",
    "BMS Hyderabad opened Feb 2024, USD 100M", "Newest pharma GCC MD in the city (appointed 28 Oct 2026)",
    "Guest", "Satya letter, LinkedIn", "Verified: VP Technology and Managing Director, BMS", "High (Apollo confirms the Oct 2026 source)",
    "https://www.cxodigitalpulse.com/?p=64241")
add("G", "Vidhya Sundaram", "AVP Global Technology Centers and Hyderabad Tech Center Lead", "MSD (Merck)", "Life sciences", "",
    "Expanded 250,000 sq ft Hitech City center opened 10 Sep 2026", "New in role (Sep 2026), ex Eli Lilly",
    "Guest", "Satya letter, LinkedIn", "Not found in Apollo search", "High",
    "https://www.biospectrumindia.com/public/news/66/28560/msd-appoints-vidhya-sundaram-as-associate-vice-president-global-technology-centers-and-hyderabad-tech-center-lead.html")
add("G", "Anil Raghav", "Managing Director, Zoetis India Capability Center", "Zoetis", "Life sciences", "Led the 2024 expansion",
    "Hyderabad center expanded Sep 2024", "Animal health data and AI hiring", "Guest", "Satya letter, LinkedIn",
    "Verified: MD and Board Director, Zoetis India Capability Center", "High",
    "https://www.cxodigitalpulse.com/anil-raghav-appointed-as-managing-director-of-zoetis-india-capability-center/")
add("G", "Ganpat Anchaliya", "Site Head, Novartis Corporate Center Hyderabad", "Novartis", "Life sciences", "",
    "Novartis's largest corporate center worldwide, 8,000+ associates", "Runs the biggest pharma GCC in the city", "Guest",
    "Satya letter, LinkedIn", "Verified: Site Head, Novartis Corporate Center, Hyderabad", "Medium (company page undated; Apollo confirms)",
    "https://www.novartis.com/in-en/about/india-country-leadership-team")
add("G", "Prashanti Bodugum", "Head of Evernorth India", "Evernorth (The Cigna Group)", "Healthcare", "",
    "Opened Nov 2024, Cigna's first innovation hub outside the US", "Led a GCC at Walmart Global Tech before", "Guest",
    "Satya letter, LinkedIn", "Not found in Apollo search", "High",
    "https://www.mediainfoline.com/movement/evernorth-appoints-prashanti-bodugum-as-new-head-of-hyderabad-innovation-hub")
add("G", "Murali Krishna", "Chief Global Officer and Country Head, Providence India", "Providence", "Healthcare", "",
    "500,000 sq ft Hi-Tech City office since Feb 2024", "AIM Top 25 GCC Heads 2026", "Guest",
    "Satya letter, LinkedIn", "Verified: Chief Global Officer and Country Head, Providence", "High",
    "https://analyticsindiamag.com/lists/top-25-gcc-heads-in-india-2026/murali-krishna")
add("G", "Rachana Bahadur", "SVP and Country Head, India", "Synchrony", "BFSI", "",
    "Largest Synchrony Global Experience Center opened in Hyderabad, Jul 2026", "AIM Top 25 GCC Head 2026", "Guest",
    "Satya letter, LinkedIn", "Verified: Country Head, Synchrony", "High",
    "https://analyticsindiamag.com/ai-news/synchrony-opens-its-largest-global-experience-center-in-hyderabad")
add("G", "Rajesh Mani", "GCC Managing Director, Citizens Financial Group India", "Citizens Financial Group", "BFSI", "First named MD",
    "GCC set up Apr 2025 at GMR Infobahn, Kokapet", "New in seat (Jul 2026), steering a build-operate GCC", "Guest",
    "Satya letter, LinkedIn", "Verified: MD, Citizens Financial Group India GCC", "High",
    "https://investor.citizensbank.com/about-us/newsroom/latest-news/2026/2026-07-21.aspx")
add("G", "Shameel Sharma", "Managing Director and Site Leader, Marriott Tech Accelerator", "Marriott International", "Travel", "",
    "First hospitality GCC in India, set up with ANSR, inaugurated Nov 2025", "Runs the first hospitality GCC; ANSR is a warm path", "Guest",
    "Via Lalit Ahuja (ANSR) plus Satya letter", "Not found in Apollo search", "High",
    "https://hrtoday.in/shameel-sharma-appointed-as-managing-director-of-marriott-tech-accelerator/")
add("G", "Divya Prakash Joshi", "VP Engineering and board member, Medtronic Engineering and Innovation Center", "Medtronic", "Life sciences", "",
    "Medtronic's largest R&D center outside the US, Hyderabad since 2011", "Engineering and product innovation story", "Guest",
    "Satya letter, LinkedIn", "Not found in Apollo search", "Medium (title changed in 2026)",
    "https://www.deccanchronicle.com/southern-states/telangana/we-have-evolved-into-an-innovation-partner-divya-prakash-joshi-1977451")

# ---------- Reserves (16): invite as confirmations come in or a seat opens ----------
R = [
 ("B. Ajith Reddy", "CEO and MD, Invest Telangana", "Government of Telangana", "Government", "Fresh from the 7 to 9 Dec summit's GCC MoUs; alternate government voice", "https://telanganatoday.com/major-ias-reshuffle-in-telangana-changes-made-in-cmo-and-departments"),
 ("Matthias Schacke", "Head, India Service Company, UBS", "UBS", "BFSI", "New Gachibowli GCC opened Feb 2026; verify vs Sameer Chothani", "https://www.ubs.com/global/en/media/display-page-ndp/en-20260211-hyderabad-new-office.html"),
 ("Mohit Dhingra", "Founding MD, BMS Hyderabad (current role to confirm)", "Bristol Myers Squibb", "Life sciences", "Launched BMS Hyderabad in Feb 2024; may have moved roles", "https://analyticsindiamag.com/lists/top-life-sciences-and-healthcare-gcc-heads-in-india-2026"),
 ("Emily Duncan", "SVP, Global Capability Network", "HCA Healthcare", "Healthcare", "US based owner of HCA's GCC network; only if travelling", "https://biospectrumindia.com/news/16/26722/hca-healthcare-sets-up-global-capability-centre-in-hyderabad.html"),
 ("Ashok Venkatachalam", "Founding MD, Evernorth India (new role not stated)", "Evernorth", "Healthcare", "Founder story; current title unknown", "https://www.mediainfoline.com/movement/evernorth-appoints-prashanti-bodugum-as-new-head-of-hyderabad-innovation-hub"),
 ("Chandra Gupta", "VP IT Operations and site leader, TMUS Global Solutions India", "T-Mobile US", "Telecom", "New telecom GCC opened Jun 2026", "https://www.siasat.com/t-mobile-opens-new-global-technology-centre-in-hyderabad-3483117/"),
 ("Abhishek Dhasmana", "VP and GM, Fanatics India", "Fanatics", "Consumer", "Hyderabad tech centre moving to a larger HITEC City office", "https://telanganatoday.com/fanatics-announces-new-digital-sports-innovation-centre-in-hyderabad-to-boost-ai-initiatives-and-high-impact-workforce-growth"),
 ("Rohin Govindarajan", "MD, Chubb Business Services India", "Chubb", "BFSI", "Insurance GCC, about 4,000 technologists; base city to confirm", "https://analyticsindiamag.com/lists/top-25-gcc-heads-in-india-2026/rohin-govindarajan"),
 ("Uma Ratnam Krishnan", "Managing Director, Optum India", "Optum", "Healthcare", "Large healthcare GCC with Hyderabad delivery; national role", "https://www.optum.in/about/news/uma-ratnam-krishnan-top-gcc-leader-2026.html"),
 ("Srinath Venkatesh", "MD India and South Asia", "Thermo Fisher Scientific", "Life sciences", "Opened Genome Valley centers Nov 2025; country role", "https://www.indianpharmapost.com/news/thermo-fisher-opens-two-new-centers-in-hyderabad-18342"),
 ("Rajesh Nambiar", "President", "Nasscom", "Industry body", "National GCC voice; stretch", "https://www.businesstoday.in/technology/story/indias-ai-first-gccs-are-reshaping-global-enterprise-strategy-nasscoms-rajesh-nambiar-532412-2026-05-20"),
 ("Bipin Pendyala", "President, HYSEA (2026 to 28)", "HYSEA", "Industry body", "Co-host candidate; route to the Minister's office", "https://deccanchronicle.com/business/in-other-news/ysea-elects-flt-lt-bipin-pendyala-as-its-new-president-at-the-34th-annual-general-body-meeting-unveils-new-managing-committee-for-2026-28-1953817"),
 ("Murali Kakarla", "President, TiE Hyderabad (2026)", "TiE Hyderabad", "Industry body", "Founder and investor network", "https://hyderabadnewshunt.com/murali-kakarla-elected-tie-hyderabad-president-2026/"),
 ("Uday Odedra", "EVP, Head of India and the Philippines", "Wells Fargo", "BFSI", "Large Hyderabad centres; Bengaluru based national head", "https://analyticsindiamag.com/lists/top-25-gcc-heads-in-india-2026/uday-odedra"),
 ("Vibhavari Jahagirdar", "Head of Global Technology for India", "JPMorgan Chase", "BFSI", "JPMorgan Hyderabad since 2011", "https://www.jpmorganchase.com/about/technology/blog/devup-hyderabad-2025"),
 ("Anudeep Durishetty", "Joint Secretary, ITE&C", "Government of Telangana", "Government", "Working-level ITE&C contact", "https://www.deccanchronicle.com/amp/southern-states/telangana/gccs-set-to-drive-invest-telangana-global-summit-2026-1993973"),
]
for n, t, o, s, why, src in R:
    add("R", n, t, o, s, "", "", why, "Reserve", "Satya letter when a seat opens", "Not checked", "Medium", src)

# Mindspace neighbours with no named head yet: find the site head before 30 Nov
FIND = ["Bank of America (BA Continuum), Mindspace", "Qualcomm, Mindspace", "Verizon, Mindspace", "AMD, Mindspace",
        "HighRadius (Hyderabad-founded), Mindspace", "Goldman Sachs, Hyderabad", "LSEG, Hyderabad", "Regeneron, Hyderabad (opening 2026)"]

TIER = {"S": "Speaker or anchor", "C": "Marquee CEO or CXO", "G": "GCC leader guest", "R": "Reserve"}

# ---- 22 Nov 2026, brief: "We need total 20 guests only. All are GCC people" ----
# The room is 20 heads of global companies' capability centers in Hyderabad (from the city's 515 GCCs).
# No minister, no Indian company CEOs, no moderators from advisory firms or industry bodies.
ROOM = ["Mamatha Madireddy", "Naveen Gullapalli", "Manish Arora", "Venkatesh Natarajan", "Vineeth Suresh", "Sumeet Mathur",
        "Mrinal Duggal", "Kamal Sharma", "Atul Kapoor", "Pradeep Menon", "Deshant Kaila", "Sirisha Voruganti", "Vamsi Tekuru",
        "Anil Raghav", "Ganpat Anchaliya", "Prashanti Bodugum", "Murali Krishna", "Rachana Bahadur", "Rajesh Mani", "Shameel Sharma"]
RESERVE = ["Krishna Kallepalli", "Divya Prakash Joshi", "Vidhya Sundaram", "Rajiv Kumar", "Matthias Schacke", "Chandra Gupta",
           "Abhishek Dhasmana", "Rohin Govindarajan", "Uma Ratnam Krishnan", "Srinath Venkatesh", "Uday Odedra", "Vibhavari Jahagirdar"]
ROLE = {"Naveen Gullapalli": "Founders conversation", "Manish Arora": "Founders conversation", "Venkatesh Natarajan": "Founders conversation",
        "Vineeth Suresh": "Founders conversation", "Mamatha Madireddy": "Opens the roundtable", "Sumeet Mathur": "Opens the roundtable",
        "Mrinal Duggal": "Opens the roundtable", "Pradeep Menon": "Guest; founders conversation backup", "Deshant Kaila": "Guest; founders conversation backup",
        "Atul Kapoor": "Guest; founders conversation backup", "Kamal Sharma": "Guest; Mindspace neighbour"}
DROPPED = [p["name"] for p in P if p["name"] not in ROOM + RESERVE]
for p in P:
    p["tier"] = "G" if p["name"] in ROOM else "R"
    if p["name"] in ROOM: p["session"] = ROLE.get(p["name"], "Guest; roundtable")
    elif p["name"] in RESERVE: p["session"] = "Reserve"
    if "ANSR" in p["path"]: p["path"] = "Satya letter, LinkedIn"
    if p["path"].startswith("Satya direct letter, LinkedIn note"): p["path"] = "Satya letter, LinkedIn note, call within 48 hours"
P = [p for p in P if p["name"] in ROOM + RESERVE]
P.sort(key=lambda p: (p["tier"] != "G", (ROOM + RESERVE).index(p["name"])))
FIND = [f for f in FIND if "HighRadius" not in f]
TIER = {"G": "GCC leader (invited)", "R": "GCC reserve"}
