# Designing an SMB Operations Intake Questionnaire for DIY Automation Plans

Research notes, compiled 2026-10-29. Research-environment caveat: direct fetches of primary pages (European Commission EDIH site, UiPath) failed because those hosts were blocked by the session's network allowlist, so several findings below rely on search-result summaries of those primary sources rather than full-text reads. Figures flagged "secondary" were reported via third-party coverage and should be verified before publication.

## Q1. What do existing assessments ask? (digital maturity / automation readiness / process discovery)

### Takeaway
Existing instruments split into two families: (a) **maturity/readiness assessments** (EU DMA, OECD D4SME) that start with firmographics (sector, size) and then score a handful of dimensions (strategy, readiness/tools adopted, skills/people, data management, automation & AI, sometimes green), and (b) **process-selection/discovery tools** (Blue Prism PAT, RPA discovery questionnaires) that inventory individual processes (trigger, steps, systems, volume, exceptions, inputs/outputs, owner) and score each on "automation potential" vs "ease of implementation." A DIY-plan intake should borrow the firmographic + dimension structure from (a) for context and the per-task inventory and two-axis scoring from (b) for prioritization.

### Cited Findings
- The EU Digital Maturity Assessment (DMA) for SMEs scores six dimensions: digital business strategy, digital readiness, human-centric digitalisation, data management, automation & AI, and green digitalisation, plus an overall maturity level. — [EDIH DMA Questionnaire for SMEs v2.1 (PDF)](https://european-digital-innovation-hubs.ec.europa.eu/system/files/2024-02/DMA%20Questionnaire%20for%20SMEs_EDIH_network_EN_v2.1.pdf); [EDIH DMA questionnaire (2024-05 version)](https://european-digital-innovation-hubs.ec.europa.eu/system/files/2024-05/DMA%20Questionnaire%20for%20SMEs_EDIH_network_EN_0.pdf)
- The DMA SME questionnaire opens with a "customer data" module (company details, sector, staff size) before the maturity module; it is administered at "T0" (before support starts) and re-run later to measure progress. — [EDIH DMA questionnaire PDF](https://european-digital-innovation-hubs.ec.europa.eu/system/files/2024-02/DMA%20Questionnaire%20for%20SMEs_EDIH_network_EN_v2.1.pdf)
- DMA scoring: each answer option maps to points that are summed into a total placing the respondent in a maturity band. — [EDIH DMA questionnaire PDF](https://european-digital-innovation-hubs.ec.europa.eu/system/files/2024-05/DMA%20Questionnaire%20for%20SMEs_EDIH_network_EN_0.pdf); [JRC/knowledge4policy DMA framework](https://knowledge4policy.ec.europa.eu/composite-indicators/coin-open-days_en/cod-digital-maturity-assessment-framework_en)
- One press item names a "digital skills improvement" dimension instead of "human-centric digitalisation" (naming discrepancy; EDIH naming is authoritative). — [EOC Cyprus](https://eoc.org.cy/?p=7955)
- A 2025 study of Luxembourg manufacturing SMEs using the DMA found human-centric digitalisation (r = 0.717) and digital business strategy (r = 0.652) correlated most strongly with overall maturity, while digital readiness (tools owned) correlated weakly. — [Technologies 13:541 (Univ. Luxembourg, ORBilu)](https://orbilu.uni.lu/bitstream/10993/66164/1/technologies-13-00541.pdf)
- OECD's D4SME 2025 survey covered 10 OECD countries (AU, CA, FR, DE, IT, JP, KR, ES, UK, US) and focused on AI (incl. generative AI), sustainability tools, fintech, and digital security. — [OECD, SME digitalisation for competitiveness](https://www.oecd.org/en/publications/sme-digitalisation-for-competitiveness_197e3077-en.html)
- OECD Western Balkans enterprise survey: adoption is concentrated in basic tools — e-invoicing 58%, social media 47%, website 41% — while cloud/ERP reach ~10% of firms. — [OECD Western Balkans Enterprise Survey, component 4](https://www.oecd.org/en/publications/western-balkans-enterprise-survey_a1b14188-en/full-report/component-4.html)
- Blue Prism's Process Assessment Tool scores each process on two question sets — "automation potential" (process as it is today) and "ease of implementation" — and estimates cost and hours saved per process. — [Blue Prism PAT docs](https://bpdocs.blueprism.com/pat/en-us/pat-about.htm)
- RPA discovery questionnaires typically cover triggers, steps, systems, volumes, exceptions, inputs, outputs, and ownership. — [Makeform RPA questionnaire generator](https://www.makeform.ai/tools/ai-rpa-questionnaire-generator)
- Process-automation kickoff templates include: map existing processes, identify pain points/bottlenecks, score opportunities by impact and feasibility, estimate savings. — [Paperform process automation discovery template](https://paperform.co/templates/process-automation-discovery-project-kickoff-form)
- Domain-specific readiness forms (e.g., AP automation) ask processing time per item and hours spent on manual data entry. — [Fomr AP automation readiness assessment](https://fomr.io/templates/accounts-payable-automation-qualifier)

### Inferences
- Because "tools owned" (digital readiness) correlated weakly with maturity while people/strategy correlated strongly, the intake should not over-index on a tool checklist; it must also capture who will own the automations, skill/comfort, and goals.
- The two-axis model (potential × ease) from Blue Prism maps neatly onto a DIY plan: "impact" questions per task + "feasibility" questions per business (tools, skills, budget, data location).
- Reusing DMA-style banding (e.g., 4 maturity levels) lets the system tailor plan complexity (e.g., "Level 1: get data out of paper/email first").

### Gaps
- Could not read the full DMA PDF text (host blocked), so verbatim DMA question wording/answer scales are not captured here. From prior knowledge (unverified in this session), DMA readiness items are checklists of adopted technologies and data-management items ask whether data is collected digitally, stored, integrated, analysed and secured — verify against the PDF.
- No published question lists found for HubSpot, Zapier, Microsoft, or Salesforce SMB "automation readiness" assessments; SBA/SCORE materials not retrieved. Treat as a gap.

## Q2. Top time-consuming manual tasks and pain points reported by small businesses

### Takeaway
Admin (email, scheduling, data entry), getting paid (invoicing/chasing late payments), and responding to inbound leads/calls are the most consistently reported time sinks and revenue leaks. Hard, primary "hours per week" figures are scarcer and less consistent than vendor marketing suggests; a defensible range is roughly 8–16+ owner hours/week on admin depending on definition.

### Cited Findings
- Thryv 2025 Business Index (Australia): 36% of SMB owners say admin work (email, scheduling, data entry) is the most time-consuming part of their week — the single biggest drain. — [Paint & Panel / Thryv](https://www.paintandpanel.com.au/news/news/thryv-launches-better-things-to-do-to-put-time-back-in-tradies-hands)
- Time etc / Censuswide (2023, 251 US entrepreneurs): average 45.5 hours/week worked, 36% spent on small administrative tasks (~16 h/week is a derived figure, not a reported one). — via [Stealth Agents research summary](https://stealthagents.com/research/entrepreneur-time-management-statistics) (secondary)
- A widely-repeated "23 hours/week on admin (SCORE 2025)" figure appears only on a content-marketing site with inconsistent category breakdowns; could not be confirmed — do not use. — [Stealth Agents](https://stealthagents.com/research/smb-administrative-overhead-statistics-2026)
- QuickBooks (Jan 2025, 2,487 US businesses <100 employees): 56% are owed money on unpaid invoices; average affected business is owed $17,500; 47% report invoices overdue >30 days. — [QuickBooks / search summary](https://quickbooks.intuit.com/r/growing-complex-businesses/midsize-payments-research/) (secondary; original report not opened)
- QuickBooks research on firms with 25+ employees: 65% spend an average of 14 hours/week on admin tasks related to collecting payments (lower for 1–15 staff, figure not given). — [QuickBooks midsize payments research](https://quickbooks.intuit.com/r/growing-complex-businesses/midsize-payments-research/)
- QuickBooks UK: ~10% of SMB owners spend 5–10 h/week chasing late invoices, 20% spend 1–4 h, 27% under 1 h. — [QuickBooks UK blog](https://quickbooks.intuit.com/uk/blog/late-payments-impact-on-businesses/)
- QuickBooks/Opinium UK (2019): SMBs waste 56.4M hours/year chasing late payments (~a week per business). — [QuickBooks UK press](https://quickbooks.intuit.com/uk/press/smbs-chase-late-payments/)
- Missed calls: Invoca 2026 benchmark of 70M tracked calls classified 44% as missed; a UK study of 142 small businesses found 47% missed the initial call; the popular "62% unanswered" stat comes from a 2016 study of only 85 businesses. — [JustCall missed-call stats](https://justcall.io/blog/missed-call-statistics.html); [Alliance Virtual Offices](https://www.alliancevirtualoffices.com/virtual-office-blog/shocking-research-finds-small-businesses-miss-almost-half-of-incoming-calls/); [Beside](https://beside.com/blog/missed-calls-cost-small-business)
- CallRail 2025 survey (vendor-cited): only 42% of callers leave a voicemail; 21% immediately call another business. — [SalesAI missed call statistics](https://salesai.com/blog/missed-call-statistics) (secondary)
- Salesforce SMB Trends (6th ed., 3,350 SMB leaders): SMBs automating processes still spend too much time inputting data manually; 56% of (Canadian) SMBs say they aren't ready for AI, 40% of these find AI too complex. — [BetaKit](https://betakit.com/salesforce-report-fifty-six-percent-of-smbs-say-theyre-not-ready-for-ai/)
- Federal Reserve SBCS 2025: 25% of employer firms cite regulatory compliance as a challenge. — via [Stealth Agents summary](https://stealthagents.com/research/small-business-owner-administrative-hours-statistics-2026) (secondary)

### Inferences
- The intake's "pain point" picker should lead with: answering calls/messages & lead follow-up; scheduling/rescheduling; invoicing & chasing payment; data entry/re-typing between tools; bookkeeping/reconciliation; email triage; social/marketing content; review management; reporting; compliance paperwork.
- Since owner-reported hours are noisy, the form should ask for time ranges (buckets) rather than exact numbers, and ask frequency separately so the system computes weekly hours.

### Gaps
- Could not retrieve the Thryv 2025 US AI-adoption PDF task-level time savings, Xero late-payment data, or Intuit's US "hours chasing" figure. No 2024–2026 Zapier SMB-specific report found (latest found: 2021).

## Q3. Highest-ROI automation use cases for SMBs

### Takeaway
Evidence is strongest for (1) appointment reminders (≈25% relative reduction in no-shows), (2) speed-to-lead / missed-call capture (≈40–50% of calls missed; fast responders massively outperform), (3) invoice and payment reminders (majority of SMBs owed money, many invoices >30 days late), and (4) review requests (most consumers will review if asked). AI chat/receptionist and content generation are fast-growing but evidence on ROI is mostly vendor self-report.

### Cited Findings
- Meta-analysis (2016, ~21 studies): people receiving digital appointment notifications were 25% less likely to no-show (RR 0.75; 15% vs 21%); multiple notifications beat single ones. — [PubMed 27798006](https://pubmed.ncbi.nlm.nih.gov/27798006/)
- Clalit RCT: message wording of SMS reminders materially changes no-show rates; simple reminders alone have a small effect vs none. — [PMC7310733](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7310733/)
- Workato study of 114 B2B companies: >99% didn't respond to leads within 5 minutes; only 31% responded by phone. — [Workato lead response study](https://workato.com/the-connector/lead-response-time-study)
- Speed-to-lead's "5 minute" effect traces to 2007 research; InsideSales analysis of 5.7M inbound leads is a more credible source; the advantage collapses within the first ~30 minutes. — [JustCall](https://justcall.io/blog/missed-call-statistics.html); [SalesAI](https://salesai.com/blog/missed-call-statistics) (secondary)
- BrightLocal 2016: 7 in 10 consumers will leave a review if asked; 2023 (secondhand) 65% left reviews in response to a business request; 40% of consumers only consider reviews from the past two weeks. — [BrightLocal 2016](https://www.brightlocal.com/learn/local-consumer-review-survey-2016/); [BrightLocal 2017](https://www.brightlocal.com/learn/local-consumer-review-survey-2017/); [NoCowboys](https://info-zone.nocowboys.co.nz/?p=2002)
- Salesforce SMB Trends: 91% of SMBs with AI say it boosts revenue, 90% say it improves efficiency; common uses are campaign optimization, content generation, chatbots, personalized prospecting emails. — [Small Business Trends](https://smallbiztrends.com/salesforce-ai-data-small-business/) (secondary)
- Thryv: US SMB AI usage rose from 39% (2024) to 55% (2025), reaching 66% in 2026; 70% say they need more training. 2024 AI users expected to save $500–$2,000 and up to 20 hours monthly. — [Thryv/BusinessWire 2025](https://investor.thryv.com/news/news-details/2025/AI-Adoption-Among-Small-Businesses-Surges-41-in-2025-According-to-New-Survey-from-Thryv/); [BusinessWire 2026](https://www.businesswire.com/news/home/20260625243838/en/Despite)
- Zapier 2021 (2,000 US knowledge workers): 88% of SMBs say automation helps them compete with larger firms; 66% call it essential. — [Small Business Trends](https://smallbiztrends.com/2021/05/small-business-automation-pandemic.html); [VentureBeat](https://venturebeat.com/business/zapier-automation-helped-small-businesses-survive-the-pandemic)

### Inferences
- The plan generator should map pain points → a fixed library of "recipes" with default ROI estimates: missed-call text-back / AI receptionist; web-form → CRM → instant reply; booking + reminders (multi-touch); invoice + auto-reminders + card-on-file/pay link; post-job review request; bank/payment → accounting sync; onboarding sequence; weekly KPI report; social scheduling.
- Industries with appointments (salons, clinics, trades) should be routed to reminder/no-show questions (ask current no-show rate and average ticket value to compute $ impact).

### Gaps
- No rigorous SMB-specific ROI study comparing these use cases head-to-head; ranking is an inference from separate evidence bases. Bookkeeping-sync and social-posting ROI evidence not found.

## Q4. How to capture a process inventory so tasks can be scored for automation priority

### Takeaway
RPA literature converges on scoring criteria: rule-based (low judgment), standardized/stable, high volume/frequency, structured digital inputs, and error/compliance cost. Capture each task as a repeatable row (task, frequency, time per occurrence, who, tools, trigger, inputs/outputs, exceptions, error impact) and compute Priority = weekly hours × rule-based score × digital-input score × (1 + error cost) ÷ implementation effort.

### Cited Findings
- Literature review: process-selection criteria usually require strict definition/structure with little subjective judgment; frequency matters mainly when the process is also standardized. — [arXiv 2007.10900](https://arxiv.org/pdf/2007.10900v1)
- Practitioner scoring scale: rule-based = 5, mixed = 3, judgment-heavy = 1. — [Morgan Franklin](https://www.morganfranklin.com/?p=11502)
- Daily/weekly tasks are strong candidates; rare one-offs rarely justify effort. — [Formtek](https://formtek.com/blog/identifying-automation-candidates-not-every-process-deserves-a-bot/)
- 2026 healthcare RPA framework: recurring criteria are volume, rule-based standardization, structured digital data input, and process stability; candidates ranked with AHP + TOPSIS multi-criteria methods. — [arXiv 2609.09137](https://arxiv.org/pdf/2609.09137)
- No settled standard exists for this assessment; a 2024 paper proposes expert-validated criteria. — [IJ-AI](https://ijai.iaescore.com/index.php/IJAI/article/download/25402/14232)
- Blue Prism PAT splits "automation potential" from "ease of implementation" and outputs hours/cost saved. — [Blue Prism PAT](https://bpdocs.blueprism.com/pat/en-us/pat-about.htm)

### Inferences (proposed scoring model)
- Weekly hours = frequency_per_week × minutes_per_occurrence ÷ 60 (use bucket midpoints).
- Rule-based score 1/3/5 from "How much judgment does this need?" (Always same steps / Mostly same with some exceptions / Different every time).
- Digital-input score: 1 paper/phone call, 3 email/PDF/text, 5 form/app/spreadsheet data.
- Error-cost multiplier from "What happens if it's late or wrong?" (Minor annoyance / Lost time / Lost money or customer / Compliance/legal risk).
- Effort/feasibility: penalize if tools lack integrations (check tool picker against a connector catalog), if user tech comfort is low, or if data is regulated.
- Keep the inventory to a short "top 3–5 tasks" list for DIY users; full RPA-style discovery is too long for a self-serve form.

### Gaps
- No empirical validation found that a multiplicative SMB score predicts realized savings; weights are judgment calls to be tuned with outcome data.

## Q5. Readiness and constraint fields

### Takeaway
Barriers cited by OECD and vendor surveys are skills/complexity, time, cost/maintenance, data readiness, and legal uncertainty — so the form must capture tech comfort, weekly time available, budget, data location, compliance regime, and DIY vs done-for-you preference to keep the plan feasible.

### Cited Findings
- OECD G7 paper: 11.9% of small firms (10–49 employees) use AI vs 40% of large firms; >50% of SMEs cite skill shortages; <30% of AI-using SMEs offer AI training (summary via third party). — [OECD, Empowering SMEs in the age of AI](https://www.oecd.org/en/publications/empowering-smes-in-the-age-of-ai_bf5a9816-en.html); [GetEasy summary](https://geteasy.ai/en/reports/oecd-ai-adoption-smes-report) (secondary)
- 2026 D4SME (≈2,000 SMEs, 12 countries, non-representative): time constraints, maintenance costs and skills gaps hinder implementation; persistent barriers include data readiness, skills, legal uncertainty, integration costs. — [OECD SME digitalisation](https://www.oecd.org/en/publications/sme-digitalisation-for-competitiveness_197e3077-en.html); [GetEasy summary](https://geteasy.ai/en/reports/oecd-ai-adoption-smes-report) (secondary)
- 40% of not-AI-ready Canadian SMBs find AI too complex. — [BetaKit](https://betakit.com/salesforce-report-fifty-six-percent-of-smbs-say-theyre-not-ready-for-ai/)
- 70% of US SMB owners say they need more AI training (Thryv 2026). — [BusinessWire](https://www.businesswire.com/news/home/20260625243838/en/Despite)
- Basic tools (e-invoicing, social, website) are far more common than cloud/ERP (~10%) in less mature markets. — [OECD Western Balkans](https://www.oecd.org/en/publications/western-balkans-enterprise-survey_a1b14188-en/full-report/component-4.html)

### Inferences
- Tech comfort and "hours/week you can spend setting this up" should gate recipe complexity (no-code native features first, then Zapier/Make, then custom).
- Compliance flags (HIPAA, PCI, GDPR/UK GDPR, CCPA, SOC2 clients, TCPA/10DLC for SMS) must suppress or modify recipes (e.g., no PHI in generic Zapier; SMS requires opt-in).

### Gaps
- No source found quantifying how mobile-only vs desktop usage changes SMB automation success; included as a field by inference.

## Q6. Form UX best practices for long business questionnaires

### Takeaway
Use a multi-step wizard with progress indicator, conditional (branching) questions, explicit required markers, back/edit, and chunks of a few questions; gather firmographics first to branch by industry. Hard primary data (Baymard/NN/g) on multi-step completion lift was not retrieved; vendor claims of 20–40% lift are unverified.

### Cited Findings
- NN/g: mark required fields explicitly (asterisk), even when most are required; marking optional fields also reduces cognitive load; avoid low-contrast asterisks. — [NN/g, Marking Required Fields](https://nngroup.com/articles/required-fields); [NN/g video](https://www.nngroup.com/videos/required-fields-forms/)
- Vendor claims: multi-step forms outperform single-page forms by 20–40% in completion (unverified, illustrative examples). — [Atticus Li glossary](https://atticusli.com/behavioral-science-glossary/progressive-disclosure/)
- Progress indicators and back/edit options reduce anxiety and abandonment; conditional fields shown only when relevant. — [OrbitForms](https://orbitforms.ai/blog/form-abandonment-prevention-strategies); [OrbitForms progressive forms](https://orbitforms.ai/blog/progressive-web-forms)
- DMA itself places firmographics (sector, size) first, enabling segmentation. — [EDIH DMA PDF](https://european-digital-innovation-hubs.ec.europa.eu/system/files/2024-02/DMA%20Questionnaire%20for%20SMEs_EDIH_network_EN_v2.1.pdf)

### Inferences
- Target ≤10–12 minutes; require only what the plan engine needs (industry, team size, top pains, tools, comfort, budget); make deep task inventory optional "improve my plan" step.
- Logo-grid tool pickers with search and "Other" free text reduce recall burden and give machine-readable tool IDs for integration checks.
- Smart defaults by industry (e.g., pre-check "Square" and "Google Business Profile" for salons) — inference, unverified.
- Save-and-resume; show a teaser result (e.g., estimated hours recoverable) before the optional deep section to reduce drop-off.

### Gaps
- Could not retrieve Baymard or NN/g primary research on multi-step/wizard completion rates or on optimal question count for B2B questionnaires.

---

### Draft form spec (synthesized from above; "Why" ties to plan logic)

**Section 1 – Business profile (required, ~2 min)**
1. Industry — dropdown (Home services/trades; Health & wellness clinic; Beauty/salon/spa; Fitness; Professional services (legal/accounting/consulting); Agency/creative; Retail (physical); E-commerce; Restaurant/food; Real estate; Construction; Education/coaching; Nonprofit; Other [text]). Why: branches later questions, picks recipe library and compliance defaults.
2. Team size incl. owner — dropdown (Just me; 2–5; 6–10; 11–25; 26–50; 51+). Why: DMA-style segmentation; solo = owner time is the bottleneck.
3. Roles on team — multi-select (Owner/manager; Front desk/admin; Sales; Field techs/service staff; Bookkeeper (in-house); Outsourced accountant/VA; Marketing). Why: assigns automation owners and handoffs.
4. How customers buy — multi-select (Book appointments; Request quotes/estimates; Buy online; Walk-in; Subscriptions/memberships; Projects/retainers). Why: determines pipeline vs booking vs e-com recipes.
5. Monthly new customers/inquiries — dropdown (<10; 10–50; 51–200; 201–1,000; 1,000+). Why: volume driver for ROI.
6. Average transaction/job value — dropdown ranges. Why: converts missed leads/no-shows to $.

**Section 2 – Goals & pain points (required)**
7. Top goals (pick up to 3) — multi-select (Save my time; Respond to leads faster; Fewer no-shows; Get paid faster; Fewer errors; More reviews/reputation; Better reporting/visibility; Scale without hiring; Better customer experience).
8. Most painful tasks (pick up to 5) — multi-select checklist: Answering calls/missed calls; Replying to inquiries/DMs; Scheduling & rescheduling; Appointment reminders; Quotes/estimates; Invoicing; Chasing late payments; Bookkeeping/reconciliation; Data entry/copying between apps; Email inbox triage; Client onboarding paperwork; Social media posting; Email marketing/newsletters; Asking for reviews; Inventory/ordering; Payroll/timesheets; Reporting; Compliance documents. Why: grounded in admin/payment/call findings (Q2); seeds the task inventory.
9. Owner admin hours/week — scale buckets (0–5; 6–10; 11–15; 16–20; 20+). Why: baseline for "hours saved" estimate.
10. Industry-branched metrics (optional): % calls missed (Don't know/<10%/10–25/25–50/>50); no-show rate; % invoices paid late; avg days to get paid.

**Section 3 – Task deep-dive (repeat for top 3 tasks from Q8; optional but recommended)**
11. Frequency — dropdown (Many times a day; Daily; A few times/week; Weekly; Monthly; Rarely).
12. Time each time — dropdown (<5 min; 5–15; 15–30; 30–60; 1–2 h; 2 h+).
13. Who does it — single-select from roles in Q3.
14. What starts it (trigger) — dropdown (Customer call; Form/booking submitted; Email arrives; Payment/invoice event; Date/time; Job completed; Manual decision).
15. Where info comes from — multi-select (Phone/voice; Paper; Email/PDF; Text/DM; Web form; Spreadsheet; Software app) → digital-input score.
16. Where info goes — multi-select tool list from Section 4.
17. Judgment needed — scale (Same steps every time / Mostly same, some exceptions / Different every time) → rule-based score 5/3/1.
18. Cost if late or wrong — dropdown (Minor; Wasted time; Lost money/customer; Legal/compliance risk) → error multiplier.
19. Describe steps (optional free text).

**Section 4 – Tools & data (required core)**
20. Tools in use — logo-grid multi-select by category with search + Other: Email/calendar (Google Workspace, Microsoft 365); Accounting (QuickBooks, Xero, FreshBooks, Wave); Payments/POS (Stripe, Square, PayPal, Clover); Booking (Calendly, Acuity, Square Appointments, Jobber, Housecall Pro, Mindbody, Vagaro); CRM (HubSpot, GoHighLevel, Salesforce, Pipedrive, Zoho); Website/forms (WordPress, Wix, Squarespace, Shopify, Google Forms, Typeform); Messaging/phone (business cell, RingCentral, OpenPhone/Quo, Google Voice); Marketing (Mailchimp, Meta, Google Business Profile); Files (Drive, Dropbox, OneDrive); Automation already (Zapier, Make, n8n, none). Why: integration feasibility and native-feature-first recipes.
21. Where customer list lives — single-select (Paper/notebook; Phone contacts; Spreadsheet; Email inbox; Software/CRM; Several places). Why: data-readiness gate (OECD barrier).
22. Already automated anything? — Yes/No + free text.

**Section 5 – Readiness & constraints (required)**
23. Tech comfort — 1–5 scale with anchors (1 = "I avoid new apps" … 5 = "I've built Zaps/workflows").
24. Time available to set up — dropdown (<1 h/week; 1–3; 3–5; 5+).
25. Monthly budget for new tools — dropdown ($0 / under $50 / $50–150 / $150–500 / $500+).
26. Preference — single-select (Do it myself with step-by-step guide; Mix; Done-for-you). Why: OECD/Thryv skills gap.
27. Primary device for running business — single-select (Mostly phone; Mostly computer; Both).
28. Compliance/data sensitivity — multi-select (Health info/HIPAA; Card payments/PCI; EU/UK customers (GDPR); California customers (CCPA); Legal/financial client confidentiality; Text-message marketing (TCPA/10DLC); None/Not sure). Why: suppress/modify recipes.
29. Internet/hardware constraints (optional) — multi-select (Unreliable internet at job sites; Shared devices; No business phone line).
30. Anything we should know? — free text.

Branching examples: appointment-based industries → no-show + reminder questions; quote-based → estimate follow-up questions; e-com → cart/order/inventory questions; Health → HIPAA preselected warning; Solo → skip roles/handoff questions.
