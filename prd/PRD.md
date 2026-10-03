# Kopi Koma Partner Portal: Product Requirements Document

Prototype (franchisor dashboard): https://kopikomapartnerportal.vercel.app
Prototype (candidate franchisee portal): https://kopikomapartnerportal.vercel.app/mitra
Demo password for all staff accounts: demo123 (accounts are listed on the login page)

## 1. Summary

Kopi Koma Partner Portal is a web platform that digitalizes the partnership process between a coffee franchisor and its candidate franchisees, from the first application until the partnership is approved by both parties. It consists of two connected applications: an internal dashboard for the franchisor team (Sales, Reviewer, Manager, Super Admin) and a Partner Portal for candidate franchisees. Every application moves through one shared 8-stage pipeline with a clear owner and deadline per stage. Reminders are sent automatically when a deadline is missed, and every action is recorded in an audit trail.

The goal is simple: no lead is forgotten, every candidate knows the status of their application, and management can see at any time whether the expansion target is on track.

## 2. Background and Assumptions

### 2.1 Client assumptions

The client in this case is fictional. I named it Kopi Koma (fictitious name) and made the following assumptions:

- Kopi Koma is a local "kopi kekinian" (grab-and-go coffee) brand with around 80 outlets, mostly in Greater Jakarta, Bandung, and Central Java.
- It offers two franchise packages:

| Package | Investment | Royalty | Estimated payback |
|---|---|---|---|
| Gerobak (coffee cart) | Rp 45,000,000 | None | 6 to 9 months |
| Cafe | Rp 450,000,000 | 5% of monthly revenue | 18 to 24 months |

- Why the Gerobak package has no royalty: Gerobak partners are required to buy raw materials (coffee, milk, syrup, cups) from Kopi Koma, so the franchisor earns from the supply margin instead of a percentage of sales. This keeps the entry package simple and affordable for first-time business owners, and avoids the cost of auditing revenue reports from many small carts. The Cafe package has a 5% royalty because its revenue is larger and it uses the brand more intensively (full store, menu, and interior standards).
- The partnership team consists of 1 Manager, 4 Sales (2 senior, 2 junior, each covering a region), and 2 Reviewers who run the eligibility assessment. A Super Admin manages the system.
- The expansion target is 120 new outlets per year (72 Gerobak and 48 Cafe). This is a stretch target: it is more aggressive than what comparable brands have publicly shown, and it is used to drive team targets and pipeline planning.
- Revenue in this document means the deal value of approved partnership packages after discount. Royalty is not counted because it occurs after the outlet opens, which is outside the scope of this product.

### 2.2 Industry context

Franchising is the main expansion channel for Indonesian F&B brands. According to the Ministry of Trade, as of February 2025 there were 311 franchisors with a Franchise Registration Certificate (STPW), 157 domestic and 154 foreign, and the culinary (F&B) sector accounted for 47.77% of them [1][2]. Note that this is a share of registered franchisors, not of outlets or revenue. In the coffee category, research by TOFFIN and MIX MarComm (SWA Media Group) found that chain coffee shops in major Indonesian cities grew from around 1,000 outlets in 2016 to more than 2,950 outlets in August 2019 [3][4]. The argument here is not that the coffee market is booming, but that brands in this category grow mainly by opening outlets through franchise partners. This makes the partnership process a core business process, not an administrative side task.

### 2.3 Pain points (assumed)

| # | Pain point | Who feels it | Impact |
|---|---|---|---|
| 1 | Leads are scattered and not centralized. They come from many channels (exhibitions, referrals, Instagram, website, walk-ins) and end up in each sales' WhatsApp chats, personal notes, and separate spreadsheets. There is no single list of all candidates, their owner, and their status. | Sales, Manager | Leads are followed up late or forgotten, two sales may contact the same candidate, and lead data is lost when a sales leaves the company. |
| 2 | Candidates do not know where their application stands and must keep asking their sales contact. | Candidate franchisee, Sales | Poor candidate experience and time spent answering status questions. Serious candidates may move to a competitor brand. |
| 3 | Quotations, discounts, and change requests are negotiated by chat. There is no single version that both parties agree on. | Sales, Manager, Candidate | Disputes about what was agreed, and approvals that cannot be traced. |
| 4 | There is no deadline per stage and no visibility of bottlenecks. | Manager | Applications stay stuck for weeks without anyone noticing. |
| 5 | Candidate screening and location decisions rely on individual judgment. | Reviewer, Manager | Inconsistent decisions and outlets opened in weak locations. |
| 6 | Targets are only checked at the end of the month in a spreadsheet. | Manager, Sales | The team learns too late that the target will be missed. |
| 7 | Compliance steps (delivering the franchise prospectus, personal data consent) are not recorded. | Franchisor | Legal risk under the franchise regulation (PP No. 35/2024) [5] and the Personal Data Protection Law (UU PDP No. 27/2022) [6]. |

## 3. Goals and Success Metrics

The metrics below are proposed targets for the first year. Some are derived from the process design and the business target, and the rest are initial assumptions that should be validated with the client during the pilot and adjusted once real baseline data exists.

| Goal | Metric | Proposed target | Basis |
|---|---|---|---|
| No lead is forgotten | Leads assigned to a sales within 1 day | 100% | Derived from the 1-day deadline of the New lead stage |
| Faster process | Average time from new lead to final decision | 26 days or less | Derived: sum of all stage deadlines (1 + 4 + 5 + 4 + 3 + 7 + 2) |
| Process discipline | Stages completed within their deadline | 85% or more | Assumption: a starting target that leaves room for exceptions such as candidates who are hard to reach |
| Better conversion | Lead to approved partnership | 12% or more | Derived from the default funnel conversion rates in Section 6.3 |
| Expansion target | New approved outlets per year | 120 (72 Gerobak, 48 Cafe) | Business target (stretch), from the per-sales targets in Section 6.3 |
| Revenue | Approved deal value per year | around Rp 24.8 billion | Derived: 6 Gerobak x Rp 45 million + 4 Cafe x Rp 450 million = Rp 2.07 billion per month |
| Candidate self-service | Quotation responses submitted through the Partner Portal | 70% or more | Assumption: the target for portal adoption, measured during the pilot |

## 4. Users and Roles

| Role | Main needs | Menu in the dashboard | Can process |
|---|---|---|---|
| Candidate franchisee | Register easily, know the status of the application, respond to the quotation without many calls | Partner Portal (separate application) | Registration, quotation response |
| Sales | One list of their own candidates and what to do next, and progress toward their target | Pipeline (own leads only), Tasks, Target | Add lead, business presentation, location survey, quotation, negotiation |
| Reviewer | A clear queue of candidates to assess, with the data needed to decide | Pipeline, Tasks | Eligibility assessment |
| Manager | Visibility of the whole pipeline, overdue items, and team performance. Decides final approval. | Pipeline, Tasks, Target, Sales Performance | Lead assignment (exceptions), final approval |
| Super Admin | Full access to support the team | Pipeline, Tasks, Target, Sales Performance | All stages (recorded under their name) |

### 4.1 Role-Based Access Control (RBAC)

Access is granted by role, not per person. Each user has exactly one role, and the system checks the role on every action. Data access follows the principle of least privilege: each role only sees and changes what it needs for its job.

| Permission | Super Admin | Manager | Sales | Reviewer | Candidate |
|---|---|---|---|---|---|
| View pipeline | All | All | Own leads only | All | Own application only (application number + email or phone) |
| Add lead | Yes | No | Yes | No | Self-registration in portal |
| Assign sales to an unassigned lead | Yes | Yes | No | No | No |
| Presentation, location survey, quotation, negotiation | Yes | No | Own leads only | No | Respond to quotation |
| Eligibility assessment | Yes | No | No | Yes | No |
| Final approval (approve or reject) | Yes | Yes | No | No | No |
| View candidate documents (ID, tax number, bank statement) | Yes | Yes | Own leads only | Yes | Own documents |
| View overdue indicators | Yes | Yes | No | No | No |
| Target vs Achievement | Team | Team | Own | No | No |
| Sales Performance | Yes | Yes | No | No | No |
| View audit trail of an application | Yes | Yes | Own leads only | Yes | No |

Every action taken by a Super Admin on behalf of another role is recorded under the Super Admin's name in the audit trail.

### 4.2 Sales regions

Sales regions in the prototype: Rendi covers Greater Tangerang; Putri covers Jakarta, Bogor, Depok, Bekasi, and Cikarang; Agus covers Greater Bandung; Wulan covers Central Java.

## 5. End-to-End Process

The process is designed from the franchisor's point of view and has 8 stages. Each stage has one person in charge (PIC) and a deadline.

### 5.1 Flowchart

![Flowchart](flowchart.png)

### 5.2 Stages and deadlines

| # | Stage | PIC | Deadline |
|---|---|---|---|
| 1 | New lead | System (automatic) or Manager | 1 day |
| 2 | Business presentation and prospectus delivery | Sales | 4 days |
| 3 | Location survey | Sales | 5 days |
| 4 | Eligibility assessment: interview, background check, financial verification, KYC, commitment | Reviewer | 4 days |
| 5 | Quotation | Sales | 3 days |
| 6 | Negotiation: the candidate responds (agree, request changes, or withdraw) | Sales | 7 days |
| 7 | Final approval: approve or reject | Manager | 2 days |
| End | Approved, Rejected, or Withdrawn | | |

### 5.3 Input, Process, Output (IPO) per stage

| Stage | Input | Process | Output |
|---|---|---|---|
| 1. New lead | Candidate data: name, phone, email, city, package, available capital, source of funds, planned location, personal data consent | Duplicate check, region matching, sales capacity check, AI fit score | Application number, assigned sales (or Manager queue), notification to sales, confirmation and tracker access for the candidate |
| 2. Business presentation | Presentation date and mode, prospectus delivery confirmation, notes | Sales presents the business model and sends the prospectus | Prospectus delivery date recorded, application moves to Location survey |
| 3. Location survey | Location address and type, survey rating, foot traffic, photos, AI location score | Sales assesses the location (discusses with Manager first if the score is below 60) | Feasible: moves to Eligibility assessment. Not feasible: rejected with reason |
| 4. Eligibility assessment | Interview result, background check, bank statement, ID and tax number (KYC), commitment | Reviewer evaluates each item on a checklist | Eligible: moves to Quotation. Not eligible: rejected with reason |
| 5. Quotation | Package, discount, payment terms, target opening date, result of discussion with Manager (for revisions) | System creates quotation version N and emails it with a portal link | Quotation version N sent and recorded |
| 6. Negotiation | Candidate response: agree (with confirmation), request changes (type and details, or new address), or withdraw | System routes the application based on the response | Agree: approval 1 of 2, moves to Final approval. Changes: back to Quotation or Location survey. Withdraw: closed |
| 7. Final approval | Complete application history and the agreed quotation | Manager approves or rejects | Approved: approval 2 of 2, revenue counted, next step is the franchise agreement. Rejected: closed with reason. The candidate is notified in both cases |

### 5.4 Key business rules

- **Lead assignment.** A lead added by a sales goes directly to the business presentation stage under that sales. A lead from the Partner Portal is assigned automatically to the sales who covers the candidate's city. It goes to the Manager's queue instead if the city is outside all regions, if the phone number or email matches an active lead (possible duplicate), or if the regional sales has reached the active lead limit (15 for senior, 10 for junior).
- **Prospectus.** The presentation stage requires the sales to confirm that the franchise prospectus has been sent. PP No. 35/2024 on Franchising, which replaced PP No. 42/2007, requires the franchisor to deliver the prospectus to the candidate at least 14 calendar days before the franchise agreement is signed [5]. Recording the delivery date in the system makes this easy to prove.
- **Location decision stays at the survey stage.** If the AI location score is below 60, the survey tab shows an SOP reminder to discuss with the Manager before declaring the location feasible. Final approval is a yes or no gate without a location revision option, so location issues are not discovered at the last step.
- **Change requests.** If the candidate requests changes during negotiation, the application returns to the Quotation stage (marked as Revision). The sales discusses the change with the Manager outside the system and must fill in "Result of discussion with Manager" when sending the next quotation version.
- **Location change.** If the candidate asks to change location, the new address is required. The application returns to the Location survey stage. If the new location is feasible, it goes directly to a revised quotation without repeating the eligibility assessment. If not feasible, the application is rejected.
- **Two-party approval.** Approval 1 of 2 is the candidate agreeing to the quotation (in the portal, or recorded by sales if the answer came by phone or in person). Approval 2 of 2 is the Manager's final approval. In the portal, the candidate must tick a confirmation that they have read and agree to quotation version N, and this is recorded in the audit trail.
- **Automatic reminders.** When a stage passes its deadline, the system notifies the PIC and the Manager through the dashboard and email. There is no manual reminder button, so follow-up does not depend on someone remembering to chase.

## 6. Features and Rationale

### 6.1 Franchisor dashboard

| Feature | What it does | Why it was chosen |
|---|---|---|
| Pipeline (kanban) | One board with 7 active stages. Each card shows package, AI score, current PIC, and days in stage. Overdue indicators are visible to Manager and Super Admin only. Completed applications are in a separate Completed table with filters. | Solves pain points 1 and 4. The whole process is visible in one place, and the board fits on a laptop screen without scrolling. |
| Automatic lead assignment | Assigns portal leads by region and flags exceptions (outside region, possible duplicate, sales at capacity) for the Manager. | Leads are followed up within 1 day, and two sales do not contact the same candidate. |
| Application detail | 7 tabs: Summary, Presentation, Location survey, Assessment, Quotation, Negotiation, History. Each stage has a structured form. | Every stage produces consistent data that the next stage can use. |
| Approval status | A 7-step timeline per application showing who is responsible and how long it has been waiting. | Anyone can answer "where is this application now?" in one click. |
| Tasks | A list of actions waiting for the logged-in user. Managers can also filter by team. | Each person knows what to do today without searching the board. |
| Quotation with versions | Quotations are versioned. Revisions must include the result of the discussion with the Manager. | Solves pain point 3. There is always one agreed version, and discounts are traceable. |
| AI fit score | A score from 0 to 100 (candidate profile 40%, location 60%) with plus and minus reasons. | Solves pain point 5. It makes screening more consistent. It is a decision aid, not an automatic rejection. |
| Target vs Achievement | Monthly, quarterly, semester, or yearly view of Gerobak, Cafe, and revenue against target, including the target to date (MTD, QTD, HTD, YTD), the remaining gap, and pipeline opportunities. A funnel is calculated backwards from conversion rates that can be adjusted. | Solves pain point 6. The team can see during the period whether it is on pace. |
| Sales Performance | One table per sales with Gerobak, Cafe, and revenue against target, and a status based on the weakest metric. | The Manager can see who needs help early. |
| Audit trail | Every action, including document access and actions by the candidate in the portal, is recorded with time and actor. | Accountability and compliance with UU PDP. |

### 6.2 Partner Portal (candidate franchisee)

| Feature | What it does | Why it was chosen |
|---|---|---|
| Registration form | Data, package choice, available capital, planned location, and required personal data consent. The lead enters the same pipeline as a self-registered lead. | A second lead channel beside sales input, connected to Instagram and the website. |
| Status tracker | The candidate checks a 7-step status with the application number and email or phone. The assigned sales and their contact are shown. | Solves pain point 2 and reduces "how is my application?" messages. |
| Quotation response | The candidate can agree (with confirmation), request changes (including a location change), or withdraw. | Shortens negotiation and gives a written record of approval 1 of 2. |

Feature selection principle: I focused on the path from application to two-party approval, which is the scope of the case. Features after approval (agreement signing, outlet opening, royalty) are placed in the roadmap.

### 6.3 Target design

Targets are set per sales per month as whole numbers and differ by seniority:

| Level | Sales | Gerobak per month | Cafe per month |
|---|---|---|---|
| Senior | Rendi, Putri | 2 | 1 |
| Junior | Agus, Wulan | 1 | 1 |
| Team total | | 6 | 4 |

This totals 10 outlets per month, or 120 outlets per year (72 Gerobak and 48 Cafe). Revenue is around Rp 2.07 billion per month. Targets for other periods are the monthly target multiplied by the number of months. During days 1 to 9 of a period, status is shown as "Early period" instead of "Critical" to avoid false alarms. From day 10, all metrics are evaluated normally.

With the default conversion assumptions (lead to presentation 60%, presentation to feasible location 55%, location to passed assessment 75%, assessment to quotation 90%, quotation to approved 55%), the team needs around 92 new leads per month to reach 10 approved outlets.

## 7. Prioritization (MoSCoW)

| Priority | Features |
|---|---|
| Must have (MVP) | Lead input by sales and portal registration; automatic lead assignment; 8-stage pipeline with deadlines and automatic reminders; stage forms; quotation with versions; two-party approval; Partner Portal tracker and quotation response; role-based access; audit trail; personal data consent |
| Should have (MVP if time allows) | AI fit score; Target vs Achievement; Sales Performance; Completed table with filters; mobile-friendly layout |
| Could have (next phase) | Electronic signature for the franchise agreement through Privy; WhatsApp notifications; real map data for the location score; document upload with automatic KYC verification; report export |
| Won't have (this phase) | Royalty tracking and outlet operations after opening; payment gateway for the partnership fee; training and onboarding modules; multi-brand support |

## 8. Non-Functional Requirements

- **Privacy and security (UU PDP No. 27/2022) [6].** Personal data consent is required before a lead is saved. Access follows roles (for example, a sales only sees their own leads). Access to documents such as ID cards and bank statements is recorded. Personal data has a defined retention period and is deleted or anonymized for rejected candidates.
- **Auditability.** Every status change, quotation version, approval, and document access is recorded with actor and time and cannot be edited.
- **Responsible AI.** The AI score is explainable (it shows reasons), is never used to reject a candidate automatically, and is reviewed periodically against actual outlet performance to detect bias, for example against certain regions.
- **Mobile friendly.** The Partner Portal is designed for mobile first because candidates usually come from Instagram or email links. The dashboard is optimized for laptops but still usable on a phone.
- **Reliability and performance.** Target availability is 99.5% during working hours. Pages load in under 3 seconds on a 4G connection.
- **Language.** The interface uses Bahasa Indonesia, keeping common business terms such as Sales, Lead, Quotation, and Pipeline.

## 9. Prototype Limitations

The prototype is a single HTML file deployed on Vercel. To make it testable without a backend, it has the following limitations:

- Data is stored in the browser (localStorage). The dashboard and Partner Portal are connected only within the same browser. A "Reset demo data" button in the account menu restores the sample data.
- The login page lists demo accounts for each role so reviewers can switch roles quickly. In production, login would use company accounts (SSO) and this list would not exist.
- Sample data (lead age, sales history, approved deals) is calculated relative to today's date, so the target pages always show a realistic current period.
- The AI fit score is simulated with rule-based weighting and simulated map data (crowd points, competitors, distance to the nearest outlet). In production it would use real location data and be calibrated with historical outlet performance.
- Email notifications are simulated as dashboard notifications.
- After both parties agree, the prototype only shows the next step: the franchise agreement is sent through Privy for a certified electronic signature. The integration itself is not built.
- The registration form has a "Fill sample data" button for faster testing.

## 10. Roadmap

| Phase | Timeline | Scope |
|---|---|---|
| 1. MVP | Months 0 to 3 | Backend and database, company login, the Must have features, email notifications, pilot with one region |
| 2. Integration | Months 3 to 6 | All regions, Privy e-signature for the franchise agreement, WhatsApp Business notifications, document upload with KYC verification, real map data for the location score |
| 3. Intelligence and after-approval | Months 6 to 12 | Fit score calibrated with actual outlet performance, outlet opening checklist and training schedule, royalty reporting, management reports |

## 11. Risks and Open Questions

| Risk or question | Mitigation |
|---|---|
| Sales keep using WhatsApp and do not update the system | Reminders and targets depend on system data, so updating the system is the easiest way for sales to look good. Training during the pilot. |
| The stretch target is not realistic | Track monthly against the target to date and review targets after the first quarter. |
| The AI score creates bias or overconfidence | Show reasons, keep humans deciding, and review score against outcomes regularly. |
| Candidates prefer to respond by phone | Sales can record the candidate's response in the Negotiation tab, so both paths are supported. |
| Open question: should the Manager also approve quotations with large discounts before they are sent? | To be confirmed with the client. Currently handled as a discussion outside the system. |

## 12. Use of AI During This Project

I used Claude (Anthropic) as an assistant throughout the project. The AI helped me move faster, but the product decisions were mine, and I checked its output before using it.

| Activity | How AI was used | My role |
|---|---|---|
| Understanding the case | Discussed the case, explored possible client profiles and pain points | Chose the client profile (local coffee brand, two packages) and decided the scope: application until two-party approval |
| Process design | Proposed stage options and rules (assignment, revisions, location change) | Simplified the flow, moved the location decision to the survey stage, removed manual reminders, and decided who approves what |
| Prototyping | Built the clickable HTML prototype through Claude Code, iterating on many rounds of my feedback | Reviewed each version, asked for changes in layout, wording, and terminology, and rejected options that made the interface cluttered |
| Testing | Ran automated browser tests (Playwright) on every role, the full end-to-end flow, and mobile screen sizes | Defined what "correct" looks like and checked the results |
| Research | Searched for industry data on franchising and coffee shop growth | Asked the AI to verify sources. One statistic turned out to be older data (2016 to 2019) that had been cited as recent, and the franchise regulation I first used (PP No. 42/2007) had been replaced by PP No. 35/2024, so I corrected both |
| Targets | Proposed target schemes and benchmarks | Chose whole-number monthly targets per sales by seniority and labeled the yearly number as a stretch target |
| Writing | Drafted this document based on the prototype | Reviewed and edited the content |

What I learned: AI is very fast at producing options and working code, but it can sound confident about data that is not accurate. Asking for sources and checking them was necessary.

Screenshots of the AI conversation are attached in the Appendix.

## References

1. ANTARA News, "Kemendag sebut sektor kuliner masih mendominasi bisnis waralaba". https://www.antaranews.com/berita/4774885/kemendag-sebut-sektor-kuliner-masih-mendominasi-bisnis-waralaba
2. Tempo, "Mendag: Waralaba Serap 97 Ribu Tenaga Kerja dengan Omzet Rp 143 Triliun". https://www.tempo.co/ekonomi/mendag-waralaba-serap-97-ribu-tenaga-kerja-dengan-omzet-rp-143-triliun-1218788
3. Marketeers, "Toffin: Nilai Pasar Kedai Kopi di Indonesia Capai Rp 4,8 Triliun". https://www.marketeers.com/toffin-nilai-pasar-kedai-kopi-di-indonesia-capai-rp-4-8-triliun/
4. Warta Ekonomi, "Bisnis Kedai Kopi di Indonesia Cerah, Jumlahnya Melesat 3X Lipat". https://wartaekonomi.co.id/read262062/bisnis-kedai-kopi-di-indonesia-cerah-jumlahnya-melesat-3x-lipat
5. JDIH BPK, Peraturan Pemerintah No. 35 Tahun 2024 tentang Waralaba. https://peraturan.bpk.go.id/Details/297489/pp-no-35-tahun-2024
6. JDIH BPK, Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi. https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022

## Appendix: AI Conversation Screenshots

[Attach screenshots or a PDF of the AI conversation here.]
