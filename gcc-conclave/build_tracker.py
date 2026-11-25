# -*- coding: utf-8 -*-
"""Invite tracker for the Prolifics GCC Conclave (17 Dec 2026). Arial, frozen header, status dropdown. Data: data.py."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from data import P, FIND, TIER
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
OUT = os.path.join(HERE, "out", "Prolifics GCC Conclave - Invite Tracker.xlsx")

from contacts import LI, EMAIL
from plan_content import CHECK, TIMELINE, BUDGET, BUDGET_CONTINGENCY
CALL7 = {"Naveen Gullapalli", "Manish Arora", "Venkatesh Natarajan", "Vineeth Suresh", "Mamatha Madireddy", "Sumeet Mathur", "Mrinal Duggal"}
OWNER = {"G": "Satya (letter), Prolifics team (call)", "R": "Prolifics team"}
WAVE = {"G": "Letter 24 to 25 Nov", "R": "One for one per decline, from 1 Dec"}

NAVY, CY = "001F5B", "00AEEF"
F = lambda **k: Font(name="Arial", size=k.pop("size", 10), **k)
thin = Side(style="thin", color="E4E8F0")
wb = Workbook()
ws = wb.active; ws.title = "Invite list"
cols = [("#", 5), ("Tier", 18), ("Name", 22), ("Title", 40), ("Organization", 22), ("Sector", 14), ("Set up the Hyderabad center?", 18),
        ("Hyderabad center", 42), ("Why invite", 46), ("Ask at the event", 26), ("Route in", 30), ("Apollo check, 21 Nov", 30), ("Confidence", 16),
        ("Work email (Apollo, 22 Nov)", 40), ("LinkedIn", 30), ("Owner", 22), ("Wave", 20), ("Status", 12), ("Next step", 26), ("Next date", 12), ("Source", 50)]
ws.append(["Prolifics GCC Conclave, Hyderabad. Thursday 17 December 2026, The Westin Hyderabad Mindspace. 5:30 to 9:30 pm. 20 GCC heads only, one seat per company. Invite tracker, updated 22 November 2026."])
ws["A1"].font = F(size=13, bold=True, color=NAVY)
ws.append(["Every role has a 2025 or 2026 source (last column). Confirm each title on LinkedIn before sending. Work emails pulled from Apollo on 22 Nov 2026; 8 reserves not pulled yet. Rows marked None found go through a warm route."])
ws["A2"].font = F(size=9, italic=True, color="6B7690")
ws.append([c for c, _ in cols])
for i, (c, w) in enumerate(cols, 1):
    cell = ws.cell(row=3, column=i); cell.font = F(bold=True, color="FFFFFF", size=9); cell.fill = PatternFill("solid", fgColor=NAVY)
    cell.alignment = Alignment(wrap_text=True, vertical="center"); ws.column_dimensions[cell.column_letter].width = w
fills = {"G": "FFFFFF", "R": "FAFAFA"}
for n, p in enumerate(P, 1):
    ws.append([n, TIER[p["tier"]], p["name"], p["title"], p["org"], p["sector"], p["founder"] or "", p["center"], p["why"], p["session"], p["path"],
               p["apollo"], p["conf"], EMAIL.get(p["name"], "Not pulled (reserve)"), LI.get(p["name"], ""), ("Satya (letter and call)" if p["name"] in CALL7 else OWNER[p["tier"]]), WAVE[p["tier"]], "To send", "", "", p["src"]])
    r = ws.max_row
    for c in range(1, len(cols) + 1):
        cell = ws.cell(row=r, column=c); cell.font = F(size=9, bold=(c == 3)); cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.fill = PatternFill("solid", fgColor=fills[p["tier"]]); cell.border = Border(bottom=thin)
    if p["apollo"].startswith(("Not found", "Apollo shows")):
        ws.cell(row=r, column=12).font = F(size=9, color="8A5A00", bold=True)
    e = ws.cell(row=r, column=14).value or ""
    if not e.endswith("(verified)"): ws.cell(row=r, column=14).font = F(size=9, color="8A5A00", bold=True)
    for c in (15, 21):
        v = ws.cell(row=r, column=c).value
        if v and v.startswith("http"): ws.cell(row=r, column=c).hyperlink = v; ws.cell(row=r, column=c).font = F(size=9, color="0077B6", underline="single")
dv = DataValidation(type="list", formula1='"To send,Sent,Replied,Yes,Maybe,No,Declined, offer January 1:1"', allow_blank=True)
ws.add_data_validation(dv); dv.add("R4:R%d" % ws.max_row)
ws.freeze_panes = "D4"; ws.auto_filter.ref = "A3:U%d" % ws.max_row

w2 = wb.create_sheet("Names to find")
w2.append(["Company", "Why", "Owner", "By"]);
for f in FIND:
    w2.append([f, "Mindspace neighbour" if "Mindspace" in f else "Large Hyderabad GCC with no named head in our research", "Prolifics team", "30 Nov 2026"])
w2.append(["BlackRock", "No Hyderabad center: India hubs are Gurugram and Mumbai. Off the list unless Satya has a direct contact", "Prolifics team", "Decision 23 Nov"])
for i, w in enumerate((44, 70, 10, 16), 1): w2.column_dimensions["ABCD"[i - 1]].width = w

w3 = wb.create_sheet("Timeline")
w3.append(["When", "What", "Owner"])
for w_, h_, items_, o_ in TIMELINE:
    row = (w_, h_ + ": " + "; ".join(items_), o_)
    w3.append(list(row))
for i, w in enumerate((22, 100, 22), 1): w3.column_dimensions["ABC"[i - 1]].width = w
w4 = wb.create_sheet("Checklist", 1)
w4.append(["#", "Workstream", "Task", "Owner", "Due", "Status", "Notes"])
k = 0
for wsn, tasks in CHECK:
    for t_, o_, d_ in tasks:
        k += 1; w4.append([k, wsn, t_, o_, d_, "To do", ""])
for i, w in enumerate((5, 24, 90, 18, 14, 13, 40), 1): w4.column_dimensions["ABCDEFG"[i - 1]].width = w
dv4 = DataValidation(type="list", formula1='"To do,In progress,Done,Blocked,Not needed"', allow_blank=True)
w4.add_data_validation(dv4); dv4.add("F2:F%d" % w4.max_row)
w4.freeze_panes = "C2"; w4.auto_filter.ref = "A1:G%d" % w4.max_row
for sh in (w2, w3, w4):
    for c in sh[1]: c.font = F(bold=True, color="FFFFFF", size=9); c.fill = PatternFill("solid", fgColor=NAVY)
    for row in sh.iter_rows(min_row=2):
        for c in row: c.font = F(size=9); c.alignment = Alignment(wrap_text=True, vertical="top")
wb.save(OUT)
txt = " ".join(str(c.value) for s in wb for r in s.iter_rows() for c in r if c.value)
w5 = wb.create_sheet("Budget", 2)
w5.append(["Lean budget, 28 covers (20 guests, up to 8 hosts). Estimates from published prices until the Westin quote arrives. Lean and ceiling in INR."])
w5["A1"].font = F(bold=True, size=11, color=NAVY)
w5.append(["Line", "Basis", "Lean (INR)", "Ceiling (INR)", "Source", "Westin quote (INR)"])
for i, c in enumerate(w5[2], 1):
    c.font = F(bold=True, color="FFFFFF", size=9); c.fill = PatternFill("solid", fgColor=NAVY)
for a, b, l, c, u in BUDGET:
    w5.append([a, b, l, c, u, None])
first, last = 3, w5.max_row
w5.append(["Contingency, 10%", "Service charge, extra covers, AV add ons", "=ROUND(SUM(C%d:C%d)*%s,0)" % (first, last, BUDGET_CONTINGENCY), "=ROUND(SUM(D%d:D%d)*%s,0)" % (first, last, BUDGET_CONTINGENCY), "", None])
w5.append(["Total", "", "=SUM(C%d:C%d)" % (first, last + 1), "=SUM(D%d:D%d)" % (first, last + 1), "", "=SUM(F%d:F%d)" % (first, last)])
for row in w5.iter_rows(min_row=3):
    for c in row:
        c.font = F(size=9, bold=(row[0].value == "Total")); c.alignment = Alignment(wrap_text=True, vertical="top")
        if c.column in (3, 4, 6): c.number_format = "#,##0"
    if row[4].value and str(row[4].value).startswith("http"): row[4].hyperlink = row[4].value; row[4].font = F(size=9, color="0077B6", underline="single")
for col, w in zip("ABCDEF", (32, 60, 14, 14, 40, 18)): w5.column_dimensions[col].width = w
print(OUT, ws.max_row - 3, "rows; dashes", sum(txt.count(ch) for ch in "–—"), "excl", txt.count("!"))
