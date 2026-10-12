---
name: rank-tracker-operations
description: "Позиции сайта через трекер (Topvisor): проверка доступа, цена и согласованный запуск платной проверки, полнота матрицы запрос×регион, история позиций. Использовать, когда просят «сними позиции», «проверь позиции в Topvisor», «сколько стоит проверка позиций», «динамика позиций за неделю»."
version: 1.1.0
author: Sirenko SEO/AIEO Skills contributors
license: MIT
created_by: agent
---

# Rank Tracker Operations

Use when the user asks to run, repair, or schedule recurring keyword-position monitoring through a rank-tracker service such as Topvisor.

## Operating sequence

1. Read the project descriptor: domain, tracker project ID, searchers/regions, keyword core, latest snapshot and report.
2. Run a **read-only probe** first: verify credentials, project access, regions/searchers, keyword/history rows and the latest history date.
3. For a manual paid run, calculate the checker price and limits; show the user the amount and obtain explicit confirmation before triggering it.
4. Trigger the approved paid checker through the central tracker. Never silently substitute GSC average position, public `site:` queries, or an old snapshot for a real rank check.
5. Poll the tracker history for the check date within the approved time/request budget. When the checker returns a positive expected-cell limit, reconcile the exact keyword × region/searcher/device matrix against that limit before reporting. Stable shortfall is **incomplete**, even when near the expected count. If provider evidence proves the expected universe changed, preserve the original expectation and the explicit revised matrix; never silently lower the denominator. Exit status 0 is not completeness evidence. Resume an existing job after timeout; do not start another paid check blindly.
6. Only then persist the snapshot, generate Markdown/CSV reports and deliver the short digest.

## Credentials and secret handling

- Keep shared tracker credentials only in the central, git-ignored `.env` or process environment; never duplicate them in consumer repositories, project files, memory, reports, or Git.
- Use the existing approved runner to resolve credentials without displaying them. Check only non-secret presence/permissions metadata when necessary. Do not request or accept secrets in chat; use approved secure credential setup.
- Never print a credential or raw API response that may contain it. An authorization error is a blocked data source, not permission to rotate secrets, modify a server, or restart Hermes.

## Report validity

- State the rank source, paid-check status, non-secret price/limits, check date, configured regions and artefact paths.
- If the stored comparison baseline is older than a week, label the real comparison period; do not call a monthly gap a weekly delta.
- Explicitly separate genuine current no-data/OUT results from incomplete current history. A partial run must be treated as incomplete, not as a ranking collapse.
- GSC is supplementary for clicks, impressions, CTR and indexing; it is not a replacement for rank-tracker positions.

## AI visibility is a separate measurement layer

When the request includes ChatGPT, Gemini, Perplexity, Google AI Overviews/AI Mode, Copilot or similar answer engines:

1. Keep a dedicated AI-visibility dataset beside the SERP dataset. Store each run’s prompt, engine/model, locale, timestamp, raw answer, citations/mentioned brands and collection cost.
2. Report AI metrics as mention rate, cited-link share, answer-level placement or vendor-defined share of voice. Never call them a SERP position: answer output changes with prompt wording, model/version, locale and repeat run.
3. Route AI data collection and interpretation to `aieo-visibility`. Use first-party GSC Generative AI reporting only after checking the actual UI/export availability, fields and applicable permissions; do not infer an API endpoint or present it as measurement of other answer engines.
4. Before an annual AI-tool commitment, run a 30–60 day pilot on a frozen prompt panel and require raw-answer export. Stop if the signal is not more stable than repeat-run variation or has no useful relation to referrals/conversions.
5. Treat official MCP/API support as an integration capability, not a quality guarantee. Make answer collection read-only by default; separate any charged provider call behind a budget cap and explicit confirmation.

## AI tracker setup: brand and prompt panel

Before collecting AI answers, configure the tracker as a disambiguation exercise, not as an SEO keyword import:

1. Use the canonical brand name without decorative punctuation unless that punctuation materially changes the brand. Add genuine spelling, transliteration, legacy-name and word-boundary aliases; do not add case-only duplicates.
2. Write a short factual brand description: audience, market, services and differentiators. Explicitly exclude common false identities when the name is ambiguous (for example, a business service is not a travel agency or an SEO tool).
3. Set one language and one market context per panel. Create separate projects or prompt groups for Russian, Spanish and English rather than mixing them; results otherwise cannot be attributed to a language/market.
4. Start with a small, balanced panel: brand/reputation, category discovery, solution evaluation, and country/vertical-specific problems. Write questions in natural language with task, context and decision need; do not paste short SEO-keyword fragments. Keep every prompt within the vendor length limit and retain the exact submitted wording.
5. Import one prompt per line or CSV `name` rows. Group prompts by intent/language before the first run so future deltas remain interpretable. Confirm the imported count and sample text before continuing.
6. Capture the setup values and prompt list as a durable project artefact before a chargeable run. If the next screen shows engines, volume, or spend, preview the full cost and obtain confirmation before launching.

## Recurring jobs

The central tracker is an optional host integration, not bundled software. Resolve `${SEO_TRACKER_DIR}` only for an existing approved compatible implementation. Load `seo-reporting-monitoring` and its central Topvisor reference before using that host CLI. Inspect current code: a `--dry-run` flag may still submit a sitemap before its early return, and checker success may accept incomplete history.

An authorized scheduled job must use the central tracker workdir and contain the concrete flow: price/budget verification → approved paid check → wait for complete history → snapshot/report → authorized delivery. It must fail visibly if the paid check or completeness verification fails, not issue a plausible report. Scheduling, importing keyword sets and notifier changes are separate external writes requiring preview/confirmation/readback.

## Common failures

- Producing a GSC-only report when the project is configured for a rank tracker.
- Starting a charged check without a price preview and explicit approval for manual runs.
- Rendering a report before the history stabilizes, creating false mass OUT alerts.
- Treating a previous month’s snapshot as a weekly baseline.
