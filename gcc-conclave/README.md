# Prolifics GCC Conclave, Hyderabad, 17 December 2026

Plan, invite list, lean budget and research for an invitation only GCC evening hosted by Satya Bolli.
Twenty guests, all heads of global capability centers in Hyderabad. Owners are Satya and the Prolifics team.

Live plan (noindex): https://prolifics-gcc-conclave.vercel.app

| File | What |
|---|---|
| `plan_content.py` | Everything the plan says: run of show, timeline, checklist, risks, decisions, lean budget |
| `data.py` | The list. Ends with the ROOM (20) and RESERVE (12) lists |
| `contacts.py` | Verified work emails and LinkedIn URLs from the Apollo pull, 22 Nov 2026. Personal data: do not share outside Prolifics |
| `build_playbook.py` | Builds the full plan: `out/playbook.html`, `out/Prolifics GCC Conclave - Full Plan.pdf` and `site/index.html` |
| `build_tracker.py` | Builds `out/Prolifics GCC Conclave - Invite Tracker.xlsx` (Invites and Budget sheets, with a Westin quote column) |
| `research-*.md` | Sources and dates for every name, venue, date and number |

## Rebuild and deploy
```
python3 build_playbook.py && python3 build_tracker.py
cd site && vercel deploy --prod --yes --name prolifics-gcc-conclave
```
Requirements: Python 3.9+, openpyxl, Google Chrome (for the PDF), Vercel CLI.

House rules: Arial, no em or en dashes, no exclamation marks, every number sourced.
Lean budget: INR 1.51 lakh, INR 2.18 lakh at the top of published prices, before the Westin's written quote.
