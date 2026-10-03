# Kopi Koma Partner Portal: Product Requirements Document

## Table of Contents

[[TOC]]

[[PAGEBREAK]]

## Executive Summary

**Kopi Koma Partner Portal** is a web application that digitalizes and centralizes the partnership process between Kopi Koma (fictitious name), a local coffee franchisor, and its candidate franchisees, from the first application until the partnership is approved by both parties. The product consists of two connected applications:

- **Franchisor Dashboard**: used by the internal team (Sales, Reviewer, Manager, Super Admin) to capture and assign leads, process each stage of the 8-stage pipeline, give final approval, and monitor sales targets.
- **Partner Portal**: used by candidate franchisees to register, track the status of their application, and respond to quotations.

This product addresses three core pain points: leads scattered across WhatsApp chats and personal spreadsheets with no central record; applications that get stuck because no stage has a clear owner or deadline; and quotations and approvals negotiated by chat with no traceable agreement.

Activities after both parties approve, such as signing the franchise agreement, opening the outlet, and collecting royalty, are out of scope. Signing the agreement through Privy (electronic signature) is referenced only as the next step after approval.

**Prototype (Franchisor Dashboard):** https://kopikomapartnerportal.vercel.app

**Prototype (Partner Portal):** https://kopikomapartnerportal.vercel.app/mitra

**Demo password:** demo123 (all staff accounts are listed on the login page)

## Assumptions

### Client

| Item | Assumption |
|---|---|
| Brand | Kopi Koma (fictitious name), a local "kopi kekinian" (grab-and-go coffee) brand with around 80 outlets in Greater Jakarta, Bandung, and Central Java |
| Packages | **Gerobak** (coffee cart): Rp 45,000,000, no royalty, payback 6 to 9 months. **Cafe**: Rp 450,000,000, royalty 5% of monthly revenue, payback 18 to 24 months |
| Why Gerobak has no royalty | Gerobak partners must buy raw materials (coffee, milk, syrup, cups) from Kopi Koma, so the franchisor earns from the supply margin. This keeps the entry package affordable and avoids auditing revenue reports from many small carts. Cafe pays royalty because its revenue is larger and it uses the brand more intensively. |
| Team | 1 Manager, 4 Sales (2 senior, 2 junior, one region each), 2 Reviewers, 1 Super Admin |
| Sales regions | Rendi: Greater Tangerang. Putri: Jakarta, Bogor, Depok, Bekasi, Cikarang. Agus: Greater Bandung. Wulan: Central Java |
| Expansion target | 120 new outlets per year (72 Gerobak, 48 Cafe). This is a stretch target, more aggressive than what comparable brands have publicly shown. |
| Revenue definition | Deal value of approved partnership packages after discount. Royalty is not counted because it happens after the outlet opens. |

### Industry context

Franchising is the main expansion channel for Indonesian F&B brands. As of February 2025, the Ministry of Trade recorded 311 franchisors with a Franchise Registration Certificate (STPW), 157 domestic and 154 foreign, and the culinary sector accounted for 47.77% of them [1][2]. This is a share of registered franchisors, not of outlets or revenue. In the coffee category, TOFFIN and MIX MarComm (SWA Media Group) found that chain coffee shops in major cities grew from around 1,000 outlets in 2016 to more than 2,950 in August 2019 [3][4]. The point is not that the market is booming, but that brands in this category grow by opening outlets through franchise partners, which makes the partnership process a core business process.

### Pain points

| # | Pain point | Who feels it | Impact |
|---|---|---|---|
| 1 | Leads are scattered and not centralized: they come from exhibitions, referrals, Instagram, the website, and walk-ins, and end up in each sales' WhatsApp chats, personal notes, and separate spreadsheets. | Sales, Manager | Leads are followed up late or forgotten, two sales contact the same candidate, and data is lost when a sales leaves. |
| 2 | Candidates do not know where their application stands and must keep asking their sales. | Candidate, Sales | Poor candidate experience. Serious candidates may move to a competitor. |
| 3 | Quotations, discounts, and change requests are negotiated by chat. | Sales, Manager, Candidate | No single agreed version, and approvals cannot be traced. |
| 4 | No deadline per stage and no visibility of bottlenecks. | Manager | Applications stay stuck for weeks unnoticed. |
| 5 | Candidate screening and location decisions rely on individual judgment. | Reviewer, Manager | Inconsistent decisions and outlets in weak locations. |
| 6 | Targets are only checked at the end of the month in a spreadsheet. | Manager, Sales | The team learns too late that the target will be missed. |
| 7 | Prospectus delivery and personal data consent are not recorded. | Franchisor | Legal risk under PP No. 35/2024 on Franchising [5] and UU PDP No. 27/2022 [6]. |

## Human vs System

The table compares what the franchisor team and candidates can do today with the manual process against the proposed system.

| Capability | Manual (current) | System | Notes |
|---|---|---|---|
| Capture leads from all channels in one place | ⚠️ Limited | ✅ | Leads are scattered in each sales' WhatsApp and spreadsheets. The system stores every lead, from sales input or portal registration, in one pipeline. |
| Assign leads by region and detect duplicates | ❌ Not available | ✅ | The Manager forwards leads by chat, and two sales can contact the same person. The system assigns portal leads by region and flags duplicates and full sales capacity. |
| See the stage and owner of every application | ⚠️ Limited | ✅ | The Manager has to ask each sales. The pipeline board shows every application with its current PIC and days waiting. |
| Track deadlines and send reminders | ❌ Not available | ✅ | Nothing signals that an application is stuck. The system reminds the PIC and Manager automatically when a stage passes its deadline. |
| Record prospectus delivery | ⚠️ Limited | ✅ | Delivery is not recorded consistently. The system requires the sales to confirm it and records the date. |
| Assess candidates and locations consistently | ⚠️ Limited | ✅ | Decisions rely on individual judgment. The system uses structured forms and an AI fit score with reasons. |
| Manage quotation versions and discounts | ⚠️ Limited | ✅ | Quotations are revised by chat. The system keeps every version and requires the Manager's input for revisions. |
| Candidate checks application status | ❌ Not available | ✅ | Candidates must ask their sales. The Partner Portal shows a 7-step tracker with the sales' contact. |
| Candidate responds to a quotation in writing | ⚠️ Limited | ✅ | Responses come by chat or phone. In the portal, the candidate agrees with an explicit confirmation, requests changes, or withdraws. |
| Trace two-party approval | ⚠️ Limited | ✅ | Approval is scattered across chats. The system records approval 1 of 2 (candidate) and 2 of 2 (Manager). |
| Monitor target vs achievement during the period | ⚠️ Limited | ✅ | Targets are checked at month end. The system shows achievement against the target to date, per sales and per package. |
| Keep an audit trail and document access log | ❌ Not available | ✅ | No record of who saw candidate data. The system logs every action and document access. |

## Goals and Success Metrics

Proposed first-year targets. Derived metrics come from the process design and business target; assumptions should be validated during the pilot.

| Metric | Target | Basis |
|---|---|---|
| Leads assigned to a sales within 1 day | 100% | Derived from the 1-day deadline of the New lead stage |
| Average time from new lead to final decision | 26 days or less | Derived: sum of stage deadlines (1 + 4 + 5 + 4 + 3 + 7 + 2) |
| Stages completed within their deadline | 85% or more | Assumption: leaves room for exceptions such as candidates who are hard to reach |
| Lead to approved partnership | 12% or more | Derived from the default funnel conversion rates (see Feature H) |
| New approved outlets per year | 120 (72 Gerobak, 48 Cafe) | Business target (stretch) |
| Approved deal value per year | around Rp 24.8 billion | Derived: 6 x Rp 45 million + 4 x Rp 450 million = Rp 2.07 billion per month |
| Quotation responses submitted through the portal | 70% or more | Assumption: portal adoption target, measured during the pilot |

## Diagram

### Flowchart

![Flowchart](flowchart.png)

### Stages and deadlines

| # | Stage | PIC | Deadline |
|---|---|---|---|
| 1 | New lead | System (automatic) or Manager | 1 day |
| 2 | Business presentation and prospectus delivery | Sales | 4 days |
| 3 | Location survey | Sales | 5 days |
| 4 | Eligibility assessment: interview, background check, financial verification, KYC, commitment | Reviewer | 4 days |
| 5 | Quotation | Sales | 3 days |
| 6 | Negotiation: candidate agrees, requests changes, or withdraws | Sales | 7 days |
| 7 | Final approval: approve or reject | Manager | 2 days |
| End | Approved, Rejected, or Withdrawn | | |

## Solution

### Solution Overview

The system covers **12 features** across two applications:

| # | App | Feature | Problem it solves | Key question the user can answer |
|---|---|---|---|---|
| A | Dashboard | Lead Capture and Auto-Assignment | Pain point 1 | "Is every new lead recorded and owned by the right sales?" |
| B | Dashboard | Pipeline and Approval Status | Pain points 1, 4 | "Where is each application now, and who is it waiting for?" |
| C | Dashboard | Stage Processing (presentation, survey, assessment) | Pain points 5, 7 | "Has this candidate passed each check, with evidence?" |
| D | Dashboard | AI Fit Score | Pain point 5 | "How well does this candidate and location fit, and why?" |
| E | Dashboard | Quotation and Negotiation | Pain point 3 | "Which quotation version is the latest, and how did the candidate respond?" |
| F | Dashboard | Final Approval | Pain point 3 | "Has this partnership been approved by both parties?" |
| G | Dashboard | Tasks and Automatic Reminders | Pain point 4 | "What do I need to do today, and what is overdue?" |
| H | Dashboard | Target vs Achievement and Sales Performance | Pain point 6 | "Are we on pace to hit this period's target, and who needs help?" |
| I | Dashboard | Access Control and Audit Trail | Pain point 7 | "Who did what, and who accessed this candidate's data?" |
| P1 | Partner Portal | Registration | Pain point 1 | "How do I apply without waiting for a sales to contact me?" |
| P2 | Partner Portal | Status Tracker | Pain point 2 | "Where is my application, and who is my sales?" |
| P3 | Partner Portal | Quotation Response | Pain point 3 | "How do I agree to, change, or decline the offer?" |

### Functional Requirements

#### Feature A: Lead Capture and Auto-Assignment

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-A-001 | As a Sales, I want to add a lead from offline channels so that every candidate is recorded in one place. | Form fields: name, phone, email, city, package, available capital, source of funds, management plan, lead source, planned location, documents. Personal data consent (UU PDP) is required. | Cannot be saved without consent and mandatory fields. The lead appears in the sales' pipeline at Business presentation. |
| FR-A-002 | As a Manager, I want portal leads assigned automatically so that no lead waits for me. | Match the candidate's city to a sales region. Send the lead to the Manager queue if the city is outside all regions, the phone or email matches an active lead (possible duplicate), or the sales has reached the active lead cap (senior 15, junior 10). | A lead in region with capacity is assigned immediately. An exception shows "No sales yet" with the reason. The Manager can assign a sales, and who assigned it and when is recorded. |

#### Feature B: Pipeline and Approval Status

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-B-001 | As a Manager, I want to see all active applications by stage so that I can spot bottlenecks. | Kanban with 7 active stages. Filter by package and search by name or city. Sales see only their own leads. | Each card shows name, city, package, AI score, current PIC, and days in stage. Overdue indicators are visible to Manager and Super Admin only. |
| FR-B-002 | As a Manager, I want to review finished applications so that I can learn why deals were won or lost. | Completed table (approved, rejected, withdrawn) with result, last stage, reason, deal value, sales, and date. | Filters by result, period, sales, and search work together. A "Completed this month" summary is shown below the board. |
| FR-B-003 | As an internal user, I want to see the approval status of one application so that I can answer "where is it now?" quickly. | 7-step timeline with PIC, completion date, and waiting time. | Opens from the application detail and the Tasks table. The current step shows the PIC and days waiting. |

#### Feature C: Stage Processing

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-C-001 | As a Sales, I want to record the business presentation so that prospectus delivery is provable. | Presentation date, mode, notes, and a required prospectus delivery confirmation. | Cannot be completed without the confirmation. The date is recorded, supporting the 14-day rule in PP No. 35/2024 [5]. |
| FR-C-002 | As a Sales, I want to record the location survey so that the location decision is made early. | Survey rating, foot traffic, notes, and a feasible or not feasible decision. If the AI location score is below 60, show an SOP reminder to discuss with the Manager first. | Not feasible: rejected with reason. Feasible: moves to Eligibility assessment, or directly to a revised quotation after a location change. |
| FR-C-003 | As a Reviewer, I want a structured checklist so that every candidate is assessed the same way. | Checklist: interview, background check, financial verification, KYC, commitment, plus pass or fail with reason. | Only Reviewer (or Super Admin) can submit. Fail: rejected with reason. Pass: moves to Quotation. |

#### Feature D: AI Fit Score

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-D-001 | As a Reviewer or Manager, I want a fit score with reasons so that screening is more consistent. | Score 0 to 100: candidate profile 40% (capital vs package, source of funds, experience, management plan, documents) and location 60% (crowd points, competitors, distance to nearest outlet, location type, survey result). | Score and plus or minus reasons are shown on the card and the Summary tab. The score never changes a stage or rejects a candidate automatically. |

#### Feature E: Quotation and Negotiation

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-E-001 | As a Sales, I want to send a versioned quotation so that there is always one agreed offer. | Package, discount, payment terms, target opening date, and notes. Each send creates version N and emails it with a portal link. A revision requires "Result of discussion with Manager". | All versions are kept in the quotation history. A revision cannot be sent without the discussion result. |
| FR-E-002 | As a Sales, I want to record a response given by phone or in person so that offline answers are not lost. | Record agree, request changes (type and details), or withdraw on behalf of the candidate. | Request changes: back to Quotation (Revision). Change location: new address required, back to Location survey. Withdraw: closed as Withdrawn. |

#### Feature F: Final Approval

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-F-001 | As a Manager, I want to approve or reject an agreed quotation so that the partnership is confirmed by both parties. | Yes or no decision with reason for rejection. No location revision at this step. | Approve: approval 2 of 2, deal value after discount counted as revenue, next step (franchise agreement through Privy) shown. Reject: reason required. The candidate sees the result in the tracker. |

#### Feature G: Tasks and Automatic Reminders

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-G-001 | As any internal user, I want one list of actions waiting for me so that I know what to do today. | Tasks table per user. The Manager can filter: My tasks, All, Sales, Reviewer. | Each row shows candidate, action needed, PIC, waiting time, and deadline status, with shortcuts to the detail and approval status. |
| FR-G-002 | As a Manager, I want overdue stages to trigger reminders so that follow-up does not depend on memory. | When days in stage exceed the deadline, notify the PIC and the Manager by dashboard notification and email. No manual reminder button. | The overdue item shows "Overdue N days" and "Reminder sent to PIC and Manager". |

#### Feature H: Target vs Achievement and Sales Performance

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-H-001 | As a Sales or Manager, I want to see achievement against target during the period so that we can act before it ends. | Period: month, quarter, semester, or year. Cards for Gerobak, Cafe, and revenue with target, gap ("N short"), target to date (MTD, QTD, HTD, YTD), and pipeline opportunities. Funnel calculated backwards from adjustable conversion rates. | Monthly targets per sales: senior 2 Gerobak + 1 Cafe, junior 1 Gerobak + 1 Cafe (team: 6 + 4 per month, 120 outlets per year). Days 1 to 9 of a period show "Early period" instead of "Critical". With default rates, the funnel shows about 92 leads per month needed. |
| FR-H-002 | As a Manager, I want to compare sales performance so that I know who needs help. | One table per sales with Gerobak, Cafe, and revenue against target, and a status based on the weakest metric. | Sorted from best to weakest. Senior or junior level is shown. Clicking a sales opens their profile. |

#### Feature I: Access Control and Audit Trail

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-I-001 | As a Super Admin, I want access to follow roles so that each user only sees what they need. | Role-based access control (RBAC) as in the matrix below. | A Sales cannot open another sales' lead. Actions by the Super Admin are recorded under their own name. |
| FR-I-002 | As a Manager, I want every action logged so that decisions and data access are accountable. | Log status changes, quotation versions, approvals, document access, and portal actions with actor and time. | The History tab shows the full log. Portal actions appear as "Candidate (partner portal)". Entries cannot be edited. |

**RBAC matrix**

| Permission | Super Admin | Manager | Sales | Reviewer | Candidate |
|---|---|---|---|---|---|
| View pipeline | All | All | Own leads | All | Own application (number + email or phone) |
| Add lead | Yes | No | Yes | No | Self-registration |
| Assign sales to an unassigned lead | Yes | Yes | No | No | No |
| Presentation, survey, quotation, negotiation | Yes | No | Own leads | No | Respond to quotation |
| Eligibility assessment | Yes | No | No | Yes | No |
| Final approval | Yes | Yes | No | No | No |
| View candidate documents | Yes | Yes | Own leads | Yes | Own documents |
| View overdue indicators | Yes | Yes | No | No | No |
| Target vs Achievement | Team | Team | Own | No | No |
| Sales Performance | Yes | Yes | No | No | No |

#### Feature P1 to P3: Partner Portal

| ID | User Story | Requirement | Acceptance Criteria |
|---|---|---|---|
| FR-P1-001 | As a candidate, I want to register online so that I can apply without waiting for a sales. | Registration form with package, capital, planned location, and required personal data consent. | An application number is shown. The lead enters the pipeline and follows FR-A-002. |
| FR-P2-001 | As a candidate, I want to check my status so that I do not need to keep asking. | Lookup with application number plus email or phone. 7-step tracker with dates and the assigned sales' contact. | A wrong combination shows an error without revealing any data. |
| FR-P3-001 | As a candidate, I want to respond to the quotation directly so that my answer is recorded. | Agree (requires ticking "I have read and agree to quotation version N"), request changes (type, details, new address for a location change), or withdraw. | Agree records approval 1 of 2 in the audit trail. After final approval, the portal shows that the agreement will be sent through Privy. |

### Input, Process, Output

| Stage | Input | Process | Output |
|---|---|---|---|
| 1. New lead | Candidate data, planned location, personal data consent | Duplicate check, region matching, capacity check, AI fit score | Application number, assigned sales or Manager queue, tracker access |
| 2. Business presentation | Date, mode, prospectus confirmation, notes | Sales presents the business model and sends the prospectus | Prospectus date recorded, moves to Location survey |
| 3. Location survey | Address, rating, foot traffic, AI location score | Sales assesses the location (with Manager if score is below 60) | Feasible: Eligibility assessment. Not feasible: Rejected |
| 4. Eligibility assessment | Interview, background check, bank statement, ID and tax number, commitment | Reviewer evaluates the checklist | Eligible: Quotation. Not eligible: Rejected |
| 5. Quotation | Package, discount, payment terms, opening date, Manager discussion result | System creates version N and emails it with a portal link | Quotation version N sent and recorded |
| 6. Negotiation | Candidate response from portal or recorded by sales | System routes by response | Agree: Final approval (1 of 2). Changes: Quotation or Location survey. Withdraw: closed |
| 7. Final approval | Application history and agreed quotation | Manager approves or rejects | Approved (2 of 2) and revenue counted, or Rejected with reason |

### Mock Ups

Screenshots from the clickable prototype. The interface uses Bahasa Indonesia.

[[GRID mockups/02_pipeline.png|Pipeline (Manager view) ;; mockups/03_detail.png|Application detail: quotation tab]]

[[GRID mockups/04_status.png|Approval status timeline ;; mockups/05_target.png|Target vs Achievement]]

[[GRID mockups/07_portal_form.png|Portal: registration ;; mockups/08_portal_tracker.png|Portal: status tracker ;; mockups/09_portal_quote.png|Portal: quotation response]]

## Nonfunctional Requirements

| Area | Requirement |
|---|---|
| Privacy and security (UU PDP No. 27/2022) [6] | Consent before a lead is saved. Access by role. Document access is logged. Data of rejected candidates is deleted or anonymized after a defined retention period. |
| Auditability | Every status change, quotation version, approval, and document access is logged with actor and time and cannot be edited. |
| Responsible AI | The fit score shows its reasons, never rejects automatically, and is reviewed against actual outlet performance to detect bias. |
| Mobile friendly | The Partner Portal is mobile first because candidates come from Instagram or email links. The dashboard is optimized for laptops and usable on phones. |
| Reliability and performance | 99.5% availability during working hours. Pages load in under 3 seconds on 4G. |
| Language | Bahasa Indonesia interface, keeping common business terms such as Sales, Lead, Quotation, and Pipeline. |

## Scope and Roadmap

| Priority | Features | Phase |
|---|---|---|
| Must have | A, B, C, E, F, G, I, P1, P2, P3 | MVP (months 0 to 3): backend, company login, email notifications, pilot in one region |
| Should have | D (AI fit score), H (targets and performance), mobile layout | MVP if time allows |
| Could have | Privy e-signature, WhatsApp notifications, real map data for the location score, document upload with KYC verification, report export | Phase 2 (months 3 to 6), all regions |
| Won't have (for now) | Royalty tracking, outlet operations after opening, payment gateway, training modules, multi-brand | Phase 3 (months 6 to 12) or later, with the fit score calibrated on real outlet performance |

## Prototype Limitations

- Data is stored in the browser (localStorage), so the dashboard and portal are connected only within the same browser. "Reset demo data" in the account menu restores the sample data.
- The login page lists demo accounts per role for quick testing. Production would use company accounts (SSO).
- Sample data is calculated relative to today's date, so target pages always show a realistic current period.
- The AI fit score is simulated with rule-based weighting and simulated map data. Production would use real location data calibrated with outlet performance.
- Email notifications are simulated as dashboard notifications. The Privy integration is not built; only the next step is shown.
- The registration form has a "Fill sample data" button for faster testing.

## Risks and Open Questions

| Risk or question | Mitigation |
|---|---|
| Sales keep using WhatsApp and do not update the system | Reminders and targets depend on system data, so updating it is the easiest way for sales to look good. Training during the pilot. |
| The stretch target is not realistic | Track against the target to date and review after the first quarter. |
| The AI score creates bias or overconfidence | Show reasons, keep humans deciding, and review against outcomes. |
| Open question: should large discounts need Manager approval before a quotation is sent? | To be confirmed with the client. Currently a discussion outside the system. |

## Use of AI

I used Claude (Anthropic) throughout the project. It helped me move faster, but the product decisions were mine, and I checked its output before using it.

| Activity | How AI was used | My role |
|---|---|---|
| Understanding the case | Explored client profiles and pain points | Chose the client profile and the scope: application until two-party approval |
| Process design | Proposed stages and rules | Simplified the flow, moved the location decision to the survey stage, removed manual reminders, decided who approves what |
| Prototyping | Built the clickable HTML prototype through Claude Code across many feedback rounds | Reviewed each version, changed layout, wording, and terminology, rejected cluttered options |
| Testing | Ran automated browser tests on every role, the end-to-end flow, and mobile sizes | Defined what "correct" looks like and checked results |
| Research | Searched for industry and regulation data | Asked for sources and verified them. Corrected a 2016 to 2019 statistic that had been cited as recent, and replaced PP No. 42/2007 with PP No. 35/2024 |
| Targets | Proposed target schemes | Chose whole-number monthly targets by seniority and labeled the yearly number as a stretch target |
| Writing | Drafted this document from the prototype | Reviewed, restructured, and edited the content |

What I learned: AI is fast at producing options and working code, but it can sound confident about inaccurate data. Asking for sources and checking them was necessary.

## References

1. ANTARA News, "Kemendag sebut sektor kuliner masih mendominasi bisnis waralaba". https://www.antaranews.com/berita/4774885/kemendag-sebut-sektor-kuliner-masih-mendominasi-bisnis-waralaba
2. Tempo, "Mendag: Waralaba Serap 97 Ribu Tenaga Kerja dengan Omzet Rp 143 Triliun". https://www.tempo.co/ekonomi/mendag-waralaba-serap-97-ribu-tenaga-kerja-dengan-omzet-rp-143-triliun-1218788
3. Marketeers, "Toffin: Nilai Pasar Kedai Kopi di Indonesia Capai Rp 4,8 Triliun". https://www.marketeers.com/toffin-nilai-pasar-kedai-kopi-di-indonesia-capai-rp-4-8-triliun/
4. Warta Ekonomi, "Bisnis Kedai Kopi di Indonesia Cerah, Jumlahnya Melesat 3X Lipat". https://wartaekonomi.co.id/read262062/bisnis-kedai-kopi-di-indonesia-cerah-jumlahnya-melesat-3x-lipat
5. JDIH BPK, Peraturan Pemerintah No. 35 Tahun 2024 tentang Waralaba. https://peraturan.bpk.go.id/Details/297489/pp-no-35-tahun-2024
6. JDIH BPK, Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi. https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022

## Appendix: AI Conversation Screenshots

[Attach screenshots or a PDF of the AI conversation here.]
