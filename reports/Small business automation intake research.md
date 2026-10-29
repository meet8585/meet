# Profile the business, then the tools, then the work

**Bottom line:** A good intake form for a DIY automation app has to establish four facts. What kind of business is this (industry plus operating model)? Which system of record does each business function run on, and can that system be integrated? Which three to five tasks are eating the owner's time? What constraints (skills, time, budget, regulation) limit the plan? Industry alone is not enough. The typical US small business is a solo operator: about **29.8 million of roughly 36.2 million US small businesses have no employees** ([Census](https://www.census.gov/library/stories/2025/05/smallest-businesses.html); [SBA Advocacy](https://advocacy.sba.gov/?p=30239)). Within one vertical, plans differ by how customers buy (appointment, quote, walk-in, subscription, product). Software stacks run from paper and checks through QuickBooks Desktop, mainstream cloud SaaS and vertical platforms, up to AI-native agents. What makes a recommendation workable is whether a tool has an open API, a gated API or no API. The best-evidenced automation wins are appointment reminders, missed-call and lead response, invoice and payment reminders, and review requests. The form should route users toward those recipes first, then tailor them by vertical and compliance regime. The recommended form has a required core of about 25 questions across five sections (about 10 minutes), plus an optional task deep-dive and one conditional industry module.

## How to read the evidence labels in this report

The research notes mix three kinds of claims, and this report keeps them apart. **Verified** claims carry an inline citation to the source the researchers found. Many of those sources are vendor blogs, aggregators or secondary summaries, so this report flags weak sourcing where it matters. Claims tagged **[BK]** are background knowledge from the researchers' training data. They were not confirmed in a source this session; treat them as likely but check them before building them into product logic. Claims tagged **[Design]** are product recommendations: the researchers' or this report's synthesis, not data. Primary-source access was limited. census.gov, sba.gov and several vendor sites were blocked during research, so several Census figures come from search summaries of the primary pages.

## Four in five US small businesses have no employees, so design for one person

The US has about **36.2 million small businesses**, which account for almost 46% of private-sector employment ([SBA Advocacy, June 2025](https://advocacy.sba.gov/?p=30239)). Of these, **29.8 million are nonemployers** with combined receipts of $1.7 trillion ([Census](https://www.census.gov/library/stories/2025/05/smallest-businesses.html)). Employer firms number about 6.4 million, and about **89% of them have fewer than 20 employees** ([SBE Council](https://sbecouncil.org/about-us/facts-and-data/)). Among small employers, **49% have 1–4 workers and 27% have 5–19** ([Pew](https://www.pewresearch.org/short-reads/2024/04/22/a-look-at-small-businesses-in-the-us/)). The largest nonemployer sectors are:

| Sector | Nonemployer count (2022) | Notes |
|---|---|---|
| Professional, scientific and technical services | **4.01M (13.5%)** | Largest by count |
| Transportation and warehousing | **3.85M** | Mostly rideshare and delivery gig workers |
| Real estate, rental and leasing | **3.15M** | **20% of nonemployer receipts** |
| Construction | about **9.6% of establishments** | Plus about 719K employer firms with 1–19 staff ([Review42](https://resources.review42.com/small-business-statistics/), secondary) |

Source for the table: [Census](https://www.census.gov/library/stories/2025/05/smallest-businesses.html), except where noted.

The same skew holds abroad. In the UK, about 75% of 5.69 million businesses have no employees ([Deplexifi summarizing DBT](https://deplexifi.com/uk/insights/small-business-statistics-uk)). In Australia, about 64% of 2.73 million businesses are non-employing ([ASBFEO](https://www.asbfeo.gov.au/sites/default/files/2025-12/Number%20of%20small%20businesses%20in%20Australia_Aug%202025.pdf)).

Two design implications follow. First, the default plan must work for one person with no IT staff, so team size belongs near the top of the form, and "just me" should skip the role and handoff questions. Second, size predicts adoption: **51% of firms with 1–9 employees adopted new technology in the past two years versus 75% of firms with 50+** ([NFIB 2025](https://www.nfib.com/news/press-release/new-nfib-report-how-small-businesses-incorporate-tech-and-ai-advancements/)). Plans for the smallest firms should start simpler.

### NAICS is too coarse; use a two-level, plain-language taxonomy

NAICS sector 81 ("Other Services") lumps auto repair, salons, dry cleaning, pet care and religious organizations together. These businesses have completely different workflows. The researchers propose about 20 plain-language tiles, each with sub-types. Each sub-type stores a NAICS code in the background so the app can later benchmark against Census data [Design]. The sector anchoring is verified against the SUSB/NES structure ([Census SUSB](https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html)). The tile list itself and the default traits are judgment, not data.

| Tile (form label) | Example sub-types | Default model / location / customer | Regulated data? |
|---|---|---|---|
| Home & trade services | Plumbing, HVAC, electrical, roofing, handyman, pest, pool | Quote + appointment / field / consumer (+B2B) | — |
| Construction & contracting | GC/remodel, specialty sub, home builder, commercial | Project / field / B2B + consumer | Certified payroll on public work [BK] |
| Cleaning, landscaping & property care | Residential cleaning, janitorial, lawn care, snow, junk removal | Recurring + quote / field / both | — |
| Food & beverage | Full-service, QSR/cafe, bar/brewery, food truck, catering, bakery | Walk-in/order / fixed or mobile / consumer | Card data |
| Retail (physical) | Boutique, gift, grocery/convenience, hardware, florist, thrift | Walk-in + product / fixed / consumer | Card data |
| E-commerce & online sales | DTC site, marketplace seller, dropship, subscription box, digital products | Product + subscription / online / consumer | Card data, sales tax |
| Makers & small manufacturing | Handmade, print/signs, food production, fabrication | Product + project / fixed + online / both | Lot traceability [BK] |
| Beauty & personal care | Hair/barber, nails, spa/massage, lash/brow, med spa, tattoo | Appointment / fixed or mobile / consumer | Med spa: health |
| Health & medical practices | Medical, dental, chiro/PT, therapy, optometry, home health, vet | Appointment / fixed / consumer | **HIPAA** (vet generally not [BK]) |
| Fitness & wellness | Studio/gym, personal trainer, martial arts/dance, coach | Appointment + membership / fixed or online / consumer | — |
| Professional services | Accounting/tax, legal, consulting, insurance agency, financial advisor, staffing | Appointment/project/retainer / online or office / both | Legal trust, tax data, insurance |
| Creative, marketing & tech services | Agency, design, web/software dev, IT/MSP, photo/video | Project + retainer / online / B2B | — |
| Real estate & property | Agent/brokerage, property management, STR host, mortgage, inspection | Project + recurring / field + online / consumer | Trust funds, fair housing [BK] |
| Automotive | Repair, body, detailing, quick-lube, towing, small dealer | Appointment/walk-in/quote / fixed or mobile / consumer | — |
| Transportation & logistics | Owner-operator trucking, courier, moving, limo, freight brokerage | Project + recurring / field / B2B + consumer | ELD/HOS |
| Education, childcare & tutoring | Daycare, in-home childcare, tutoring, lessons, online courses | Recurring + appointment / fixed or online / consumer | Minors, state licensing |
| Pet services | Grooming, boarding/daycare, walking/sitting, training | Appointment + recurring / field or fixed / consumer | — |
| Events, hospitality & recreation | Event planner, wedding vendors, venue, B&B, tours | Project + appointment / mixed / consumer | — |
| Nonprofit & community | Charity, association, church, arts org, club | Donors/members recurring | Donor receipts [BK] |
| Agriculture | Farm/ranch, CSA, nursery, agritourism | Product + subscription / fixed / both | USDA, pesticide records [BK] |

For the UI, the researchers suggest merging to about 15 tiles. Fold Construction into Trades, Creative/Tech into Professional services, and Agriculture into Makers. Keep Beauty, Health and Food separate, because their automation stacks (booking and no-shows, HIPAA intake, POS and menus) diverge sharply [Design]. Gig drivers are the second-largest nonemployer group, but they have little to automate in their own operations. A "Trucking / courier / moving" sub-type covers them without giving them their own tile [Design].

### Operating model predicts the plan better than industry does

A mobile dog groomer and a grooming salon share an industry, but they need different automations [Design]. For that reason the form should pre-fill five operating-model traits from the chosen sub-type and ask the user to confirm or override them.

- **How work arrives** decides the core stack:
  - Appointment → booking, reminders and no-show control.
  - Project or quote → lead intake, estimates, deposits and change orders.
  - Recurring → recurring billing and dunning.
  - Product → inventory, fulfilment and abandoned-cart flows.
- **Where work happens** pulls in dispatch, routing, photos and mobile invoicing when the work is at the customer's site.
- **Customer type**: B2B brings proposals, contracts, net-terms invoicing and a CRM pipeline. B2C brings reviews, SMS and booking.
- **Team size** sets how much handoff logic the plan needs.
- **Regulated data** sets guardrails on which tools the plan may recommend.

All five are analytical choices. The researchers found no dataset that quantifies the mix of appointment, project and subscription models across small businesses.

### Digital maturity varies by sector, so plan complexity should too

Census business-survey readings put AI use at about **18–20% of firms nationally**. It is highest in information (about 38–40%), finance (about 34%) and professional services (about 33%), and lowest in accommodation and food (about 8%) and agriculture (about 5%) ([Federal Reserve, Apr 2026](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html); sector splits via secondary compilations such as [Axis Intelligence](https://axis-intelligence.com/ai-adoption-by-industry-statistics/)).

Survey definitions matter enormously:

- **U.S. Chamber:** **58%** of small businesses use generative AI ([IPWatchdog summary](https://ipwatchdog.com/2025/08/18/us-chamber-report-small-businesses-rapidly-adopting-ai-despite-regulatory-concerns/)).
- **NFIB:** **24%** of small employers use AI ([ASBN/NFIB](https://www.asbn.com/articles/nfib-survey-reveals-how-small-businesses-are-adopting-ai-and-tech-to-stay-competitive/)).
- **Census, August 2025:** **8.8%** use AI to produce goods or services ([Revenued](https://www.revenued.com/small-business-ai-usage)).

The practical rule is to ask "which AI tools, for which tasks," not "do you use AI." Restaurants show a related pattern of tool sprawl: **65% adopted a new tool in a year, but only 49% call their systems connected** ([7shifts via Eatery Club](https://www.eatery.club/en/blog/a-new-report-highlights-the-restaurant-industry-s-digital-divide)). In such sectors, integration is the plan's main job, not adding more apps.

The form should therefore tag sectors for one of two plan styles [Design]:

- **"Start simple, phone/SMS-first":** food, retail, trades, auto, agriculture and personal care.
- **"Integrate and orchestrate":** professional, creative/tech, real estate and finance.

## Every business function sits on a ladder from paper to AI agents

Across business functions, the same four-rung ladder repeats: legacy (paper, desktop, on-prem), mainstream SaaS, modern cloud/API-first, and AI-native. Hard SMB market-share data is scarce in every category, and the figures that exist are directional:

- **Accounting:** QuickBooks dominates US small-business accounting. One aggregator puts it at **62%** ([ElectroIQ](https://electroiq.com/stats/quickbooks-statistics/), method undisclosed). Xero leads in the UK, Australia and New Zealand, with **4.4M+ subscribers** ([Growth Share Matrix](https://growthsharematrix.com/blogs/competitors/xero)).
- **Point of sale:** Across all US POS installs, Square holds about 27–28% and Toast about 24% ([Host Merchant Services](https://hostmerchantservices.com/articles/point-of-sale-market-share/)). In small restaurants, Clover, Toast and Square split the market ([Duck-Hub citing Baird](https://www.duck-hub.com/blog/restaurant-pos-market-statistics)).
- **Payroll:** Gusto serves **300K+ businesses** and Paychex about **745K** ([Small Business Trends](https://smallbiztrends.com/payroll-companies-in-usa/)).
- **CRM:** HubSpot has about **289K paying customers** and is the default small-business CRM because of its free tier ([Resonate](https://resonatehq.com/blog/hubspot-market-share); [Builts.ai](https://builts.ai/blog/best-crm-small-business-2026/)).
- **Automation platforms:** Zapier's catalog of about **7,000–8,000 apps** dwarfs Make's (about 1,500–2,000) and n8n's (about 400 native nodes) ([DigitalApplied](https://www.digitalapplied.com/blog/zapier-vs-make-vs-n8n-2026)).

Legacy is not a niche. Nearly **80% of very small firms (under $1M revenue) and 83% of small firms still pay by paper check** ([Atlanta Fed](https://www.atlantafed.org/blogs/take-on-payments/2026/01/12/why-do-businesses-still-use-paper-checks)). One blog estimates that combined Xero and QuickBooks Online penetration is close to **2% of about 29M US small businesses**, which implies most micro-firms keep books in spreadsheets, paper or desktop software, or leave them to an accountant ([Blake Oliver](https://blakeoliver.com/blog/tag/marketshare)). Every tool question in the form must therefore include explicit manual answers.

The catalog below is the option list for the form's tool picker. The product names and rung placement are the researchers' classification [BK]. The integration notes marked as cited are verified. Spot-check the rest against the Zapier, Make and n8n directories before shipping.

| Function | Legacy / manual | Mainstream | Modern cloud | AI-native layer |
|---|---|---|---|---|
| Accounting | Paper ledger, Excel; QuickBooks Desktop; Sage 50 (ex-Peachtree); Tally (India) | QuickBooks Online, Xero, MYOB (AU) | FreshBooks, Wave, Zoho Books; Sage Intacct/NetSuite upmarket | Pilot, Digits, Puzzle; Intuit Assist |
| Payments / POS / invoicing | Cash register, bank card terminal, paper invoices, checks | Square, Clover, Toast, PayPal, QBO/Xero invoicing, Bill.com | Stripe, Shopify POS, Lightspeed | AI collections agents (emerging) |
| Payroll & HR | Handwritten checks via accountant; QB Desktop payroll | ADP RUN, Paychex Flex, QuickBooks Payroll | Gusto, Rippling, OnPay, Justworks, Deel; Homebase, When I Work | — |
| CRM & sales | Rolodex, business cards, Outlook contacts, Excel, ACT! | Salesforce, HubSpot, Keap | Zoho CRM, Pipedrive, GoHighLevel, monday CRM, Copper | AI SDR and lead-response tools |
| Scheduling | Paper book, phone + shared calendar | Google/Outlook calendar, Square Appointments | Calendly, Acuity, Setmore, SimplyBook, MS Bookings, Cal.com | AI voice booking agents |
| Email / social / reviews | Outlook BCC blasts | Constant Contact, Mailchimp, Meta Business Suite, Google Business Profile, Yelp, Thryv | Klaviyo, Brevo, Kit, MailerLite; Hootsuite, Buffer, Later; Birdeye, Podium, NiceJob | AI content generation |
| Phone & messaging | Landline + answering machine, on-prem PBX, personal cell, human answering service | Google Voice, WhatsApp Business app | RingCentral, Nextiva, Dialpad, Grasshopper, OpenPhone (Quo), Aircall; Twilio, SimpleTexting; Tidio, Intercom | AI receptionists: Smith.ai, Goodcall, Rosie, Dialzara |
| Docs & storage | Filing cabinets, fax, Office 2016/2019, local file server, on-prem Exchange | Microsoft 365, Google Workspace, Dropbox, Box | Notion | Copilot, Gemini |
| Projects & tasks | Whiteboard, paper, email threads, Excel | Trello, MS Planner | Asana, monday, ClickUp, Basecamp, Airtable | Agents inside these tools |
| Website & e-commerce | None/Facebook page, static HTML, GoDaddy Builder, Weebly | WordPress/WooCommerce, Wix, Squarespace, Etsy, Amazon, eBay | Shopify, Webflow | Wix AI, Durable, Framer AI |
| Forms & e-signature | Paper/clipboard, fillable PDFs | Google/Microsoft Forms, DocuSign | Jotform, Typeform, Tally, Fillout, PandaDoc, Dropbox Sign | AI document extraction |
| Inventory & shipping | Clipboard counts, Excel, carrier counter | QuickBooks/Square/Shopify inventory, Fishbowl | Cin7, inFlow, Sortly, Katana, Zoho Inventory; ShipStation, Shippo, Pirate Ship | — |
| Support / helpdesk | Shared inbox, voicemail | Zendesk, Freshdesk | Help Scout, Gorgias, Zoho Desk, HubSpot Service | Intercom Fin |
| Automation | Copy-paste, Excel macros/VBA | Zapier, Power Automate, IFTTT | Make, n8n, Activepieces | ChatGPT, Claude, Gemini; MCP-connected agents |

AI receptionist pricing in October 2026 shows that the AI-native tier is affordable for small businesses. Examples: **Smith.ai at $150/mo for 75 AI-answered calls**, **Rosie at $49/mo for 250 minutes**, and **Dialzara from $29/mo** ([JustCall](https://justcall.io/blog/best-smith-ai-alternatives.html); [Dupple](https://dupple.com/learn/best-ai-receptionists)).

### Integration tier matters more than brand

For plan generation, the most useful attribute of a tool is how it can be connected, not its name. Modern cloud SaaS almost always has a public API and a Zapier app. The automation-hostile zone is legacy desktop/on-prem software plus partner-gated platforms. One verified example: Toast's API license is "limited, revocable, non-transferable" and tied to Toast's approval of the specific use ([Toast API terms](https://pos.toasttab.com/api-terms-of-use)). The researchers' tiering below is classification, not per-tool verification [BK]:

| Tier | Meaning | Examples | What the plan should do [Design] |
|---|---|---|---|
| **A — open API + native Zapier/Make/n8n** | Directly automatable | QuickBooks Online, Xero, Stripe, Square, Shopify, HubSpot, Pipedrive, Google Workspace, Microsoft 365, Calendly, Mailchimp, Klaviyo, Jotform, DocuSign, Gusto, RingCentral, Twilio | Native features first, then no-code recipes |
| **B — gated or thin** | Possible with approvals, paid tiers or partner apps | Toast (cited), Clover, ADP, Paychex, Google Business Profile, Yelp, Wix, Squarespace, Wave, Amazon SP-API, WhatsApp Cloud API, Airbnb | Use the vendor's marketplace apps or a certified partner |
| **C — closed or local** | No practical API | QuickBooks Desktop, Sage 50, Tally, ACT! desktop, on-prem Exchange, Google Voice, landlines, fax, paper | AI document extraction, CSV export/import, RPA or browser agents, or migrate first |

### 2025–2027 support cliffs create forced-migration moments

Several of these dates are verified and are natural triggers for a "migrate first" step in a plan:

| Product | What changes | Source |
|---|---|---|
| QuickBooks Desktop Pro/Premier/Mac Plus | New subscriptions stopped Sept 2024 | [WizCommerce](https://wizcommerce.com/quickbooks-desktop-discontinued-everything-you-need-to-know/) |
| QuickBooks Desktop 2023 | **Lost payroll, bank feeds and security updates on May 31, 2026**; Desktop 2024 reportedly supported to about Sept 2027 | [Insightful Accountant](https://blog.insightfulaccountant.com/quickbooks-desktop-accountant-2023-discontinued-after-may-31-2026) |
| QuickBooks Desktop Point of Sale | **Services shut down Oct 3, 2023**; Intuit points users to Shopify | [Intuit](https://quickbooks.intuit.com/learn-support/en-us/help-article/discontinued-offering/quickbooks-desktop-point-sale-discontinuation/L407dYuCG_US_en_US) |
| Office 2016/2019, Exchange Server 2016/2019, Skype for Business Server | **End of support Oct 14, 2025** | [Microsoft Learn](https://learn.microsoft.com/en-us/lifecycle/announcements/october-14-2025-products-end-of-support) |
| Microsoft Publisher | **End of support Oct 13, 2026** | [The Register](https://www.theregister.com/2026/01/12/microsoft_2026_culls/) |
| CoConstruct (Buildertrend) | No new projects from about **Apr 1, 2027**; dates come from competitors citing Buildertrend notices | [JobTread](https://jobtread.com/blog/leaving-coconstruct-here-is-why-builders-are-choosing-jobtread) |

The table omits two retirements that were not verified this session: the consumer Skype service (May 2025) and Bench Accounting's collapse at the end of 2024 [BK].

The usual migration ladders give the plan a "current state → next step" map [Design]:

- **Accounting:** paper/Excel → QuickBooks Desktop or Sage 50 → QBO or Xero → AI bookkeeping.
- **POS:** register or bank terminal → Square or Clover (Toast for restaurants).
- **Payroll:** accountant-written checks → ADP, Paychex or QB Payroll → Gusto, Rippling or OnPay.
- **CRM:** Rolodex/Excel → HubSpot free, Zoho or Pipedrive.
- **Phone:** landline → VoIP → AI receptionist on top.
- **Automation:** none → Zapier → Make or n8n → MCP-connected agents.

## Vertical systems of record decide what is automatable

In most verticals, a vertical platform is the system of record, and horizontal tools orbit it. Two things matter most. Incumbents are now bundling their own AI agents, and API openness predicts how far a DIY plan can go. The form therefore needs a per-industry "core software" question. Its answer options should come from the lists below, each with an "Other" free-text option.

### Verified vertical developments that should shape recommendations

**Incumbents are shipping their own AI front desks and agents.** If a user already pays for one of these, the plan should turn it on before suggesting a third-party tool [Design].

- Jobber's AI Receptionist went generally available in August 2025 and had handled **200,000+ conversations** at launch ([PM Magazine](https://www.pmmag.com/articles/106754-jobber-launches-ai-powered-receptionist)).
- ServiceTitan opened its "Max" AI package to all residential contractors at Pantheon 2026 ([ServiceTitan](https://www.servicetitan.com/press/servicetitan-announcing-new-and-expanded-capabilities-at-pantheon-2026)).
- Housecall Pro sells an "AI Team" ([Carly](https://www.usecarly.com/blog/housecall-pro-ai-receptionist/)).
- Jane ships an AI Scribe ([Jane](https://jane.app/features/charting-ai-scribe)).
- Dentrix Ascend ran **191M insurance eligibility checks in 2025** ([Business Wire](https://www.businesswire.com/news/home/20260309270533/en/Henry-Schein-One-Unveils-the-Next-Era-of-Dentrix-Ascend-for-DSOs-and-Gr)).
- AppFolio launched agentic "Realm-X Performers" in June 2025 ([AppFolio PR](https://www.barchart.com/story/news/32825817/appfolio-unveils-ai-agents-to-transform-performance-in-real-estate)).
- Clio bought vLex for about **US$1B** in November 2025 ([LawNext](https://www.lawnext.com/2025/11/clio-completes-historic-1-billion-vlex-acquisition-announces-500-million-series-g-at-5-billion-valuation-plus-exclusive-interview-with-ceo-and-cfo.html)).

**Consolidation and rebrands mean the tool picker needs aliases** so users can find the product under the name they know [Design]:

- kvCORE is now **BoldTrail** ([Inman](https://www.inman.com/2024/06/20/inside-real-estate-folds-kvcore-as-part-of-major-rebrand-as-boldtrail/)).
- Vend is now **Lightspeed Retail X-Series** ([Lightspeed](https://lightspeedhq.com/vend)).
- Mindbody, ClassPass and Booker sit under **Playlist** ([Athletech News](https://athletechnews.com/mindbody-classpass-unveil-playlist-as-new-parent-company/)).
- Studio Ninja now operates as **Captura** ([Agiled](https://agiled.app/compare/studioninja-vs-honeybook)).
- Bloomerang absorbed **Qgiv** in December 2023 ([Bloomerang](https://bloomerang.com/news/bloomerang-acquires-qgiv)).
- Rose Rocket rebuilt itself as **TMS.ai** ([Rose Rocket](https://www.roserocket.com/blog/release-rose-rocket-ai-native-tms)).

**Gated access is a hard constraint.**

- Airbnb's API is open only to certified partners, reportedly with no new partners being accepted ([Lodgify](https://webflow-mkt.lodgify.com/encyclopedia/airbnb-api), competitor source).
- CoConstruct has no standalone public API ([Supergood](https://supergood.ai/api-report-card/coconstruct)).
- MRPeasy exposes its API only at its top tier, about $149/user/month ([Qoblex](https://qoblex.com/blog/mrpeasy-vs-fishbowl/)).
- Legacy legal integrations are eroding. Newer PCLaw versions no longer support the Amicus link, and setting it up costs $750 ([CrossPointe](https://crosspointecg.com/pclaw/); [AbacusNext](https://support.abacusnext.com/hc/en-us/articles/360041349432-How-do-I-link-Amicus-Attorney-by-CARET-with-PCLaw)).

### Vertical software catalog for the "core software" question

Rows mix verified items (cited in the bullets above or in the notes) with [BK] items. Each row's verification status is stated. Installed-base numbers are company-reported: Toast about **180,000 locations** in Q2 2026 ([Business Wire](https://www.businesswire.com/news/home/20260804267340/en/)), Tekmetric 15K+ shops, Shopmonkey 8K+ ([Shopmonkey](https://www.shopmonkey.io/blog/best-auto-repair-shop-management-software-2026-top-picks-compared)).

| Vertical | Legacy / on-prem | Mainstream / modern cloud | AI layer | Verification |
|---|---|---|---|---|
| Home services & trades | Paper carbon work orders, FieldEdge, Successware | ServiceTitan, Jobber, Housecall Pro; Workiz, ServiceM8, Tradify, GorillaDesk/PestPac, LMN/Aspire, ZenMaid | Jobber Receptionist, HCP AI Team, ServiceTitan Max/Atlas | Big three + AI verified; others [BK] |
| Construction | Sage 100 Contractor, Foundation, Sage 300 CRE | Buildertrend, Procore, JobTread, Houzz Pro, Contractor Foreman, Knowify | Procore/Buildertrend AI | CoConstruct sunset, JobTread verified; most others [BK] |
| Restaurants | NCR Aloha (still developed), Oracle MICROS | Toast, Square, Clover; 7shifts, OpenTable/Resy, Otter/Deliverect/Chowly, MarginEdge/xtraCHEF | Toast IQ; voice ordering (Loman, Slang, PopMenu, ConverseNow) | POS + AI phone verified; add-ons [BK] |
| Retail | QuickBooks Desktop POS (dead), cash register | Shopify POS, Square for Retail, Lightspeed (R/X-Series), Clover, Heartland | — | QB POS, Vend verified; rest [BK] |
| Beauty & personal care | Paper appointment book | Vagaro, Boulevard, GlossGenius, Fresha, Square Appointments, Mindbody/Booker, Zenoti, Phorest, Timely | Third-party AI receptionists (most send pay links, not mid-call deposits) | Verified ([Dupple](https://dupple.com/learn/best-salon-booking-software); [Stork](https://www.stork.ai/blog/ai-receptionist-for-salons-2026)); some [BK] |
| Fitness | Spreadsheets | Mindbody, Wodify, PushPress, Zen Planner, ABC Glofox | — | Verified ([Capterra](https://www.capterra.co.uk/compare/159663/172781/wodify/vs/pushpress)); ownership details [BK] |
| Dental | Dentrix (on-prem), Eaglesoft | Dentrix Ascend, Open Dental, Denticon; Weave (comms) | Eligibility Pro, Weave insurance capture, Arini | Verified |
| Medical | Server-based EHRs | athenahealth, eClinicalWorks, NextGen, Tebra, DrChrono | AI scribes | [BK] |
| Therapy / allied health | Paper notes | SimplePractice, Jane, TherapyNotes, ChiroTouch | Jane AI Scribe | Jane, SimplePractice verified; others [BK] |
| Veterinary | Cornerstone (IDEXX, server-based), AVImark, ImproMed | ezyVet, Covetrus Pulse, Digitail, Vetspire | AI SOAP notes (Shepherd) | Cornerstone, ezyVet verified ([RaftLabs](https://www.raftlabs.com/blog/best-veterinary-practice-management-software)); others [BK] |
| Auto repair | Mitchell 1 Manager SE, R.O. Writer, Protractor; dealers on CDK/Reynolds | Tekmetric, Shopmonkey, Shop-Ware, AutoLeap; PartsTech, AutoVitals | — | Tekmetric/Shopmonkey/Mitchell verified (vendor); rest [BK] |
| Childcare & tutoring | Paper sign-in, Tadpoles | Brightwheel, Procare, Kangarootime, Lillio, Famly; TutorBird, Teachworks, Jackrabbit; Teachable/Kajabi | — | Brightwheel, Procare verified; rest [BK] |
| Pet services | Kennel Connection, paper/Google Calendar | MoeGo, Gingr, PetExec, DaySmart Pet | — | MoeGo, Gingr verified ([Capterra](https://www.capterra.ca/compare/136469/165732/gingr/vs/moego)); rest [BK] |
| Hospitality / STR | Spreadsheets + OTA extranets, desktop PMS | Hostaway, Guesty, Hospitable, Lodgify, Smoobu; Cloudbeds, Little Hotelier | Native AI guest messaging | Channel managers verified (vendor claims); hotel PMS [BK] |
| Accounting / tax firms | Drake, Lacerte, UltraTax, ProSeries, CCH (desktop tax engines) | Karbon, TaxDome, Canopy, Financial Cents | Canopy AI intake / Smart Prep | Practice mgmt verified; tax engines [BK] |
| Law | PCLaw, Timeslips, Amicus, Tabs3 | Clio, MyCase, PracticePanther, Smokeball, Filevine | Clio Work + vLex Vincent | Clio, PCLaw verified; others [BK] |
| Agencies / consultants / creatives | Spreadsheets, QB Desktop | HoneyBook, Dubsado, Bonsai, Harvest, Toggl; Studio Ninja (Captura), Pixieset | HoneyBook AI | HoneyBook, Studio Ninja verified; others [BK] |
| Real estate sales | Top Producer, IXACT | BoldTrail, Follow Up Boss, Lofty, dotloop, SkySlope | AI lead response | BoldTrail verified; rest [BK] |
| Property management | Yardi Voyager, Rent Manager, spreadsheets | AppFolio, Buildium, Yardi Breeze, DoorLoop, Rentvine | Realm-X Performers, Buildium Lumina | AppFolio, Buildium verified ([G2](https://www.g2.com/compare/appfolio-property-manager-vs-buildium-vs-yardi-breeze)); rest [BK] |
| Insurance agencies | Applied TAM, AMS360 desktop roots | Applied Epic (larger), HawkSoft, NowCerts (1–5 users), EZLynx | AI COI/servicing agents | Epic/HawkSoft/NowCerts verified ([QuoteSweep](https://www.quotesweep.com/blog/ams-comparison-2026)); rest [BK] |
| E-commerce / makers | Magento 1, on-prem ERP | Shopify, WooCommerce, BigCommerce, Amazon, Etsy; ShipStation, Cin7; Katana, MRPeasy, Fishbowl | Shopify Sidekick | MRPeasy/Katana sync verified; rest [BK] |
| Trucking / logistics | Paper, Excel, TruckMate | Tailwind TMS, Axon, Rose Rocket/TMS.ai; ELDs (Samsara, Motive) | TMS.ai | Tailwind, Axon, TMS.ai verified; rest [BK] |
| Nonprofit / church | Raiser's Edge 7, DonorPerfect | Bloomerang (+Qgiv), Little Green Light, Planning Center, Givebutter | Blackbaud Copilot | Bloomerang verified; rest [BK] |

### Compliance is the main brake on automation design

Some compliance constraints are verified and should hard-wire guardrails into the plan generator:

- **PCI DSS v4.0.1** has been fully in force since **March 31, 2025** ([SecurityMetrics](https://www.securitymetrics.com/program-education/pci-dss-v4-faqs)). Hosted checkout (Stripe, Shopify) keeps a small merchant in the lightest questionnaire, SAQ A ([Beancount](https://beancount.io/blog/2026/07/09/pci-dss-4-0-small-merchant-guide)). The plan should therefore send payment links, never have an agent capture card numbers [Design].
- **HIPAA** requires a business associate agreement (BAA) with any vendor that touches protected health information. Jane signs BAAs but does not publish the text ([Paubox](https://www.paubox.com/blog/is-jane-app-hipaa-compliant-2025-update)). A health practice's plan must check BAA coverage for every tool in the chain, including the AI features and the large language model (LLM) provider [Design].
- **ELD rules (trucking):** FMCSA revoked **34–38 ELDs in 2025**, and carriers get 60 days to replace a revoked device ([FreightWaves](https://www.freightwaves.com/news/fmcsa-removes-five-elds-warns-fleets-to-switch-by-dec-16)).
- **Childcare ratios** are set by each state, and software makes the center configure its own state's rules ([Procare](https://www.procaresoftware.com/capabilities/monitor-staff-child-ratios/)).

Several other constraints matter but are [BK] and need verification before they become product rules:

- **SMS:** TCPA consent and 10DLC registration for automated texting.
- **Legal:** ABA Rule 1.15 trust accounting and Formal Opinion 512 on generative AI.
- **Tax:** IRC §7216 limits on sharing taxpayer data with third-party AI, and the FTC Safeguards Rule's written security plan.
- **Real estate:** buyer-representation agreements after the NAR settlement, and fair-housing exposure in AI screening.
- **Construction:** certified payroll and lien deadlines.
- **E-commerce:** sales-tax nexus and the end of the de minimis import exemption.
- **Nonprofits:** written acknowledgment for gifts of $250 or more.

## The intake form: five core sections, one optional deep-dive, one industry module

Existing instruments supply the structure. The EU Digital Maturity Assessment opens with firmographics (sector, size) and then scores dimensions such as strategy, readiness, people, data, and automation and AI ([EDIH DMA questionnaire](https://european-digital-innovation-hubs.ec.europa.eu/system/files/2024-02/DMA%20Questionnaire%20for%20SMEs_EDIH_network_EN_v2.1.pdf)). Blue Prism's Process Assessment Tool scores each process on two axes, "automation potential" and "ease of implementation", and estimates hours saved ([Blue Prism](https://bpdocs.blueprism.com/pat/en-us/pat-about.htm)).

One finding should temper the instinct to build a giant tool checklist. In a study of Luxembourg manufacturing SMEs, **people/human-centric factors (r = 0.717) and strategy (r = 0.652) correlated most strongly with digital maturity, while tools owned correlated weakly** ([Univ. Luxembourg](https://orbilu.uni.lu/bitstream/10993/66164/1/technologies-13-00541.pdf)). The form must capture who will own the automations and how comfortable they are, not just what software they have.

The pain-point options are grounded in survey evidence:

- **Admin load:** 36% of SMB owners name admin (email, scheduling, data entry) as their biggest time drain ([Thryv via Paint & Panel](https://www.paintandpanel.com.au/news/news/thryv-launches-better-things-to-do-to-put-time-back-in-tradies-hands)).
- **Unpaid invoices:** **56% of US small businesses are owed money on unpaid invoices**, averaging **$17,500**, and 47% have invoices more than 30 days overdue ([QuickBooks](https://quickbooks.intuit.com/r/growing-complex-businesses/midsize-payments-research/), secondary).
- **Missed calls:** about **44% of 70M tracked calls were missed** ([JustCall citing Invoca](https://justcall.io/blog/missed-call-statistics.html)). In a UK study, 47% of 142 small businesses missed the first call ([Alliance Virtual Offices](https://www.alliancevirtualoffices.com/virtual-office-blog/shocking-research-finds-small-businesses-miss-almost-half-of-incoming-calls/)).
- **Unreliable figure:** the much-repeated "23 hours a week on admin" statistic could not be traced to SCORE and should not be used ([Stealth Agents](https://stealthagents.com/research/smb-administrative-overhead-statistics-2026)).

The UX rules are lightly evidenced. NN/g supports explicit required-field markers ([NN/g](https://nngroup.com/articles/required-fields)). Multi-step wizards with progress bars, back/edit and conditional fields are standard practice. The often-quoted 20–40% completion lift for multi-step forms is an unverified vendor claim ([Atticus Li](https://atticusli.com/behavioral-science-glossary/progressive-disclosure/)).

Recommendations [Design]:

- Target 10–12 minutes for the required core.
- Ask for ranges, not exact numbers.
- Use a searchable logo grid with aliases and "Other" for tools.
- Pre-fill defaults from the chosen sub-type.
- Save progress so users can resume later.
- Show a teaser result (for example, "about 6 hours/week recoverable") before offering the optional deep-dive.

Everything in the tables below is [Design] unless a "Why" cell cites evidence.

### Section 1 — Business profile (required, about 2 minutes)

| # | Question | Field type | Answer options | Why it matters for the plan |
|---|---|---|---|---|
| 1.1 | What best describes your business? | Tile grid, single-select + optional "also" secondary | The ~15–20 tiles above + Other (text) | Selects recipe library, industry module and compliance defaults; secondary handles hybrids (bakery + online shop) |
| 1.2 | Which type? | Dynamic single-select + Other | Sub-types for the chosen tile | Pre-fills 1.3–1.5 traits; stores a hidden NAICS code for benchmarking |
| 1.3 | How do customers buy from you? | Multi-select, pre-checked | Book appointments; Request quotes/estimates; Walk in / order at counter; Buy products online; Subscriptions/memberships/recurring service; Projects/retainers; Donations/membership dues | Chooses the core stack: booking + reminders vs quote-to-cash vs POS vs e-commerce vs recurring billing |
| 1.4 | Where does the work happen? | Multi-select, pre-checked | At the customer's location; At our shop/office/studio; Online/remote | Field work adds dispatch, routing, photos, mobile invoicing, offline-tolerant tools |
| 1.5 | Who are your customers? | Multi-select | Consumers; Businesses; Government; Donors/members | B2B adds proposals, contracts, net terms, pipeline; B2C adds reviews, SMS, booking |
| 1.6 | How many people work in the business, including you? | Single-select | Just me; 2–4; 5–9; 10–19; 20–49; 50–249 | Maps to Census/Pew/UK bands; "just me" skips roles/handoffs and makes owner time the bottleneck |
| 1.7 | Who does what? (skip if solo) | Multi-select | Owner/manager; Front desk/admin; Sales; Field techs/service staff; In-house bookkeeper; Outside accountant/bookkeeper; Virtual assistant; Marketing | Assigns an owner to each automation and designs handoffs |
| 1.8 | How many locations? | Single-select | 1; 2–3; 4–10; 10+; Mobile only | Multi-location needs centralized booking/reporting and changes tool choice |
| 1.9 | Country and state/province | Dropdowns | Country list; region list | Drives tool availability (QBO vs Xero vs MYOB vs Tally), privacy law (GDPR, CCPA) and SMS rules |
| 1.10 | New inquiries/customers per month | Single-select | <10; 10–50; 51–200; 201–1,000; 1,000+ | Volume driver for ROI; low-volume firms get lighter tools |
| 1.11 | Typical sale or job value | Single-select | <$50; $50–200; $200–1K; $1K–10K; $10K+ | Converts missed calls, no-shows and late invoices into dollars |
| 1.12 | Annual revenue (optional) | Single-select | <$50K; $50–250K; $250K–1M; $1–5M; >$5M; Prefer not to say | Sets budget expectations and tool tier |

### Section 2 — Goals and pain points (required, about 2 minutes)

| # | Question | Field type | Answer options | Why it matters |
|---|---|---|---|---|
| 2.1 | What do you most want? (pick up to 3) | Multi-select, max 3 | Save my time; Respond to leads faster; Fewer no-shows; Get paid faster; Fewer errors; More reviews; See my numbers clearly; Grow without hiring; Better customer experience | Weights recipe ranking and the plan's headline |
| 2.2 | Which tasks are most painful? (pick up to 5) | Checklist, max 5, filtered by industry | Answering calls / missed calls; Replying to inquiries, DMs, web forms; Scheduling & rescheduling; Reminders & no-shows; Quotes/estimates & follow-up; Invoicing; Chasing late payments; Bookkeeping & reconciliation; Re-typing data between apps; Email inbox triage; Client onboarding paperwork/intake forms; Contracts & e-signatures; Social posting; Email newsletters; Asking for reviews; Inventory & reordering; Payroll & timesheets; Staff scheduling; Reporting; Compliance documents | Seeds the task inventory and maps directly to the recipe library; options reflect the admin, payment and call evidence above |
| 2.3 | Hours per week you personally spend on admin | Single-select | 0–5; 6–10; 11–15; 16–20; 20+ | Baseline for "hours recovered"; reported owner figures range roughly 8–16 h/week from weak sources |
| 2.4 | Baseline metrics (optional, shown by model) | Single-selects, each with "Don't know" | Calls missed: <10% / 10–25% / 25–50% / >50%; No-show rate: <5% / 5–10% / 10–20% / >20%; Invoices paid late: <10% / 10–30% / 30–50% / >50%; Days to get paid: <7 / 7–30 / 31–60 / 60+ | Lets the plan quantify dollar impact; shown only to appointment, quote or invoice-heavy models |

### Section 3 — Tools and data (required, about 3 minutes)

| # | Question | Field type | Answer options | Why it matters |
|---|---|---|---|---|
| 3.1 | Your main industry software | Searchable single/multi-select, filtered by tile | Vertical catalog above + "None — I use general tools" + Other | Identifies the system of record and its native automations to switch on first |
| 3.2 | What do you use for each function? | Logo-grid multi-select per function, with search, aliases and Other | Per the horizontal catalog; **every function includes manual options**: Paper/notebook; Excel/Google Sheets; Personal phone/texts; Paper checks; Fax; Desktop software; On-site server; "My accountant/bookkeeper handles it"; "Nothing" | Integration tier lookup (A/B/C); manual answers trigger digitize-first steps |
| 3.3 | Flagged legacy tools (auto-shown) | Info + single-select | If QB Desktop, QB POS, Office 2016/2019, on-prem Exchange, CoConstruct etc. selected: "Planning to switch?" Yes, soon / Maybe / No | Inserts a migration step before automations that the old tool would block |
| 3.4 | For each core tool, how do you feel about it? | Per-tool single-select | Keep it; Open to replacing; Actively want to replace | Tells the engine whether to automate around a tool or recommend switching |
| 3.5 | Where does your customer list live? | Single-select | Paper/notebook; Phone contacts; Spreadsheet; Email inbox; Industry software/CRM; Several places | Data-readiness gate; scattered data means "consolidate contacts" is step one |
| 3.6 | Do you have admin logins to your key accounts? | Single-select | Yes, all; Some (a vendor/agency/ex-employee controls others); Not sure | DIY setup fails without admin access to connect apps |
| 3.7 | Which AI tools do you use, and for what? | Multi-select tools + multi-select tasks | ChatGPT, Claude, Gemini, Copilot, vendor-built AI, None × Writing; Customer replies; Marketing content; Bookkeeping; Research; Phone answering | AI adoption estimates range from about 9% to 58% depending on definition, so ask concretely; sets the starting point for AI recipes |
| 3.8 | Already automated anything? | Yes/No + text | Free text | Avoids duplicating, and signals skill level |

### Section 4 — Task deep-dive (optional "improve my plan", repeat for top 3 tasks from 2.2)

This section operationalizes the RPA literature's selection criteria. Good candidates are rule-based with little judgment, standardized and stable, high-frequency, and built on structured digital inputs ([arXiv 2007.10900](https://arxiv.org/pdf/2007.10900v1); [arXiv 2609.09137](https://arxiv.org/pdf/2609.09137)). It also borrows the 5/3/1 rule-based scale used by practitioners ([Morgan Franklin](https://www.morganfranklin.com/?p=11502)).

| # | Question | Field type | Answer options | Feeds score |
|---|---|---|---|---|
| 4.1 | How often? | Single-select | Many times a day; Daily; A few times a week; Weekly; Monthly; Rarely | Frequency per week (midpoint) |
| 4.2 | How long each time? | Single-select | <5 min; 5–15; 15–30; 30–60; 1–2 h; 2 h+ | Minutes per occurrence |
| 4.3 | Who does it? | Single-select from 1.7 | Roles | Automation owner; owner-time is weighted higher |
| 4.4 | What starts it? | Single-select | Customer calls; Form/booking submitted; Email arrives; Payment/invoice event; A date or deadline; Job completed; Someone decides | Determines the trigger in the recipe |
| 4.5 | Where does the information come from? | Multi-select | Phone/voice; Paper; Email/PDF; Text/DM; Web form; Spreadsheet; Software app | Digital-input score: paper/phone = 1, email/PDF/text = 3, form/app/sheet = 5 |
| 4.6 | Where does it end up? | Multi-select from Section 3 tools | Tools | Integration path and tier |
| 4.7 | How much judgment does it take? | Single-select | Same steps every time; Mostly the same, some exceptions; Different every time | Rule-based score 5 / 3 / 1 |
| 4.8 | What happens if it's late or wrong? | Single-select | Minor annoyance; Wasted time; Lost money or customer; Legal/compliance risk | Error multiplier; compliance risk forces a human-approval step |
| 4.9 | Describe the steps (optional) | Long text | Free text | LLM parsing for edge cases |

The proposed priority score is **weekly hours × rule-based score × digital-input score × (1 + error cost) ÷ implementation effort**. Effort rises when tools are Tier B or C, tech comfort is low, or data is regulated. This mirrors Blue Prism's potential-versus-ease split. No study validates these weights, so treat them as starting values to tune against outcome data [Design].

### Section 5 — Readiness and constraints (required, about 2 minutes)

These fields come straight from documented barriers. OECD work cites skills shortages for more than half of SMEs, plus time, maintenance costs, data readiness and legal uncertainty ([OECD](https://www.oecd.org/en/publications/sme-digitalisation-for-competitiveness_197e3077-en.html)). **70% of US SMB owners say they need more AI training** ([Thryv 2026](https://www.businesswire.com/news/home/20260625243838/en/Despite)).

| # | Question | Field type | Answer options | Why it matters |
|---|---|---|---|---|
| 5.1 | How comfortable are you with setting up apps? | 1–5 scale with anchors | 1 "I avoid new apps" … 3 "I can follow a video tutorial" … 5 "I've built Zaps/workflows" | Gates recipe complexity: native features → Zapier/Make templates → n8n/API |
| 5.2 | Time you can spend on setup | Single-select | <1 h/week; 1–3; 3–5; 5+ | Sequences the plan into weekly milestones |
| 5.3 | Monthly budget for new tools | Single-select | $0; <$50; $50–150; $150–500; $500+ | Filters tool recommendations by price tier |
| 5.4 | How do you want to do this? | Single-select | Fully DIY with step-by-step guides; Mix — DIY plus help on hard parts; Done-for-you | Output format and whether to suggest a consultant or vendor setup service |
| 5.5 | Main device for running the business | Single-select | Mostly phone; Mostly computer; Both | Phone-first users get mobile-app and SMS-based recipes |
| 5.6 | Sensitive data and rules that apply | Multi-select, pre-checked by industry | Patient health info (HIPAA); Card payments (PCI); Client funds/trust accounts; Tax return data; Children/minors; EU/UK customers (GDPR); California customers (CCPA); Text-message marketing (TCPA/10DLC); Licensed/regulated profession; None/Not sure | Suppresses or modifies recipes: BAA-only tools for PHI, payment links instead of card capture, SMS consent capture, human sign-off on regulated steps |
| 5.7 | Practical constraints (optional) | Multi-select | Unreliable internet at job sites; Shared devices; No dedicated business phone number; Staff not tech-savvy; Seasonal business | Offline-capable tools, number porting/second line, training steps, seasonal timing |
| 5.8 | Anything else? | Long text | Free text | Catches context that doesn't fit the options |

### Section 6 — Conditional industry modules (2–5 questions each)

Each module is shown only for the matching tile or model. These are [Design] recommendations built on the verified and [BK] task lists in the notes.

| Module (trigger) | Questions → options | Plan outputs it enables |
|---|---|---|
| Appointment-based (salon, clinic, fitness, pet, auto) | How do clients book? (Phone; Text/DM; Online booking; Walk-in) · Deposits or card on file? (Yes/No) · Rebooking: do you ask at checkout? · Waitlist? | Online booking, multi-touch reminders, deposit/no-show policy through hosted pay links, rebooking and waitlist fill |
| Quote/project (trades, construction, agencies, events) | How are estimates made? (Paper; Spreadsheet; Software) · % of quotes followed up (Don't know/<25/25–75/>75) · Deposits/progress billing? · Change orders? · Subcontractors? | Lead form → CRM → instant reply, estimate follow-up sequences, deposit invoices, change-order e-sign, sub COI tracking |
| Field service (on-site work) | Dispatch method (Phone/text; Whiteboard; Software) · Paper work orders? · Photos required? · Maintenance agreements? | Digital work orders, on-my-way texts, photo-to-job notes, agreement renewals, mobile invoicing |
| Food & beverage | POS · Delivery apps used (DoorDash, Uber Eats, Grubhub, own) · Phone orders/reservations volume · Invoice entry method · Staff scheduling tool | Delivery tablet consolidation, AI phone ordering, invoice-to-food-cost capture, shift scheduling |
| Retail / e-commerce | Sales channels (store, own site, Amazon, Etsy, eBay, wholesale) · SKU count (<50/50–500/500–5K/5K+) · Inventory counted how? · Ships how? · Returns volume | Channel/inventory sync, reorder points, shipping labels, "where is my order" auto-replies, payout reconciliation |
| Health practices | EHR/PMS · Accepts insurance? · Eligibility checks done how? (Portal by hand; Clearinghouse; Software) · Intake forms paper or digital? · BAAs on file? | Digital intake, eligibility automation, recall/reactivation, AI scribe (BAA-covered only) |
| Professional services | Billing model (Hourly; Fixed; Retainer; Contingency) · Time tracking tool · Client document collection method · Trust account? · Engagement letters e-signed? | Client portal/organizers, document chasing, time-to-invoice sync, engagement e-sign; trust steps kept human |
| Real estate & property | Agent or PM · CRM/PM software · Lead sources (portals, referrals, ads) · Units managed · Maintenance request intake | Instant lead response + nurture, transaction checklists, maintenance triage, rent reminders, owner statements |
| Childcare & education | Licensed capacity · Subsidy (state CCAP) billing? · Attendance method · Parent communication channel | Digital check-in feeding billing, immunization/form tracking, parent messaging; state-configured ratios |
| Transportation | Truck count · ELD provider · How loads arrive (email rate cons; Load boards; Direct) · Factoring? · IFTA handled by | Rate-con parsing to load entry, BOL/POD capture to invoice/factoring, IFTA mileage reports; ELD revocation check |
| Nonprofit | Donor CRM · Online giving tool · Gifts/year · Volunteers? · Grants? | Gift acknowledgments, year-end statements, dedupe, volunteer scheduling |
| Subscription/membership | Billing tool · Failed-payment rate · Cancellation process | Dunning, win-back, freeze/cancel flows |

### From answers to a plan

The generator should map pain points to a fixed recipe library, prioritized where the evidence is strongest:

- **Appointment reminders.** A meta-analysis of about 21 studies found people receiving digital reminders were **25% less likely to no-show** (15% vs 21%), and multiple notifications beat a single one ([PubMed 27798006](https://pubmed.ncbi.nlm.nih.gov/27798006/)). Wording also matters ([PMC7310733](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7310733/)).
- **Speed-to-lead.** In one study, **over 99% of 114 B2B companies failed to respond to leads within 5 minutes** ([Workato](https://workato.com/the-connector/lead-response-time-study)).
- **Review requests.** Seven in ten consumers will leave a review if asked ([BrightLocal 2016](https://www.brightlocal.com/learn/local-consumer-review-survey-2016/)).
- **Invoice reminders.** These follow from the unpaid-invoice data above.

Evidence for AI chat, content generation and bookkeeping sync is mostly vendor self-report. Rank those recipes lower until outcome data arrives.

The sequencing logic for a plan [Design]:

1. Fix data first. If the customer list or books are on paper or scattered, consolidate them before automating.
2. Migrate off tools that are past their support cliff.
3. Switch on native automations in the existing system of record.
4. Add Tier A no-code recipes.
5. Reach Tier B/C tools only through marketplace apps, exports or document extraction.
6. Apply compliance filters at every step: PHI only through BAA-covered tools, hosted payment links instead of card capture, SMS opt-in, and human approval on trust-account, e-file and other regulated steps.

## Conclusion

Most of a good automation plan comes from two answers that most intake forms do not ask: what kind of API sits behind each tool the business uses, and how the business's work arrives. Industry labels mostly decide the vocabulary and the compliance guardrails. The integration tier of the system of record decides what a DIY user can do this month. The operating model decides which proven recipes (reminders, lead response, payment chasing, reviews) apply. Because tools owned correlate weakly with maturity, the readiness questions (comfort, time, admin access, data location) can matter as much as the tool picker.

Two time-sensitive opportunities stand out. First, incumbents now bundle AI receptionists and agents (Jobber, ServiceTitan, Toast, Jane, Dentrix Ascend, AppFolio), so the highest-value step in many plans is "turn on what you already pay for", not "buy a new tool". Second, 2025–2027 support cliffs (QuickBooks Desktop, Office/Exchange, CoConstruct) are forcing migrations, and a plan can turn each one into an automation upgrade. Before launch, the team should verify the [BK] items in the vertical tool catalog and the Zapier/Make/n8n coverage of each tool against live directories. It should also start logging which recipes users actually complete, so the priority-score weights can be tuned against real outcomes rather than judgment.
