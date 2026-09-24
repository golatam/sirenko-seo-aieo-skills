---
name: ga4-project-reporting
description: "Use when reporting GA4 traffic and conversion outcomes."
version: 1.1.0
author: Hermes Agent
created_by: agent
---

# GA4 project reporting

Use for a project that needs GA4 reporting by country, month, acquisition channel, or source/medium, especially when the result must live in the project's own Google Drive.

## Core rule: report ownership before formatting

For an analysis request, default to local read-only output. Creating/updating Google Sheets or Drive is a separate external write: preview the target account, file/tabs, sharing and scope; obtain confirmation and read back the exact target. Do not request write OAuth scopes for a read-only/local report. The ownership workflow below applies only when a cloud workbook is requested and approved.

1. Resolve the **project Google account** from the mail/account registry or explicit user instruction.
2. Verify the OAuth token identity with Gmail profile or equivalent; do not assume a shared Analytics account is also the desired Drive owner.
3. Ensure that project token has both GA readonly and Google Sheets/Drive write scopes.
4. Create the spreadsheet using that **project token**, not a personal/default token.
5. Read back Drive metadata and verify `owners.emailAddress` before reporting success.

If the user cannot open a sheet that API says exists, check the owner and tell them to open it while signed into that exact account. Do not silently recreate files in a different account.

## Default readable workbook shape

For country-level monthly reporting, prefer four focused tabs over a dense all-in-one sheet:

1. **Пользователи** — rows: country; columns: completed calendar months; metric: active users.
2. **Выручка** — rows: country; columns: completed calendar months; metric: reported revenue.
3. **Каналы** — country × `sessionDefaultChannelGroup`, with active users, sessions, and revenue for the selected period.
4. **Источники** — country × channel × `sessionSourceMedium`, with the same core metrics.

Formatting:
- freeze first row and country column;
- add filters;
- use one simple header row and readable column widths;
- use numeric month columns, not prose labels such as “growth” / “decline”, when the user needs month-to-month comparison;
- do not drop acquisition tabs when simplifying user/revenue tabs.

## Query design

- Use **six completed calendar months** when the request is “last six months” and month-on-month comparison matters; avoid mixing partial current month with full months unless explicitly requested.
- Country/month request: dimensions `country`, `yearMonth`; metrics `activeUsers`, `totalRevenue`.
- Channel request: dimensions `country`, `sessionDefaultChannelGroup`; metrics `activeUsers`, `sessions`, `totalRevenue`.
- Source request: dimensions `country`, `sessionDefaultChannelGroup`, `sessionSourceMedium`; same metrics.
- Respect pagination and preserve a raw export or source table when a report has many rows.

## SEO/AIEO outcomes

For SEO landing cohorts, AI referrals, key events and qualified leads, load `references/organic-ai-outcomes.md`. Keep measurement setup in `web-analytics-architecture` and cross-source analysis in `seo-reporting-monitoring`; do not create a parallel definition of clicks, sessions or revenue.

## Revenue-sign convention

Never silently change financial signs. If the user explicitly says GA4 negative revenue values should be read as positive, display `abs(totalRevenue)` and label the field clearly, for example **“Выручка, USD (+)”**. State in the workbook/readout that it is an analyst-applied sign convention, not a GA4 correction.

## Insight guardrails

Before turning the report into commercial conclusions, check:

- share of `Unassigned` / `(not set)` in sessions and revenue;
- sessions per active user by channel/source;
- concentration by country;
- abrupt month-on-month shifts;
- whether organic/direct channels show implausibly low or high revenue.

When unattributed traffic or revenue dominates, lead with the data-quality warning. Present country trends as directional signals, not as validated unit economics. See `references/ga4-data-quality-checks.md`.

## Delivery checklist

- [ ] Spreadsheet owner is the intended project account.
- [ ] Tabs have only the metrics the user asked to compare.
- [ ] Month columns use full calendar periods and are labelled.
- [ ] Channel and source tabs are retained unless the user explicitly removes them.
- [ ] Sheet contents and Drive owner were read back after writing.
- [ ] Any attribution/revenue anomaly is surfaced plainly.
