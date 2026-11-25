# Prolifics codebases, 24 November 2026

Four zips. Each one unzips into a folder called `prolifics/`. Unzip all four into the same place and the
folders line up, which the deck builders need (they read GTM content and website images from the sibling folders).

| Zip | Folder | What | Live |
|---|---|---|---|
| Prolifics - Website - Codebase | `prolifics/homepage` | Static site generator (Python) and the built site in `dist/`: 98 pages, group company pages, industry logo wall, HubSpot forms per practice | https://prolifics-home-preview.vercel.app |
| Prolifics - GTM 2027 - Codebase | `prolifics/gtm` | Salesforce, ServiceNow and FDE go to market: model, target lists, microsite generator, emails, ads, brochures, plan and snapshot builders | Hub and microsites on Vercel |
| Prolifics - GCC Conclave - Codebase | `prolifics/gcc-conclave` | Plan, checklist, lean budget, invite list and tracker builders | https://prolifics-gcc-conclave.vercel.app |
| Prolifics - Decks - Codebase | `prolifics/` (root files), `client-partner-brief`, `website-deck`, `sales-training`, `lib` | Client partner briefing, the two slides (WordPress and HubSpot vs Salesforce), website decisions deck, sales training, account intelligence decks | PDFs in Drive |

Each project has its own README (and CLAUDE.md where present) with build and deploy commands.

Requirements: Python 3.9+, Pillow, openpyxl, Google Chrome (PDF rendering), Vercel CLI for deploys, Node 18+ for sales-training only (`npm install` first).

Not included on purpose: `.git` history, `.vercel` project links, `node_modules`, caches, scraped reference HTML, and
rebuildable GTM outputs (brochure PDFs, hub images, built microsites). Run the builders to regenerate them.
`gcc-conclave/contacts.py` and the tracker hold guest work emails: keep them inside Prolifics.
