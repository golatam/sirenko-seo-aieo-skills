# Research method: evidence to page decisions

## 1. Establish demand lanes

A lane is `market + language + engine + device`; add city/location when it changes intent. Country and language are not interchangeable. Spanish in Spain, Mexico and Colombia can require different queries, offers and legal facts. Preserve accents and the original phrase. Never silently translate a query and attach the original volume to its translation.

Recover the offer, customer job, conversion event and feasible delivery scope before collecting a large keyword list. Inspect existing page inventory and dates first: updating a suitable page may beat creating a new one. Inventory available data by source, period, dimensions, permissions and sampling limit. A connector's presence proves neither access to the right property nor a usable export.

Choose a bounded sample: business-critical query families, existing high-value pages, known alternatives and emerging questions. State what is excluded and why. Seed from scoped sales/support evidence, authorized site-search exports, GSC, public competitor pages, community language and product documentation. Keep private quotes anonymized and do not submit customer records to external tools without permission.

## 2. Separate observations from proposals

Keep three layers:
1. **Observed wording:** exact query or question, source locator, timestamp and lane.
2. **Measured metrics:** a provider observation, not the language model's judgment.
3. **Interpretation:** intent, priority, cluster and rationale, with confidence and contrary evidence.

Search suggestions and PAA are discovery signals, not volume measurements. Only record autocomplete or PAA when actually observed with a supported source. A generic web-search response does not automatically expose either. Generated variations remain `hypothesis` until observed; no minimum keyword count justifies filling gaps with plausible data.

Retain long-tail questions intact. Short head terms may hide multiple jobs. A measured zero can reflect rounding, coverage or a niche B2B query; preserve the zero, provider and limitation, then evaluate customer relevance. Blank means unknown, never zero.

Store metrics long-form so GSC impressions, monthly keyword estimates and vendor KD cannot be silently mixed. GSC impressions describe this property's exposure, not total market search frequency. KD scales are provider-specific. CPC requires a currency and match/market context. Never sum near-duplicate keyword estimates as unique audience size; disclose overlap even for a directional total. Trend indices are relative to their original request/baseline, not search counts.

## 3. Competitors: two maps

Use `competitor-analysis` for direct/indirect/substitute/benchmark distinctions and dated pricing/offer evidence. Add a separate search-competitor set: publishers, directories, forums, marketplaces, regulators and brands actually appearing for the sampled queries.

For each observed result/page collect:
- Query/lane/snapshot and URL; ranking presence only if the data source reports it.
- User job and page type: category, product, comparison, service, guide, tool, local listing.
- Promise, intended action and how the page supports it.
- Evidence assets: genuine case study, dataset, calculation, screenshots, examples, named expert review.
- Missing or outdated answers that affect a decision, not just missing headings.
- What the project can credibly do better and what proof it would need.

A public case study proves a published claim, not that its result is independently verified. A `site:` search is a discovery aid, not an exhaustive URL inventory. Do not call a competitor page high traffic without actual traffic data and source qualification.

A useful gap is `customer task + insufficient current answer + credible unique contribution + relevant next action`. A topic absent from competitors is not automatically an opportunity; test demand and fit. A competitor's complete answer may be a reason not to create another article.

## 4. SERP-informed clustering

Input: candidate queries and saved, comparable SERP snapshots. Procedure:
1. Select representative queries across distinct apparent intents. Use the same engine, locale, device and comparable capture dates; declare result depth.
2. Store observed organic results separately from ads, maps, videos and answer features. Keep exact source URLs. Record any observed canonical separately; don't collapse URLs by guessed canonicalization.
3. Inspect page type and task in the result pages, not just titles. Record mixed SERPs and geographic interpretations.
4. Form candidate groups from shared task and format. Compare organic URL sets with code: intersections, union and overlap fraction, with denominator/depth visible. Do not compare incomplete snapshots as if their depth were equal.
5. Merge only when one page can satisfy both tasks without compromising either. If result formats differ or the group is mixed, split or hold. Validate boundary queries, not just the easy cluster center.
6. Save the rationale, snapshots and exceptions. Recheck ambiguous/high-value boundaries before drafting.

URL overlap is supporting evidence, not a ranking law. Choose and disclose any project-specific threshold; test its boundary decisions manually. Semantic similarity without SERPs creates a `provisional` group. Missing local SERPs must remain visible rather than being replaced with US/English observations.

## 5. Query-to-page map

Map each accepted query/intent lane to one primary page ID. Several queries can serve the same page; a page can cover related intents only when the observed task supports it. For a mixed query, use separate intent rows and explicit rationale, not accidental duplicates.

Actions:
- `keep`: suitable current page; no change justified.
- `refresh`: same job/URL, evidence or presentation needs updating.
- `create`: no suitable page, supported intent and useful contribution available.
- `merge_review`: overlap needs architecture/editorial decision, not an approved redirect.
- `defer`: evidence, product availability, expertise or feasibility is missing.

Target state is `existing`, `proposed` or `none`. Do not put a proposed URL into a crawl inventory as if it exists. Existing targets need page evidence; proposed targets need intent evidence and an architecture check. Pass URL ownership/hierarchy and link changes to `seo-site-architecture`.

### Cannibalization investigation

Input: suspect URLs plus query/page/time data for the same lane. Procedure:
1. Compare actual page purpose, canonical state and conversion journey.
2. Inspect repeated GSC query-page distributions or rank snapshots, URL switching and the intended target's performance. Preserve date granularity; an aggregate alone can conceal switching.
3. Check confounders: brand queries, sitelinks, locale variants, normal different intent, redirects/migrations, indexability changes, seasonality and rank-tracker scope.
4. Record the observed overlap and its likely cost. Use `suspected` when there is only overlap, `supported` when repeated observations and page-purpose evidence support harmful competition, and `not_supported` when different jobs explain it. Causation remains a hypothesis unless tested.
5. Recommend keep/differentiate/consolidation review with a rollback and measurement plan. Preserve unique useful content and receiving-page suitability if consolidation is approved later.

Stop: without appropriate time/query/page evidence, do not label cannibalization confirmed or execute destructive consolidation.

## 6. Prioritize and make strategy falsifiable

Use ordinal priority (`now`, `next`, `later`, `blocked`), with explicit reasons:
- Customer/commercial value: evidence that solving the task matters and a legitimate next step exists.
- Evidence advantage: access to a useful case, worked demonstration, public dataset analysis or expert review.
- Demand confidence: direct customer/query evidence versus a proposal.
- Feasibility: indexability, production/review capacity, legal constraints and dependencies.
- Cost and risk: effort in hours only when estimated by an owner; cash estimates carry currency and assumptions.

If requested, build a weighted decision model using agreed weights and code, not a claimed objective SEO score. Show inputs, missing fields and sensitivity. Never calculate priority from invented frequency/KD. Do not promise revenue from rankings; a scenario forecast must expose traffic, CTR, conversion, value, time horizon and overlap assumptions.

Produce a capacity-limited backlog with page IDs, evidence requests, owner, due/review date, expected user outcome, measured event and falsification gate. Dependencies come first: fixing indexability or obtaining expert review can block content. Reserve a learning step, not an arbitrary content quota. Without measured outcomes, deliver a research backlog rather than an ROI-ranked publishing calendar.

## Partial-access deliverables

- Public website + no accounts: competitor/task evidence, candidate queries, sampled SERPs if available, provisional map and access request. No numeric demand/traffic/KD.
- GSC only: owned visibility and query-page patterns; not full market demand and not independent rank coverage.
- Keyword export only: provider metrics with scope; no claim that the site ranks or that its pages convert.
- No reliable localized SERPs: lane-specific candidate lists and validation plan; clustering remains provisional.
- No crawl inventory: mark existing-page coverage partial and block consolidation or new-URL certainty.

Always state the exact excluded capability and what evidence would unlock it.
