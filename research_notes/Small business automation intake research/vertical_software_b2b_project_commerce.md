# Vertical Software for Small Businesses: Professional Services, Project-Based, Commerce and Industrial (as of Oct 2026)

Method note: I ran 16 web searches (no full-page fetches) on 2026-10-29. Most search results were vendor marketing, competitor comparisons, or G2/Capterra pages. Primary-source confirmation was thin for several verticals. Every item under "Cited Findings" has a source. Items under "Inferences" that start with **[BK]** come from background knowledge (training data to mid-2026) and were NOT verified in this session. The report writer should treat [BK] items as likely but unconfirmed and keep that caveat.

---

## Q1. Dominant tools, legacy holdouts and the tool landscape per vertical (legacy to AI-native), with API availability

### Takeaway
Every vertical has the same layers: an entrenched legacy or on-prem system of record (tax engines, PCLaw/Timeslips, Applied Epic/AMS360, Sage 100 Contractor, Fishbowl/Sage 100, Blackbaud), a mainstream cloud practice or job-management layer (Clio, Karbon/TaxDome, Buildertrend/Procore, AppFolio/Buildium, Shopify), and a 2025–26 wave of incumbents rebranding as "AI-native" or "agentic" (Clio + vLex, Rose Rocket -> TMS.ai, AppFolio Realm-X Performers, Canopy AI intake). Consolidation is real. CoConstruct is being retired into Buildertrend, kvCORE was renamed BoldTrail, Studio Ninja was bought by ImageQuix/Captura, and Bloomerang bought Qgiv. Modern cloud tools usually have public APIs. Legacy desktop tools (tax engines, PCLaw, Timeslips, Sage 100 Contractor) mostly do not, which is where RPA, file-drop or browser automation is needed.

### Cited Findings

**Accounting / bookkeeping / tax firms**
- Canopy lists native document management, billing, client portal and e-signature, plus AI Document-Intake, Smart Prep, AI-Tax Delivery and IRS transcript management. — [Canopy (vendor)](https://www.getcanopy.com/?p=13914)
- TaxDome markets mobile document scanning, e-signatures, workflow templates from data collection through invoicing, and AI-powered team performance/profitability reporting. — [TaxDome blog (vendor)](https://taxdome.com/blog/best-karbon-alternatives)
- Karbon relies on integrations (Dropbox, OneDrive, SuiteFiles) for document management. Customizable organizers and e-signatures need third-party tools (per a Canopy comparison and Karbon's own material). Karbon calls TaxDome "significantly cheaper" than Canopy. — [Karbon: TaxDome vs Canopy](https://karbonhq.com/resources/taxdome-vs-canopy/); [G2 Canopy vs Karbon](https://www.g2.com/compare/canopy-2026-05-12-vs-karbon-2025-03-03)
- On G2 agentic-AI scores, Karbon rates above Canopy on autonomous task execution (8.3 vs 6.7) and natural-language interaction (8.1 vs 6.4). These rest on only 7–8 reviews. — [G2 Canopy vs Karbon](https://www.g2.com/compare/canopy-2026-05-12-vs-karbon-2025-03-03)
- Not found: the Karbon "State of Practice" survey. My search returned only unrelated "carbon" reports.

**Law firms**
- Clio completed a ~US$1B acquisition of vLex in Nov 2025, alongside a US$500M Series G at a US$5B valuation (led by NEA). Coverage calls it the largest legal-tech M&A deal to date. — [Canadian Lawyer](https://www.canadianlawyermag.com/resources/legal-technology/clio-completes-us1-billion-acquisition-of-vlex-closes-us500-million-funding-round-at-us5-billion-valuation/393346); [LawNext](https://www.lawnext.com/2025/11/clio-completes-historic-1-billion-vlex-acquisition-announces-500-million-series-g-at-5-billion-valuation-plus-exclusive-interview-with-ceo-and-cfo.html); [vLex (vendor)](https://vlex.com/news/vLex-Joins-Clio-in-Landmark-1B-Acquisition-And-Clio-Announces-Series-G-5B-Valuation)
- Clio now combines Clio Work, Clio Manage, Clio Grow and Clio Draft with vLex's Vincent AI (1B+ documents, 110 jurisdictions) as the "Intelligent Legal Work Platform". Clio Work (unveiled at ClioCon, Oct 2025) pairs matter data with legal research for AI research and case strategy. — [Canadian Lawyer](https://www.canadianlawyermag.com/resources/legal-technology/clio-completes-us1-billion-acquisition-of-vlex-closes-us500-million-funding-round-at-us5-billion-valuation/393346); [LawNext](https://www.lawnext.com/2025/11/clio-completes-historic-1-billion-vlex-acquisition-announces-500-million-series-g-at-5-billion-valuation-plus-exclusive-interview-with-ceo-and-cfo.html)
- Legacy holdouts:
  - Recent PCLaw versions no longer support the PCLaw–Amicus Attorney link, according to a reseller notice.
  - The same reseller notice says the PCLaw maker raised Annual Maintenance Plan pricing to $89/user/month.
  - Abacus Next charges $750 in professional services to set up the Amicus–PCLaw link.
  - Sources: [CrossPointe CG (reseller)](https://crosspointecg.com/pclaw/); [AbacusNext support](https://support.abacusnext.com/hc/en-us/articles/360041349432-How-do-I-link-Amicus-Attorney-by-CARET-with-PCLaw)
- Clio markets against Timeslips as "not cloud-based", requiring servers and VPNs (competitor framing). No end-of-life announcement was found for PCLaw, Amicus or Timeslips. — [Clio vs Timeslips](https://www.clio.com/compare/clio-vs-timeslips/)

**Real estate (agents/brokerages and property management)**
- Inside Real Estate retired the kvCORE name in mid-2024 and rebranded its product portfolio as **BoldTrail**. The company said no products or features were sunset, only renamed and unified. — [Inman](https://www.inman.com/2024/06/20/inside-real-estate-folds-kvcore-as-part-of-major-rebrand-as-boldtrail/); [HousingWire](https://housingwire.com/articles/inside-real-estate-rebrands-product-portfolio-as-boldtrail); [BoldTrail blog](https://boldtrail.com/blog/kvcore-vs-boldtrail/)
- AppFolio launched Realm-X (a GPT-powered copilot) in 2023 and announced **Realm-X Performers** (agentic workflow automation) in June 2025. — [Barchart/AppFolio PR](https://www.barchart.com/story/news/32825817/appfolio-unveils-ai-agents-to-transform-performance-in-real-estate); [AppFolio blog (vendor)](https://www.appfolio.com/blog/best-agentic-ai-property-management-software-compared-2026)
- Buildium embeds "Lumina AI" for accounting, leasing, maintenance and communication workflows. On G2, Buildium outscores AppFolio on most agentic-AI items (e.g., autonomous task execution 8.3 vs 7.7). Yardi Breeze scores lowest. Samples are small. — [G2 comparison](https://www.g2.com/compare/appfolio-property-manager-vs-buildium-vs-yardi-breeze); [stork.ai (aggregator)](https://www.stork.ai/alternatives/buildium)
- Third-party AI leasing/front-desk vendors advertise integrations with AppFolio, Buildium and Yardi Breeze. — [myaifrontdesk (vendor)](https://www.myaifrontdesk.com/multifamily/appfolio-realm-x-alternative)

**Insurance agencies**
- A 2026 comparison positions Applied Epic as the "industry standard" for larger agencies (20+ users). It recommends HawkSoft or NowCerts (Momentum AMP) for 1–5-user agencies. — [QuoteSweep AMS comparison 2026](https://www.quotesweep.com/blog/ams-comparison-2026)
- Applied Epic is described as having "open and scalable architecture" for Applied and third-party integrations. EZLynx is listed with an API and markets an all-in-one rater, AMS and customer portal. — [Software Advice](https://www.softwareadvice.com/insurance/applied-epic-profile/vs/ezlynx/); [GetApp](https://www.getapp.co.uk/compare/122115/122419/applied-epic/vs/ezlynx)

**Construction and contractors**
- Buildertrend (which acquired CoConstruct, most sources say Feb 2021) is phasing CoConstruct out. CoConstruct gets no new features. Per a JobTread post citing Buildertrend notices, no new CoConstruct projects can start from **April 1, 2027**, and migrations must begin by **June 30, 2027**. These dates are not confirmed against an official Buildertrend source. — [JobTread blog](https://jobtread.com/blog/leaving-coconstruct-here-is-why-builders-are-choosing-jobtread); [JobTread press release](https://www.jobtread.com/news/jobtread-opens-a-migration-path-for-builders-facing-the-coconstruct-phase-out); [Projul migration guide](https://projul.com/blog/coconstruct-shutdown-migration-guide/)
- CoConstruct has no standalone public API. — [Supergood API report card](https://supergood.ai/api-report-card/coconstruct)
- JobTread, BuildTools and Projul are actively marketing CoConstruct migration paths. — [BuildTools](https://www.buildtools.com/blog/2026-04-07-coconstruct-alternative-buildtools-migration)

**E-commerce and small manufacturers**
- MRPeasy has a native Shopify integration that syncs orders, stock movements, shipments, customers and order status. Reviewers report slight sync lag. MRPeasy does not push "virtual inventory" (buildable kits) to Shopify. — [MRPeasy Shopify page](https://mrpeasy.com/shopify); [Shopify App Store](https://apps.shopify.com/mrpeasy-manufacturing-system); [Shopify Community](https://community.shopify.com/t/shopify-and-manufacturing-inventory-platform/273581)
- One Katana user reported Katana-to-Shopify inventory sync breaking for days (anecdotal). — [Shopify Community](https://community.shopify.com/t/shopify-and-manufacturing-inventory-platform/273581)
- MRPeasy API access and webhooks are only in its top tier (~$149/user/month). Fishbowl is positioned for ~$3M–$50M revenue companies. — [Qoblex (competitor blog)](https://qoblex.com/blog/mrpeasy-vs-fishbowl/)

**Logistics / trucking**
- Tailwind TMS targets small and mid-size carriers (dispatch, accounting, IFTA, maintenance). It is priced per seat at ~$99/$149/$199 per user/month, with EDI only in the top tier. — [rfp.wiki](https://www.rfp.wiki/supply-chain-logistics-transportation/transportation-logistics/trucking-erp-software/tailwind-software/rose-rocket)
- Axon targets ~25–100-truck carriers with combined dispatch and accounting. Implementation takes 4–8 weeks, and the UI is described as less modern. — [GoFreight 2026](https://gofreight.com/blog/best-tms-trucking-companies)
- Rose Rocket launched **TMS.ai** in Feb 2025 as an "AI-native" TMS, a rebuild and rebrand of its platform. The company still contracts as Rose Rocket Inc. Its focus has shifted toward brokers, 3PLs and configurable supply-chain ERP. Reported starting price is ~$2,080/month (competitor-sourced). — [Rose Rocket blog](https://www.roserocket.com/blog/release-rose-rocket-ai-native-tms); [CCJ](https://www.ccjdigital.com/technology/article/15737912/rose-rocket-selfdisrupts-creating-an-ainative-tms); [Datatruck (competitor)](https://www.datatruck.io/blog/rose-rocket-tms-alternatives)

**Nonprofits and churches**
- Bloomerang acquired Qgiv (online giving, events, peer-to-peer) in **Dec 2023**, not 2025, after buying Kindful (2021) and InitLive (2023). The combined customer base is 23,000+ nonprofits. Warburg Pincus invested in Feb 2024. — [Bloomerang news](https://bloomerang.com/news/bloomerang-acquires-qgiv); [NonProfit Times](https://thenonprofittimes.com/npt_articles/bloomerang-crm-acquires-fundraiser-qgiv/)

**Photographers / event / wedding vendors**
- Studio Ninja was acquired by ImageQuix in Dec 2023 and now operates under the **Captura** brand. It integrates with Pic-Time, ShootProof and Pixieset. Its starter plan is ~$16/month, limited to 5 active jobs with no workflow automation. — [Agiled comparison (competitor)](https://agiled.app/compare/studioninja-vs-honeybook)
- HoneyBook raised prices in Feb 2025 (starter ~$36/month) and includes AI on all plans. — [Agiled comparison](https://agiled.app/compare/studioninja-vs-honeybook); [HoneyBook blog](https://www.honeybook.com/blog/honeybook-vs-studio-ninja)

### Inferences (per-vertical landscape; [BK] = background knowledge, unverified this session)

| Vertical | Legacy / on-prem | Mainstream | Modern cloud | AI-native / AI push | API status |
|---|---|---|---|---|---|
| Accounting/tax | [BK] Drake, Lacerte, UltraTax CS, ProSeries (desktop tax engines; Intuit ProConnect is the cloud sibling); CCH ProSystem fx | [BK] QuickBooks Online/Xero + practice mgmt | Karbon, TaxDome, Canopy, [BK] Financial Cents, Jetpack Workflow | Canopy AI intake/Smart Prep (cited); [BK] Intuit Assist, TR CoCounsel in UltraTax | [BK] Tax engines: little or no public API (file import/export, RPA). Karbon has a public API. TaxDome API limited/newer. QBO/Xero have rich APIs |
| Law | PCLaw, Timeslips, Amicus (cited, still sold, integrations eroding); [BK] Tabs3, ProLaw | Clio, [BK] MyCase (AffiniPay), PracticePanther, Smokeball | Clio, Smokeball (AI time capture), [BK] Filevine (PI) | Clio Work + vLex Vincent (cited); [BK] Harvey, CoCounsel, EvenUp (PI) | [BK] Clio: robust open API + 250+ app marketplace; MyCase/PracticePanther: APIs/Zapier; legacy: none |
| Agencies/consultants | [BK] spreadsheets, QuickBooks Desktop | HoneyBook, Dubsado, Harvest, Toggl | Bonsai, [BK] Productive, Teamwork, ClickUp | HoneyBook AI (cited) | [BK] Harvest/Toggl: strong public APIs; HoneyBook: limited (Zapier); Dubsado: Zapier/webhooks |
| Real estate sales | [BK] Top Producer, IXACT | BoldTrail (ex-kvCORE, cited), Follow Up Boss (Zillow-owned [BK]), dotloop (Zillow [BK]), SkySlope | [BK] Lofty, Sierra, Real's reZEN | [BK] AI ISA/lead response tools | [BK] Follow Up Boss: strong open API; dotloop: public API; SkySlope: partner API |
| Property mgmt | [BK] Yardi Voyager, Rent Manager (on-prem roots), spreadsheets | AppFolio, Buildium (RealPage), Yardi Breeze | DoorLoop, [BK] Rentvine, TenantCloud | AppFolio Realm-X Performers, Buildium Lumina (cited) | [BK] Buildium: open API; AppFolio: partner-gated "Stack" API; Yardi: Interfaces program (paid); DoorLoop: API |
| Insurance | [BK] Applied TAM (sunset into Epic), AMS360 (Vertafore, desktop roots) | Applied Epic, AMS360, HawkSoft | EZLynx (Applied-owned [BK]), NowCerts/Momentum (cited) | [BK] AI COI/servicing agents (e.g., Sonant, Patra) | Applied Epic open-architecture (cited); [BK] Vertafore Orange Partner APIs; HawkSoft historically closed (HawkSoft 6 adding API, unverified) |
| Construction | Sage 100 Contractor, [BK] Foundation (on-prem/hosted), Sage 300 CRE | Buildertrend, Procore | JobTread, [BK] Houzz Pro, Contractor Foreman, Knowify | [BK] Procore Helix/agents, Buildertrend AI | CoConstruct none (cited); [BK] Procore: extensive public API; JobTread: GraphQL "Pave" API; Buildertrend: limited/partner |
| E-commerce | [BK] Magento 1 (EOL 2020), on-prem ERPs | Shopify, WooCommerce, BigCommerce, Amazon Seller Central, Etsy | ShipStation, Cin7, Linnworks | [BK] Shopify Sidekick/agentic checkout | [BK] All have public APIs (Amazon SP-API, Etsy Open API v3, Shopify GraphQL Admin) |
| Manufacturing / wholesale | [BK] Sage 100, Macola (now ECI), QuickBooks Desktop Enterprise | Fishbowl, NetSuite, Odoo | Katana, MRPeasy (cited) | [BK] vendor copilots | MRPeasy API top tier only (cited); [BK] Katana open API; Fishbowl REST API (newer); NetSuite SuiteTalk; Odoo XML-RPC/JSON |
| Logistics | [BK] TruckMate, McLeod (larger), paper/Excel | Axon, Tailwind (cited) | Rose Rocket/TMS.ai (cited), [BK] Alvys, Truckbase | TMS.ai (cited); [BK] AI rate-con/BOL parsing | [BK] ELDs (Samsara, Motive) have strong APIs; small-carrier TMS APIs vary; EDI common |
| Nonprofit/church | [BK] Blackbaud Raiser's Edge 7 (desktop, migrated to NXT), DonorPerfect | Bloomerang (+Qgiv, cited), Little Green Light, Planning Center | [BK] Givebutter, Virtuous | [BK] Blackbaud "Copilot" features | [BK] Blackbaud SKY API (gated); Planning Center public API; LGL API; Bloomerang API |
| Photographers/events | [BK] Tave (acquired by VSCO) | HoneyBook, Studio Ninja (Captura, cited) | Pixieset Studio Manager, [BK] Sprout Studio | HoneyBook AI (cited) | [BK] mostly Zapier-level; few public APIs |
| Agriculture | [BK] spreadsheets, QuickBooks | [BK] Granular (Corteva), FarmLogs/Bushel, John Deere Operations Center, Climate FieldView | [BK] Traction Ag, Farmbrite | — | [BK] Deere and FieldView have developer APIs |

### Gaps
- No primary-source verification for these items: Drake, Lacerte, UltraTax, ProSeries market shares; MyCase, PracticePanther or Smokeball current status; Follow Up Boss, dotloop or SkySlope ownership; Harvest, Toggl, Bonsai, Dubsado details; Procore, JobTread or Foundation; Shopify, Amazon, Etsy API status; Cin7/Linnworks; NetSuite/Odoo/Macola; Blackbaud, LGL, Planning Center; Pixieset; agriculture. Search budget was spent on discontinuation and consolidation checks.
- Not located: the Karbon State of Practice report and the NAR 2025 technology survey.
- Not confirmed: HawkSoft API status, and AppFolio or Yardi API access terms.
- Not confirmed against a vendor primary source: the official CoConstruct shutdown dates.

---

## Q2. Most common manual and repetitive tasks (automation-ripe) per vertical

### Takeaway
Most of the manual work is in moving documents and data between systems, not in the core system of record. Examples: chasing client documents (tax, mortgage/real estate, insurance renewals), re-keying data between disconnected tools (Katana to Shopify, CoConstruct to accounting, tax engine to practice management), time capture and billing, and status updates. Vendors are now aiming AI at exactly these tasks (Canopy AI document intake, AppFolio agentic workflows, TMS.ai). Smaller firms are adopting AI much more slowly than larger firms, which leaves a gap that third-party automation can fill.

### Cited Findings
- Only 8% of solo practitioners and 4% of small law firms have adopted AI "widely or universally". — [Clio 2025 Legal Trends for Solo & Small Firms](https://www.clio.com/au/?p=1958); [Canadian Lawyer](https://www.canadianlawyermag.com/news/general/solos-and-small-firms-lag-with-ai-adoption-clio-report/392441)
- Clio's mid-sized report: 72% of smaller firms use AI in some capacity, but only 10% extensively. A 93% adoption figure is reported inconsistently, as either mid-sized firms only or mid-sized plus solo. — [Clio mid-sized press release](https://www.clio.com/about/press/clios-2025-legal-trends-for-mid-sized-law-firm-report/)
- Accounting vendors are targeting document intake (Canopy AI Document-Intake), tax organizers and IRS transcript retrieval. TaxDome templates run from data collection to invoicing, which shows where the manual labor is. — [Canopy](https://www.getcanopy.com/?p=13914); [TaxDome](https://taxdome.com/blog/best-karbon-alternatives)
- Property management AI is targeting accounting, leasing, maintenance and resident communication (Buildium Lumina, AppFolio Realm-X Performers). — [G2](https://www.g2.com/compare/appfolio-property-manager-vs-buildium-vs-yardi-breeze); [AppFolio PR](https://www.barchart.com/story/news/32825817/appfolio-unveils-ai-agents-to-transform-performance-in-real-estate)
- Inventory and order sync between MRP and storefront is fragile. Users report sync lag and multi-day failures, and kit/virtual inventory is not pushed. — [Shopify Community](https://community.shopify.com/t/shopify-and-manufacturing-inventory-platform/273581)
- Legacy integrations cost money and break: the PCLaw–Amicus time-posting link is unsupported in new versions, and setting it up costs $750. — [CrossPointe](https://crosspointecg.com/pclaw/); [AbacusNext](https://support.abacusnext.com/hc/en-us/articles/360041349432-How-do-I-link-Amicus-Attorney-by-CARET-with-PCLaw)
- Studio Ninja's starter tier has no workflow automation, so photographers on entry plans run inquiry, contract and invoice steps by hand. — [Agiled](https://agiled.app/compare/studioninja-vs-honeybook)

### Inferences (automation-ripe tasks; [BK] where not cited)
- **Accounting/tax:**
  - PBC/document chasing and organizers.
  - Engagement letters and e-sign.
  - Moving source docs (W-2/1099/K-1) into Drake, Lacerte or UltraTax ([BK] OCR import tools such as SurePrep, GruntWorx).
  - E-file status and acknowledgment follow-up, and IRS notice triage.
  - Monthly bookkeeping close: bank-feed categorization and receipt matching.
  - Recurring billing.
- **Law:**
  - Intake and conflict checks.
  - Time capture: [BK] Smokeball automatic time tracking is the reference example.
  - Trust-account three-way reconciliation.
  - Invoicing and collections.
  - Court deadline calendaring.
  - Document assembly.
  - Client status updates.
- **Agencies/consultants:**
  - Proposals, contracts and deposit invoices.
  - Time entries to invoices (Harvest/Toggl to QuickBooks).
  - Scope-change tracking.
  - Weekly client reports.
- **Real estate:**
  - Lead response and nurture.
  - Transaction checklists and disclosure-document collection for broker compliance review (dotloop/SkySlope).
  - Commission disbursement.
  - Property management: maintenance triage, rent delinquency follow-up, lease renewals, owner statements, applicant screening.
- **Insurance:**
  - Renewal remarketing and multi-carrier quoting (rater re-keying).
  - Certificates of insurance (COI) issuance.
  - Endorsements and policy-change servicing.
  - Downloading carrier documents into the AMS.
  - Commission reconciliation.
- **Construction:**
  - Estimates and takeoffs.
  - Change orders.
  - Daily logs.
  - Lien waivers and subcontractor COI tracking.
  - AIA G702/G703 progress billing.
  - Job-cost sync between the PM tool and accounting (Sage 100 Contractor, Foundation, QuickBooks).
  - CoConstruct-to-new-platform migration is a time-bound opportunity.
- **E-commerce:**
  - Order, inventory and listing sync across channels (Shopify, Amazon, Etsy).
  - Purchase orders and reorder points.
  - Returns and refunds.
  - Customer service "where is my order" (WISMO) tickets.
  - Payout reconciliation into accounting.
- **Manufacturing/wholesale:**
  - B2B order entry from email/PDF purchase orders.
  - BOM-driven purchasing.
  - EDI with retailers.
  - Lot and serial traceability records.
- **Logistics:**
  - Load entry from emailed rate confirmations.
  - BOL/POD collection and invoicing (factoring submission).
  - IFTA fuel-tax mileage reporting.
  - Driver settlements.
  - Customer track-and-trace updates.
  - Rose Rocket/TMS.ai's "AI-native" pitch targets these tasks.
- **Nonprofit/church:**
  - Gift entry and acknowledgment letters.
  - Year-end giving statements.
  - Donor data deduplication.
  - Volunteer scheduling.
  - Grant reporting.
- **Photographers/events:**
  - Inquiry response, availability checks and booking.
  - Contracts, retainers and payment-plan reminders.
  - Questionnaires.
  - Gallery delivery and print-sale follow-up.
- **Agriculture:**
  - Field records.
  - Input and spray logs.
  - Grain contracts and settlements.
  - H-2A labor paperwork.
  - USDA/FSA program filings.

### Gaps
- No quantitative survey data (hours per week by task) was found for any vertical other than legal AI adoption.
- Not located: the Karbon State of Practice, NAR tech survey, IVANS/insurance, and AGC/construction tech surveys.

---

## Q3. Compliance constraints per vertical

### Takeaway
Compliance is the main reason legacy systems stay in place and the main limit on automation design. Specific constraints:
- Trucking: ELD mandates, with FMCSA revoking devices at an accelerating rate.
- Law: trust/IOLTA accounting rules.
- Tax: IRS e-file and data-security rules.
- Real estate: disclosure and transaction-file retention.
- Construction: lien and certified-payroll rules.

Automation tools must keep audit trails and avoid touching regulated steps (trust disbursement, e-file signature) without a human sign-off.

### Cited Findings
- **ELD mandate (trucking):**
  - FMCSA revoked 34–38 ELDs in 2025, depending on the reporting date, up 62–80%+ vs 21 in 2024.
  - Five devices were revoked in Oct 2025 (Premium ELD, True Logbook, Xplore ELD, Kami ELD, Evo ELD 1), with a switch deadline of Dec 16, 2025.
  - Four more were revoked in Jan 2026, with replacement required by Mar 15.
  - Carriers have 60 days to replace a revoked device. After that they are treated as operating without an ELD and risk out-of-service orders.
  - About 1,133 ELDs were registered as of Oct 17, 2025.
  - FMCSA is overhauling ELD vetting to close re-registration loopholes.
  - Sources: [FreightWaves](https://www.freightwaves.com/news/fmcsa-removes-five-elds-warns-fleets-to-switch-by-dec-16); [FreightWaves revocations up 62%](https://www.freightwaves.com/?p=568509); [J.J. Keller](https://www.jjkeller.com/news/article/5-ELDs-removed-from-FMCSA-s-list_id-885a2862-45af-46dd-8270-6713da950e78); [Land Line](https://landline.media/feds-add-a-pair-of-elds-to-the-revoked-list/)
- **Tax:** Canopy builds in IRS transcript management, which shows that IRS-connected workflows (e.g., transcript retrieval through e-Services) are a core practice-management feature. — [Canopy](https://www.getcanopy.com/?p=13914)

### Inferences ([BK], not verified this session)
- **Tax:**
  - Each IRS e-file provider needs an EFIN and must follow IRS Pub 1345.
  - Signatures: Form 8879 e-signature identity rules.
  - Data security:
    - FTC Safeguards Rule (GLBA) requires a Written Information Security Plan (WISP).
    - IRC §7216 limits use or disclosure of taxpayer data, including sending it to third-party AI tools without consent.
    - IRS Pub 4557 security guidance.
  - Preparer filing: e-file mandate for preparers filing 10+ returns; PTIN.
  - Return volume moves to e-file every season, so tax engines remain the system of record.
- **Law:**
  - ABA Model Rule 1.15 and state IOLTA rules require three-way trust reconciliation and forbid commingling. This is why trust-aware billing (Clio, LawPay) matters.
  - ABA Formal Opinion 512 (July 2024) covers generative AI: competence, confidentiality and fees.
  - Conflict checks and confidentiality limit which automations are acceptable.
- **Real estate:**
  - Transaction files must hold state-mandated disclosures: seller property condition, lead-based paint (federal, pre-1978 housing), and agency disclosure. Broker review and retention (often 3–7 years by state) are required.
  - Post-NAR-settlement (Aug 2024): written buyer-representation agreements are required before touring, adding a document step.
  - RESPA, and Fair Housing exposure in AI lead and tenant screening.
  - Property management: state security-deposit trust rules, FCRA for tenant screening, source-of-income laws.
- **Insurance:**
  - State producer licensing and appointments.
  - E&O documentation of coverage offers and rejections.
  - State privacy and insurance data-security laws (NAIC model law, NYDFS Part 500 for NY licensees).
  - NAIC AI model bulletin (adopted by many states).
- **Construction:**
  - Mechanics' lien notice deadlines (state-specific).
  - Certified payroll (Davis-Bacon, WH-347) on public work.
  - OSHA recordkeeping.
  - Contractor licensing and subcontractor COI tracking.
  - Retainage. AIA billing formats.
- **E-commerce:**
  - Post-Wayfair economic-nexus sales tax across states.
  - Marketplace-facilitator rules.
  - INFORM Consumers Act (marketplace seller verification, 2023).
  - PCI-DSS.
  - Amazon/Etsy policy compliance.
  - The de minimis import exemption ended for all countries in Aug 2025, which affects DTC brands that import goods.
- **Manufacturing/wholesale:**
  - Lot traceability.
  - FDA FSMA 204 food traceability rule (compliance date delayed to 2028).
  - Retailer EDI compliance chargebacks.
- **Logistics (beyond ELDs):**
  - Hours of Service (HOS).
  - IFTA/IRP.
  - Drug & Alcohol Clearinghouse.
  - Driver qualification files.
  - Broker authority and bonds.
- **Nonprofit:**
  - IRS contribution acknowledgment for gifts of $250 or more.
  - Form 990.
  - State charitable solicitation registration.
  - Donor privacy.
- **Agriculture:**
  - USDA/FSA reporting.
  - EPA Worker Protection Standard and restricted-use pesticide records.
  - H-2A.

### Gaps
- None of the non-ELD compliance items above were re-verified with primary sources in this session. Before publishing, the report writer should confirm:
  - the current FSMA 204 date
  - the de minimis status
  - ABA Opinion 512
  - §7216 and FTC Safeguards details
  - any 2026 IRS e-file changes
- No ELD revocation batches after Jan 2026 were found. Check the current list at eld.fmcsa.dot.gov.
- No source found on state-level AI rules specific to small-business vertical software (e.g., Colorado AI Act's effect on tenant screening or insurance).
