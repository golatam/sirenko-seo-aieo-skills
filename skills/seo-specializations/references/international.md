# International / multilingual SEO

## Input → output → validation

**Input:** target markets/languages, local business eligibility/offers, query/SERP evidence by locale, existing domains/routes/canonicals, CMS translation workflow, native reviewers and analytics.
**Output:** [locale-matrix.csv](../templates/locale-matrix.csv), intent-to-page map, locale URL design, reciprocal hreflang clusters, localization briefs and test/rollout plan.
**Validation:** each target page serves a real local audience, is reachable/crawlable, has coherent canonical/alternate signals and reviewed local facts. A language translation alone does not prove market fit.

## 1. Locale and intent discovery

Separate country, language, script, currency and service availability. Spanish content does not imply the same query intent in Spain/Mexico; English language does not mean US pricing/law.
For each market record searcher task, native query variants, current local SERP features, local competitors, relevant sources and conversion constraints. Use `seo-research-strategy`; no fabricated keyword volume or borrowed cross-country demand.
Check whether the business can actually sell/serve there. Tax/shipping/licensing/privacy/legal advice requires the appropriate expert; SEO cannot authorize market entry.
Native reviewer validates terminology, units, examples, cultural context and commercial/legal claims. Mark machine drafts unreviewed; do not stamp them localized because the language changed.

## 2. URL architecture and fallback

Assess ccTLD/subdomain/subdirectory tradeoffs: ownership/infrastructure, legal constraints, existing signals, staffing and migration risk. No universal claim that one structure always ranks better.
Use distinct discoverable language URLs; avoid relying only on cookies/IP/Accept-Language. Google notes locale-adaptive rerouting may hide variants from crawling.[21]
Provide visible language/region switch links preserving the equivalent page when possible. Do not forcibly send every foreign visitor/bot to a homepage or prevent access to another locale. A notice/suggestion is different from an unavoidable redirect.
Document fallback for missing translation: do not emit hreflang to nonexistent pages or pretend untranslated content is localized. x-default is a useful deliberate unmatched-language/selector fallback, not mandatory magic.[8]

## 3. Page equivalence and canonical decisions

Cluster actual alternate versions of the same content/intent. A country-specific unrelated service page is not automatically the alternate of the homepage.
For genuine translations, prevent accidental canonical-to-original that undermines intended indexing. For similar same-language regional duplicates, choose a preferred version and consistent canonical/hreflang policy using official guidance; do not mechanically self-canonicalize every duplicate or consolidate distinct local pages.[21]
Check status, redirect chain, indexability, canonical target, content language and rendered head for every cluster member. Google-selected canonical may differ; observe via authorized inspection, not claim it from source HTML.
Different currencies/availability or legal terms may justify distinct variants; align commerce feed and product URL design with the ecommerce module.

## 4. Hreflang implementation and tests

Choose an implementation that the team can maintain: HTML head, HTTP headers (including suitable non-HTML), or XML sitemap. Multiple methods are not required; if mixed, outputs must agree.[8]
For each cluster verify:
- literal locale token format against current supported Google language/script/region codes; preserve invalid input in the finding rather than silently «repairing» it;
- fully qualified alternate URLs, valid live target and intended canonical association;
- each member self-reference plus alternates, same set across the intended complete cluster;
- reciprocal/return links: A→B and B→A; Google ignores non-returning pairs; missing return is a concrete defect, not a score deduction;[8]
- no duplicate locale mapped to conflicting targets; no homepage-only alternates on deeper pages;
- x-default only when a meaningful fallback is chosen; do not add a fictitious locale/country token;
- correct rendered head/header/sitemap namespace and no publication of drafts/staging domains.

Use a validator/crawl already available, or parse a bounded export; do not claim a full-site graph check from three URLs. Count nodes/edges/missing returns in code and provide failing URLs/edges. Templates are not auto-deployable markup.

## 5. Local content and citations

Research/claim sources should match the market and language: regulation from that jurisdiction, current local prices/units, locally relevant expert evidence. A US source does not automatically prove a Spanish offer/claim.
Localize title, headings, body, navigation, alt/captions, contact, currency/delivery, FAQs, forms, errors and structured-data values. Check form routing to staff who can support the language. Do not translate customer reviews into purported original quotes without labeling.
Earned media/outreach uses `seo-authority-promotion`: genuine local relevance, native DRAFT, disclosure/approval. Do not create synthetic «local authority» pages or fake country offices.

## 6. Cross-language AI citation test

Route protocol to `aieo-visibility`, but preserve `prompt_language`, market, engine/surface, date/session, response language, cited URL, detected page language, content equivalence and citation fidelity.
A Spanish response citing an English page is an observed mismatch/opportunity, not automatic hreflang failure. Separate wrong market/offer from merely different citation language. Repeat observations before attributing changes to localization. No API/UI equivalence assumed.

## 7. Rollout and acceptance

Changeset: added/removed routes, canonical/alternate diffs, redirect map if migrating, country restrictions, reviewer, risk/rollback and exact tests. Approval required before CMS/CDN or sitemap writes.
Pilot a complete alternate cluster rather than one isolated page. Read back public headers/rendered head and reciprocal target pages; test manual locale switching, deep links, forms, mobile and selected currency. Check indexing later separately from deployment.
Measure by country × language URL × intent cohort, comparable periods and available conversions. Track seasonality, promotion, inventory and migration. Rank/citation/traffic improvements are not guaranteed.

## Evidence

Localized versions and reciprocal rules [8], multilingual/multi-regional routing and canonical guidance [21]. Source URLs/provenance: [sources.md](sources.md).
