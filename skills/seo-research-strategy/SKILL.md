---
name: seo-research-strategy
description: "Use when planning SEO demand and content strategy."
version: 1.0.0
author: Hermes Agent
license: MIT
created_by: agent
metadata:
  hermes:
    tags: [seo, research, keywords, competitors, intent, strategy]
    related_skills: [seo-aieo, competitor-analysis, seo-content-operations, seo-site-architecture, seo-specializations, technical-seo-audits, aieo-visibility, seo-authority-promotion, seo-reporting-monitoring, google-search-console-operations, rank-tracker-operations, ga4-project-reporting]
---

# SEO Research and Strategy

## When to Use
Use for demand discovery, keyword research, SERP/competitor gaps, clustering, query-to-page mapping, cannibalization investigation and a prioritized SEO roadmap. This is the research owner under `seo-aieo`, not a technical audit or a promise of ranking growth.

Load `competitor-analysis` for market/offer positioning. Its evidence discipline applies here; business competitors and search competitors are separate sets. Do not inherit a geography default without recording it.

## Procedure
Read [research-method](references/research-method.md) and [data-contracts](references/data-contracts.md) before collecting a project dataset. Read [sources](references/sources.md) when revising the method or importing donor ideas.

### 1. Recover the decision and scope
- **Input:** project notes, domain, offer, existing content/data, requested decision.
- **Procedure:** inspect relevant project files with `search_files`/`read_file`; establish customer job, commercial goal, country, language, engine, device, resources, exclusions and access. Separate each country/language lane. Record assumptions rather than silently using a global market.
- **Output:** [research brief](templates/research-brief.md), a source inventory and bounded sampling plan in the chosen project artifact directory.
- **Verification/stop:** a domain without an offer or audience supports only reconnaissance. Stop prioritization if the missing decision changes the market or page type; ask one decisive question.

### 2. Gather demand and competitor evidence
- **Input:** brief, scoped customer evidence, site inventory, authorized exports and public sources.
- **Procedure:** collect exact customer phrasing and query variants; inspect local-language SERPs and relevant competitor pages. Use `web_search` for discovery, `web_extract` for page evidence, browser only for missing rendered content. Follow pagination on exports/APIs and reconcile totals. Route GSC, rank data and GA4 to their specialist skills; discover actual tool schemas before using a connector.
- **Output:** [queries.csv](templates/queries.csv), [metrics.csv](templates/metrics.csv), source-grounded competitor matrix inside [strategy.md](templates/strategy.md).
- **Verification/stop:** trace every query to a source or label it `hypothesis`. No frequency, KD, traffic or market-share invention. Missing access means blanks plus precise limits, not invented estimates. No paid calls or installation without separate permission.

### 3. Observe SERPs and cluster by intent
- **Input:** query candidates, selected locale/device and dated result samples.
- **Procedure:** record actual engine results in [serp.csv](templates/serp.csv); inspect page types and user jobs. Compare overlapping ranking URLs within the same lane; use textual similarity only to propose candidates. Split mixed intents or mark unresolved clusters. Generic search-tool result order is not Google rank.
- **Output:** documented cluster assignments, representative snapshots, observed overlap and the reason one page could satisfy each group.
- **Verification/stop:** do not call semantic-only groups SERP-validated. No universal overlap threshold. Without localized SERP evidence, keep provisional assignments and a small targeted validation queue.

### 4. Map queries to pages and test overlap
- **Input:** clusters, existing URLs/canonicals and query-page observations if available.
- **Procedure:** select an existing page, propose a new page or defer; keep one primary target per query/market/language/intent. Investigate competing URLs using repeated observations, intent, page purpose and outcomes. Distinguish normal multiple visibility from harmful overlap.
- **Output:** [query-page-map.csv](templates/query-page-map.csv), evidence-linked overlap decisions and architecture handoff.
- **Verification/stop:** do not merge, redirect, delete or canonicalize solely because two pages share words. No GSC/rank evidence means cannibalization is `suspected` or `unknown`, not proven.

### 5. Choose a feasible strategy
- **Input:** validated/provisional map, business value, evidence gap, production capacity and technical constraints.
- **Procedure:** prioritize by customer value, product fit, ability to contribute useful evidence, observed demand and delivery cost. Record qualitative judgments separately from measured metrics. Sequence blocked dependencies before content production; include alternatives and stop conditions.
- **Output:** completed strategy with prioritized page backlog, owners, dependencies, review dates, next experiment and measurable success/failure definition. Hand each page's query map and evidence request to `seo-content-operations`.
- **Verification/stop:** no forecast without disclosed assumptions and a calculation. A low vendor KD is not a guaranteed quick win; an unknown or zero estimate is not automatic rejection.

### 6. Validate and hand off
- **Input:** all saved datasets and roadmap.
- **Procedure:** parse CSVs with Python (`csv.DictReader`), reconcile counts, IDs, joins, locale consistency, source paths, numeric units and missingness using the contract. Review unresolved targets and sampling limits. Keep raw exports separate and unchanged.
- **Output:** artifact paths, row/coverage counts, accepted decisions, provisional decisions, blockers and next owner. Templates contain headers/placeholders only; populate them with real evidence, not illustrative data.
- **Verification/stop:** no duplicate primary query mapping in the same intent lane; no metric without provenance; no claim of exhaustive coverage from a sample. Fix failures or deliver a labeled partial artifact.

## Routing and Boundaries
- `seo-site-architecture`: URL structure, hierarchy and internal-link implementation after mapping.
- `technical-seo-audits`: crawl/index/canonical blockers and implementation verification.
- `seo-specializations`: local, international, ecommerce and other context-specific execution.
- `aieo-visibility`: prompt sampling and observed AI mentions/citations. A SERP feature is not an AI-visibility measurement.
- `seo-authority-promotion`: distribution and earned coverage, not unauthorized outreach.
- `seo-reporting-monitoring`: monitoring cadence and outcome interpretation; `rank-tracker-operations` retains independent rank observations rather than being replaced by GSC.

## Pitfalls
- Mixing countries, languages, providers, devices or periods into a single demand number.
- Rewriting long-tail queries to fit a word limit, deleting zero-volume terms indiscriminately, or equating autocomplete absence with no demand.
- Treating competitor headings as keywords they rank for, or rank visibility as business importance.
- Creating a new page for every synonym, or calling all page overlap cannibalization.
- Publishing, submitting forms, sending messages or changing live sites during research. External writes require exact preview, user confirmation and target readback.

## Verification
Completion means the requested decision is supported by saved evidence, a query-to-page map, prioritized actions and explicit unknowns. A useful partial result can omit unavailable metrics but cannot claim demand size, rank coverage or harmful cannibalization that was not observed.
