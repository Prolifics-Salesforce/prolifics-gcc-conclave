# -*- coding: utf-8 -*-
"""Plan content for the Prolifics GCC Conclave: run of show, timeline, checklist, risks.
22 Nov 2026 revision: 20 guests only, all GCC heads. No minister, no Indian company CEOs, no outside moderators.
Shared by build_playbook.py (web page and PDF) and build_tracker.py (Checklist sheet).
House rules: no dashes, no exclamation marks, no pricing, every number sourced."""

# Run of show on the day. (time, what, who, detail)
DAY = [
    ("3:00 pm", "Prolifics team at the Westin", "Prolifics team", "Walk the Evolve private room with the banquet manager"),
    ("3:30 pm", "Room and AV set up", "Westin AV, Prolifics team", "One U-shape for 28 in Evolve (seats 33), four table mics, one handheld, a screen for Satya's keynote, name cards at every seat"),
    ("4:00 pm", "Technical rehearsal", "Prolifics team, AV lead", "Every mic, Satya's slides, the clicker, house lights for photos"),
    ("4:30 pm", "Host briefing", "Prolifics team", "Each Prolifics host gets two or three named guests to welcome, introduce and sit beside"),
    ("4:45 pm", "Kitchen and service check", "Prolifics team with the banquet manager", "Dinner is served at the same table after the roundtable: confirm timing and the set menu"),
    ("5:30 pm", "Arrivals, coffee, introductions", "Satya at the door", "Satya greets each guest by name; hosts make the first introductions"),
    ("6:00 pm", "Welcome and a round of names", "Prolifics team", "Three minute welcome, then each guest gives their name, company and one line on their center"),
    ("6:15 pm", "Keynote", "Satya Bolli", "15 minutes: 48 years of building for global enterprises, and what an AI ready GCC needs next"),
    ("6:30 pm", "Founders conversation: built here from zero", "Satya with Amgen, Lilly, Vanguard and Heineken", "35 minutes. How each center went from announcement to its first hundred people, and what they would do differently"),
    ("7:05 pm", "Closed door roundtable: AI in production at the GCC", "Opened by HSBC, ServiceNow and Sanofi; facilitated by the Prolifics team", "50 minutes, Chatham House rule. Three openers speak for three minutes each, then the whole table. No photos"),
    ("7:55 pm", "Dinner in the room", "Satya and the Prolifics hosts", "Served at the same U-shape, one Prolifics host every four or five seats; seating mixes sectors"),
    ("9:30 pm", "Close", "Satya", "Thank you at the exit; valet ready from 9:15 pm"),
]

# Timeline. (when, headline, items, owner)
TIMELINE = [
    ("Mon 23 Nov", "Approve and hold", ["Satya and the Prolifics team approve the date, venue, the 20 names, the 12 reserves and the letter",
     "Hold the Evolve private room on a 48 hour option and ask for a written quote for 28 dinners",
     "Confirm the flagged titles on LinkedIn"], "Satya, Prolifics team"),
    ("Tue 24 to Wed 25 Nov", "All 20 invitations out", ["Satya's personal letter to all 20, from his own mailbox", "LinkedIn note from Satya the same day",
     "Direct routes for the two with no email: Manish Arora (Lilly) and Kamal Sharma (Carrier, hand delivered in Mindspace)"], "Satya, Prolifics team"),
    ("Thu 26 to Mon 30 Nov", "Calls and contract", ["Satya calls the 4 founders and 3 roundtable openers within 48 hours", "The Prolifics team calls the other 13",
     "Sign the Westin contract", "Event page live on prolifics.com, unlisted, for guests only", "Find the heads of the Mindspace GCCs for the reserve list"], "Satya, Prolifics team"),
    ("Tue 1 to Fri 4 Dec", "Follow up and decide", ["Follow up 1 by email on day 3, follow up 2 by phone on day 7", "A reserve goes out for each decline, one for one, so the room never passes 20",
     "Book AV and the photographer; brief the designer", "Friday 4 Dec: go or no go"], "Prolifics team"),
    ("Mon 7 to Wed 9 Dec", "Summit week", ["No new invitations while the Invest Telangana Global Summit runs", "Meet invitees in person at the summit",
     "Draft the founders conversation questions and the roundtable prompts"], "Satya, Prolifics team"),
    ("Thu 10 to Mon 14 Dec", "Final count and prep", ["Final count and menu to the Westin by Fri 11 Dec", "20 minute prep call with each founder and each roundtable opener",
     "Satya's keynote final", "Print name cards, table cards, the agenda card and one standee"], "Prolifics team"),
    ("Tue 15 to Wed 16 Dec", "Reminders and rehearsal", ["Confirmation note with directions, parking and timing to every yes", "Satya rehearses the keynote and the founders conversation",
     "Seating plan and host pairing sheet", "WhatsApp reminder on the morning of 17 Dec"], "Prolifics team"),
    ("Thu 17 Dec", "Conclave", ["Team on site from 3:00 pm", "Doors 5:30 pm, close 9:30 pm"], "All"),
    ("Fri 18 Dec onward", "Follow through", ["Thank you note from Satya to every guest within 24 hours", "Photos to guests who agreed to them",
     "One page insights note from the roundtable, by Fri 8 Jan", "1:1 meetings with Satya through January"], "Satya, Prolifics team"),
]

# Checklist. (workstream, [(task, owner, due)])
CHECK = [
    ("Approvals", [
        ("Approve Thursday 17 December, 5:30 to 9:30 pm (backup Tuesday 15 December)", "Satya, Prolifics team", "Mon 23 Nov"),
        ("Approve The Westin Hyderabad Mindspace, Evolve private room, one room for the whole evening", "Satya, Prolifics team", "Mon 23 Nov"),
        ("Approve the 20 names and the 12 reserves; swap in any GCC heads from Satya's and the Prolifics team's own networks", "Satya, Prolifics team", "Mon 23 Nov"),
        ("Approve the rule: one seat per company, no deputies or plus ones", "Satya", "Mon 23 Nov"),
        ("Approve the letter, LinkedIn note and follow up wording", "Satya", "Mon 23 Nov"),
        ("Approve the lean budget: INR 1.51 lakh, ceiling INR 2.18 lakh (see Budget)", "Satya", "Mon 23 Nov"),
        ("Name the Prolifics hosts, up to 7 besides Satya", "Prolifics team", "Fri 27 Nov"),
    ]),
    ("Venue and hospitality", [
        ("Hold Evolve for 48 hours; ask for a written quote: 28 dinners, room hire waived against food, AV included", "Prolifics team", "Mon 23 Nov"),
        ("Sign the Westin contract and pay the deposit", "Prolifics team", "Mon 30 Nov"),
        ("Agree the room set: one U-shape for 28, dinner served at the same table", "Prolifics team", "Fri 4 Dec"),
        ("Choose the menu, with vegetarian, Jain and non alcoholic options", "Prolifics team", "Tue 8 Dec"),
        ("Give the final count and dietary list to the Westin", "Prolifics team", "Fri 11 Dec"),
        ("Confirm guest parking or valet is included in the quote", "Prolifics team", "Mon 14 Dec"),
        ("Finish the seating plan, mixing sectors, one Prolifics host per table", "Prolifics team", "Wed 16 Dec"),
    ]),
    ("Invitations and RSVPs", [
        ("Confirm the flagged titles on LinkedIn (Sirisha Voruganti, Vamsi Tekuru, Ganpat Anchaliya)", "Prolifics team", "Mon 23 Nov"),
        ("Write the one line personal reason for each of the 20 letters", "Prolifics team", "Mon 23 Nov"),
        ("Send all 20 letters from Satya's own mailbox", "Satya", "Wed 25 Nov"),
        ("Send LinkedIn notes from Satya to all 20", "Satya", "Wed 25 Nov"),
        ("Reach Manish Arora (Lilly) through Satya's network; no email on file", "Satya, Prolifics team", "Wed 25 Nov"),
        ("Hand deliver Kamal Sharma's invitation at Carrier in Mindspace; no email on file", "Prolifics team", "Wed 25 Nov"),
        ("Satya calls the 4 founders and the 3 roundtable openers", "Satya", "Fri 27 Nov"),
        ("The Prolifics team calls the other 13", "Prolifics team", "Mon 30 Nov"),
        ("Follow up 1 by email on day 3 after each letter", "Prolifics team", "Rolling"),
        ("Follow up 2 by phone on day 7 after each letter", "Prolifics team", "Rolling"),
        ("Pull Apollo emails for the 8 reserves who have none yet", "Prolifics team", "Mon 30 Nov"),
        ("Send one reserve for each decline, so the room never passes 20", "Prolifics team", "From Tue 1 Dec"),
        ("Update the tracker status every evening (To send, Sent, Replied, Yes, Maybe, No)", "Prolifics team", "Daily"),
    ]),
    ("Content", [
        ("Go or no go (see the rule in the timeline)", "Satya, Prolifics team", "Fri 4 Dec"),
        ("Write the founders conversation questions: four themes, two questions each", "Prolifics team", "Mon 7 Dec"),
        ("Write the roundtable prompts and brief the three openers", "Prolifics team", "Fri 11 Dec"),
        ("Collect bios, photos and preferred titles from the 7 with a role", "Prolifics team", "Tue 8 Dec"),
        ("Draft Satya's 15 minute keynote", "Prolifics team", "Thu 10 Dec"),
        ("Hold the 20 minute prep call with each founder and each opener", "Prolifics team", "Mon 14 Dec"),
        ("Rehearse the keynote and the conversation with Satya", "Prolifics team", "Tue 15 Dec"),
    ]),
    ("Brand, print and production", [
        ("Put the event page live on prolifics.com, unlisted and noindex, guests only", "Prolifics team", "Mon 30 Nov"),
        ("Book the Westin AV: four table mics, one handheld, screen, clicker", "Prolifics team", "Fri 4 Dec"),
        ("Book a photographer for 5:30 to 7:05 pm only, with no photos during the roundtable", "Prolifics team", "Fri 4 Dec"),
        ("Brief the designer: one standee, agenda card, name cards, table cards", "Prolifics team", "Fri 4 Dec"),
        ("Approve the designs", "Prolifics team", "Wed 9 Dec"),
        ("Print everything and deliver it to the Westin", "Prolifics team", "Mon 14 Dec"),
        ("Print the guest list and the host pairing sheet", "Prolifics team", "Wed 16 Dec"),
    ]),
    ("Guest experience", [
        ("Collect dietary needs from every yes", "Prolifics team", "Fri 11 Dec"),
        ("Send the confirmation note with directions, parking, dress and timing", "Prolifics team", "Tue 15 Dec"),
        ("Pair each Prolifics host with two or three named guests", "Prolifics team", "Wed 16 Dec"),
        ("Send the WhatsApp reminder on the morning of the event, only to guests who said yes", "Prolifics team", "Thu 17 Dec"),
    ]),
    ("Follow through", [
        ("Send Satya's thank you note to every guest", "Satya", "Fri 18 Dec"),
        ("Share photos only with guests who agreed", "Prolifics team", "Mon 21 Dec"),
        ("Satya posts on LinkedIn, naming only guests who agreed", "Satya, Prolifics team", "Fri 18 Dec"),
        ("Send a one page insights note from the roundtable, with no attributed quotes", "Prolifics team", "Fri 8 Jan"),
        ("Book 1:1 meetings with Satya for every guest who asks", "Prolifics team", "January"),
        ("Log every guest, reply and next step in the CRM", "Prolifics team", "Wed 23 Dec"),
    ]),
]

RISKS = [
    ("Summit fatigue", "GCC heads spend 7 to 9 Dec at the Invest Telangana Global Summit", "All letters out by 25 Nov; no invitations that week; meet invitees at the summit"),
    ("Late notice", "22 days from the letters to the event", "All 20 at once, a call within 48 hours, a reserve for each decline"),
    ("Too few yeses", "Fewer than 12 by 4 Dec", "8 to 11: drop the keynote and run the roundtable and dinner only. Under 8: move to January"),
    ("A founder drops out late", "The conversation needs at least three", "Backups already in the room: Schwab, McDonald's, HCA"),
    ("The room grows past 20", "Deputies and plus ones dilute a room of heads", "One seat per company; reserves go out one for one"),
    ("Stale titles", "Leaders move often; three names are flagged", "Confirm each title on LinkedIn before the letter goes"),
    ("Looks like a sales event", "GCC heads decline vendor evenings", "No Prolifics pitch; Satya speaks as a builder; follow ups only in January"),
    ("The Westin quote comes in above budget", "Published per plate prices for the Westin vary widely", "Hold the cap of INR 3,000 a plate before tax; ask for a set menu, or move to Trident HITEC City (published group dinner rate INR 1,750)"),
]

DECISIONS = [
    "Date: Thursday 17 December, 5:30 to 9:30 pm, backup Tuesday 15 December",
    "Venue: The Westin Hyderabad Mindspace, Evolve private room for the whole evening (no Ballroom, no Lawns, no rain backup)",
    "The 20 GCC heads and the 12 reserves, plus any swaps from Satya's and the Prolifics team's own networks",
    "One seat per company: no deputies, no plus ones",
    "Satya signs all 20 letters and makes 7 calls; the Prolifics team makes the other 13",
    "The lean budget: INR 1.51 lakh, with a ceiling of INR 2.18 lakh",
]

# Lean budget (23 Nov 2026, brief: "Keep it very lean, to the point"). 28 covers (20 guests, up to 8 Prolifics hosts).
# Estimates from published sources until the Westin's written quote arrives. GST at 18% on hotel catering.
M = "https://www.marriott.com/en-us/hotels/hydwi-the-westin-hyderabad-mindspace/events"
BUDGET = [
    # (line, basis, lean INR, ceiling INR, source)
    ("Dinner, 28 covers", "INR 3,000 a person, the Westin's published dinner rate; ceiling INR 4,500 (listing sites)", 84000, 126000, M),
    ("Arrival tea, coffee and bites, 28", "INR 500 a person, the Westin's published coffee break rate", 14000, 14000, M),
    ("GST on food at 18%", "Applies to hotel catering where room tariffs exceed INR 7,500", 17640, 25200, "https://www.businesstoday.in/personal-finance/tax/story/18-gst-hits-hotel-restaurants-where-room-tariff-exceeds-rs-7500-per-day-check-details-470411-2025-04-02"),
    ("Evolve private room", "Ask for room hire to be waived against the food spend; capacity banquet 30, U-shape 33", 0, 0, M),
    ("AV: screen, projector, mics", "Listed as available on request at the Westin; outside rental runs INR 750 to 1,500 for a projector and INR 550 for a screen", 5000, 10000, "https://dir.indiamart.com/impcat/projectors-rental.html"),
    ("Photographer, 5:30 to 7:05 pm only", "Hyderabad studio day rate INR 12,000; ceiling INR 18,000", 12000, 18000, "https://www.weddingbazaar.com/wedding-photographers/hyderabad/4-seasons-cinematic"),
    ("Print: name cards, table cards, agenda", "About 90 pieces at INR 6 to 30 each", 2700, 2700, "https://m.indiamart.com/impcat/table-tent-cards.html"),
    ("One roll-up standee", "INR 1,500 to 2,000 in Hyderabad", 2000, 2000, "https://printo.in/p/standees-printing-in-hyderabad"),
    ("Bar", "Not in the lean budget; soft drinks and mocktails only unless Satya decides otherwise", 0, 0, ""),
    ("Gifts, travel, decor", "None: the evening is the gift", 0, 0, ""),
]
BUDGET_CONTINGENCY = 0.10
