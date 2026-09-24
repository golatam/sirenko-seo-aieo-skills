# Intent → URL → navigation → links

## Demand and inventory

Start from business task and user utility, not combinatorial keyword permutations. Record engine/market/language, date, query evidence, observed SERP URLs/features and source. A SERP sample informs intent, but is location/time-sensitive; GSC query/page overlap is diagnostic, not automatic cannibalization. Provider search volume is an estimate with source/date, not a known business opportunity. If no keyword source exists, label demand hypotheses and choose research before expansion.

Inventory current URLs from CMS, sitemaps, internal crawl, logs and console/export where available. Preserve source strings; deduplicate with explicit comparison rules, not destructive normalization. Tag template, entity, locale, intent, indexed intent/policy, content owner, business role, status and source coverage. Never assume the sitemap is the entire site.

## Mapping decisions

For each intent cluster choose retain/improve/create/merge/retire/hold, with primary URL and alternatives:
- Keep synonyms on one useful page unless user tasks/content or actual SERPs justify separation.
- Split genuinely different tasks, formats or entities when each destination can satisfy the task independently; don't impose one page per keyword or one URL per entity universally.
- Merge overlapping pages only after examining actual content, links, conversions and search context; multiple pages receiving impressions on a query is not by itself a defect.
- A page may serve supporting queries; record those without creating duplicate URLs.
- Give new URLs a stable entity/intent key. Enforce uniqueness and deterministic slug collision handling; preserve established URLs and route future name changes through explicit redirects.
- For languages/regions, use explicit equivalent-page mapping, not literal slug substitution. Route translation/regional strategy to `seo-specializations`.

Deliver the URL map plus an intelligible navigation tree (not merely a folder diagram). For each page explain why it exists, its unique user value, how users find it and what next action it supports. Breadcrumb hierarchy should reflect actual organization, not be invented from every slash in a URL.

## Link graph design

Specify global navigation, category hubs, breadcrumbs, contextual links and related-item rules separately. Use ordinary crawlable anchor hrefs for critical navigation; do not depend exclusively on click handlers, form submission or infinite scroll. Descriptive anchors should fit the sentence and target, not repeat an exact-match keyword mechanically. Link quantity should follow user relevance; no universal 3–5 links/1000 words threshold.

Use `templates/link-map.csv` for planned edges and template rules. For automation, define matching attributes and tie-breaks, cap unnecessary repeated links, avoid self-links and validate actual destinations. Related-item suggestions need semantic/user relevance, not random links just to fill a quota. Contextual cross-links across hubs can be useful; rigid 'silos' should not obstruct users.

Verify important destinations are reachable from named seeds, count actual edges/depth per observed graph and identify unvisited regions. 'Within three clicks' can be a design heuristic, never a universal engine requirement. A sitemap-only page is an orphan candidate; limited crawler reach is not proof of orphaning. Compare raw/rendered graphs and CMS inventory via `technical-seo-audits`.

## URL classes and indexing policy

| Class | Design question / test |
|---|---|
| Useful distinct category/detail | Has own intent/content, discoverable routes and consistent preferred URL? |
| True duplicate/sort/tracking | Can links prefer a clean URL and appropriate canonical/redirect without losing user functionality? |
| Useful facet with demand | Unique stable content/stock/value and navigable HTML route? Treat as a landing-page candidate, not automatically canonical to parent. |
| Endless facet combinations | Explicit crawl trap prevention; bound allowed combinations and test that wanted pages remain reachable. |
| Internal search/empty/transient | Decide intended inclusion, user utility and lifecycle; do not index all query combinations by default. |
| Pagination/load more | Each useful segment has direct URLs/crawlable links; avoid canonicalizing distinct content blindly to page 1. |
| Retired/missing entity | Relevant replacement → deliberate redirect; no replacement → honest 404/410 or useful retained information where justified. |

Differentiate crawling, index control and canonical consolidation; robots disallow may prevent noindex discovery. Canonical is a signal, not guaranteed deindexation. Technical audit verifies header/meta semantics and current engine guidance.

## Identity handoff

Follow the shared **Identity handoff** reference in `seo-aieo` for the query/page/provider crosswalk; load that umbrella reference through skill_view. The architecture CSV keeps one row per source `mapping_id` with query/page IDs, lane and provisional/blocked state. A new proposed slug for the same logical page preserves target_page_id and records old→new in decision evidence; changing the assignment needs new mapping/architecture IDs and explicit supersedes/lineage. Do not join rank history by phrase or current URL, and do not promote provisional mapping status because architecture is approved. Content receives source mapping IDs plus the current architecture decision.

## Engineering handoff / acceptance

- Every approved cluster has an intended destination or documented hold; conflicting primary ownership resolved.
- Every new URL has entity identity, data/content owner, template, source evidence and index policy.
- Each high-priority destination has tested navigation/contextual edges; no target redirects/404s contrary to design.
- URL collisions, unsafe host links, query traps, empty states and untranslated locale routes have tests.
- Metadata/schema/content are coherent; source/render differences tested per template; no promised CTR gains from title length.
- Existing changed URLs have migration map, staging acceptance, rollback owner and approved production readback.
- Release outcomes tracked by cohort with source/date; design completeness is not proof of indexing or revenue.
