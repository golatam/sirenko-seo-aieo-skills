# Native AI consoles: definitions, exports and limitations

Checked 2026-09-24. Public official documentation is evidence of product capability, **not proof of this account's permissions, report availability, or actual client performance**. The observed-answer JSONL summarizer does not import native console aggregates; retain these as separate metric families.

## Google Search Console — confirmed UI report

Official help: https://support.google.com/webmasters/answer/16984139 . It states rollout to all websites worldwide as of 2026-08-31, while its 'Not seeing the report?' section still mentions staged availability and insufficient impressions. Treat this wording tension as a reason to inspect the actual property, not to guarantee a visible report.

- Search report covers AI Overviews + AI Mode, excludes Search Labs experiments. Metric documented: **impressions** (links shown), not mention/recommendation/fidelity. Documented dimensions: Pages, Countries, Dates, Devices. Do not claim clicks, CTR, average position, user query text, prompt/answer exports, or an AIO-vs-AI-Mode dimension from this report.
- Pages mostly attributed to canonical URL; help describes final linked URL after redirects. Chart aggregated by property unless URL-filtered; table by page for Pages and by property for country/device/date. Multiple site URLs need not yield multiple property impressions. Chart/table sums can differ.
- Daily dates are PT. Preliminary chart data is marked; table row limit is 1000. The launch blog also discusses hourly granularity; inspect the actual view/export rather than assuming every date range exposes hours.
- **Native export confirmed:** help says export downloads chart and table data. Critical caveat: displayed `~` or `-` (unavailable/not a number) becomes **zero in download**. Preserve original UI missingness evidence; never interpret every exported 0 as a true measured zero.
- **Dedicated API extraction unconfirmed:** checked Search Analytics reference lists web/image/video/news/googleNews/discover, no documented dedicated generative-AI type or named AI filter. A generic string parameter in an MCP schema is not evidence. Do not invent an API, search type, searchAppearance enum or consumer-answer source. UI export is the supported documented path found here; recheck official API docs before future automation.
- AI data is included in ordinary Web performance. Do not add it to the ordinary Web totals or infer AI clicks by subtraction.

### Inclusion control is separate, consequential and read-only in an audit

https://support.google.com/webmasters/answer/16908024 documents Settings → Search generative AI: include / exclude / inherit from parent. Default for root properties is include; child properties may inherit. Exclusion affects AI Overviews, AI Mode and generative Discover links/content/grounding; it is not a ranking signal for other Search or an AI-training control. The Google guide also requires indexing and snippet eligibility. Check effective inherited state and property hierarchy if report is absent; do not flip the setting automatically. Changes require owner approval and separate verification after propagation.

### Discover is a separate AI report

https://support.google.com/webmasters/answer/16983858 documents impressions in Discover generative features, separate chart/table export and page-based aggregation. Links must scroll into view; per-result/session counting applies. No mixing with Search's property aggregates. The June launch blog documents Pages/Countries/Dates and Devices **for Search only**; recheck actual Discover columns instead of inferring device availability. The help extraction was partial for lists during this review; do not claim unsupported extra dimensions.

## Bing Webmaster Tools AI Performance — confirmed native dashboard

Official February announcement:
https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview

- Supported coverage: Microsoft Copilot, AI-generated Bing summaries and selected partner integrations, aggregated; not all AI engines or all consumer Copilot interactions by implication.
- Total citations = citations displayed as sources in generated answers; Average Cited Pages = daily average of unique cited site pages over selected range. URL-level citation activity and time trends are documented.
- Grounding queries are retrieval phrases used by AI and a **sample** of overall citation activity, not a complete list of original user prompts or search demand. Do not infer completeness or reconstruct raw answers.
- Citation counts do not measure placement, ranking, authority or faithful support. They are not Google impressions, visits, conversions or our frozen-panel answer-rate denominator.

June update confirmed:
https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare

Intents, Topics, Citation Share and Compare are preview capabilities rolling out globally. Intent/topic labels are evolving AI/ML classifications, possibly broad for niche subjects. Citation Share = site's citations / all sites' citations **for the same grounding query**, not traffic share, ranking, quality score or list of competitor domains. Compare overlays periods; changes can reflect models, freshness, partner refresh and demand, not necessarily the site's intervention.

**Export/API status in this review:** public blog pages confirm reporting but not an AI export schema or dedicated AI endpoint. Help URL https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c returned a JavaScript shell/sign-in text; browser recovery was unavailable in this runtime. Therefore automated export/API availability remains **not verified**, not 'does not exist'. Do not repurpose ordinary Bing search-performance endpoints as AI Performance. Use an owner-provided native export if the live UI offers it and record exact columns; otherwise manually transcribe a bounded visible table with dual-check and label it `manual_ui_transcription`, not native export. Do not bypass login or scrape private internal endpoints.

## Яндекс.Вебмастер — «Видимость сайта в Алисе AI»

Official help checked 2026-09-24: https://yandex.ru/support/webmaster/ru/service/alice-answers . The UI report is documented; this review does not establish access to a particular account or a dedicated Alice API.

- Covers the last **3 months**, updated **weekly**. Its query universe is restricted to queries where the site already appears sufficiently high in Search; it is not the whole market or a frozen prompt panel.
- Native SoV = queries with the site's mention in Alice answers / queries with Alice answers **within that covered universe**. Keep this metric separate from Bing Citation Share and locally observed answer rates. A changing eligible-query universe can change the metric; a before/after correlation is not proof of SEO causality.
- Examples → Sites and Queries/pages are selected examples in non-ranking order, not a complete competitor ranking or query census. Query-list download is documented; that does not establish export of the whole historical chart or all raw answers.
- A fresh «Посмотреть в ответе» opens a newly generated answer and can differ from the historical example. Save capture time and surface; never label a new answer as the archived answer that caused the metric.
- «Пока недостаточно данных» is unknown/insufficient, not zero visibility. The report is not intended to supply click/impression counts. Preserve visible scope, period, native labels, filters and missingness with any export.
- Follow `seo-specializations` for Yandex/Alice technical and content workflows. Do not infer Alice endpoints from ordinary Webmaster API resources, change account settings, or request secrets in chat.

## Acquisition and reconciliation protocol

1. Resolve authenticated property/account, owner authorization, exact report and source surface. Inspect the real UI read-only or request existing exports through a secure file path. Never request credentials in chat.
2. Record export manifest: source_url/report title, property, acquisition_method (`native_ui_export`/`approved_api`/`manual_ui_transcription`), UTC extraction time, source date range + timezone, selected tab/dimensions, filters, aggregation, data freshness, visibility/inclusion state if relevant, native file format and checksum (tool-computed), displayed total and row count.
3. Preserve original immutable export and missing-marker screenshot/text. Import into a separate normalized table with explicit `metric`, `value`, `missingness_status`, `dimension`, `dimension_value`, `period`, `source`, `aggregation`, `limitations`. Do not manufacture query/device/AI-surface columns that weren't exported. Unknown isn't zero; if original missingness cannot be recovered, label zero ambiguity.
4. Validate dates, nonnegative numeric metrics, column names, row count and truncation. Distinguish chart totals, table totals, page vs property and sampled grounding queries. Exact-dedupe overlapping export identity, not arbitrary rows from different periods. Do not sum duplicate snapshots.
5. Compare only same property/report/filter/aggregation/finalized duration and explain deployment/panel/model changes. Reconcile by documented definition; unexplained gaps stay open. Deliver source artifacts, not invented performance numbers.
