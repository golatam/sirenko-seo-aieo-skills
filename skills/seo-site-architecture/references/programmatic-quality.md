# Programmatic quality and controlled rollout

## Principle

Programmatic generation is a delivery method, not an exemption from quality. No page class is automatically 'safe at scale'. Google's doorway and scaled-content policies concern usefulness and purpose, not a magic URL/word-count threshold or whether AI wrote it.

Use when a dataset/template can produce many URLs. Begin read-only with schema, example records and a staged sample, not mass publication. A legitimate request for location pages does not authorize invented local presence, reviews or service availability.

## Gates before generation

1. **Purpose/demand:** distinct user task, entity and evidenced need. Reject permutations differing only by keyword/city name or funneling users to the same usable destination without added utility.
2. **Data provenance:** rights/license, authoritative fields, retrieval date/update SLA, coverage, missing values and prohibited/sensitive data. No fabricated statistics, invented prices or scraped/rewritten material without distinct added value. External APIs require permissions and budget.
3. **Identity:** stable record IDs, deterministic slug rules, collision tests, duplicate entities and variants. Audit raw inputs before transformations; preserve source values.
4. **Standalone usefulness:** compare pages with variable names hidden. Could a user accomplish the promised task? Do data, tools, examples, inventory or expert explanations differ meaningfully? Similarity metrics only prioritize review; no universal % uniqueness/word count guarantees quality or immunity.
5. **Editorial truth:** facts tied to sources, appropriate qualifications, clear ownership/update dates, human subject-matter review for high-risk claims. AI assistance is not banned but does not excuse low value.
6. **Template behavior:** incomplete/null data, zero stock, extreme lengths, duplicate names, accents/non-Latin text, pagination and locale fallbacks. Do not fill missing evidence with boilerplate or false assertions.
7. **Technical:** status, intended index policy, canonical/hreflang, content/meta parity, relevant schema, navigation, sitemap eligibility and mobile function verified in staging through technical audit.

## Sampling plan

Save cohort population/selection rule and random seed, plus reviewers/results. Sample each template, locale, entity class and data completeness tier; include boundaries, lowest-quality records, important pages and a reproducible random sample. Review all new template variants; automated checks can cover every generated record **offline** without a live crawl. If a stratum is absent, coverage is incomplete.

Starting suggestion (operator default, not Google law): one template's first 10–20 draft pages, human review of every draft in that pilot. Adjust before work based on business risk and capacity; never present an arbitrary 5% sample or 30/50/500-page threshold as a safety guarantee. Document sample/population counts with code. Don't call an entire unreviewed universe validated.

## Stop and expansion gates

Write exact project criteria in `templates/programmatic-gate.md` before release:
- **Stop launch:** no standalone value; false/unlicensed/stale critical data; doorway design; unresolved entity/URL collisions; accidental noindex/canonical/redirect break; content safety or claims failure.
- **Stop expansion:** pilot production readback fails; newly observed critical template errors; crawl/resource costs exceed agreed budget; sampled pages fail quality; coverage insufficient for next cohort. Indexing delay is a reason to investigate, not proof of a penalty.
- **Expand:** editorial and technical acceptance signed off, pilot production verified, agreed observation window elapsed with source-backed findings, no stop criteria active and explicit next-batch approval. Missing measurement is not a pass; use a documented owner decision to extend observation, not invent results.
- **Roll back/contain:** disable generation or revert the faulty approved release; preserve evidence, protect existing useful pages and follow migration/incident procedure for URL changes. Do not blanket-noindex everything without diagnosis/approval.

A typical sequence is draft sample → staging QA → approved small production cohort → production readback → agreed monitoring window → approve next cohort. Use cohort size and dates suitable for the site, not a universal publish-100/wait-two-weeks rule. Each stage reports factual completion, not a ranking guarantee.

Track discovered/fetched/index-selected URLs separately, then impressions, clicks, engagement and conversions by cohort where data exists. Include control templates, seasonality and deploy timing; correlation alone cannot prove uplift. No mass indexing requests, link buying or doorway proliferation to 'force' pilot success.

## Official policy checks

Read current Google policies before a real rollout; these sections were inspected 2026-09-24:
- https://developers.google.com/search/docs/essentials/spam-policies#doorways
- https://developers.google.com/search/docs/essentials/spam-policies#scaled-content

Useful content can be short, long, templated or hand-written; neither a minimum word count nor a uniqueness score is Google's quality test. The official policy defines scaled abuse as generating many pages primarily to manipulate rankings rather than help users, regardless of how created.
