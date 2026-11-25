# -*- coding: utf-8 -*-
"""Prolifics GCC Conclave: the full plan as one page (Artifact) and a PDF for Drive.
Content: plan_content.py (run of show, timeline, checklist, risks), data.py (people), contacts.py (email status).
Outputs: out/playbook.html (artifact body), out/Prolifics GCC Conclave - Full Plan.pdf"""
import os, sys, re, html, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from data import P, FIND
from contacts import EMAIL
from plan_content import DAY, TIMELINE, CHECK, RISKS, DECISIONS, BUDGET, BUDGET_CONTINGENCY
OUT = os.path.join(HERE, "out")
E = html.escape
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SRC = {
    "telangana": ("Telangana Today, 13 Sep 2026, FICCI and ANAROCK report", "https://telanganatoday.com/hyderabad-has-515-gccs-another-50-70-expected-within-a-year-report"),
    "jll": ("JLL, 17 Feb 2026", "https://www.jll.com/en-in/newsroom/india-s-gcc-expansion-hits-record-31-million"),
    "siasat": ("Siasat, 17 Sep 2026", "https://www.siasat.com/new-telangana-gcc-policy-to-focus-on-ai-space-semiconductors-3543873/"),
    "zinnov": ("Nasscom and Zinnov, India GCC Landscape 2026", "https://zinnov.com/centers-of-excellence/zinnov-nasscom-india-gcc-landscape-2026-report/"),
    "summit": ("Telangana Today, 11 Nov 2026", "https://telanganatoday.com/telangana-opens-registrations-for-global-summit-2026"),
    "hca": ("Construction World, 17 Nov 2026", "https://www.constructionworld.in/policy-updates-and-economic-news/hca-global-services-pre-leases-644000-sq-ft-at-mindspace/100456"),
    "westin": ("Marriott events page, The Westin Hyderabad Mindspace", "https://www.marriott.com/en-us/hotels/hydwi-the-westin-hyderabad-mindspace/events"),
    "holidays": ("Siasat, Telangana holiday list 2026", "https://www.siasat.com/list-of-general-optional-holidays-in-telangana-for-2026-3310481"),
    "qe": ("QE Conclave 2026 listing", "https://happeningnext.com/event/qe-conclave-2026-eid1ef0l8jq9vka"),
    "aaa": ("AAA, year end travel period", "https://newsroom.aaa.com/2025/12/aaa-year-end-holiday-travel-forecast/"),
    "offices": ("Prolifics locations", "https://prolifics.ai/locations"),
}
def src(k):
    t, u = SRC[k]; return '<a class="src" href="%s" target="_blank" rel="noopener">%s</a>' % (u, E(t))

def email_chip(name, tier):
    e = EMAIL.get(name)
    if tier == "R" or e is None: return '<span class="chip mute">Email not pulled</span>'
    if e.endswith("(verified)"): return '<span class="chip ok">Email verified</span>'
    if "confirm it is" in e: return '<span class="chip warn">Email verified, confirm person</span>'
    if "estimated" in e: return '<span class="chip warn">Email estimated</span>'
    return '<span class="chip route">No email: direct route</span>'

def person_rows(tier):
    rows = []
    for p in P:
        if p["tier"] != tier: continue
        f = '<span class="chip founder">Founder</span>' if p["founder"].startswith(("Yes", "Likely")) else ""
        route = p["path"]
        rows.append('<tr><td><b>%s</b><span class="sub">%s</span></td><td>%s<span class="sub">%s</span></td><td>%s</td><td>%s</td><td class="chips">%s%s</td></tr>' % (
            E(p["name"]), E(p["title"]), E(p["org"]), E(p["sector"]), E(p["session"]), E(route), f, email_chip(p["name"], tier)))
    return "".join(rows)

def guest_table(tier, title, note):
    n = sum(1 for p in P if p["tier"] == tier)
    return ('<h3>%s <span class="count">%d</span></h3><p class="note">%s</p><div class="tw"><table class="people"><thead><tr><th>Name</th><th>Organization</th><th>Role on the night</th><th>Route in</th><th>Status</th></tr></thead><tbody>%s</tbody></table></div>'
            % (E(title), n, E(note), person_rows(tier)))

# counts
tiers = {t: sum(1 for p in P if p["tier"] == t) for t in "SCGR"}
now = [p for p in P if p["tier"] != "R"]
founders = sum(1 for p in now if p["founder"].startswith(("Yes", "Likely")))
ver = sum(1 for p in now if EMAIL.get(p["name"], "").endswith("(verified)"))
est = sum(1 for p in now if "estimated" in EMAIL.get(p["name"], "") or "confirm it is" in EMAIL.get(p["name"], ""))
warm = sum(1 for p in now if "None found" in EMAIL.get(p["name"], ""))
ntask = sum(len(t) for _, t in CHECK)
owners = ["Satya", "Prolifics team"]

ros = "".join('<li><time>%s</time><div><b>%s</b><span class="who">%s</span><p>%s</p></div></li>' % (E(t), E(w), E(o), E(d)) for t, w, o, d in DAY)
tl = "".join('<li><div class="when">%s</div><div><h4>%s</h4><ul>%s</ul><p class="own">Owner: %s</p></div></li>' % (
    E(w), E(h), "".join("<li>%s</li>" % E(i) for i in items), E(o)) for w, h, items, o in TIMELINE)

def ckid(ws, i): return re.sub(r"[^a-z0-9]+", "-", ws.lower()).strip("-") + "-" + str(i)
ck = []
for ws, tasks in CHECK:
    items = "".join('<li data-owner="%s"><label for="%s"><input type="checkbox" id="%s"><span class="t">%s</span><span class="meta"><span class="own">%s</span><span class="due">%s</span></span></label></li>' % (
        E(o), ckid(ws, i), ckid(ws, i), E(t), E(o), E(d)) for i, (t, o, d) in enumerate(tasks))
    ck.append('<section class="ws"><h3>%s <span class="prog" data-ws>0 of %d</span></h3><ul class="ck">%s</ul></section>' % (E(ws), len(tasks), items))

risks = "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (E(a), E(b), E(c)) for a, b, c in RISKS)
decs = "".join("<li>%s</li>" % E(d) for d in DECISIONS)
inr = lambda v: "{:,}".format(int(round(v)))
def lakh(v): return "INR %.2f lakh" % (v / 100000.0)
b_lean = sum(r[2] for r in BUDGET); b_ceil = sum(r[3] for r in BUDGET)
c_lean = b_lean * BUDGET_CONTINGENCY; c_ceil = b_ceil * BUDGET_CONTINGENCY
T_LEAN, T_CEIL = b_lean + c_lean, b_ceil + c_ceil
bud_rows = "".join('<tr><td><b>%s</b></td><td>%s%s</td><td>%s</td><td>%s</td></tr>' % (E(a), E(b), (' <a href="%s" rel="noopener">source</a>' % E(u)) if u else "", inr(l), inr(c)) for a, b, l, c, u in BUDGET)
bud_rows += '<tr><td><b>Contingency, 10%%</b></td><td>Service charge, extra covers, AV add ons</td><td>%s</td><td>%s</td></tr>' % (inr(c_lean), inr(c_ceil))
bud_rows += '<tr><td><b>Total</b></td><td>About %s a guest at the lean figure</td><td><b>%s</b></td><td><b>%s</b></td></tr>' % (inr(T_LEAN / 20), inr(T_LEAN), inr(T_CEIL))
bud_intro = "One room, one set menu, no bar, no gifts. The lean figure is %s; the ceiling, if the Westin prices at the top of published ranges, is %s." % (lakh(T_LEAN), lakh(T_CEIL))
find = "".join("<li>%s</li>" % E(f) for f in FIND)

CSS = r"""
/* Layout: sticky contents rail on the left, one reading column on the right; collapses to one column under 900px */
:root{--paper:#FFFFFF;--panel:#F3F6FB;--ink:#0D1B3D;--muted:#5A6684;--line:#DCE3EE;--navy:#001F5B;--cyan:#00AEEF;--cyan-ink:#0077B6;
--ok:#147A4A;--ok-bg:#E3F6EC;--warn:#8A5A00;--warn-bg:#FFF4DB;--route-bg:#EEF0FF;--route:#3D3FA8;
--display:"Inter Tight","Arial",sans-serif;--body:"Inter","Arial",sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#0B1326;--panel:#121D36;--ink:#E7ECF6;--muted:#9AA7C2;--line:#24314F;--navy:#9CC3FF;--cyan:#38C6FF;--cyan-ink:#6FD3FF;
--ok:#6FDBA6;--ok-bg:#12321F;--warn:#F2C46B;--warn-bg:#3A2B0C;--route-bg:#1E2150;--route:#B4B6FF;color-scheme:dark}}
:root[data-theme="dark"]{--paper:#0B1326;--panel:#121D36;--ink:#E7ECF6;--muted:#9AA7C2;--line:#24314F;--navy:#9CC3FF;--cyan:#38C6FF;--cyan-ink:#6FD3FF;
--ok:#6FDBA6;--ok-bg:#12321F;--warn:#F2C46B;--warn-bg:#3A2B0C;--route-bg:#1E2150;--route:#B4B6FF;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font:15px/1.6 var(--body);margin:0}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:40px 80px;display:grid;grid-template-columns:200px minmax(0,1fr);gap:56px}
nav.toc{position:sticky;top:calc(env(safe-area-inset-top,0px) + 24px);align-self:start;font-size:13px}
nav.toc p{font:600 11px/1 var(--body);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}
nav.toc ol{list-style:none;margin:0;padding:0;display:grid;gap:2px;counter-reset:s}
nav.toc a{display:block;padding:5px 10px;border-radius:6px;color:var(--ink);text-decoration:none;counter-increment:s}
nav.toc a:hover,nav.toc a:focus-visible{background:var(--panel);outline:none}
main{min-width:0}
header.top{border-bottom:1px solid var(--line);padding-bottom:28px;margin-bottom:8px}
.eyebrow{font:600 12px/1 var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--cyan-ink);margin:0 0 14px}
h1{font:700 clamp(30px,4.4vw,46px)/1.08 var(--display);letter-spacing:-.02em;color:var(--navy);margin:0 0 14px;text-wrap:balance}
.lede{font-size:18px;color:var(--muted);max-width:62ch;margin:0}
.status{margin-top:18px;font-size:13px;color:var(--muted)}
.status b{color:var(--ink)}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:10px;overflow:hidden;margin-top:28px}
.facts div{background:var(--paper);padding:16px 18px}
.facts dt{font:600 11px/1 var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
.facts dd{margin:0;font:600 16px/1.35 var(--display);color:var(--ink)}
.facts dd small{display:block;font:400 13px/1.4 var(--body);color:var(--muted);margin-top:4px}
section.s{padding-top:48px;scroll-margin-top:20px}
h2{font:700 26px/1.2 var(--display);letter-spacing:-.01em;color:var(--navy);margin:0 0 6px;text-wrap:balance}
h2 .n{color:var(--cyan-ink);font-variant-numeric:tabular-nums;margin-right:10px}
.intro{color:var(--muted);margin:0 0 22px;max-width:70ch}
h3{font:600 17px/1.3 var(--display);color:var(--ink);margin:28px 0 6px}
h3 .count{font:600 12px/1 var(--body);background:var(--panel);color:var(--muted);padding:4px 8px;border-radius:20px;margin-left:6px;vertical-align:2px}
p{margin:0 0 12px}
a{color:var(--cyan-ink)}
a.src{font-size:12px;color:var(--muted)}
ul.plain{margin:0;padding-left:20px;display:grid;gap:6px}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}
.box{background:var(--panel);border-radius:10px;padding:18px 20px;min-width:0}
.box h4{font:600 13px/1 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px;margin-bottom:18px}
.stat b{display:block;font:700 34px/1 var(--display);color:var(--navy);letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.stat p{font-size:13.5px;color:var(--muted);margin:8px 0 4px}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th{text-align:left;font:600 11px/1.2 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);background:var(--panel);padding:10px 12px;white-space:nowrap}
td{padding:11px 12px;border-top:1px solid var(--line);vertical-align:top}
td .sub{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
table.people{min-width:860px}
table.people td:first-child{min-width:190px}
td.chips{white-space:nowrap}
.chip{display:inline-block;font:600 11px/1 var(--body);padding:5px 8px;border-radius:5px;margin:0 4px 4px 0}
.chip.ok{background:var(--ok-bg);color:var(--ok)}.chip.warn{background:var(--warn-bg);color:var(--warn)}
.chip.route{background:var(--route-bg);color:var(--route)}.chip.mute{background:var(--panel);color:var(--muted)}
.chip.founder{background:var(--cyan);color:#001F5B}
.call{font:600 11px/1 var(--body);padding:4px 8px;border-radius:5px;white-space:nowrap}
.call.go{background:var(--ok-bg);color:var(--ok)}.call.no{background:var(--warn-bg);color:var(--warn)}.call.mid{background:var(--panel);color:var(--muted)}
ol.ros{list-style:none;margin:0;padding:0;border-left:2px solid var(--line)}
ol.ros li{display:grid;grid-template-columns:96px minmax(0,1fr);gap:16px;padding:12px 0 12px 18px;position:relative}
ol.ros li::before{content:"";position:absolute;left:-6px;top:19px;width:10px;height:10px;border-radius:50%;background:var(--paper);border:2px solid var(--cyan)}
ol.ros time{font:600 14px/1.5 var(--display);color:var(--navy);font-variant-numeric:tabular-nums}
ol.ros b{font-family:var(--display)}
ol.ros .who{display:block;font-size:13px;color:var(--cyan-ink)}
ol.ros p{margin:2px 0 0;color:var(--muted);font-size:13.5px}
ol.tl{list-style:none;margin:0;padding:0;display:grid;gap:0}
ol.tl>li{display:grid;grid-template-columns:170px minmax(0,1fr);gap:20px;padding:18px 0;border-top:1px solid var(--line)}
ol.tl .when{font:700 15px/1.35 var(--display);color:var(--navy)}
ol.tl h4{font:600 15px/1.3 var(--display);margin:0 0 8px}
ol.tl ul{margin:0;padding-left:18px;display:grid;gap:4px;font-size:14px}
ol.tl .own{font-size:12.5px;color:var(--muted);margin:8px 0 0}
.gate{border:2px solid var(--cyan);border-radius:10px;padding:16px 20px;margin-top:20px}
.gate b{color:var(--navy)}
.filters{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:8px}
.filters span{font-size:13px;color:var(--muted);margin-right:4px}
.filters button{font:500 13px/1 var(--body);border:1px solid var(--line);background:var(--paper);color:var(--ink);padding:8px 12px;border-radius:20px;cursor:pointer}
.filters button[aria-pressed="true"]{background:var(--navy);color:var(--paper);border-color:var(--navy)}
.filters button:focus-visible,input:focus-visible{outline:2px solid var(--cyan);outline-offset:2px}
.overall{font-size:13px;color:var(--muted);margin-left:auto}
.ws h3{display:flex;align-items:baseline;gap:10px}
.prog{font:500 12px/1 var(--body);color:var(--muted);margin-left:auto;font-variant-numeric:tabular-nums}
ul.ck{list-style:none;margin:0;padding:0;border:1px solid var(--line);border-radius:10px;overflow:hidden}
ul.ck li+li{border-top:1px solid var(--line)}
ul.ck label{display:grid;grid-template-columns:22px minmax(0,1fr) auto;gap:12px;align-items:start;padding:11px 14px;cursor:pointer}
ul.ck input{width:17px;height:17px;margin:2px 0 0;accent-color:var(--navy)}
ul.ck .meta{display:flex;flex-direction:column;align-items:flex-end;gap:3px;font-size:12px;white-space:nowrap}
ul.ck .own{color:var(--cyan-ink);font-weight:600}
ul.ck .due{color:var(--muted);font-variant-numeric:tabular-nums}
ul.ck input:checked~.t{color:var(--muted);text-decoration:line-through}
ul.ck li.hide{display:none}
.mail{background:var(--panel);border-radius:10px;padding:18px 20px;font-size:14px}
.mail p:last-child{margin:0}
.mail .subj{font-weight:600}
.local{font-size:12.5px;color:var(--muted);margin:6px 0 0}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--line);font-size:13px;color:var(--muted)}
@media (max-width:900px){.wrap{grid-template-columns:minmax(0,1fr);gap:0;padding-block:24px 60px}nav.toc{display:none}
ol.tl>li{grid-template-columns:minmax(0,1fr);gap:6px}ol.ros li{grid-template-columns:minmax(0,1fr);gap:2px}
ul.ck label{grid-template-columns:22px minmax(0,1fr)}ul.ck .meta{grid-column:2;flex-direction:row;gap:12px;align-items:center}}
@media print{nav.toc,.filters,.local{display:none}.wrap{display:block;padding:0}section.s{break-inside:auto;padding-top:28px}
ol.tl>li,ol.ros li,ul.ck li,tr{break-inside:avoid}table.people{min-width:0;font-size:11px}.tw{overflow:visible}body{font-size:12.5px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

dates = [("Mon 7 to Wed 9 Dec", "no", "Avoid", "Invest Telangana Global Summit. GCC heads and the state government are all there", "summit"),
         ("Fri 11 Dec", "no", "Avoid", "QE Conclave 2026, quality engineering leaders, at HICC the same evening", "qe"),
         ("Tue 15 Dec", "mid", "Backup", "Clear of holidays and events; two fewer days to invite", "holidays"),
         ("Wed 16 Dec", "mid", "Fallback", "World Data Center Summit in Hyderabad the same day", None),
         ("Thu 17 Dec", "go", "Recommended", "22 days from the letters, a week after the summit, no Telangana holiday, no GCC event found, before US year end travel starts on 20 Dec", "aaa"),
         ("Fri 18 Dec", "no", "Avoid", "Friday evening, and the start of US year end travel", "aaa")]
date_rows = "".join('<tr><td><b>%s</b></td><td><span class="call %s">%s</span></td><td>%s%s</td></tr>' % (
    E(d), c, E(k), E(w), (" " + src(s)) if s else "") for d, c, k, w, s in dates)

BODY = """<title>Prolifics GCC Conclave Plan</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600;700&family=Inter:wght@400;500;600&display=swap">
<style>%(css)s</style>
<div class="wrap">
<nav class="toc" aria-label="Contents"><p>Contents</p><ol>
<li><a href="#glance">At a glance</a></li><li><a href="#goals">Goals</a></li><li><a href="#why">Why now</a></li><li><a href="#where">Date and venue</a></li>
<li><a href="#show">Run of show</a></li><li><a href="#list">Invite list</a></li><li><a href="#reach">Outreach</a></li><li><a href="#team">Team</a></li>
<li><a href="#timeline">Timeline</a></li><li><a href="#checklist">Checklist</a></li><li><a href="#risks">Risks</a></li><li><a href="#budget">Budget</a></li><li><a href="#decide">Decisions</a></li></ol></nav>
<main>
<header class="top" id="glance">
<p class="eyebrow">Prolifics GCC Conclave, Hyderabad</p>
<h1>Built in Hyderabad: from first desk to AI at scale</h1>
<p class="lede">An invitation only evening for the leaders who built and now run Hyderabad's global capability centers, hosted by Satya Bolli. Twenty guests, all heads of global companies' capability centers in Hyderabad, one seat per company. This is the full plan: who we invite and why, the run of show, the day by day timeline and a checklist with an owner and a date for every task.</p>
<p class="status">Plan status: <b>for approval by Satya and the Prolifics team on Monday 23 November 2026</b>. Nothing has been sent.</p>
<dl class="facts">
<div><dt>Date</dt><dd>Thursday 17 December 2026<small>5:30 to 9:30 pm. Backup Tuesday 15 December</small></dd></div>
<div><dt>Venue</dt><dd>The Westin Hyderabad Mindspace<small>Evolve private room for the whole evening</small></dd></div>
<div><dt>Host</dt><dd>Satya Bolli<small>Chairman and Managing Director, keynote</small></dd></div>
<div><dt>Room</dt><dd>20 GCC heads<small>One seat per company, plus Satya and up to 7 Prolifics hosts</small></dd></div>
<div><dt>Invitations</dt><dd>%(now)d now, %(res)d reserves<small>%(founders)d of the %(now)d set up their Hyderabad center</small></dd></div>
</dl>
</header>

<section class="s" id="goals"><h2><span class="n">1</span>Goals and how we measure them</h2>
<p class="intro">One evening that puts Satya among the people who build and run Hyderabad's GCCs, and earns a reason to meet each of them again in January.</p>
<div class="cols">
<div class="box"><h4>What success looks like</h4><ul class="plain">
<li>20 GCC heads in the room on 17 December</li><li>12 or more yeses by Friday 4 December, including at least 3 of the 4 founders</li>
<li>Every guest the head of their center, not a deputy</li>
<li>A 1:1 meeting with Satya booked in January with every guest who asks</li></ul></div>
<div class="box"><h4>What we will not do</h4><ul class="plain">
<li>No Prolifics sales pitch on stage. Satya speaks as a builder among builders</li><li>No photos or quotes from the roundtable; Chatham House rule after 7 pm</li>
<li>No deputies or plus ones: one seat per company</li><li>No guest named in public without their permission</li><li>No sales follow up before January</li></ul></div>
</div></section>

<section class="s" id="why"><h2><span class="n">2</span>Why now</h2>
<p class="intro">Hyderabad is where new GCCs land, and most of the people who set them up are still running them.</p>
<div class="stats">
<div class="stat"><b>515</b><p>GCCs in Hyderabad as of March 2026, employing more than 3 lakh people</p>%(s_tel)s</div>
<div class="stat"><b>20 to 23%%</b><p>of India's GCC market is in Hyderabad</p>%(s_jll)s</div>
<div class="stat"><b>75</b><p>new GCCs in Telangana in 2025 to 26, the most of any state</p>%(s_sia)s</div>
<div class="stat"><b>2,117</b><p>GCCs in India in FY2026</p>%(s_zin)s</div></div>
<div class="cols">
<div class="box"><h4>The founders are reachable</h4><p>Amgen, Lilly, Vanguard, McDonald's and HCA opened in 2025; Heineken, Schwab and Southwest in 2026. The people who built them are on our list (sources in the tracker).</p></div>
<div class="box"><h4>Policy momentum</h4><p>The Invest Telangana Global Summit runs 7 to 9 December and a draft state GCC policy is out. Our evening lands a week later. %(s_sum)s</p></div>
<div class="box"><h4>Prolifics is the neighbour</h4><p>Prolifics works from Mindspace Buildings 12B and 20 %(s_off)s. HCA has pre-leased 644,000 sq ft in Mindspace Building 8 %(s_hca)s, and Carrier's hub is there too.</p></div>
</div></section>

<section class="s" id="where"><h2><span class="n">3</span>Date and venue</h2>
<p class="intro">Thursday 17 December at The Westin Hyderabad Mindspace, inside the business park where Prolifics has its Hyderabad offices.</p>
<h3>Every December date we checked</h3><div class="tw"><table><thead><tr><th>Date</th><th>Call</th><th>Why</th></tr></thead><tbody>%(dates)s</tbody></table></div>
<div class="cols" style="margin-top:20px">
<div class="box"><h4>The Westin space</h4><ul class="plain"><li>Evolve private room (banquet 30, U-shape 33): one U-shape for 28</li>
<li>Keynote, roundtable and dinner in one room: no Ballroom, no Lawns, no rain plan needed</li><li>Room hire to be waived against the food spend</li><li>Inside Mindspace, Raheja IT Park, Madhapur: neighbours can walk over</li></ul><p style="margin-top:10px">%(s_wes)s</p></div>
<div class="box"><h4>If the Westin is not available</h4><ul class="plain"><li>Trident, HITEC City Main Road</li><li>ITC Kohenur, Madhapur</li>
<li>Not Novotel HICC: too large, and it hosts the QE Conclave on 11 December</li></ul></div>
</div></section>

<section class="s" id="show"><h2><span class="n">4</span>Run of show, Thursday 17 December</h2>
<p class="intro">A short keynote, one founders conversation, one closed door roundtable, then dinner. Twenty guests around one table, done by 9:30 pm on a weeknight. Guests named here are invited, not confirmed.</p>
<ol class="ros">%(ros)s</ol></section>

<section class="s" id="list"><h2><span class="n">5</span>The invite list</h2>
<p class="intro">Twenty heads of global capability centers in Hyderabad, drawn from the city's 515 GCCs %(s_tel)s, with %(res)d GCC reserves who go out one for one as declines arrive. Every name is the current head of the center, with a 2025 or 2026 source in the tracker. Sector mix of the 20: banking and finance 6, life sciences 6, healthcare 3, consumer 2, technology, industrial and travel 1 each. Work emails from Apollo: %(ver)d of the 20 verified, %(warm)d through a direct route. The emails are in the tracker, not on this page.</p>
<div class="cols"><div class="box"><h4>Corrections to the brief</h4><ul class="plain">
<li><b>Eli Lilly</b> is in. Manish Arora built the Hyderabad center, which is in Gachibowli, not Mindspace</li>
<li><b>BlackRock</b> has no Hyderabad center. Its India hubs are Gurugram and Mumbai, so it is off the list unless Satya has a direct contact</li>
<li><b>Mindspace GCCs</b> on the list: Carrier now, and HCA moving into Building 8</li></ul></div>
<div class="box"><h4>Taken off for the 20 guest room</h4><ul class="plain"><li>The IT Minister and state officials</li><li>Dr. Reddy's and Cyient leaders: Indian companies, not GCCs</li>
<li>ANSR, Zinnov, Nasscom, HYSEA and TiE: advisers and industry bodies</li><li>Second names from BMS, HCA and Evernorth: one seat per company</li>
<li>Microsoft IDC, Southwest, Medtronic and MSD move to reserves</li></ul></div>
<div class="box"><h4>More reserves to find by 30 November</h4><ul class="plain">%(find)s</ul></div></div>
%(t_g)s%(t_r)s
</section>

<section class="s" id="reach"><h2><span class="n">6</span>How we reach them</h2>
<p class="intro">Every invitation says why this person belongs in the room, not why Prolifics wants them there.</p>
<div class="tw"><table><thead><tr><th>Who</th><th>What they get from the evening</th><th>Channel</th></tr></thead><tbody>
<tr><td><b>4 founders</b></td><td>A seat in the founders conversation: how they built the center, told to peers</td><td>Satya's letter, LinkedIn note, a call from Satya within 48 hours</td></tr>
<tr><td><b>3 roundtable openers</b></td><td>Three minutes to set the agenda for how GCCs put AI into production</td><td>Satya's letter, LinkedIn note, a call from Satya</td></tr>
<tr><td><b>13 other heads</b></td><td>The founders' playbook in one evening, and nineteen peers at one table</td><td>Satya's letter, LinkedIn note, a call from the Prolifics team</td></tr>
<tr><td><b>12 reserves</b></td><td>The same seat, offered as one opens</td><td>Satya's letter, from 1 December</td></tr>
</tbody></table></div>
<h3>Channels, in order</h3><ul class="plain">
<li><b>Personal letter from Satya</b> by email from his own mailbox, with a one line reason written for each person</li>
<li><b>LinkedIn note from Satya</b> the same day, to all 20</li>
<li><b>Direct routes</b> for the two with no email: Satya's network for Manish Arora (Lilly), a hand delivered card for Kamal Sharma (Carrier, in Mindspace)</li>
<li><b>Phone</b> from Satya or the Prolifics team to all 20 within 48 hours</li><li><b>WhatsApp</b> only after a yes, for logistics</li></ul>
<h3>The messages (drafts for Satya to edit)</h3>
<div class="cols">
<div class="mail"><p class="subj">Subject: Built in Hyderabad: an evening with the founders, 17 December</p>
<p>Dear {First name},</p><p>You {built / lead} {Company}'s {center} in Hyderabad, {one line on what they did}. On Thursday 17 December I am hosting a small, invitation only evening at The Westin Hyderabad Mindspace for the leaders who built this city's global capability centers.</p>
<p>I would be honored if you would {join a short panel on building a center from zero / join us as my guest}. Twenty GCC heads around one table, one per company, a closed door roundtable and dinner, done by 9:30 pm.</p>
<p>May my office send you the details?</p><p>Warm regards,<br>Satya Bolli<br>Chairman and Managing Director, Prolifics</p></div>
<div style="display:grid;gap:14px;align-content:start">
<div class="mail"><p class="subj">LinkedIn note (under 300 characters)</p><p>{First name}, I am hosting twenty heads of Hyderabad's GCCs for an evening on 17 Dec at Mindspace, one per company. Your story building {Company}'s center belongs in that room. I have sent details by email. Satya</p></div>
<div class="mail"><p class="subj">Follow up 1, day 3, email</p><p>Confirmed so far: {two or three names, with their permission}. We are keeping it to twenty GCC heads, one per company. Can I count you in?</p></div>
<div class="mail"><p class="subj">Follow up 2, day 7, phone</p><p>Satya or the Prolifics team calls. If the date does not work, offer a 1:1 with Satya in January.</p></div></div></div>
</section>

<section class="s" id="team"><h2><span class="n">7</span>Team and roles</h2>
<div class="tw"><table><thead><tr><th>Person</th><th>Owns</th><th>On the night</th></tr></thead><tbody>
<tr><td><b>Satya Bolli</b></td><td>Signs all 20 letters, calls the 4 founders and 3 openers, approves the plan</td><td>Greets every guest, keynote, leads the founders conversation</td></tr>
<tr><td><b>Prolifics team</b></td><td>The list, the other 13 calls, all follow ups, the venue and AV, the event page, briefs, the keynote draft, print, the photographer, dietary needs, seating, the go or no go, the final count, the morning reminder, the CRM</td><td>Welcome, roundtable facilitator, room and AV, run of show, rain call, guest list at the door</td></tr>
<tr><td><b>Prolifics hosts (up to 7)</b></td><td>Named by the Prolifics team by 27 November</td><td>Each looks after two or three named guests and hosts a dinner table</td></tr>
</tbody></table></div></section>

<section class="s" id="timeline"><h2><span class="n">8</span>Timeline</h2>
<p class="intro">All 20 letters out by 25 November, go or no go on 4 December, final count to the Westin by 11 December.</p>
<ol class="tl">%(tl)s</ol>
<div class="gate"><b>Go or no go, Friday 4 December.</b> With 12 or more yeses, including at least 3 of the 4 founders, run the full evening. With 8 to 11, drop the keynote and run the roundtable and dinner. Under 8, move to January.</div>
</section>

<section class="s" id="checklist"><h2><span class="n">9</span>Checklist</h2>
<p class="intro">%(ntask)d tasks in %(nws)d workstreams, each with one owner and a due date. Filter by owner to see one person's list.</p>
<div class="filters" role="group" aria-label="Filter by owner"><span>Show</span>
<button type="button" data-f="all" aria-pressed="true">Everyone</button>%(fbtn)s<span class="overall" id="overall"></span></div>
<p class="local">Ticks are saved in this browser only. The team's shared status lives in the Checklist sheet of the invite tracker.</p>
%(ck)s
</section>

<section class="s" id="risks"><h2><span class="n">10</span>Risks and what we do</h2>
<div class="tw"><table><thead><tr><th>Risk</th><th>Why it matters</th><th>What we do</th></tr></thead><tbody>%(risks)s</tbody></table></div></section>

<section class="s" id="budget"><h2><span class="n">11</span>Lean budget</h2>
<p class="intro">%(bud_intro)s</p>
<div class="tw"><table><thead><tr><th>Line</th><th>Basis</th><th>Lean (INR)</th><th>Ceiling (INR)</th></tr></thead><tbody>%(bud_rows)s</tbody></table></div>
<p class="local">Estimates from published prices, linked in each row, until the Westin sends a written quote. Ask the hotel for: a quote for 28 dinners, room hire waived, AV included, service charge, and parking.</p></section>

<section class="s" id="decide"><h2><span class="n">12</span>Decisions for Monday 23 November</h2>
<ul class="plain">%(decs)s</ul>
<h3>Files</h3><ul class="plain">
<li>Invite tracker (names, emails, LinkedIn, status, checklist): Drive, Client Decks 2026, Prolifics, GCC Conclave</li>
<li>Plan deck (13 slides) and this plan as a PDF: same folder</li></ul></section>

<footer>Prepared 22 November 2026 for Satya Bolli and the Prolifics team. Speakers and guests named here are invited, not confirmed. Budget figures are estimates until the Westin quote arrives.</footer>
</main></div>
<script>
(function(){
  var KEY="gcc-conclave-checklist-v1", state={};
  try{state=JSON.parse(localStorage.getItem(KEY)||"{}")}catch(e){state={}}
  var boxes=[].slice.call(document.querySelectorAll("ul.ck input"));
  boxes.forEach(function(b){ if(state[b.id]) b.checked=true; b.addEventListener("change",function(){ state[b.id]=b.checked; try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){} tally(); }); });
  var filter="all";
  function tally(){
    var done=0,shown=0;
    document.querySelectorAll("section.ws").forEach(function(ws){
      var items=[].slice.call(ws.querySelectorAll("li")), vis=0, d=0;
      items.forEach(function(li){ var on=filter==="all"||li.dataset.owner.indexOf(filter)>-1; li.classList.toggle("hide",!on); if(on){vis++; if(li.querySelector("input").checked) d++;} });
      ws.hidden = vis===0; ws.querySelector(".prog").textContent=d+" of "+vis+" done"; done+=d; shown+=vis;
    });
    document.getElementById("overall").textContent=done+" of "+shown+" done";
  }
  document.querySelectorAll(".filters button").forEach(function(btn){ btn.addEventListener("click",function(){
    filter=btn.dataset.f; document.querySelectorAll(".filters button").forEach(function(x){x.setAttribute("aria-pressed",String(x===btn))}); tally(); }); });
  tally();
})();
</script>
""" % dict(css=CSS, now=len(now), res=tiers["R"], founders=founders, ver=ver, est=est, warm=warm,
          s_tel=src("telangana"), s_jll=src("jll"), s_sia=src("siasat"), s_zin=src("zinnov"), s_sum=src("summit"), s_off=src("offices"), s_hca=src("hca"), s_wes=src("westin"),
          dates=date_rows, ros=ros, find=find,
          t_g=guest_table("G", "The 20", "Heads of global companies' capability centers. Seven have a role on the night; the rest join the roundtable and dinner."),
          t_r=guest_table("R", "Reserves", "All GCC heads. One goes out for each decline, so the room never passes 20. Emails for 8 are pulled before sending."),
          tl=tl, ntask=ntask, nws=len(CHECK), bud_rows=bud_rows, bud_intro=E(bud_intro), fbtn="".join('<button type="button" data-f="%s" aria-pressed="false">%s</button>' % (o, o) for o in owners),
          ck="".join(ck), risks=risks, decs=decs)

os.makedirs(OUT, exist_ok=True)
page = os.path.join(OUT, "playbook.html"); open(page, "w", encoding="utf-8").write(BODY)
full = os.path.join(OUT, "playbook-print.html")
open(full, "w", encoding="utf-8").write('<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + BODY + "</body></html>")
pdf = os.path.join(OUT, "Prolifics GCC Conclave - Full Plan.pdf")
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=6000", "--print-to-pdf=" + pdf, "file://" + full], capture_output=True, timeout=180)
txt = re.sub(r"<[^>]+>", " ", re.sub(r"<(style|script)\b.*?</\1>", "", BODY, flags=re.S))
print("bytes", len(BODY), "pdf", os.path.exists(pdf), "tasks", ntask, "verified", ver, "confirm", est, "warm", warm,
      "dashes", len(re.findall("[–—]", BODY)), "excl", txt.count("!"))

# Standalone copy for Vercel (noindex, private preview link)
SITE = os.path.join(HERE, "site"); os.makedirs(SITE, exist_ok=True)
open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(
    '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<meta name="robots" content="noindex,nofollow"></head><body>' + BODY + "</body></html>")
open(os.path.join(SITE, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
open(os.path.join(SITE, "vercel.json"), "w").write(json.dumps({"headers": [{"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}]}, indent=2))
print("site", SITE)
