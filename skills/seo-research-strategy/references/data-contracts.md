# Research artifact contracts (v1)

Copy the templates into a project/run directory selected from real project context. Do not write project data back into the skill. Preserve raw exports separately. UTF-8 CSV, header order preserved, RFC-style quoting; blank cells mean unknown/not applicable, never invented zero. Use stable IDs and ISO-8601 timestamps with timezone; dates use YYYY-MM-DD. Country: ISO alpha-2 or an explicit documented multi-country scope. Language: BCP-47. Device: `desktop|mobile|tablet|all|unknown`. Do not infer unspecified export dimensions.

## queries.csv

One row per exact query in a market/language/engine/device lane. Required: query_id, query, lane fields, source_type, source_url_or_file, source_locator, observed_at, verification_status. Deduplicate only after preserving originals; trim accidental whitespace for comparison but do not delete accents or merge translations.

`source_type`: `gsc|rank_tracker|keyword_provider|serp|customer|community|competitor|hypothesis`. `verification_status`: `observed|hypothesis`. For a hypothesis, source locator points to the reasoning/brief and observed_at is its creation timestamp, not a claimed search observation. Intent: `informational|commercial|transactional|navigational|local|mixed|unknown`; buyer stage: `discover|evaluate|buy|use|unknown`. These are analyst judgments, not measured fields.

## metrics.csv

One metric observation per row, foreign key query_id. Numeric value can be blank only with `metric_status=unknown|unavailable`. `metric_status=measured|provider_estimate` requires a numeric value, unit, provider, source and period. Zero is retained when actually reported. Query lane must agree with the original; split the query ID if the source measures another lane.

Typical metric/unit pairs:
- `gsc_clicks` / `clicks`, `gsc_impressions` / `impressions`, `gsc_ctr` / `ratio_0_1`, `gsc_position` / `average_position`.
- `search_volume` / `searches_per_month` with provider averaging period; an estimate, not actual unique searches/users.
- `kd` / `provider_score_0_100` only if this is the provider's documented scale; otherwise record its real unit.
- `cpc` / `currency_per_click:USD` (replace currency as sourced).
- `trend_index` / `relative_index_0_100` with baseline/request scope in limitation.

Do not flatten multiple providers into one metric or derive GSC market volume. Record excluded rows, privacy suppression, data freshness, period comparability and aggregation in limitation. Compute CTR from summed clicks / summed impressions when appropriate; never average row CTRs. Do not sum average position or KD.

## serp.csv

One observed result per snapshot/query/lane. Required: snapshot_id, query_id, lane, observed_at, result_url, result_type, source_url_or_file, source_locator, scope_note. `result_type`: `organic|ad|map|video|answer_feature|other`. `organic_rank` is a positive integer only for observed organic rank; blank otherwise. A search-tool discovery list without explicit engine ranking leaves rank blank and explains the limitation. Do not insert fictitious result rows to pad a top ten.

`observed_canonical_url` is populated only from a fetched page or authoritative export. `page_type` and `intent` are reviewed interpretations. scope_note records location, requested/obtained depth, exclusions, personalization/login if known and acquisition method. Snapshot IDs cannot cross query/lane or capture-time boundaries.

## query-page-map.csv

Required: mapping_id, query_id, cluster_id, market, language, intent, target_state, action, mapping_status, evidence_url_or_file, evidence_locator, cannibalization_status, rationale, owner. `owner=unassigned` is allowed but blocks execution handoff, not research delivery.

`mapping_status`: `validated|provisional|blocked`. `cannibalization_status`: `unknown|suspected|supported|not_supported`. `target_state`: `existing|proposed|none`. `action`: `keep|refresh|create|merge_review|defer`. A non-deferred row requires target_page_id and target_url. Target URL must be a full URL, even when proposed; proposed status prevents it being mistaken for live. `none` requires defer. Semicolon-separated serp_snapshot_ids reference saved snapshots; validated SERP clustering needs real matching snapshots. Other source locators may reference GSC rows or page-review notes.

Uniqueness: one primary assignment per `(query_id, market, language, intent)` and one stable target_page_id per target URL/language. Validate query market/language against queries.csv. A cluster cannot silently combine different lanes; if a cross-lane strategic topic groups them, retain distinct operational cluster IDs.

## Programmatic verification procedure

1. Parse each CSV with Python `csv.DictReader` using `encoding='utf-8-sig'`, never split rows on commas. Compare fieldnames with the saved template and reject extra/missing cells. Report header-only files as empty templates, not completed research.
2. Count rows and deduplicate IDs/keys in code. Reconcile input/output counts, excluded rows and pagination against source totals; disclose sample boundaries and suppression.
3. Check required cells, allowed enums, valid timestamp/URL shapes, numeric values and documented units. Blank unknowns must remain distinct from measured zero.
4. Build query and snapshot dictionaries. Check foreign keys, snapshot lane consistency, source locators and target mapping uniqueness. Flag missing files and unverified external URLs rather than declaring provenance complete.
5. For validated mappings require supporting evidence, actual reviewed snapshots if claiming SERP validation, and an existing-page check if target_state is existing. Programmatic integrity cannot prove intent quality: manually review mixed/boundary clusters and consequential decisions.
6. Save a validation summary with actual counts, errors, limitations and decision readiness. A clean parser is not proof of demand, causation or ranking success.

## Handoff contract

`seo-content-operations` receives brief + map row(s) + page ID + query/intent lane + evidence assets still needed + owner + acceptance event. `seo-site-architecture` receives proposed/existing URL decisions and ambiguous overlaps. Monitoring receives unchanged query IDs, locale/engine/device and dated baseline; never replace a rank-tracker baseline with GSC average position.
