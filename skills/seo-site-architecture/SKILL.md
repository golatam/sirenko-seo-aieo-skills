---
name: seo-site-architecture
description: "Use when designing SEO site architecture or page scale."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [seo, architecture, intent, internal-links, programmatic]
    related_skills: [technical-seo-audits, seo-specializations, seo-reporting-monitoring]
---

# SEO Site Architecture

## When to Use

Use for intent→URL maps, new sections, consolidation, navigation/internal linking, facets/pagination and programmatic page systems. This is design and quality control, not a keyword-volume service or bulk publisher. For technical diagnosis, use `technical-seo-audits`; local/ecommerce/international/Yandex specifics route to `seo-specializations`.

## Input / output

Input: business outcomes, audience/tasks, market/language, evidence-backed demand clusters, existing URL inventory/content, data model, constraints and ownership. Missing search volume/SERP evidence stays unknown; do not invent demand to justify pages.

Output: `templates/intent-url-map.csv`, `templates/link-map.csv`, tree/navigation decisions, index policy by URL class, `templates/programmatic-gate.md`, and implementation acceptance tests. Changed live URLs also need the technical audit skill's migration map/rollback plan.

## Workflow

1. **Audit what exists.** Use supplied CMS/crawl/GSC inventories within permissions. Keep existing URLs unless a measurable need justifies a move. Document incomplete inventory and existing pages competing for the same user task.
2. **Map intent to a useful destination.** Load `references/intent-linking.md`. Assign a primary URL to each coherent intent/entity/locale; distinguish genuinely different tasks from synonyms. Compare real SERP/task evidence before splitting or merging; one keyword per URL is not a rule.
3. **Design navigation and URL policy.** Produce hubs, useful categories, breadcrumb parents, contextual links and pagination. Record index/crawl/canonical treatment for real duplicates, facets/search, thin/empty states and locales. URL shape alone does not create architecture.
4. **Design links as testable edges.** Specify source, destination, anchor/context, template rule and user benefit. Ensure important destinations have crawlable HTML href routes and a reasonable depth from named seeds. No arbitrary links-per-word quotas or orphan claims based on a partial crawl.
5. **Gate programmatic scale.** Load `references/programmatic-quality.md` before generation/rollout. Validate source rights/freshness, demand, entity uniqueness, standalone usefulness, template exceptions and editorial accuracy. No doorway/location-swapping pages or scaled low-value content, regardless of whether AI or humans generate it.
6. **Stage, review, then authorize.** Start with a bounded representative cohort; define stop/expand gates and rollback **before** publishing. Read-only design never authorizes site writes. Each rollout batch requires explicit scope/approval; read back production pages/links after approved changes.
7. **Measure and revise.** Technical acceptance → discovery/recrawl → index selection → user/search outcomes are separate gates. Use `technical-seo-audits` for verification and `seo-reporting-monitoring` for observed cohorts/results. Slow indexing alone is neither proof of low quality nor permission to mass-submit more pages.

## Rules

- Preserve URL identifiers exactly in source inventories; normalized comparison keys must be separate columns. Never silently change slugs/query strings/case.
- Do not canonicalize meaningful distinct pages to a parent just to reduce index count. Don't use robots disallow as a substitute for noindex or removal.
- Stop launch for unsupported facts, stale/unlicensed data, false local presence, no standalone value, broken mappings or unmet technical gates. User approval cannot make spam policy risk disappear.
- No fabricated reviews, generated authority, hidden text, manipulative internal link stuffing or guaranteed indexing/ranking.

## References

- `references/intent-linking.md` — clustering, URL decisions, linking, facets and acceptance.
- `references/programmatic-quality.md` — source/template QA, sampling, staged release and stop gates.
- `references/source-adaptation.md` — pinned donor concepts and official anti-spam sources.
- `templates/intent-url-map.csv`, `templates/link-map.csv`, `templates/programmatic-gate.md` — handoff contracts.
